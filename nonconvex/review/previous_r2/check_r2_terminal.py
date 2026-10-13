"""Exact corroboration of the R2 terminal calculus proofs.

Run with ``python review/check_r2_terminal.py`` from the project root.
Only the Python standard library and the adjacent rational_algebra.py are used.
There are no grids, floating-point evaluations, or sampled interval conclusions.
The interval proofs remain the curvature and tangent arguments in terminal.qmd.
"""

from fractions import Fraction as F
from pathlib import Path
import json

from rational_algebra import R


CHECKS = []


def check(name, expression):
    passed = expression.zero() if isinstance(expression, R) else bool(expression)
    CHECKS.append({"name": name, "passed": passed})
    if not passed:
        raise AssertionError(name)


h = R((0, 1))
L = 1 + h
s = (1381 * h + 1712) / (500 * (h + 2))
v = 2 * (h + 7) / 67
pi_upper = F(987, 100)

# The existing Psi payment, before introducing either reciprocal majorant.
e_psi = 3 * (60 * h**2 + 127 * h - 8) / (h * L * (h + 2) * (60 * h + 127))
k_psi = e_psi - 1 / (2 * (h + 2)**2)
A_minus = 493 / (100 * (h + 2)**2)
J_psi = 1 - 2 * k_psi / (1 - k_psi) - (F(129, 100) + 1 / (4 * L)) * k_psi
gain_psi = A_minus * (26 * h - 5) / (60 * h**2) * (1 + 33 / (400 * L))
Z_psi = s + h * (J_psi + gain_psi) - v * pi_upper * h**2 * e_psi
N = 300 * h**3 + 1295 * h**2 + 1349 * h - 96
D = 2 * h * L * (h + 2)**2 * (60 * h + 127)
S = 2 * h * N / (D - N)

b0 = F(213469, 1920000)
b1 = F(225, 268)
b2 = F(11452440743, 3591200000)
b3 = F(1773689, 1600000)
b4 = F(74489644841, 4502400000)
b5 = F(23869857, 3927875)
R0 = (F(389, 3350) * h - F(25913, 33500) - b0 / h
      + b1 / (h + 1)**2 - b2 / (h + 1)
      + b3 / (h + 2)**2 + b4 / (h + 2)
      - b5 / (h + F(127, 60)))
check("Psi head-energy identity", k_psi - N / D)
check("Psi common partial-fraction identity", R0 - (Z_psi + S))

# Lower Psi interval: reciprocal majorant and its curvature proof.
M_minus = F(199, 40) / (h + 2) - 1 / (9 * h)
G_minus = R0 - M_minus
P_minus = (1751 * h - 80) * (D - N) - 720 * h**2 * (h + 2) * N
check("Psi lower majorant product identity",
      M_minus - S - P_minus / (360 * h * (h + 2) * (D - N)))
check("Psi lower product third derivative",
      P_minus.diff().diff().diff()
      - (618762 + 11400720 * h + 7281240 * h**2 - 705600 * h**3))
check("Psi lower third-derivative bound constant", 618762 - F(705600, 8) == 530562)
check("Psi lower second-derivative endpoint",
      P_minus.diff().diff().at(F(3, 8)) == F(18878731, 256) > 70000)
check("Psi lower product tangent value", P_minus.at(F(1, 2)) == F(6687, 16) > 400)
check("Psi lower product tangent derivative",
      0 < P_minus.diff().at(F(1, 2)) == F(33711, 8) < 4300)
check("Psi lower product tangent margin", 400 - F(4300**2, 140000) == F(3751, 14))

epsilon = b0 - F(1, 9)
d1 = b4 - F(199, 40)
check("Psi lower small pole coefficient", epsilon == F(407, 5760000))
check("Psi lower shifted coefficient", d1 == F(52090204841, 4502400000))
xh = 1 / (h + 2)
lower_curvature = (d1 + 3 * b3 * xh
                   - (b2 * (1 - xh) - 3 * b1 * xh) / (1 - xh)**4
                   - b5 / (1 + F(7, 60) * xh)**3
                   - epsilon * ((h + 2) / h)**3)
check("Psi lower normalized curvature identity",
      (h + 2)**3 * G_minus.diff().diff() / 2 - lower_curvature)
check("Psi lower coefficient bounds",
      b2 < F(16, 5) and b1 > F(67, 80) and b3 > F(11, 10) and d1 > F(23, 2))
x = R((0, 1))
max_a = F(16, 5)
max_b = F(67, 80)
max_function = (max_a - (max_a + 3 * max_b) * x) / (1 - x)**4
check("Psi lower scalar-maximum derivative",
      max_function.diff()
      - 3 * ((max_a - max_b) - (max_a + 3 * max_b) * x) / (1 - x)**5)
check("Psi lower scalar maximum value",
      max_function.at((max_a - max_b) / (max_a + 3 * max_b))
      == (max_a + 3 * max_b)**4 / (256 * max_b**3)
      == F(457**4, 20480 * 67**3))
check("Psi lower scalar maximum bound",
      F(71, 10) - F(457**4, 20480 * 67**3) == F(115441503, 6159626240))
check("Psi lower shifted-reciprocal bound",
      F(16, 3) - b5 * F(150, 157)**3 == F(12199946824, 364810943217))
check("Psi lower small-pole loss bound",
      F(1, 50) - epsilon * F(19, 3)**3 == F(318787, 155520000))
check("Psi lower positive curvature margin",
      F(23, 2) + F(33, 25) - F(71, 10) - F(16, 3) - F(1, 50) == F(11, 30))
check("Psi lower payment tangent value",
      G_minus.at(F(1, 2)) == F(105145468, 7396171875) > F(7, 500))
check("Psi lower payment tangent slope",
      G_minus.diff().at(F(1, 2)) == -F(357200649213, 5160884375000) < 0)
check("Psi lower payment margin",
      G_minus.at(F(1, 2)) - F(7, 500) == F(6396247, 29584687500))

# Upper Psi interval: one reciprocal, followed by normalized-curvature concavity.
M_plus = 5 / (h + F(231, 100))
G_plus = R0 - M_plus
P_plus = 5 * (D - N) - 2 * h * (h + F(231, 100)) * N
check("Psi upper majorant product identity",
      M_plus - S - P_plus / ((h + F(231, 100)) * (D - N)))
check("Psi upper product second derivative",
      P_plus.diff().diff() - (3528 * h**2 + F(29073, 5) * h + F(2231, 25)))
check("Psi upper second-derivative endpoint",
      P_plus.diff().diff().at(F(1, 2)) == F(193927, 50) > 3800)
check("Psi upper product tangent value", P_plus.at(F(1, 2)) == F(7971, 400) > 19)
check("Psi upper product tangent slope",
      P_plus.diff().at(F(1, 2)) == -F(60607, 200)
      and abs(P_plus.diff().at(F(1, 2))) < 304)
check("Psi upper product tangent margin", 19 - F(304**2, 7600) == F(3249, 475) > 6)

alpha = F(7, 60)
beta = F(31, 100)
curvature_reciprocals = (b0 / (1 - 2 * x)**3 + b2 / (1 - x)**3
                         + b5 / (1 + alpha * x)**3 + 5 / (1 + beta * x)**3
                         - 3 * b1 * x / (1 - x)**4)
Q = b4 + 3 * b3 * x - curvature_reciprocals
Qh = (b4 + 3 * b3 / (h + 2) - b0 * ((h + 2) / h)**3
      - b2 * ((h + 2) / (h + 1))**3
      - b5 * ((h + 2) / (h + F(127, 60)))**3
      - 5 * ((h + 2) / (h + F(231, 100)))**3
      + 3 * b1 * (h + 2)**3 / (h + 1)**4)
check("Psi upper normalized curvature identity", (h + 2)**3 * G_plus.diff().diff() / 2 - Qh)
positive_bracket = (4 * b0 * (1 - x)**6 / (1 - 2 * x)**5
                    + b2 * (1 - x) - b1 * (2 + 3 * x))
check("Psi upper reciprocal second-derivative decomposition",
      curvature_reciprocals.diff().diff() - 12 * positive_bracket / (1 - x)**6
      - 12 * alpha**2 * b5 / (1 + alpha * x)**5
      - 60 * beta**2 / (1 + beta * x)**5)
check("Psi upper convexity coefficient bounds",
      b0 > F(1, 10) and b2 > F(19, 6) and b1 < F(17, 20))
check("Psi upper first bracket bound",
      F(19, 6) * F(3, 4) - F(17, 20) * F(11, 4) == F(3, 80))
ratio = (1 - x)**6 / (1 - 2 * x)**5
check("Psi upper ratio logarithmic derivative",
      ratio.diff() / ratio - (4 + 2 * x) / ((1 - x) * (1 - 2 * x)))
check("Psi upper ratio endpoint", ratio.at(F(1, 4)) == F(729, 128))
check("Psi upper second bracket bound", F(729, 320) - F(7, 5) == F(281, 320) > 0)

# Coarse endpoint bounds appearing in the integrated proof.
check("Psi upper coarse coefficient bounds",
      b0 < F(9, 80) and b1 > F(5, 6) and b2 < F(319, 100)
      and F(11, 10) < b3 < F(9, 8) and F(33, 2) < b4 < 17 and b5 < F(61, 10))
q_left_lower = (F(33, 2) + F(11, 20) + F(108, 125) - F(243, 640)
                - F(17226, 3125) - F(61, 10) - 5)
check("Psi upper curvature at x=1/6 by coarse bounds", Q.at(F(1, 6)) > q_left_lower > F(9, 10))
check("Psi upper first shifted reciprocal at x=2/7", F(61, 10) * F(30, 31)**3 < F(28, 5))
check("Psi upper second shifted reciprocal at x=2/7", 5 * F(350, 381)**3 < F(39, 10))
q_middle_lower = (F(33, 2) + F(33, 35) + F(343, 125) - F(343, 240)
                  - F(109417, 12500) - F(28, 5) - F(39, 10))
check("Psi upper curvature at x=2/7 by coarse bounds", Q.at(F(2, 7)) > q_middle_lower > F(1, 2))
q_right_upper = 17 + F(27, 20) + F(1275, 162) - F(25, 2) - F(2375, 162)
check("Psi upper curvature at x=2/5 by coarse bounds", Q.at(F(2, 5)) < q_right_upper == -F(1523, 1620) < 0)

check("Psi upper left-endpoint payment", G_plus.at(F(1, 2)) == F(2433531573, 923699687500) > F(1, 400))
check("Psi upper transition derivative",
      G_plus.diff().at(F(3, 2)) == -F(149796111140233433, 6010955790564375000) < 0)
check("Psi upper tangent value",
      G_plus.at(F(17, 8)) == F(30400178207917, 13725647553750000) > F(1, 500))
check("Psi upper tangent slope",
      0 < G_plus.diff().at(F(17, 8))
      == F(11525960738983536155737, 32591802711187012605468750) < F(1, 2000))
check("Psi upper positive tangent margin", F(1, 500) - F(5, 8) * F(1, 2000) == F(27, 16000))
check("Psi comparison of lower and upper uniform margins", F(7, 500) > F(27, 16000))

# Phi: one reciprocal majorant and the convex three-pole payment.
e_phi = 3 * (13 * h - 2) / (13 * h * L * (h + 2))
r_phi = 15 * e_phi / 16
J_phi = 1 - 2 * r_phi / (1 - r_phi) - 3 * r_phi / 2
Z_phi = s + h * J_phi - v * pi_upper * h**2 * e_phi
Q_phi = 208 * h**3 + 624 * h**2 - 169 * h + 90
check("Phi reciprocal denominator identity", Q_phi - 208 * h * L * (h + 2) * (1 - r_phi))
check("Phi short subtraction identity", Q_phi - 16 * h * (h + 3) * (13 * h - 2) - (32 * h**2 - 73 * h + 90))
check("Phi reciprocal majorant identity",
      F(45, 8) / (h + 3) - 2 * h * r_phi / (1 - r_phi)
      - 45 * (32 * h**2 - 73 * h + 90) / (8 * (h + 3) * Q_phi))
check("Phi positive completed square",
      32 * h**2 - 73 * h + 90 - 32 * (h - F(73, 64))**2 - F(6191, 128))
c1 = F(174393, 139360)
c2 = F(54705, 6968)
c3 = F(45, 8)
G_phi = (F(389, 3350) * h - F(277649, 435500)
         - c1 / (h + 1) + c2 / (h + 2) - c3 / (h + 3))
check("Phi payment partial fractions",
      G_phi - (Z_phi + 2 * h * r_phi / (1 - r_phi) - F(45, 8) / (h + 3)))
f_phi = c1 / (1 - x)**3 + c3 / (1 + x)**3
check("Phi normalized curvature identity",
      (h + 2)**3 * G_phi.diff().diff() / 2
      - (c2 - c1 * ((h + 2) / (h + 1))**3 - c3 * ((h + 2) / (h + 3))**3))
check("Phi reciprocal-sum convexity identity",
      f_phi.diff().diff() - 12 * c1 / (1 - x)**5 - 12 * c3 / (1 + x)**5)
check("Phi curvature coefficient bounds", c1 < F(21, 16) and c2 > F(15, 2))
check("Phi first curvature-endpoint cube bounds", F(6, 5)**3 < 2 and F(6, 7)**3 < F(2, 3))
check("Phi second curvature-endpoint cube bounds", F(30, 19)**3 < 4 and F(30, 41)**3 < F(2, 5))
check("Phi first curvature endpoint", f_phi.at(F(1, 6)) < F(51, 8) < F(15, 2))
check("Phi second curvature endpoint", f_phi.at(F(11, 30)) < 4 * F(21, 16) + F(2, 5) * F(45, 8) == F(15, 2))
check("Phi tangent value", G_phi.at(F(9, 4)) == F(9786437, 673718500) > F(7, 500))
check("Phi tangent slope", 0 < G_phi.diff().at(F(9, 4)) == F(209699639, 52112125975) < F(1, 200))
check("Phi left tangent distance", F(9, 4) - F(8, 11) == F(67, 44))
check("Phi positive tangent margin", F(7, 500) - F(67, 8800) == F(281, 44000) > F(3, 500))


def main():
    endpoint_data = {
        "psi_lower_payment_at_1_2": str(G_minus.at(F(1, 2))),
        "psi_lower_derivative_at_1_2": str(G_minus.diff().at(F(1, 2))),
        "psi_upper_payment_at_1_2": str(G_plus.at(F(1, 2))),
        "psi_upper_derivative_at_3_2": str(G_plus.diff().at(F(3, 2))),
        "psi_upper_payment_at_17_8": str(G_plus.at(F(17, 8))),
        "psi_upper_derivative_at_17_8": str(G_plus.diff().at(F(17, 8))),
        "phi_payment_at_9_4": str(G_phi.at(F(9, 4))),
        "phi_derivative_at_9_4": str(G_phi.diff().at(F(9, 4))),
    }
    record = {
        "scope": "R2 terminal Psi and Phi replacements",
        "arithmetic": "Exact fractions and exact rational-function identities",
        "all_passed": all(item["passed"] for item in CHECKS),
        "count": len(CHECKS),
        "checks": CHECKS,
        "exact_endpoint_data": endpoint_data,
        "interpretation": (
            "These checks corroborate displayed identities and individual rational comparisons. "
            "They do not establish interval signs by numerical sampling. The interval proofs are "
            "the reciprocal-majorant, curvature, concavity, and tangent arguments in terminal.qmd. "
            "This is not official qmd-prover verification."
        ),
    }
    output = Path(__file__).resolve().with_name("r2_terminal_exact_checks.json")
    output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"all_passed": record["all_passed"], "count": record["count"], "output": str(output)}))


if __name__ == "__main__":
    main()
