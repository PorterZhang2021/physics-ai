# Linear Algebra Study Guide

**Layer 1 — First subject to tackle**
**Duration:** Weeks 1–4 (within the 12-week Layer 1 period)

---

## Resources (in order of use)

| Resource | Format | Where |
|----------|--------|-------|
| 3Blue1Brown *Essence of Linear Algebra* | 16 videos, 10–20 min each | YouTube / Bilibili — watch **before** reading |
| Strang *Introduction to Linear Algebra* | Textbook | Ch. 1–2, 4, 6 |
| MIT OCW 18.06 | Lectures + problem sets | ocw.mit.edu/18-06 — Strang's own course, free |

---

## Week 1 — Vectors and Matrices (Strang Ch. 1–2)

Watch 3B1B episodes 1–5 first, then read.

**Key concepts:**
- Vectors as geometric arrows, not just lists of numbers
- Matrix × vector as a linear transformation of space
- Matrix × matrix as composing two transformations
- The four fundamental subspaces (build intuition only — you'll return to these)

**Hand exercise:** Compute a 2×2 matrix multiplication by hand, then draw both the input and output vectors to see the transformation geometrically.

---

## Week 2 — Solving Linear Systems (Strang Ch. 2, continued)

**Key concepts:**
- Gaussian elimination / row reduction
- When does Ax = b have a solution? No solution? Infinitely many?
- LU factorization (understand the idea; no need to implement from scratch yet)

**NumPy checkpoint:**
```python
import numpy as np

A = np.array([[2, 1], [1, 3]])
b = np.array([5, 10])
x = np.linalg.solve(A, b)
print(x)  # verify by hand first
```

---

## Week 3 — Orthogonality (Strang Ch. 4)

Watch 3B1B episodes 6–9 first, then read.

**Key concepts:**
- Dot products and projections
- Orthogonal matrices: why Q^T Q = I matters
- Least squares — solving Ax = b when no exact solution exists

**Why it matters for AI:**
Gradient descent moves orthogonally to loss contours. Attention scores in Transformers use dot products. PCA is orthogonal projection.

---

## Week 4 — Eigenvalues and Eigenvectors (Strang Ch. 6)

Watch 3B1B episodes 13–14 first, then read.

**Key concepts:**
- Definition: Av = λv — a vector whose direction is unchanged by the transformation
- Characteristic polynomial: det(A − λI) = 0
- Diagonalization: A = PDP⁻¹ (when it exists)
- Symmetric matrices always have real eigenvalues and orthogonal eigenvectors

**Hand exercise:** Find the eigenvalues of `[[3, 1], [0, 2]]` from scratch, then verify:
```python
eigenvalues, eigenvectors = np.linalg.eig(A)
```

**Why it matters for AI:**
PCA finds eigenvectors of the covariance matrix. The Hamiltonian in quantum mechanics is a matrix whose eigenvalues are energy levels. Stability of gradient descent depends on eigenvalues of the Hessian.

---

## Completion Milestones

- [ ] Can compute a 3×3 matrix multiplication by hand
- [ ] Can explain geometrically what matrix multiplication *does* (not just how to calculate it)
- [ ] Can find eigenvalues of a 2×2 matrix by hand using the characteristic polynomial
- [ ] Can explain in words why eigenvectors are special — what property distinguishes them from all other vectors
- [ ] Can implement least squares in NumPy and explain what it minimizes
- [ ] Can explain why symmetric matrices always have orthogonal eigenvectors (connects directly to quantum mechanics later)

---

## Feynman Self-Test (after each week)

Use this template when studying with AI:

> "Let me explain [concept]; tell me where I have problems:
> A matrix is ...
> Eigenvalues mean ...
> What I'm not sure about is ..."

Active recall beats re-reading every time.

---

**Start here:** Watch 3B1B episode 1 — *"Vectors, what even are they?"* (9 minutes). It sets up the geometric intuition for everything that follows.