"""Exact corroboration of the R4 differential head comparison.

This script checks displayed identities and rational scalar comparisons only.
It uses no floating-point arithmetic, sample grids, or executable sign premise.
The global proof is the calculus argument in r4_terminal_proposal.md.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sys

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "review"))
from rational_algebra import R

checks = []


def check(name, expression):
    result = expression.zero() if isinstance(expression, R) else bool(expression)
    checks.append({"name": name, "passed": result})
    if not result:
        raise AssertionError(name)


h = R((0, 1))
L = h + 1
N = 300*h**3 + 1295*h**2 + 1349*h - 96
D = 2*h*L*(h+2)**2*(60*h+127)
e = 3*(60*h**2+127*h-8)/(h*L*(h+2)*(60*h+127))
k = e - 1/(2*(h+2)**2)
S = 2*h*N/(D-N)
M = F(9, 2)/(h+2) + F(6, 5)/(h+2)**2 - 1/(9*h)
q = F(15, 2)*(h+2)**2*(D-N)*(M-S)/h
q_product = (395*h**2+878*h-40)*(D-N)/(12*h**2) - 15*(h+2)**2*N

check("original head variable is unchanged", k-N/D)
check("head loss uses the original k", S-2*h*k/(1-k))
check("weighted gap product identity", q-q_product)
check("positive linear rescaling, without squaring", M-S-2*h*q/(15*(h+2)**2*(D-N)))

q3 = 7680/h**5 - 48804/h**4 + 58071 - 12820*h - 33000*h**2
check("third derivative of the weighted gap", q.diff().diff().diff()-q3)
check("normalized third derivative", h**4*q3-(7680/h-48804+h**4*(58071-12820*h-33000*h**2)))
check("lower-height reciprocal bound", F(7680, 1)/F(3, 8)-48804 == -28324)
check("strict coarse constant in cubic bound", 58071 < 59000)

y = R((0, 1))
g = y**2*(59000-33000*y)
check("scalar cubic derivative", g.diff()-y*(118000-99000*y))
check("positive scalar critical point", F(118000, 99000) == F(118, 99) > 0)
gmax = F(4*59000**3, 27*33000**2)
check("scalar cubic maximum value", g.at(F(118, 99)) == gmax == F(821516000, 29403))
check("scalar cubic maximum bound", gmax < 28000)
check("strict negative third-derivative margin", -28324+28000 == -324 < 0)

check("lower-interval curvature endpoint", q.diff().diff().at(2) == F(140594, 3) > 45000)
check("strong-convexity tangent value", q.at(F(1, 2)) == F(5979, 32))
check("strong-convexity tangent slope", q.diff().at(F(1, 2)) == -F(11609, 4))
z = h-F(1, 2)
tangent = F(5979, 32)-F(11609, 4)*z+22500*z**2
minimum = F(5979, 32)-F(11609, 4)**2/90000
check("strong-convexity square completion", tangent-minimum-22500*(z-F(11609, 180000))**2)
check("strong-convexity strict margin", minimum == F(134286119, 1440000) > 90)
check("upper-interval initial derivative", q.diff().at(2) == F(537851, 4) > 0)
check("upper-interval left endpoint value", q.at(2) == 113604 > 90)
check("upper-interval right endpoint value", q.at(4) == 227460 > 90)

# Confirm that the new comparison uses precisely the retained response and M.
b0 = F(213469, 1920000)
b1 = F(225, 268)
b2 = F(11452440743, 3591200000)
b3 = F(1773689, 1600000)
b4 = F(74489644841, 4502400000)
b5 = F(23869857, 3927875)
R0 = F(389,3350)*h-F(25913,33500)-b0/h+b1/(h+1)**2-b2/(h+1)+b3/(h+2)**2+b4/(h+2)-b5/(h+F(127,60))
s = (1381*h+1712)/(500*(h+2))
v = 2*(h+7)/67
A = 493/(100*(h+2)**2)
J = 1-2*k/(1-k)-(F(129,100)+1/(4*L))*k
Gstar = A*(26*h-5)/(60*h**2)*(1+33/(400*L))
Z = s+h*(J+Gstar)-v*F(987,100)*h**2*e
G = R0-M
check("unchanged original response partial fractions", R0-Z-S)
check("original payment differs by the positive gap", Z-G-(M-S))
check("retained tangent height value", G.at(1) == F(208251137,16401600000) > F(1,80))
check("retained tangent height slope", -F(1,400) < G.diff().at(1) == -F(42620371163,18402595200000) < 0)
check("retained upper-interval slope", G.diff().at(F(3,2)) == F(5115313959269,1118040013125000) > 0)
check("retained reciprocal tangent remainder", F(1,2)*(F(1,3)-(h-1)/9-1/(h+2))+(h-1)**2/(18*(h+2)))
check("retained strict payment margin", F(1,80)-F(1,800)-F(25,2736) == F(289,136800) > F(27,16000))

output = {
    "kind": "exact algebraic corroboration only; global implications proved in prose",
    "checks": checks,
    "passed": all(c["passed"] for c in checks),
    "count": len(checks),
}
path = Path(__file__).with_name("r4_terminal_exact_checks.json")
path.write_text(json.dumps(output, indent=2)+"\n")
print(json.dumps({"passed": output["passed"], "count": output["count"], "output": str(path)}))
