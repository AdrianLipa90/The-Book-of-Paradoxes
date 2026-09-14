#!/usr/bin/env python3
"""Exact/finite audit for the Zeno contraction reduction.

This validator uses Fraction arithmetic only. Finite iteration checks are
regressions; the identities themselves are proved algebraically in the note.
"""
from fractions import Fraction as F
import json


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]


def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(2)] for i in range(2)]


def scale(c, A):
    return [[c * A[i][j] for j in range(2)] for i in range(2)]


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def mv(A, x):
    return [sum(A[i][j] * x[j] for j in range(2)) for i in range(2)]


def mpow(A, n):
    I = [[F(1), F(0)], [F(0), F(1)]]
    out = I
    base = A
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n >>= 1
    return out


I = [[F(1), F(0)], [F(0), F(1)]]
J = [[F(0), F(1)], [F(1), F(0)]]
P = scale(F(1, 2), add(I, J))
D = scale(F(1, 2), sub(I, J))
Z0 = [[F(0), F(0)], [F(0), F(0)]]

checks = {}
checks["involution"] = mul(J, J) == I
checks["projector_P"] = mul(P, P) == P
checks["projector_D"] = mul(D, D) == D
checks["orthogonal_algebraic_split"] = mul(P, D) == Z0 and mul(D, P) == Z0
checks["resolution_identity"] = add(P, D) == I
checks["involution_split"] = sub(P, D) == J

lam = F(1, 2)
Z = add(P, scale(lam, D))
checks["zeno_power_formula_n0_12"] = all(
    mpow(Z, n) == add(P, scale(lam**n, D))
    for n in range(13)
)

x = [F(3, 7), F(-5, 11)]
Dx = mv(D, x)
checks["distinction_contraction_n0_12"] = all(
    mv(D, mv(mpow(Z, n), x)) == [lam**n * v for v in Dx]
    for n in range(13)
)

checks["dichotomy_geometric_series_n1_64"] = all(
    sum((F(1, 2)**k for k in range(1, n + 1)), F(0))
    == F(1) - F(1, 2)**n
    for n in range(1, 65)
)

# Critical-strip affine reflection as a typed application, not an RH proof.
sigma, t = F(3, 4), F(5, 7)
jr = (F(1) - sigma, t)
pr = ((sigma + jr[0]) / 2, (t + jr[1]) / 2)
dr = ((sigma - jr[0]) / 2, (t - jr[1]) / 2)
checks["riemann_affine_fixed_projection"] = pr == (F(1, 2), t)
checks["riemann_affine_distinction"] = dr == (sigma - F(1, 2), F(0))
checks["riemann_zeno_formula_n0_12"] = all(
    (F(1, 2) + lam**n * (sigma - F(1, 2)), t)
    == (pr[0] + lam**n * dr[0], pr[1] + lam**n * dr[1])
    for n in range(13)
)

passed = all(checks.values())
payload = {
    "schema": "BOOK_OF_PARADOXES_ZENO_CLOSURE_V0_1",
    "technical_status": "PASS" if passed else "FAIL",
    "claim_status": "CLOSED_REDUCTION" if passed else "UNRESOLVED",
    "lambda": "1/2",
    "finite_regression_depth": 12,
    "checks": checks,
    "firewall": {
        "proves_RH": False,
        "claims_zero_set_invariance": False,
        "finite_regression_is_proof": False,
    },
}
print(json.dumps(payload, indent=2, sort_keys=True))
raise SystemExit(0 if passed else 1)
