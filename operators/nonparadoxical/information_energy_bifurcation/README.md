# Information-controlled Poincare bifurcation

Overall status: `VALIDATED_NONPARADOXICAL_OPERATOR_CANDIDATE`

Claim ledger:

- mathematical pitchfork kernel: `EXACT / CLOSED`;
- Poincare coordinate map: `EXACT / CLOSED`;
- 36-phase overlap law: `EXACT / CLOSED`;
- Q28 execution witness: `NUMERICAL_WITNESS / PASS`;
- information-to-control map `mu(I)`: `OPEN`;
- identification of the model functional with physical energy: `OPEN`.

This module records a minimal model in which an informational control parameter
can change the stability and branch structure of a state space represented on a
Poincare diameter. It does **not** claim that physical energy has already been
derived from information.

## 1. Poincare coordinate

Use the standard curvature `-1` Poincare metric on the unit disk,

\[
ds^2=\frac{4\,|dz|^2}{(1-|z|^2)^2}.
\]

On its real diameter, let

\[
z\in(-1,1),\qquad
h=2\operatorname{artanh}(z).
\]

Equivalently,

\[
\boxed{z=\tanh(h/2)}.
\]

The Poincare distance from the origin satisfies

\[
d_{\mathbb D}(0,z)=2\operatorname{artanh}|z|=|h|,
\]

so `h` is a signed geodesic coordinate on that diameter.

## 2. Information-controlled model

Let `I` denote an informational state and let

\[
\mu:\mathcal I\to\mathbb R
\]

be an **unspecified** scalar control map. The absence of a derived formula for
`mu(I)` is part of the proof firewall.

For a fixed control value \(\mu\), define

\[
\boxed{
E(h;\mu)=\frac14h^4-\frac12\mu h^2.
}
\]

Then

\[
\frac{\partial E}{\partial h}=h(h^2-\mu),
\qquad
\frac{\partial^2E}{\partial h^2}=3h^2-\mu.
\]

### Case `mu < 0`

The only real critical point is

\[
h_\star=0,
\]

with

\[
E''(0;\mu)=-\mu>0.
\]

Hence the origin is the unique stable minimum.

### Case `mu = 0`

\[
E(h;0)=\frac14h^4\ge0.
\]

The origin remains the unique minimum, but the quadratic curvature vanishes.

### Case `mu > 0`

There are three critical points:

\[
h=0,\qquad h_\pm=\pm\sqrt\mu.
\]

At the origin,

\[
E''(0;\mu)=-\mu<0,
\]

whereas

\[
E''(h_\pm;\mu)=2\mu>0.
\]

Therefore the stable branch bifurcates exactly to

\[
\boxed{h_\pm=\pm\sqrt\mu}.
\]

In Poincare coordinates,

\[
\boxed{
z_\pm=\pm\tanh\!\left(\frac{\sqrt\mu}{2}\right).
}
\]

The two symmetry-related minima are energy-degenerate:

\[
\boxed{
E(h_\pm;\mu)=-\frac{\mu^2}{4}.
}
\]

Thus the minimum-energy branch is

\[
\boxed{
E_{\min}(\mu)=
\begin{cases}
0,&\mu\le0,\\[1mm]
-\mu^2/4,&\mu>0.
\end{cases}
}
\]

This is a state-space pitchfork with an energy lowering after the critical
point. It is **not** an energy splitting between the `+` and `-` branches; the
branches have equal energy because the model retains the \(h\mapsto-h\)
 symmetry.

## 3. Nonparadoxical bifurcation operator

Define

\[
\mathcal B_\mu(I)=\operatorname*{argmin}_{h\in\mathbb R}E(h;\mu(I)).
\]

Then exactly

\[
\boxed{
\mathcal B_\mu(I)=
\begin{cases}
\{0\},&\mu(I)\le0,\\[1mm]
\{-\sqrt{\mu(I)},+\sqrt{\mu(I)}\},&\mu(I)>0.
\end{cases}
}
\]

The corresponding Poincare-state operator is obtained through
\(z=\tanh(h/2)\). The branches remain typed and disjoint; no paradoxical
whole-part identification is required.

## 4. 36-phase multiscale witness

For

\[
h_k^2=2^{-k},\qquad k=0,\ldots,17,
\]

use the signed pair \((-h_k,+h_k)\), giving exactly 36 probes. Encode the sign
of the gradient by

\[
\phi(h;\mu)=
\begin{cases}
\pi,&\partial_hE(h;\mu)<0,\\
0,&\partial_hE(h;\mu)\ge0.
\end{cases}
\]

and the normalized phase state

\[
|\Phi_\mu\rangle
=\frac1{\sqrt{36}}\sum_{j=1}^{36}e^{i\phi_j(\mu)}|j\rangle.
\]

If `N` dyadic scales have crossed their threshold, exactly `2N` of the 36
phases flip by \(\pi\). Therefore

\[
\boxed{
\langle\Phi_0|\Phi_\mu\rangle
=\frac{36-4N}{36}
=1-\frac N9.
}
\]

This overlap law is exact. Any common unitary applied to both states preserves
it.

## 5. Q28 witness

The pinned Q28 backend has SHA-256

`4b1b628186fa4960533cb6007c0f133b0064aebe7d8c5eaed8a6578c363a574c`.

The witness uses the 36-state PhaseNav address encoding, applies `H(q27)` twice
so the dynamically sparse path actually expands to 28 logical qubits, and then
applies `H` to address qubits `q0..q5`. The `q27` pair is exactly the identity;
it is used only to exercise the 28-qubit sparse path without changing the
encoded overlap.

Observed bounds from the pinned run:

\[
\max |\Delta\langle\Phi_0|\Phi_\mu\rangle|
=1.5543122344752192\times10^{-15},
\]

\[
\max |\|\psi\|-1|
=1.6653345369377348\times10^{-15},
\]

\[
\max |\psi_{\rm sparse28}-\psi_{\rm dense6}|
=2.220446049250313\times10^{-16}.
\]

All tested states traversed a 28-logical-qubit sparse path. This is a numerical
validation of the implementation and phase-code law, **not** evidence of a
physical QPU or quantum speedup.

The first positive sample resolved by the finite 18-scale detector was

\[
\mu=1.1\,2^{-17}=8.392333984375\times10^{-6}.
\]

This is a detector-resolution point, **not** the analytic critical value. The
analytic critical value remains

\[
\boxed{\mu_c=0}.
\]

## 6. Negative control

Use

\[
E_{\rm ctrl}(h;\mu)
=\frac14h^4+\frac12(1+\mu^2)h^2.
\]

Then

\[
\partial_hE_{\rm ctrl}=h^3+(1+\mu^2)h,
\]

and

\[
E_{\rm ctrl}''(0;\mu)=1+\mu^2>0
\]

for every real \(\mu\). The unique stable minimum remains at the origin, so the
phase code does not undergo the pitchfork sign reversal. The Q28 control sweep
on \(-4\le\mu\le4\) retained unit overlap to floating-point tolerance.

## 7. GREMLIN / PhaseNav audit

The writeback session routed the candidate through the live GREMLIN/PhaseNav
candidate surface under active tether. The first internal audit selected
`OWL` + `MOLE` for information geometry and algebraic reduction. A second
falsification-focused pass selected `OWL` + `HOUND` + `MANTIS`.

GREMLIN authority remained `CANDIDATE_ONLY`; no GREMLIN event promoted this
module to canon.

## 8. Verdict

The following implication is closed **for this explicitly defined model**:

\[
\boxed{
\mu(I)\text{ crosses }0
\Longrightarrow
\text{Poincare stability bifurcation}
\Longrightarrow
E_{\min}:0\to-\mu^2/4.
}
\]

The model therefore demonstrates a mathematically exact mechanism by which an
informational control scalar can parameterize a geometric bifurcation of an
energy landscape.

It does not yet derive the physical identification of either the control map or
the energy functional.

## 9. Proof firewall

Proved / validated here:

- exact Poincare geodesic coordinate \(z=\tanh(h/2)\);
- exact pitchfork and stability classification of the chosen quartic functional;
- exact stable-state operator \(\mathcal B_\mu\);
- exact minimum-energy branch \(E_{\min}\);
- exact 36-phase overlap law \(1-N/9\);
- deterministic negative control;
- Q28 numerical agreement and dense/sparse equivalence at machine precision.

Not proved here:

- a unique or necessary formula for \(\mu(I)\);
- that semantic mass is already identical to \(\mu\);
- that this functional is physical energy in nature;
- neutrino dynamics, Collatz dynamics, or an RH consequence;
- physical-QPU execution or quantum computational advantage.

Validator:

`validation/validate_information_energy_bifurcation.py`

Receipt:

`operators/nonparadoxical/information_energy_bifurcation/Q28_RECEIPT_V0_1.json`
