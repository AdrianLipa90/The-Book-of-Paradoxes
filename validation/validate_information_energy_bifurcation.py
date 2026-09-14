#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

TOL = 1e-12
ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "operators/nonparadoxical/information_energy_bifurcation/Q28_RECEIPT_V0_1.json"
EXPECTED_BACKEND_SHA256 = "4b1b628186fa4960533cb6007c0f133b0064aebe7d8c5eaed8a6578c363a574c"


def energy(h: float, mu: float) -> float:
    return 0.25 * h**4 - 0.5 * mu * h**2


def grad(h: float, mu: float) -> float:
    return h**3 - mu * h


def hessian(h: float, mu: float) -> float:
    return 3.0 * h**2 - mu


def z_from_h(h: float) -> float:
    return math.tanh(h / 2.0)


def h_from_z(z: float) -> float:
    return 2.0 * math.atanh(z)


def phase_code(mu: float) -> list[float]:
    out: list[float] = []
    for k in range(18):
        h = 2.0 ** (-k / 2.0)
        for x in (-h, h):
            out.append(math.pi if grad(x, mu) < 0.0 else 0.0)
    return out


def flipped_scales(mu: float) -> int:
    base = phase_code(0.0)
    cur = phase_code(mu)
    flips = sum(a != b for a, b in zip(base, cur))
    assert flips % 2 == 0
    return flips // 2


def overlap_prediction(mu: float) -> float:
    return 1.0 - flipped_scales(mu) / 9.0


def check_exact_kernel() -> None:
    for mu in (-4.0, -1.0, -0.25):
        assert hessian(0.0, mu) > 0.0
        assert energy(0.0, mu) == 0.0
        for h in (-2.0, -0.5, 0.5, 2.0):
            assert energy(h, mu) > 0.0

    assert hessian(0.0, 0.0) == 0.0
    assert energy(0.0, 0.0) == 0.0
    for h in (-2.0, -0.5, 0.5, 2.0):
        assert energy(h, 0.0) > 0.0

    for mu in (0.01, 0.1, 0.25, 0.5, 1.0, 4.0):
        hstar = math.sqrt(mu)
        assert abs(grad(hstar, mu)) < TOL
        assert abs(grad(-hstar, mu)) < TOL
        assert hessian(0.0, mu) < 0.0
        assert abs(hessian(hstar, mu) - 2.0 * mu) < TOL
        assert abs(energy(hstar, mu) + mu * mu / 4.0) < TOL
        z = z_from_h(hstar)
        assert 0.0 < z < 1.0
        assert abs(h_from_z(z) - hstar) < TOL


def check_control() -> None:
    for mu in (-4.0, -1.0, 0.0, 1.0, 4.0):
        assert 1.0 + mu * mu > 0.0
        for h in (-2.0, -0.5, 0.5, 2.0):
            g = h**3 + (1.0 + mu * mu) * h
            assert g * h > 0.0


def check_receipt() -> None:
    r = json.loads(RECEIPT.read_text(encoding="utf-8"))
    assert r["schema"] == "BOOK_OF_PARADOXES_INFORMATION_ENERGY_BIFURCATION_Q28_RECEIPT_V0_1"
    assert r["claim_scope"]["physical_qpu_claim"] is False
    assert r["claim_scope"]["quantum_speedup_claim"] is False
    assert r["claim_scope"]["information_to_mu_binding"] == "OPEN"
    assert r["claim_scope"]["physical_energy_binding"] == "OPEN"

    q = r["q28_execution"]
    assert q["backend_sha256"] == EXPECTED_BACKEND_SHA256
    assert q["capacity"]["max_qubits"] == 28
    assert q["capacity"]["mode_address_qubits"] == 6
    assert q["capacity"]["workspace_qubits"] == 22
    assert q["capacity"]["physical_qpu_claim"] is False
    assert q["max_norm_error"] < TOL
    assert q["max_dense_sparse_amplitude_delta"] < TOL
    assert all(q["verdicts"].values())

    for row in q["representative_rows"]:
        mu = float(row["mu"])
        n = flipped_scales(mu)
        predicted = 1.0 - n / 9.0
        assert int(row["flipped_scales"]) == n
        assert int(row["n_qubits"]) == 28
        assert abs(float(row["predicted"]) - predicted) < TOL
        assert abs(float(row["overlap_real"]) - predicted) < TOL
        assert float(row["overlap_err"]) < TOL
        assert float(row["norm_err"]) < TOL

    assert int(q["control_sample_count"]) == 9
    assert q["control_mu_range"] == [-4.0, 4.0]
    assert float(q["control_max_err_from_one"]) < TOL
    assert float(q["control_max_norm_error"]) < TOL
    assert float(q["max_overlap_error"]) < TOL

    first_positive = next(row for row in q["representative_rows"] if float(row["mu"]) > 0.0)
    expected_first = 1.1 * 2.0 ** -17
    assert abs(float(first_positive["mu"]) - expected_first) < 1e-18
    assert int(first_positive["flipped_scales"]) == 1


def main() -> None:
    check_exact_kernel()
    check_control()
    check_receipt()
    print("PASS exact Poincare pitchfork kernel")
    print("PASS exact 36-phase overlap law")
    print("PASS negative control")
    print("PASS pinned Q28 28-qubit sparse witness")
    print("PASS proof-firewall metadata")
    print("VERDICT: PASS")


if __name__ == "__main__":
    main()
