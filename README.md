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

## Supporting nonparadoxical operators

These operators are kept separate from the paradox catalogue. They may be used
as reductions, bridges, or falsification tools without being classified as
paradoxes themselves.

- **Information-controlled Poincare bifurcation** — `VALIDATED_NONPARADOXICAL_OPERATOR_CANDIDATE`
  - exact signed geodesic coordinate: `z=tanh(h/2)`
  - exact quartic pitchfork: `E(h;mu)=h^4/4-mu*h^2/2`
  - exact stable branches: `h=0` for `mu<=0`, `h=±sqrt(mu)` for `mu>0`
  - exact minimum-energy branch: `E_min=0` or `-mu^2/4`
  - exact 36-phase overlap law: `1-N/9`
  - pinned Q28 28-logical-qubit sparse witness: `PASS`
  - information-to-`mu` and physical-energy bindings remain `OPEN`

  See [`operators/nonparadoxical/information_energy_bifurcation/README.md`](operators/nonparadoxical/information_energy_bifurcation/README.md).

## Epistemic policy

Repository presence is not proof. Claims are typed as `EXACT`, `STANDARD_THEOREM`,
`NUMERICAL_WITNESS`, `CONDITIONAL`, `OPEN`, or `FAIL`. Cross-repository inputs are
pinned to source commit IDs where possible.
