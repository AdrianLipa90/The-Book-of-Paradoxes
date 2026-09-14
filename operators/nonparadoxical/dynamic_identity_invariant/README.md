# Dynamic Identity Invariant

Status: `VALIDATED_NONPARADOXICAL_OPERATOR / PERIODIC_SIMPLEX_V0_2_CLOSED`.

This operator library entry records a transport-compatible invariant on tetrahedral/Stella, abstract graph, and one explicit periodic regular-simplex carrier. It is not classified as a paradox.

No biological, psychological, personal, consciousness, or physical identity binding is claimed.

## 1. Local sector

For a unit local frame, define a Hermitian involution `Sigma_a`. On the tetrahedral Pauli carrier,

\[
\Sigma_a=\mathbf n_a\cdot\boldsymbol\sigma,
\qquad
\Sigma_a^2=I,
\]

with

\[
\mathbf n_i\cdot\mathbf n_j=-\frac13\qquad(i\ne j).
\]

For non-antipodal frames define

\[
\boxed{
U_{ab}=\frac{I+\Sigma_a\Sigma_b}
{\sqrt{2(1+\mathbf n_a\cdot\mathbf n_b)}}.
}
\]

Then

\[
U_{ab}U_{ab}^\dagger=I,
\qquad
\boxed{\Sigma_aU_{ab}=U_{ab}\Sigma_b.}
\]

## 2. Graph operator

On a node graph define

\[
\boxed{
\Sigma_G=\sum_a|a\rangle\langle a|\otimes\Sigma_a.
}
\]

If `[M_a,Sigma_a]=0` on every node and every used edge satisfies the intertwining equation, then the compatible block Hamiltonian obeys

\[
\boxed{[H,\Sigma_G]=0.}
\]

For a time-dependent family the standard invariant equation is

\[
\boxed{
\partial_t\Sigma_G+\frac{i}{\hbar}[H(t),\Sigma_G(t)]=0.
}
\]

## 3. Tetrahedral face holonomy

For canonical tetrahedral transports,

\[
U_{01}U_{12}U_{20}=+i\Sigma_0,
\qquad
U_{02}U_{21}U_{10}=-i\Sigma_0.
\]

Hence

\[
W^2=-I,
\qquad
W^4=I,
\qquad
[W,\Sigma_0]=0.
\]

The tetrahedral spherical face has

\[
A=\frac{2\pi}{3},
\qquad
\boxed{\Omega=\pi.}
\]

Therefore

\[
\boxed{-\frac13\to\Omega_3=\pi\to[1/2].}
\]

This is a generation relation; `1/3=1/2` is not asserted.

## 4. v0.2 regular-simplex closure

The explicit v0.2 construction is documented in

`PERIODIC_SIMPLEX_BLOCH_FLOQUET_V0_2.md`.

For `n>=2`, a centered regular `n`-simplex is represented by Clifford involutions `Sigma_i` with

\[
\{\Sigma_i,\Sigma_j\}=-\frac2nI\qquad(i\ne j),
\]

and canonical edge transport

\[
\boxed{
U_{ij}=\sqrt{\frac{n}{2(n-1)}}(I+\Sigma_i\Sigma_j).
}
\]

For `n>=3`, the triangular face turn fraction is

\[
\boxed{
q_n=\frac{3\arccos[-1/(n-1)]-\pi}{2\pi}.
}
\]

Exactly,

\[
\boxed{q_n=\frac12\iff n=3.}
\]

Thus the tetrahedron is the unique regular simplex whose canonical triangular holonomy is an exact half-turn.

## 5. Explicit periodic Bloch construction

Use integer cells, a cyclic simplex-label permutation between neighboring cells, and the same compatible `U_ij` on every intra- and inter-cell edge. The Bloch fiber satisfies

\[
\boxed{[H_n(k),\Sigma_{\rm cell}]=0\quad\forall k.}
\]

Because `Sigma_cell^2=I`, the projectors

\[
P_\pm=\frac12(I\pm\Sigma_{\rm cell})
\]

give

\[
\boxed{P_+H_n(k)P_-=P_-H_n(k)P_+=0.}
\]

This closes one explicit periodic regular-simplex realization. Arbitrary gluings remain subject to the edge-intertwining gate.

If a time-periodic `H_n(k,t)` commutes with `Sigma_cell` for every `k,t`, its one-period Floquet propagator also commutes with `Sigma_cell`.

## 6. Falsification

The validator retains a negative control. Replacing one compatible transport by the identity while its source and target local operators differ produces a nonzero global commutator.

The v0.2 validation additionally checks the regular-simplex turn-fraction law over a finite sample and the exact tetrahedral half-turn value. The general theorem is supplied by the algebraic derivation in the v0.2 document; the finite computation is a witness, not its proof.

## 7. Relation to the information-energy operator

This branch descends from `feat/information-energy-bifurcation-v0.1`, so both nonparadoxical operators coexist on one auditable lineage.

The DII operator does not derive the information-control map `mu(I)`, does not identify its spectrum with physical energy, and does not alter the existing `OPEN` status of those bindings.

## 8. Claim table

| Statement | Status |
|---|---|
| tetrahedral local involutions | `EXACT` |
| canonical edge unitarity and intertwining | `EXACT` |
| graph commutator theorem under stated hypotheses | `EXACT` |
| tetrahedral face holonomy `+/- i Sigma` | `EXACT` |
| regular-simplex triangular holonomy law | `EXACT` |
| tetrahedral half-turn uniqueness in regular-simplex family | `EXACT` |
| explicit periodic regular-simplex realization | `EXACT_CONSTRUCTION` |
| Bloch compatibility for that construction | `EXACT` |
| `+/-` invariant-sector split | `EXACT` |
| time-Floquet preservation under instantaneous compatibility | `EXACT` |
| arbitrary periodic simplex gluing | `NOT_CLAIMED` |
| information-to-`mu` binding | `OPEN` |
| physical-energy binding | `OPEN` |
| personal/biological/consciousness/physical identity binding | `NOT_CLAIMED` |
