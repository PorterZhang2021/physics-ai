#!/usr/bin/env python3
"""Translate Jupyter notebooks from Chinese to English."""

import json
import re
import time
import sys
from pathlib import Path
from deep_translator import GoogleTranslator

# Files to translate
NOTEBOOKS = [
    "ai/ai-fundamentals.ipynb",
    "ai/ml-fundamentals.ipynb",
    "ai/roadmap.ipynb",
    "ai/01-math/roadmap.ipynb",
    "cross/roadmap.ipynb",
    "cross/01-math/roadmap.ipynb",
    "guides/interactive-study-guide.ipynb",
]

# Regex to detect Chinese characters
CHINESE_RE = re.compile(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]+')

def has_chinese(text):
    return bool(CHINESE_RE.search(text))

def translate_text(translator, text, retries=3):
    """Translate text with retry logic."""
    if not text or not has_chinese(text):
        return text
    for attempt in range(retries):
        try:
            # Add small delay to avoid rate limits
            time.sleep(0.3)
            return translator.translate(text)
        except Exception as e:
            print(f"  Translation error (attempt {attempt+1}/{retries}): {e}")
            time.sleep(2 ** attempt)
    print("  Failed to translate, keeping original.")
    return text


def translate_code_line(translator, line):
    """Translate Chinese text in a code line while preserving code structure."""
    if not has_chinese(line):
        return line

    # Comment line
    stripped = line.lstrip()
    if stripped.startswith('#'):
        return translate_text(translator, line)

    # String literal with Chinese - find and translate
    # Match single/double/triple quoted strings
    pattern = re.compile(r"([fF]?[rR]?['\"]{1,3})(.*?)(['\"]{1,3})", re.DOTALL)

    def replacer(m):
        quote_start = m.group(1)
        content = m.group(2)
        quote_end = m.group(3)
        if has_chinese(content):
            translated = translate_text(translator, content)
            return quote_start + translated + quote_end
        return m.group(0)

    return pattern.sub(replacer, line)


def translate_cell(translator, cell, notebook_name, cell_idx):
    """Translate a single cell."""
    cell_type = cell.get('cell_type', '')

    if cell_type == 'markdown':
        source = cell.get('source', [])
        if isinstance(source, list):
            text = ''.join(source)
        else:
            text = source
        if has_chinese(text):
            translated = translate_text(translator, text)
            cell['source'] = translated.split('\n')
            # Preserve empty lines at end if original had them
            while len(cell['source']) > 1 and cell['source'][-1] == '' and not text.endswith('\n\n'):
                if text.endswith('\n'):
                    break
                cell['source'].pop()
            # Handle trailing newlines properly
            if text.endswith('\n') and (not cell['source'] or cell['source'][-1] != ''):
                cell['source'].append('')
        return

    if cell_type == 'code':
        source = cell.get('source', [])
        if isinstance(source, list):
            new_source = []
            for line in source:
                new_source.append(translate_code_line(translator, line))
            cell['source'] = new_source
        elif isinstance(source, str):
            lines = source.split('\n')
            new_lines = [translate_code_line(translator, line) for line in lines]
            cell['source'] = '\n'.join(new_lines)

        # Translate outputs
        for output in cell.get('outputs', []):
            output_type = output.get('output_type', '')
            if output_type in ('stream', 'execute_result', 'display_data'):
                if 'text' in output and isinstance(output['text'], list):
                    new_text = []
                    for line in output['text']:
                        if has_chinese(line):
                            new_text.append(translate_text(translator, line))
                        else:
                            new_text.append(line)
                    output['text'] = new_text
                elif 'data' in output and 'text/plain' in output['data']:
                    text = output['data']['text/plain']
                    if isinstance(text, list):
                        text = ''.join(text)
                    if has_chinese(text):
                        translated = translate_text(translator, text)
                        output['data']['text/plain'] = translated.split('\n')
        return

    if cell_type == 'raw':
        source = cell.get('source', [])
        if isinstance(source, list):
            text = ''.join(source)
        else:
            text = source
        if has_chinese(text):
            translated = translate_text(translator, text)
            cell['source'] = translated.split('\n')
        return


def translate_notebook(path, translator):
    """Translate a single notebook file."""
    print(f"\n{'='*60}")
    print(f"Translating: {path}")
    print(f"{'='*60}")

    with open(path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    cells = notebook.get('cells', [])
    total_cells = len(cells)
    chinese_cells = 0

    for idx, cell in enumerate(cells):
        # Quick check if cell has Chinese
        cell_json = json.dumps(cell, ensure_ascii=False)
        if not has_chinese(cell_json):
            continue

        chinese_cells += 1
        print(f"  Cell {idx+1}/{total_cells} ({cell.get('cell_type', 'unknown')})...")
        translate_cell(translator, cell, path, idx)

    print(f"  Translated {chinese_cells}/{total_cells} cells.")

    # Write back
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=1)

    print(f"  Saved: {path}")


def main():
    translator = GoogleTranslator(source='zh-CN', target='en')

    for nb_path in NOTEBOOKS:
        full_path = Path(nb_path)
        if not full_path.exists():
            print(f"WARNING: File not found: {nb_path}")
            continue
        try:
            translate_notebook(str(full_path), translator)
        except Exception as e:
            print(f"ERROR translating {nb_path}: {e}")
            import traceback
            traceback.print_exc()

    print("\n" + "="*60)
    print("All notebooks processed!")
    print("="*60)


if __name__ == '__main__':
    main()
