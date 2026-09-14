# Dynamic Identity Invariant

Status: `VALIDATED_NONPARADOXICAL_OPERATOR`.

This operator library entry records a transport-compatible invariant on a tetrahedral/Stella carrier and on an abstract node graph. It is not classified as a paradox.

No biological, psychological, personal, or physical identity binding is claimed.

## 1. Local sector

For a unit vector \(\mathbf n_a\), define

\[
\Sigma_a=\mathbf n_a\cdot\boldsymbol\sigma,
\qquad
\Sigma_a^2=I.
\]

For the regular tetrahedral frame,

\[
\mathbf n_i\cdot\mathbf n_j=-\frac13
\qquad(i\ne j).
\]

For non-antipodal local frames define

\[
\boxed{
U_{ab}=\frac{I+\Sigma_a\Sigma_b}
{\sqrt{2(1+\mathbf n_a\cdot\mathbf n_b)}}.
}
\]

Then

\[
U_{ab}U_{ab}^\dagger=I
\]

and

\[
\boxed{U_{ab}\Sigma_bU_{ab}^\dagger=\Sigma_a.}
\]

Equivalently,

\[
\Sigma_aU_{ab}=U_{ab}\Sigma_b.
\]

## 2. Graph operator

On a node graph define

\[
\boxed{
\Sigma_G=\sum_a|a\rangle\langle a|\otimes\Sigma_a.
}
\]

For a block Hamiltonian whose on-site terms obey

\[
[M_a,\Sigma_a]=0
\]

and whose edge blocks use transports satisfying

\[
\Sigma_aU_{ab}=U_{ab}\Sigma_b,
\]

every block of the commutator vanishes. Hence

\[
\boxed{[H,\Sigma_G]=0.}
\]

This is an exact algebraic statement under the stated hypotheses.

For a time-dependent family, the corresponding standard invariant equation is

\[
\boxed{
\partial_t\Sigma_G+
\frac{i}{\hbar}[H(t),\Sigma_G(t)]=0.
}
\]

## 3. Tetrahedral face holonomy

For canonical tetrahedral transports,

\[
\boxed{U_{01}U_{12}U_{20}=+i\Sigma_0}
\]

and for the opposite orientation

\[
\boxed{U_{02}U_{21}U_{10}=-i\Sigma_0.}
\]

Thus

\[
W^2=-I,
\qquad
W^4=I,
\qquad
[W,\Sigma_0]=0.
\]

The spherical triangle determined by one tetrahedral face has

\[
\cos s=-\frac13,
\qquad
A=\frac{2\pi}{3},
\qquad
\boxed{\Omega=3A-\pi=\pi.}
\]

Therefore the typed relation is

\[
\boxed{
-\frac13\ \text{tetrahedral geometry}
\longrightarrow
\pi\ \text{face holonomy}
\longrightarrow
[1/2]\ \text{turn class}.
}
\]

This does not identify \(1/3\) with \(1/2\).

## 4. Loop consistency

For any compatible closed loop \(\gamma\),

\[
W_\gamma=\prod_{(ab)\in\gamma}U_{ab}
\]

must satisfy

\[
\boxed{[W_\gamma,\Sigma_a]=0}
\]

at the loop base node.

The validator includes a negative control. Replacing one compatible edge transport with the identity makes the global commutator nonzero, so the invariant is not obtained automatically from graph connectivity alone.

## 5. Periodic extension

For a periodic graph or simplicial complex with Bloch–Floquet fibers \(H(k)\), a compatible sector must satisfy

\[
\boxed{[H(k),\Sigma_G(k)]=0\quad\forall k.}
\]

For a regular \(n\)-simplex,

\[
\mathbf v_i\cdot\mathbf v_j=-\frac1n.
\]

A higher-dimensional realization may use a Clifford representation with

\[
\{\Gamma(\mathbf v),\Gamma(\mathbf w)\}=2(\mathbf v\cdot\mathbf w)I.
\]

The abstract graph theorem remains exact if its intertwining hypotheses hold. A specific periodic \(n\)-simplex realization remains `CONDITIONAL` until its representation, gluing data, loop holonomies, and Bloch sectors are explicitly validated.

## 6. Relation to the information-energy operator

This branch descends from `feat/information-energy-bifurcation-v0.1`, so both nonparadoxical operators coexist on one auditable lineage.

The present operator does **not** derive the information-control map \(\mu(I)\), does not identify its graph spectrum with physical energy, and does not alter the existing `OPEN` status of those bindings.

A future periodic model may test both conditions simultaneously:

\[
[H(k),\Sigma_G(k)]=0
\]

and a separately specified spectral bifurcation condition. No equivalence between those two conditions is claimed here.

## 7. Claim table

| Statement | Status |
|---|---|
| tetrahedral local involutions | `EXACT` |
| canonical edge unitarity and intertwining | `EXACT` |
| graph commutator theorem under stated hypotheses | `EXACT` |
| tetrahedral face holonomy \(\pm i\Sigma\) | `EXACT` |
| tetrahedral spherical excess \(\pi\) | `EXACT` |
| time-dependent invariant equation | `STANDARD_INVARIANT_EQUATION` |
| periodic Bloch compatibility gate | `EXACT_GIVEN_SPECIFIED_PERIODIC_DATA` |
| general periodic \(n\)-simplex realization | `CONDITIONAL` |
| information-to-\(\mu\) binding | `OPEN` |
| physical-energy binding | `OPEN` |
| personal/biological/physical identity binding | `NOT_CLAIMED` |
