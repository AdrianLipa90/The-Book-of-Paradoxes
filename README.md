# The Book of Paradoxes

A theorem-first reconstruction of paradoxes as explicit mathematical structures.

## Current closed reductions

- **Banach–Tarski** — `CLOSED_REDUCTION`
  - source geometry: tetrahedral Gram class in `Herm_0(2) ≅ R^3`
  - antipodal completion: stella octangula
  - forced cross-sector angle: `cos(theta)=1/3`
  - disjoint-pair transport axes: orthogonal
  - standard consequence: a conjugate pair of rotations generates `F_2 < SO(3)`
  - classical consequence: Banach–Tarski equidecomposition (with Choice)

  See [`paradoxes/banach_tarski/README.md`](paradoxes/banach_tarski/README.md).

- **Zeno** — `CLOSED_REDUCTION`
  - involution split: `Pi=(I+J)/2`, `D=(I-J)/2`
  - contraction: `Z_lambda=Pi+lambda D`
  - exact iterate: `Z_lambda^n=Pi+lambda^n D`
  - dichotomy case: `lambda=1/2`
  - limit: contraction to `Fix(J)`
  - Riemann critical-strip specialization retained only as a typed crosswalk, not an RH proof

  See [`paradoxes/zeno/README.md`](paradoxes/zeno/README.md).

## Epistemic policy

Repository presence is not proof. Claims are typed as `EXACT`, `STANDARD_THEOREM`,
`NUMERICAL_WITNESS`, `CONDITIONAL`, `OPEN`, or `FAIL`. Cross-repository inputs are
pinned to source commit IDs where possible.
