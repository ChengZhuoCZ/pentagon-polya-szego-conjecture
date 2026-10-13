"""Supplementary exact algebra for R3 R.6; the analytic proof is in robin.qmd.

Only Python's standard library is used. These checks manipulate Laurent
polynomials over Q[a,c,z], with T=c(2a+5-c). They are identity checks, not
numerical samples, sign certificates, or an official qmd-prover verdict.
"""

from fractions import Fraction
from math import comb
from pathlib import Path
import json


class P:
    def __init__(self, terms=None):
        self.terms = {
            power: Fraction(value)
            for power, value in (terms or {}).items()
            if value
        }

    @staticmethod
    def lift(value):
        if isinstance(value, P):
            return value
        return P({(0, 0, 0): Fraction(value)})

    def __add__(self, other):
        other = P.lift(other)
        result = dict(self.terms)
        for power, value in other.terms.items():
            result[power] = result.get(power, 0) + value
        return P(result)

    __radd__ = __add__

    def __neg__(self):
        return P({power: -value for power, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-P.lift(other))

    def __rsub__(self, other):
        return P.lift(other) + (-self)

    def __mul__(self, other):
        other = P.lift(other)
        result = {}
        for left_power, left_value in self.terms.items():
            for right_power, right_value in other.terms.items():
                power = tuple(x + y for x, y in zip(left_power, right_power))
                result[power] = result.get(power, 0) + left_value * right_value
        return P(result)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        if exponent < 0:
            raise ValueError("Use the explicit Laurent monomial for z^-1.")
        result = P.lift(1)
        for _ in range(exponent):
            result = result * self
        return result

    def dz(self):
        result = {}
        for (pa, pc, pz), value in self.terms.items():
            if pz:
                result[(pa, pc, pz - 1)] = value * pz
        return P(result)

    def at_z_one(self):
        result = {}
        for (pa, pc, _), value in self.terms.items():
            power = (pa, pc, 0)
            result[power] = result.get(power, 0) + value
        return P(result)


def clean_operator(operator):
    return {order: P.lift(value) for order, value in operator.items()
            if P.lift(value).terms}


def compose(left, right):
    """Compose sum p_k D^k with sum q_j D^j by the exact Leibniz rule."""
    result = {}
    for k, pk in left.items():
        for j, qj in right.items():
            derivative = P.lift(qj)
            for r in range(k + 1):
                order = k - r + j
                term = comb(k, r) * P.lift(pk) * derivative
                result[order] = result.get(order, P()) + term
                derivative = derivative.dz()
    return clean_operator(result)


checks = []


def assert_identity(label, left, right=0):
    difference = P.lift(left) - P.lift(right)
    if difference.terms:
        raise AssertionError(f"{label}: nonzero exact Laurent polynomial")
    checks.append(label)


def assert_operator(label, left, right):
    for order in set(left) | set(right):
        difference = P.lift(left.get(order, 0)) - P.lift(right.get(order, 0))
        if difference.terms:
            raise AssertionError(f"{label}: coefficient of D^{order} differs")
    checks.append(label)


a = P({(1, 0, 0): 1})
c = P({(0, 1, 0): 1})
z = P({(0, 0, 1): 1})
zi = P({(0, 0, -1): 1})

minus = {1: P.lift(1), 0: -a * zi}
plus = {1: P.lift(1), 0: a * zi}
la = {2: P.lift(-1), 0: a * (a - 1) * zi**2}
la_next = {2: P.lift(-1), 0: a * (a + 1) * zi**2}

assert_operator("L_a = -B_a A_a",
                {k: -v for k, v in compose(plus, minus).items()}, la)
assert_operator("L_(a+1) = -A_a B_a",
                {k: -v for k, v in compose(minus, plus).items()}, la_next)
assert_operator("L_(a+1) A_a = A_a L_a",
                compose(la_next, minus), compose(minus, la))

A = 2 * a + 1
M = 2 * a + 3
T = c * (2 * a + 5 - c)
B = A * c + T
H = A * M - B * z**2
C = M - c

assert_identity("H(1) = C D, where C D = A C - T",
                H.at_z_one(), A * C - T)

# b=w'/w=N/H; clear H^2 after differentiating this rational function.
N = a * zi * H - T * z * (M - c * z**2)
residual_times_H2 = (
    (a * (a - 1) * zi**2 - T) * H**2
    - N.dz() * H + N * H.dz() - N**2
)
assert_identity("Direct barrier residual",
                residual_times_H2, T**2 * c**2 * z**4 * (1 - z**2))

# Clear B H in the derivative of the closed elementary expression.
assert_identity("Closed barrier has the same logarithmic derivative",
                T * c * z * H + M * T**2 * z,
                T * z * B * (M - c * z**2))

assert_identity("Riccati numerator collapse",
                H + 2 * M - (M - c * z**2)**2,
                c**2 * z**2 * (1 - z**2))

report = {
    "arithmetic": "Exact Laurent-polynomial arithmetic over rational numbers",
    "parameter_relation": "T = c (2 a + 5 - c)",
    "check_count": len(checks),
    "all_passed": True,
    "proof_relies_on_execution": False,
    "official_qmd_prover_verdict": False,
    "checks": checks,
    "scope": "Supplementary identity checks only; analytic hypotheses are proved in the source."
}
output = Path(__file__).with_name("r3_tail_exact_checks.json")
output.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
