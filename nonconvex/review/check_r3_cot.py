"""Exact supplementary checks for the R3 cotangent Sturm comparison.

Run with Python 3 from any directory.  This uses the standard library and
the adjacent rational_algebra.py.  All parameters remain formal during
the identity checks; scalar comparisons use exact fractions.  There are
no sampled intervals or numerical trigonometric evaluations.
"""

from fractions import Fraction as F
from pathlib import Path
import json

from rational_algebra import R


checks = []


def check(name, condition):
    checks.append({"name": name, "passed": bool(condition)})


# Polynomials in t, with rational functions of the formal parameter Pi
# as coefficients.  This keeps both variables symbolic.
def add(*polynomials):
    return [sum((p[j] for p in polynomials if j < len(p)), R(0))
            for j in range(max(map(len, polynomials)))]


def scale(polynomial, scalar):
    return [R(scalar) * coefficient for coefficient in polynomial]


def multiply(p, q):
    result = [R(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            result[i + j] = result[i + j] + x * y
    return result


def derivative(polynomial):
    return [j * polynomial[j] for j in range(1, len(polynomial))] or [R(0)]


pi2 = R((0, 1))
a = F(3, 2) * pi2 - F(45, 4)
t = [R(0), R(1)]
q = [R(1), R(-F(5, 4)), R(F(1, 4))]
w = [R(1), R(-F(1, 9))]

# For p(x)=x f(t), t=x^2/Pi, f=Q(t)w(t)^a, compute the exact
# polynomial -(6f'+4tf''+Pi*f)/w^(a-2) before inserting its claimed form.
residual = add(
    scale(multiply(add(scale(derivative(q), 6),
                       scale(multiply(t, derivative(derivative(q))), 4),
                       scale(q, pi2)), multiply(w, w)), -1),
    multiply(add(scale(q, 6 * a / 9),
                 scale(multiply(t, derivative(q)), 8 * a / 9)), w),
    scale(multiply(t, q), -4 * a * (a - 1) / 81),
)
c0 = F(665, 72) + F(5, 27) * pi2 - pi2 ** 2 / 9
c1 = F(175, 432) - F(239, 162) * pi2 + F(5, 36) * pi2 ** 2
c2 = -F(1295, 1296) + F(131, 324) * pi2 - pi2 ** 2 / 36
c3 = -pi2 / 324
expected = [R(0), c0, c1, c2, c3]
check("complete formal differential residual identity",
      len(residual) == len(expected) and all((u - v).zero() for u, v in zip(residual, expected)))
check("cancellation at t=0", residual[0].zero())
check("logarithmic-derivative coefficient giving exactly H",
      (a / (9 * pi2) - (F(1, 6) - 5 / (4 * pi2))).zero())
check("quadratic factor Q=(1-t)(1-t/4)",
      all((u - v).zero() for u, v in zip(q, multiply([R(1), R(-1)], [R(1), R(-F(1, 4))]))))
check("c0 derivative identity", (c0.diff() - (5 - 6 * pi2) / 27).zero())
check("c2 derivative identity", (c2.diff() - (131 - 18 * pi2) / 324).zero())
check("c1+2c2 identity",
      (c1 + 2 * c2 - (pi2 ** 2 / 12 - 2 * pi2 / 3 - F(2065, 1296))).zero())
check("derivative of c1+2c2", ((c1 + 2 * c2).diff() - (pi2 - 4) / 6).zero())
check("R(1) identity", (c0 + c1 + c2 + c3 - (F(700, 81) - 8 * pi2 / 9)).zero())

lower, upper = F(49, 5), F(99, 10)
check("permitted weakening of pi lower bound", F(493, 50) > lower)
check("permitted weakening of pi upper bound", F(987, 100) < upper)
check("lower endpoint for exponent a", a.at(lower) == F(69, 20) > 0)
check("upper endpoint for exponent a", a.at(upper) == F(18, 5))
check("positive lower bound for the powered base", 1 - F(1, 9) == F(8, 9) > 0)
check("c0 is decreasing on the entire pi interval", 5 - 6 * lower < 0)
check("c2 is decreasing on the entire pi interval", 131 - 18 * lower < 0)
check("c1+2c2 is increasing on the entire pi interval", lower - 4 > 0)
check("strict lower endpoint comparison for c0", c0.at(upper) == F(323, 1800) > 0)
check("strict lower endpoint comparison for c2", c2.at(upper) == F(4553, 16200) > 0)
check("strict upper comparison for c1+2c2", (c1 + 2 * c2).at(upper) == -F(419, 16200) < 0)
check("strict upper endpoint comparison for R(1)",
      (c0 + c1 + c2 + c3).at(lower) == -F(28, 405) < 0)
check("negative cubic coefficient throughout the pi interval", lower > 0)

summary = {
    "scope": "Supplementary formal identities and exact rational comparisons; no parameter sampling.",
    "official_qmd_prover_run": False,
    "proof_relies_on_execution": False,
    "check_count": len(checks),
    "all_passed": all(item["passed"] for item in checks),
    "checks": checks,
}
Path(__file__).with_name("r3_cot_exact_checks.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps({key: value for key, value in summary.items() if key != "checks"}, indent=2))
raise SystemExit(0 if summary["all_passed"] else 1)
