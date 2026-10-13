#!/usr/bin/env python3
"""Supplementary exact checks for the uniform M.4 derivation.

The manuscript proof is elementary and does not rely on execution of this file.
Only Python's standard library is used. This is not qmd-prover verification.
"""

from fractions import Fraction as Q
import json
from pathlib import Path


def polynomial(*coefficients):
    result = [Q(c) for c in coefficients]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def add(*items):
    result = [Q(0)] * max(map(len, items))
    for item in items:
        for i, value in enumerate(item):
            result[i] += value
    return polynomial(*result)


def scale(k, item):
    return polynomial(*(Q(k) * c for c in item))


def multiply(*items):
    result = polynomial(1)
    for item in items:
        coefficients = [Q(0)] * (len(result) + len(item) - 1)
        for i, a in enumerate(result):
            for j, b in enumerate(item):
                coefficients[i + j] += a * b
        result = polynomial(*coefficients)
    return result


def derivative(item):
    return polynomial(*(i * item[i] for i in range(1, len(item))))


checks = []


def check(name, condition):
    checks.append({"name": name, "passed": bool(condition)})


h = polynomial(0, 1)
L = polynomial(1, 1)
h2 = polynomial(2, 1)
h5 = polynomial(5, 1)
Dh = polynomial(2, 2, 1)
cubic = polynomial(2, -4, -1, 1)

check("geometric_j_minus_h_over_L_squared", add(multiply(h2, L), scale(-1, Dh)) == h)
check(
    "geometric_cubic_factorization",
    add(multiply(polynomial(-2, 1), polynomial(-1, 1), h2), polynomial(-2)) == cubic,
)
check(
    "geometric_j_minus_one_quarter",
    add(scale(4, multiply(h, h2)), scale(-1, multiply(L, Dh)), cubic) == polynomial(0),
)
check(
    "R_envelope_derivative",
    add(scale(4, Dh), scale(-4, multiply(h, derivative(Dh)))) == polynomial(8, 0, -4),
)
check("order_endpoint", Q(49, 10) * Q(8, 13) ** 2 - Q(39, 20) * Q(19, 20) == Q(211, 67600))
check("energy_endpoint", Q(3 * 3, 2 * 4 * 7) == Q(9, 56))
check("head_range_margin", Q(1, 6) - Q(9, 56) == Q(1, 168))
check("scaled_energy_endpoint", Q(3 * 4 * 5, 6 * 9) == Q(10, 9))
check("scaled_energy_upper", Q(10, 9) * Q(99, 10) == 11)
check("radicand_endpoint", (2 * Q(39, 20) + 5) ** 2 - 44 == Q(3521, 100))
check("radical_margin", Q(3521, 100) - Q(59, 10) ** 2 == Q(2, 5))
check("C_lower_endpoint", Q(39, 20) + Q(1, 2) + Q(59, 20) == Q(27, 5))
check("D_lower_endpoint", Q(49, 10) - Q(55, 27) == Q(773, 270))
check("D_positive_margin", Q(773, 270) - Q(20, 7) == Q(11, 1890))

# Multiply the partial-fraction identity by h(h+2)(h+5).
partial_fraction_residual = add(
    scale(Q(3, 4) - Q(39, 20), multiply(h2, h5)),
    scale(Q(3, 2), multiply(h, h5)),
    scale(Q(-54, 5), multiply(h, h2)),
    scale(Q(3, 2), multiply(polynomial(8, 7), L)),
)
check("uniform_response_partial_fractions", partial_fraction_residual == polynomial(0))

F3 = 1 + Q(3, 4 * 3) + Q(3, 2 * 5) - Q(54, 5 * 8)
Fp3 = -Q(3, 4 * 3**2) - Q(3, 2 * 5**2) + Q(54, 5 * 8**2)
check("convexity_lower_margin", 6 + Q(81, 16) - Q(54, 5) == Q(21, 80))
check("tangent_value", F3 == Q(1, 5))
check("tangent_slope", Fp3 == Q(61, 2400) and Fp3 > 0)
check("tangent_uniform_margin", F3 - Fp3 == Q(419, 2400))
check("one_sixth_margin", Q(419, 2400) - Q(1, 6) == Q(19, 2400))
check("original_declaration_margin", Q(1, 6) > Q(1, 150))

result = {
    "description": "Supplementary exact identities and endpoint arithmetic for R4 M.4",
    "official_qmd_prover_verdict": False,
    "proof_relies_on_execution": False,
    "check_count": len(checks),
    "all_passed": all(item["passed"] for item in checks),
    "checks": checks,
}
destination = Path(__file__).with_name("r4_boundary_exact_checks.json")
destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"check_count": result["check_count"], "all_passed": result["all_passed"]}))
if not result["all_passed"]:
    raise SystemExit(1)
