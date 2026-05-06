# Physics × AI

> Topological Matter · Quantum Transport · Machine Learning

A self-study repository for building AI and physics capabilities from the ground up,
ultimately targeting research at the intersection of condensed matter physics and modern machine learning.

---

## Goal

> Taking condensed matter physics as the main stage, computational methods as tools, and AI as an accelerator,
> deeply study the physical properties of topological matter and quantum transport mechanisms.

---

## Repository Structure

```
physics-ai/
├── ai/               # AI/ML learning path (Layer 1–5)
│   ├── roadmap.ipynb          # Main reference: full AI roadmap
│   ├── ai-fundamentals.ipynb  # Overview of 6 major AI directions
│   └── ml-fundamentals.ipynb  # ML core algorithms + exercises
├── cross/            # Physics × AI research path (Layer 1–6)
│   ├── roadmap.ipynb          # Main reference: full physics roadmap
│   └── 01-math/roadmap.ipynb  # Phase 1: math foundations detail
└── guides/
    └── interactive-study-guide.ipynb  # Prompt templates for study dialogue
```

---

## Two Roadmaps, One Destination

| | `ai/roadmap.ipynb` | `cross/roadmap.ipynb` |
|---|---|---|
| Focus | AI/ML skills | Condensed matter physics + AI |
| Duration | ~2 years | ~3 years |
| Goal | GNN · Equivariant Networks · NQS | Topological matter research |
| Layer 5 | AI × Physics (GNN, e3nn, NetKet) | Same — fully aligned with `ai/` Layer 5 |

**These two roadmaps share Layer 1 (Math) and converge at Layer 5 (AI × Physics).**
Completing `ai/` means Layer 5 of `cross/` is already done.

---

## Recommended Study Plan

Do **not** complete one roadmap before starting the other.
After the shared Layer 1, run them in parallel — physics and AI do not block each other until Layer 5.

| Period | AI Path (`ai/`) | Physics Path (`cross/`) |
|---|---|---|
| Months 0–4 | **Layer 1: Math** (shared) | ← same content |
| Months 4–12 | Layer 2–3: Python + ML | Layer 2: QM + Solid State |
| Months 12–24 | Layer 4–5: DL + GNN + e3nn | Layer 3–4: Topology + kwant |
| Month 24+ | Complete | Layer 5 already covered by `ai/` |

---

## Layer 1: Where to Start

Both roadmaps begin with the same three modules — start here:

| Module | Resource | Priority |
|---|---|---|
| Linear Algebra | Strang *Introduction to Linear Algebra* Ch.1-2, 4, 6 | ★★★★★ |
| Calculus | 3Blue1Brown *Essence of Calculus* (free, YouTube) | ★★★★★ |
| Probability & Statistics | Blitzstein *Introduction to Probability* Ch.1-5 (free PDF) | ★★★★☆ |

**Tip:** Start Linear Algebra and Calculus in parallel. Do not wait to finish one before starting the other.

---

## Key Milestones

| Time | Milestone |
|---|---|
| Month 4 | Can derive eigenvalues and chain rule by hand |
| Month 8 | First band structure plot in Python (graphene E-k) |
| Month 12 | Griffiths QM Ch.1-5 complete; PyTorch training loop from scratch |
| Month 18 | Full topological workflow: SSH edge states in kwant |
| Month 24 | GNN predicts material properties; AI × topology crossover |
| Month 36 | Can pose an original research question |

---

## Core Tools

```bash
pip install numpy scipy matplotlib pandas scikit-learn
pip install torch  # pytorch.org for system-specific install
pip install torch-geometric  # GNN
pip install e3nn netket kwant  # AI x Physics
```