# Banach–Tarski: tetrahedral/stella-octangula reduction

Status: `CLOSED_REDUCTION`

## 1. Scope

This note does **not** re-prove the Banach–Tarski theorem from first principles.
It isolates a non-arbitrary geometric route from the tetrahedral Gram class used
in TIR to the classical free-rotation kernel used in Banach–Tarski.

The final equidecomposition step remains the standard theorem and uses the Axiom
of Choice.

## 2. Pinned TIR source

Pinned TIR commit:

`1c58548e1f9387158c25d717a6ac081c70b4b7d6`

Source:

`TIR/integration/TIR_TETRAHEDRAL_CONGRUENCE_CLASS_CLOSURE_V0_1.md`

The exact common tetrahedral Gram class is

\[
n_i\cdot n_j=
\begin{cases}
1,&i=j,\\
-1/3,&i\ne j,
\end{cases}
\qquad
\sum_{i=1}^4 n_i=0,
\qquad
\sum_{i=1}^4n_in_i^T=\frac43I_3.
\]

A canonical representative is

\[
n_1=\frac1{\sqrt3}(1,1,1),\quad
n_2=\frac1{\sqrt3}(1,-1,-1),
\]

\[
n_3=\frac1{\sqrt3}(-1,1,-1),\quad
n_4=\frac1{\sqrt3}(-1,-1,1).
\]

## 3. Canonical antipodal completion

Define

\[
T_+=\{n_1,n_2,n_3,n_4\},
\qquad
T_-=-T_+.
\]

The antipodally closed set

\[
\Sigma=T_+\cup T_-
\]

is the eight-vertex stella-octangula/cube vertex set

\[
\Sigma=
\left\{
\frac1{\sqrt3}(\pm1,\pm1,\pm1)
\right\}.
\]

This is a canonical construction once antipodal closure is required; it is not
claimed here that TIR dynamics independently forces that closure.

The full Gram matrix is

\[
G_8=
\begin{pmatrix}
G_4&-G_4\\
-G_4&G_4
\end{pmatrix},
\qquad
G_4=\frac43I_4-\frac13\mathbf1\mathbf1^T.
\]

Hence `rank(G_8)=3`, with eigenvalues `8/3` (multiplicity 3) and `0`
(multiplicity 5).

## 4. Cross-sector relation alphabet

For `i != j`,

\[
n_i\cdot(-n_j)=+\frac13.
\]

For pure Bloch states, using

\[
R(n,m)=\frac{1+n\cdot m}{2},
\]

the stella relation alphabet is

\[
R\in\left\{0,\frac13,\frac23,1\right\}.
\]

In particular, every unmatched cross-sector pair has

\[
R(n_i,-n_j)=\frac23.
\]

Therefore its Bloch separation angle satisfies

\[
\boxed{\cos\theta=\frac13},
\qquad
\boxed{\theta=\arccos(1/3)}.
\]

The corresponding Fubini–Study distance is

\[
d_{FS}=\frac{\theta}{2}
=\arccos\sqrt{\frac23}.
\]

## 5. Orthogonal-axis lemma

For an ordered unmatched cross-sector pair define the minimal-rotation axis

\[
a_{ij}
:=
\frac{n_i\times(-n_j)}
{\|n_i\times(-n_j)\|}.
\]

Take a perfect matching of the tetrahedral labels,

\[
(ij\mid kl),
\qquad
\{i,j,k,l\}=\{1,2,3,4\}.
\]

Then

\[
\begin{aligned}
(n_i\times n_j)\cdot(n_k\times n_l)
&=(n_i\cdot n_k)(n_j\cdot n_l)
 -(n_i\cdot n_l)(n_j\cdot n_k)\\
&=\left(-\frac13\right)^2
 -\left(-\frac13\right)^2\\
&=0.
\end{aligned}
\]

Thus

\[
\boxed{a_{ij}\perp a_{kl}}.
\]

The three perfect matchings are

\[
(12\mid34),\qquad
(13\mid24),\qquad
(14\mid23).
\]

So the tetrahedral Gram class plus antipodal closure supplies both ingredients
of the classical free-rotation construction:

\[
\boxed{\text{common angle }\arccos(1/3)}
\]

and

\[
\boxed{\text{orthogonal rotation axes}}.
\]

Neither numerical ingredient is fitted.

## 6. Explicit generator witness

For the matching `(14|23)`, choose oriented axes

\[
a=\frac{(-1,1,0)}{\sqrt2},
\qquad
b=\frac{(1,1,0)}{\sqrt2}.
\]

Minimal rotations of angle

\[
\theta=\arccos(1/3)
\]

may be represented by

\[
A=
\frac13
\begin{pmatrix}
2&-1&2\\
-1&2&2\\
-2&-2&1
\end{pmatrix},
\]

\[
B=
\frac13
\begin{pmatrix}
2&1&-2\\
1&2&2\\
2&-2&1
\end{pmatrix}.
\]

They satisfy exactly

\[
A^TA=B^TB=I,
\qquad
\det A=\det B=1,
\]

\[
\frac{\operatorname{tr}A-1}{2}
=
\frac{\operatorname{tr}B-1}{2}
=
\frac13,
\]

and, for the canonical tetrahedral representative,

\[
A n_1=-n_4,
\qquad
B n_2=-n_3.
\]

Their rotation axes are orthogonal.

Any oriented pair of orthogonal axes is related to the standard coordinate-axis
pair by one element of `SO(3)`. Therefore `(A,B)` is simultaneously conjugate
to the classical orthogonal-axis rotation pair with angle `arccos(1/3)`.

The standard free-rotation theorem then gives

\[
\boxed{\langle A,B\rangle\cong F_2}.
\]

This freeness is a standard theorem input, not inferred from finite numerical
search.

## 7. SU(2) lift

For any unmatched cross-sector pair, the minimal spin lift can be written

\[
W_{ij}^{BT}
=
\sqrt{\frac23}\,I
-
\frac{i}{\sqrt3}\,a_{ij}\cdot\sigma
\in SU(2),
\]

with

\[
\operatorname{Ad}(W_{ij}^{BT})\in SO(3)
\]

equal to the corresponding rotation of angle `arccos(1/3)`.

This is type-compatible with the TIR spatial transport family

\[
W_{ij}^{X}\in SU(2),
\qquad
R_{ij}=\operatorname{Ad}_{W_{ij}^{X}}\in SO(3).
\]

No claim is made here that every dynamical TIR `W_ij^X` must equal this minimal
transport.

## 8. Classical Banach–Tarski tail

Once

\[
F_2<SO(3)
\]

is available, the remaining chain is classical:

\[
F_2
\to
\text{paradoxical decomposition of }F_2
\to
\text{free action on }S^2\setminus D
\to
\text{paradoxical decomposition of }S^2
\to
\text{radial extension / absorption}
\to
B^3\sim B^3\sqcup B^3.
\]

Here `D` is the countable union of fixed-point sets of nonidentity group
elements. Selecting orbit representatives invokes Choice.

The result does **not** mean ordinary volume satisfies `1 = 2`; the pieces are
non-Lebesgue-measurable, so finite additivity of Lebesgue volume is not
available for the decomposition pieces.

## 9. Computational validator

Run

```text
python validation/validate_banach_tarski_stella.py
```

The validator checks:

- tetrahedral Gram data;
- stella dot-product spectrum;
- all three perfect-matching axis orthogonalities;
- exact `SO(3)` identities for `A` and `B`;
- exact endpoint maps;
- `cos(theta)=1/3`;
- a bounded reduced-word nonidentity witness through length 12.

The word search is explicitly classified `NUMERICAL/FINITE WITNESS`; the
infinite freeness claim uses the standard theorem above.

## 10. Verdict

\[
\boxed{\text{BANACH--TARSKI: CLOSED REDUCTION}}
\]

The genuinely new bridge recorded here is

\[
\boxed{
\text{tetrahedral Gram}
\to
\text{antipodal stella completion}
\to
\cos\theta=\frac13
+
\text{orthogonal axes}
\to
\text{classical free-rotation kernel}.
}
\]

## References

1. TIR pinned source:
   `AdrianLipa90/The-Fundamental-Theory-of-Informational-Relations`,
   commit `1c58548e1f9387158c25d717a6ac081c70b4b7d6`,
   `TIR/integration/TIR_TETRAHEDRAL_CONGRUENCE_CLASS_CLOSURE_V0_1.md`.
2. Isabelle AFP, *Banach–Tarski Paradox* formalization, including the free
   rotations in `SO(3)` and the equidecomposition chain.
3. Standard Banach–Tarski proofs using orthogonal rotations with
   `cos(theta)=1/3`.
