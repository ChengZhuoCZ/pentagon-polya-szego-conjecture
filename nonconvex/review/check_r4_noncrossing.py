"""Exact supplementary checks for the R4 noncrossing comparison family.

Run with Python 3 from any directory. Only the standard library and the
adjacent rational_algebra.py are used. Differential identities are checked
as rational functions in a formal variable. Scalar checks use Fraction;
there are no parameter grids, floating-point tests, or ODE approximations.
The mathematical proof is complete without execution of this script.
"""

from fractions import Fraction as F
from pathlib import Path
import json

from rational_algebra import R


checks = []


def check(name, condition):
    checks.append({"name": name, "passed": bool(condition)})


c = F(1, 23)
check("common denominator lower bound", 1 - F(5, 9) - c == F(83, 207) > 0)
check("uniform square upper bound",
      F(1, 4) - F(61, 297) - c == F(31, 27324) > 0)
check("uniform positive residual gap",
      F(13, 207) - F(1, 16) == F(1, 3312) > 0)

cases = (
    (2, F(25, 2), F(11, 4), F(83, 207), F(27, 1162),
     F(1036, 359), F(195, 1436)),
    (3, F(61, 3), F(21, 10), F(2276, 5313), F(2071, 307260),
     F(1084, 515), F(1, 206)),
)

for a, energy, threshold, h1_expected, singular_gap, free_expected, free_gap in cases:
    label = f"order {a}: "
    A = F(2 * a + 1)
    alpha = energy / A
    beta = alpha ** 2 / (A + 2)
    gamma = 2 * alpha / (A + 4)
    theta = energy / ((A + 2) * (A + 4))

    t = R((0, 1))
    H = 1 - gamma * t - c * t ** 2
    Y = alpha + beta * t / H
    residual = A * Y + 2 * t * Y.diff() - t * Y ** 2 - energy
    expected = (alpha ** 2 * t ** 3 / H ** 2
                * (c * (A + 6) / (A + 2) - (theta + c * t) ** 2))
    check(label + "complete formal rational residual identity", (residual - expected).zero())
    check(label + "H-tH' identity", (H - t * H.diff() - 1 - c * t ** 2).zero())
    check(label + "first cancellation", (A + 2) * beta == alpha ** 2)
    check(label + "second cancellation", (A + 4) * gamma == 2 * alpha)
    check(label + "square parameter identity", alpha * gamma - beta == alpha * theta)

    # Independent differentiation in z of the logarithmic derivative of w.
    z = R((0, 1))
    Hz = 1 - gamma * z ** 2 - c * z ** 4
    Yz = alpha + beta * z ** 2 / Hz
    log_derivative = a / z - z * Yz
    direct_residual = (-log_derivative.diff() - log_derivative ** 2
                       + a * (a - 1) / z ** 2 - energy)
    direct_expected = (alpha ** 2 * z ** 6 / Hz ** 2
                       * (c * (A + 6) / (A + 2) - (theta + c * z ** 2) ** 2))
    check(label + "independent differential residual in z", (direct_residual - direct_expected).zero())
    check(label + "positive-denominator parameter bound", 0 < gamma <= F(5, 9))
    check(label + "square parameter upper bound", 0 < theta <= F(61, 297))
    check(label + "positive term lower bound", c * (A + 6) / (A + 2) >= F(13, 207))
    check(label + "regular normalization data", H.at(0) == 1 and Y.at(0) == alpha)
    check(label + "interface denominator", H.at(1) == h1_expected > 0)
    D = a - Y.at(1)
    check(label + "direct singular interface inequality", D + threshold == singular_gap > 0)

    q = energy / 16
    x = R((0, 1))
    p = x * (1 - q * x ** 2 / 12) ** 2
    polynomial_residual = -p.diff().diff() - q * p
    polynomial_expected = q ** 2 * x ** 3 * (4 - q * x ** 2) / 144
    check(label + "free polynomial differential identity", (polynomial_residual - polynomial_expected).zero())
    check(label + "free comparison parameter range", 0 < q < 4)
    check(label + "positive interface value of free polynomial", p.at(1) > 0)
    free_derivative = 4 * p.diff().at(1) / p.at(1)
    check(label + "free derivative rational formula",
          free_derivative == 4 * (1 - q / (3 - q / 4)) == free_expected)
    check(label + "free interface inequality", free_derivative - threshold == free_gap > 0)
    check(label + "positive complete derivative jump", D + free_derivative > 0)
    free_ratio = 16 * polynomial_residual / p
    free_ratio_expected = q ** 2 * x ** 2 * (4 - q * x ** 2) / (9 * (1 - q * x ** 2 / 12) ** 2)
    check(label + "bounded free residual ratio identity", (free_ratio - free_ratio_expected).zero())
    check(label + "shared physical energy", 16 * q == energy)

check("order 2 scaling to exact retained constant", F(25, 16) * F(25, 2) == F(625, 32))
check("order 3 scaling to exact retained constant", F(25, 16) * F(61, 3) == F(1525, 48))
check("order 2 retained final margin", F(625, 32) - F(39, 2) == F(1, 32) > 0)
check("order 3 retained final margin", F(1525, 48) - F(1587, 50) == F(37, 1200) > 0)

summary = {
    "scope": "Supplementary formal rational identities and exact scalar comparisons; no parameter sampling.",
    "official_qmd_prover_run": False,
    "proof_relies_on_execution": False,
    "check_count": len(checks),
    "all_passed": all(item["passed"] for item in checks),
    "checks": checks,
}
Path(__file__).with_name("r4_noncrossing_exact_checks.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps({key: value for key, value in summary.items() if key != "checks"}, indent=2))
raise SystemExit(0 if summary["all_passed"] else 1)
