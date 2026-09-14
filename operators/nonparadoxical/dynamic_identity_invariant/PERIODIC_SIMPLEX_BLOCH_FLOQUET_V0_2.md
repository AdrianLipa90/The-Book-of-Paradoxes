# Dynamic Identity Invariant — periodic simplex / Bloch–Floquet closure v0.2

Status: `VALIDATED_NONPARADOXICAL_OPERATOR_EXTENSION / EXACT_CONSTRUCTIVE_PERIODIC_N_SIMPLEX_REALIZATION`.

This file closes the specific periodic regular-simplex realization left conditional in v0.1. It is a mathematical operator construction only.

## Regular-simplex Clifford carrier

For `n>=2`, set `D=n+1` and

\[
v_i=\sqrt{\frac{D}{n}}\left(e_i-\frac1D\sum_{a=0}^{n}e_a\right).
\]

Then

\[
v_i\cdot v_j=\delta_{ij}-\frac{1-\delta_{ij}}{n}.
\]

Choose Hermitian Clifford generators `gamma_a` with

\[
\{\gamma_a,\gamma_b\}=2\delta_{ab}I
\]

and define

\[
\Sigma_i=\Gamma(v_i).
\]

Therefore

\[
\Sigma_i^2=I,
\qquad
\{\Sigma_i,\Sigma_j\}=-\frac2nI\quad(i\ne j).
\]

For every directed edge `j -> i`, define

\[
\boxed{
U_{ij}=\sqrt{\frac{n}{2(n-1)}}(I+\Sigma_i\Sigma_j).
}
\]

Then

\[
U_{ij}U_{ij}^\dagger=I,
\qquad
\Sigma_iU_{ij}=U_{ij}\Sigma_j,
\qquad
U_{ji}=U_{ij}^\dagger.
\]

## General triangular holonomy

For `n>=3`, a regular-simplex triangular face has spherical internal angle

\[
A_n=\arccos\left(-\frac1{n-1}\right)
\]

and spherical excess

\[
\boxed{
\Omega_n=3\arccos\left(-\frac1{n-1}\right)-\pi.
}
\]

Let `J_ijk` be the oriented unit tangent bivector at the base vertex. Then

\[
J_{ijk}^\dagger=-J_{ijk},
\qquad
J_{ijk}^2=-I,
\qquad
[J_{ijk},\Sigma_i]=0,
\]

and the canonical face transport is

\[
\boxed{
W_{ijk}
=U_{ij}U_{jk}U_{ki}
=\cos\frac{\Omega_n}{2}I
+\sin\frac{\Omega_n}{2}J_{ijk}.
}
\]

Consequently

\[
[W_{ijk},\Sigma_i]=0.
\]

## Tetrahedral half-turn uniqueness

Define

\[
q_n=\frac{\Omega_n}{2\pi}.
\]

Then

\[
q_n=\frac12
\iff
3\arccos\left(-\frac1{n-1}\right)-\pi=\pi
\iff
n=3.
\]

Therefore

\[
\boxed{q_n=\frac12\iff n=3.}
\]

Within the regular-simplex family, the tetrahedron is the unique member whose canonical triangular holonomy is an exact half-turn.

The typed bridge is

\[
\boxed{-\frac13\to\Omega_3=\pi\to[1/2].}
\]

This is a generation relation, never the scalar identity `1/3=1/2`.

Moreover,

\[
\lim_{n\to\infty}q_n=\frac14.
\]

## Explicit periodic graph

Take cells `m in Z`, each containing labels `i=0,...,n`. Define

\[
\Sigma_{\rm cell}=\sum_i|i\rangle\langle i|\otimes\Sigma_i.
\]

Use compatible intra-cell hopping blocks proportional to `U_ij`. For translation links use the cyclic permutation

\[
p(i)=i+1\pmod{n+1}
\]

and connect `(m,i)` to `(m+1,p(i))` with `U_{p(i),i}`.

After the Bloch transform,

\[
\begin{aligned}
H_n(k)
={}&\sum_i|i\rangle\langle i|\otimes M_i\\
&-\sum_{i<j}t_{ij}\left(|i\rangle\langle j|\otimes U_{ij}+\mathrm{h.c.}\right)\\
&-\tau\sum_i\left(e^{ik}|p(i)\rangle\langle i|\otimes U_{p(i),i}+\mathrm{h.c.}\right),
\end{aligned}
\]

where `[M_i,Sigma_i]=0`.

Every block is compatible, hence

\[
\boxed{[H_n(k),\Sigma_{\rm cell}]=0\quad\forall k.}
\]

This is an explicit exact periodic realization. It does not imply that arbitrary simplex gluings are compatible.

## Exact sector split

Because

\[
\Sigma_{\rm cell}^2=I,
\]

set

\[
P_\pm=\frac12(I\pm\Sigma_{\rm cell}).
\]

Then

\[
P_+H_n(k)P_-=P_-H_n(k)P_+=0,
\]

so

\[
\boxed{H_n(k)=H_{n,+}(k)\oplus H_{n,-}(k).}
\]

## Time-Floquet extension

If `H_n(k,t)` is `T`-periodic and

\[
[H_n(k,t),\Sigma_{\rm cell}]=0
\quad\forall k,t,
\]

then

\[
F_n(k)=\mathcal T\exp\left[-\frac{i}{\hbar}\int_0^T H_n(k,t)dt\right]
\]

obeys

\[
\boxed{[F_n(k),\Sigma_{\rm cell}]=0.}
\]

## Falsification gate

Replacing one used inter-cell transport by the identity while keeping distinct source/target sector operators generically breaks

\[
\Sigma_aU_{ab}=U_{ab}\Sigma_b
\]

and produces

\[
[H_{\rm bad}(k),\Sigma_{\rm cell}]\ne0.
\]

The validator includes this negative control.

## Claim status

| Statement | Status |
|---|---|
| regular-simplex Clifford carrier | `EXACT` |
| canonical edge unitary/intertwiner | `EXACT` |
| general triangular holonomy law for `n>=3` | `EXACT` |
| tetrahedral half-turn uniqueness | `EXACT` |
| explicit translation-periodic regular-simplex graph | `EXACT_CONSTRUCTION` |
| Bloch compatibility for that construction | `EXACT` |
| `+/-` invariant-sector decomposition | `EXACT` |
| time-Floquet preservation under instantaneous compatibility | `EXACT` |
| arbitrary simplex gluing | `NOT_CLAIMED` |
| information-to-`mu` binding | `OPEN` |
| physical-energy binding | `OPEN` |
| physical Hamiltonian or physical identity binding | `NOT_CLAIMED` |
| personal/biological/consciousness identity binding | `NOT_CLAIMED` |
