"""Exact checks of the displayed R2 crossing identities and endpoint arithmetic.

Run with Python 3 from any working directory.  Only the standard library and
the adjacent rational_algebra.py are required.  These checks use formal
polynomial identities and rational arithmetic, with no parameter sampling.
They are supplementary development checks, not mathematical premises and
not a qmd-prover verification.
"""

from fractions import Fraction as Q
from pathlib import Path
import json

from rational_algebra import R


checks = []


def check(name, condition):
    checks.append({"name": name, "passed": bool(condition)})


# The barrier identity is quadratic in the formal parameter s.  Check each
# coefficient as an exact rational function of y, instead of sampling s.
y = R((0, 1))
alpha = 1 / y - y
beta = -2 * y / (1 - y ** 2)
check("singular barrier: coefficient of s^2",
      (-alpha ** 2 + 1 / y ** 2 - (2 - y ** 2)).zero())
check("singular barrier: coefficient of s",
      (-alpha.diff() - 2 * alpha * beta - 1 / y ** 2 - 5).zero())
check("singular barrier: constant coefficient",
      (-beta.diff() - beta ** 2 - 2 / (1 - y ** 2)).zero())

# p_q(z) is quadratic in q; its differential residual is cubic in q.
p0, p1, p2 = y, -y ** 3 / 6, y ** 5 / 144
check("free barrier: coefficient of q^0", (-p0.diff().diff()).zero())
check("free barrier: coefficient of q^1", (-p1.diff().diff() - p0).zero())
check("free barrier: coefficient of q^2",
      (-p2.diff().diff() - p1 - y ** 3 / 36).zero())
check("free barrier: coefficient of q^3", (-p2 + y ** 5 / 144).zero())

s = y
gap = s ** 2 + 5 * s + Q(45, 16) * s - (25 * s - 11) / 2
check("completed-square lower bound for B_s-C_s",
      (gap - (s - Q(75, 32)) ** 2 - Q(7, 1024)).zero())


class P:
    """A small exact polynomial in the formal variables a,b,c,t."""

    def __init__(self, value=0):
        if isinstance(value, P):
            self.terms = dict(value.terms)
        elif isinstance(value, dict):
            self.terms = {e: Q(v) for e, v in value.items() if v}
        else:
            self.terms = {(0, 0, 0, 0): Q(value)} if value else {}

    def __add__(self, other):
        terms = dict(self.terms)
        for e, v in P(other).terms.items():
            terms[e] = terms.get(e, Q(0)) + v
        return P(terms)

    __radd__ = __add__

    def __neg__(self):
        return P({e: -v for e, v in self.terms.items()})

    def __sub__(self, other):
        return self + -P(other)

    def __rsub__(self, other):
        return P(other) + -self

    def __mul__(self, other):
        terms = {}
        for e, v in self.terms.items():
            for f, w in P(other).terms.items():
                power = tuple(e[j] + f[j] for j in range(4))
                terms[power] = terms.get(power, Q(0)) + v * w
        return P(terms)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        result = P(1)
        for _ in range(exponent):
            result *= self
        return result

    def diff(self, variable=3):
        terms = {}
        for e, v in self.terms.items():
            if e[variable]:
                power = list(e)
                power[variable] -= 1
                terms[tuple(power)] = e[variable] * v
        return P(terms)

    def zero(self):
        return not self.terms


a, b, c, t = [P({tuple(int(k == j) for k in range(4)): 1}) for j in range(4)]
quadratic = a + b * t + c * t ** 2


def second_derivative_numerator(numerator, denominator):
    """Return the numerator above denominator^3 for (numerator/denominator)''."""
    first = numerator.diff() * denominator - numerator * denominator.diff()
    return first.diff() * denominator - 2 * first * denominator.diff()


check("formal curvature identity for t/(a+bt+ct^2)",
      (second_derivative_numerator(t, quadratic)
       + 2 * (a * b + 3 * a * c * t - c ** 2 * t ** 3)).zero())
check("formal curvature identity for t^2/(a+bt+ct^2)",
      (second_derivative_numerator(t ** 2, quadratic)
       - 2 * (a ** 2 - 3 * a * c * t ** 2 - b * c * t ** 3)).zero())
check("formal convexity numerator for a*t/(b-c*t)",
      (second_derivative_numerator(a * t, b - c * t) - 2 * a * b * c).zero())


def area_cost(t):
    return Q(9, 25) + Q(138, 25) * t + Q(29, 25) * t * t


def target(s):
    return (25 * s - 11) / 2


def singular_bound(s, t):
    f = area_cost(t)
    return 1 + s * t - s * t / f - 2 * t / (f - 1)


def free_penalty(c, t):
    f = area_cost(t)
    return (10 * c * t * t / (49 * f - 5 * c * t * t)
            + Q(13, 2) * c * t * t / (49 * f - Q(5, 4) * c * t * t))


t0, t1 = Q(1, 4), Q(3, 2)
check("area cost at 1/4", area_cost(t0) == Q(29, 16))
check("area cost at 3/2", area_cost(t1) == Q(45, 4))
check("target at order 2", target(Q(2)) == Q(39, 2))
check("target at order 3", target(Q(3)) == 32)
check("strict rational lower bound for sqrt(2)", 2 > Q(45, 32) ** 2)
check("first-interval P(1/4)",
      Q(1, 3) + Q(8, 39) * t0 - Q(496, 87) * t0 ** 2 == Q(32, 1131) > 0)
check("uniform coefficient in first-interval P", (437 * Q(3) - 319) / 174 == Q(496, 87))
check("negative concavity constant 10a-4", 10 * Q(9, 25) - 4 == -Q(2, 5))
check("minimum of d", 5 * Q(39, 2) - 49 * Q(29, 25) == Q(2033, 50) > 40)
check("minimum of e", 49 * Q(29, 25) - Q(5, 4) * 32 == Q(421, 25) > 0)
check("maximum of e", 49 * Q(29, 25) - Q(5, 4) * Q(39, 2) == Q(6493, 200) < 33)
check("free penalty at t=1/4 and C=32",
      free_penalty(Q(32), t0) == Q(320, 1261) + Q(208, 1381))
check("two short bounds for the first endpoint",
      Q(320, 1261) < Q(1, 3) and Q(208, 1381) < Q(1, 6))
check("singular bound at t=1/4 and s=2",
      singular_bound(Q(2), t0) == 1 + Q(13, 58) - Q(8, 13))
check("first endpoint response margin",
      Q(1, 3) + Q(13, 58) - Q(1, 2) == Q(5, 87) > 0)
check("singular bound at t=3/2 and s=2", singular_bound(Q(2), t1) == Q(2116, 615) > 3)
check("free penalty at t=3/2 and C=39/2",
      free_penalty(Q(39, 2), t1) == Q(78, 59) + Q(1014, 1765))
check("two short bounds for the order-2 endpoint",
      Q(78, 59) < Q(3, 2) and Q(1014, 1765) < Q(3, 5))
check("singular bound at t=3/2 and s=3", singular_bound(Q(3), t1) == Q(1971, 410))
check("free penalty at t=3/2 and C=32",
      free_penalty(Q(32), t1) == Q(64, 17) + Q(208, 205))
check("hard endpoint response margin 39/1394",
      singular_bound(Q(3), t1) - free_penalty(Q(32), t1) == Q(39, 1394) > 0)
check("comparison of the two endpoint margins", Q(5, 87) > Q(39, 1394) > 0)
check("maximum free energy on the first interval", 32 * t0 * t0 / area_cost(t0) == Q(32, 29) < 4)
check("maximum free energy on the second interval", 32 * t1 * t1 / area_cost(t1) == Q(32, 5) < Q(49, 5))
check("rational pi lower-bound weakening", Q(493, 50) > Q(49, 5))
check("rational cotangent coefficient bound", Q(987, 100) / 3 - Q(5, 2) == Q(79, 100))
check("combined cotangent coefficient", Q(1, 2) + Q(79, 100) == Q(129, 100) < Q(13, 10))

summary = {
    "scope": "Supplementary exact polynomial identities and rational arithmetic; no parameter sampling.",
    "official_qmd_prover_run": False,
    "proof_relies_on_execution": False,
    "check_count": len(checks),
    "all_passed": all(item["passed"] for item in checks),
    "checks": checks,
}
output = Path(__file__).with_name("r2_crossing_exact_checks.json")
output.write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps({key: value for key, value in summary.items() if key != "checks"}, indent=2))
raise SystemExit(0 if summary["all_passed"] else 1)
