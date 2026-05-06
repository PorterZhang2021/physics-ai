# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A self-study Jupyter notebook repository for building skills at the intersection of condensed matter physics and machine learning — specifically targeting topological matter, quantum transport, and AI tools like GNNs and equivariant neural networks.

## Environment Setup

```bash
pip install numpy scipy matplotlib pandas scikit-learn
pip install torch                   # pytorch.org for system-specific install
pip install torch-geometric         # GNN
pip install e3nn netket kwant pythtb z2pack  # AI x Physics
pip install jupyter
```

Run notebooks:
```bash
jupyter notebook
# or for a specific file:
jupyter notebook ai/roadmap.ipynb
```

## Repo Architecture

Two parallel roadmaps that share Layer 1 (Math) and converge at Layer 5 (AI × Physics):

| Directory | Roadmap | Duration | Goal |
|-----------|---------|----------|------|
| `ai/` | AI/ML skills path | ~2 years | GNN · Equivariant Networks · NQS |
| `cross/` | Condensed matter + AI research path | ~3 years | Topological matter research |
| `guides/` | Study methodology | — | Prompt templates for Feynman-technique AI dialogue |

**The two roadmaps are meant to be run in parallel after month 4, not completed sequentially.**

### `ai/` Layer Structure
- **Layer 1** (months 0–3): Math — Linear Algebra (Strang), Calculus (3B1B), Probability (Blitzstein)
- **Layer 2** (months 0–4): Python — NumPy, Matplotlib, Pandas
- **Layer 3** (months 3–8): ML — scikit-learn, supervised/unsupervised learning
- **Layer 4** (months 6–14): Deep Learning — PyTorch, MLP, Transformer
- **Layer 5** (months 12–25): AI × Physics — GNN (PyTorch Geometric), Equivariant networks (e3nn/NequIP), NQS (NetKet)

### `cross/` Layer Structure
- **Layer 1** (months 0–3): Same math as `ai/`, plus Differential Geometry and Group Theory (deferred to month 12)
- **Layer 2** (months 2–14): Core Physics — Griffiths QM, Kittel Solid State, Statistical Mechanics
- **Layer 3** (months 12–22): Specialized Physics — Berry phase, Topological Insulators (Asbóth→Bernevig), Quantum Transport (Datta/NEGF)
- **Layer 4** (months 3–36): Computational — Tight-binding (NumPy), kwant (transport), pythtb + Z2Pack (invariants)
- **Layer 5** (months 8–36): AI Tools — mirrors `ai/` Layers 3–5
- **Layer 6**: Research frontiers (follow arXiv: cond-mat + cs.LG)

### Key Files
- `ai/roadmap.ipynb` — Master reference for the AI path; contains full layer breakdown and timeline
- `cross/roadmap.ipynb` — Master reference for the physics path; contains 6-layer knowledge map
- `ai/ml-fundamentals.ipynb` — Hands-on ML algorithm exercises (Layer 3 exercise book)
- `ai/ai-fundamentals.ipynb` — Overview of 6 AI directions (NLP, CV, RL, GenAI, Multimodal, AI×Physics)
- `guides/interactive-study-guide.ipynb` — Structured prompt templates for studying with AI using the Feynman technique

## Adding New Notebooks

New phase-specific notebooks go under `ai/0N-<phase>/` or `cross/0N-<phase>/` (e.g. `ai/02-python/`, `cross/03-topology/`). Top-level files in each directory are overview/reference; subdirectories hold phase detail.

## Notebook Conventions

Notebooks are written in English. Visualization cells use `plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'DejaVu Sans']` for font compatibility. Roadmap notebooks generate Matplotlib diagrams as their primary output — they do not require external data files.