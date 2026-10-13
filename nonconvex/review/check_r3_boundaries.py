"""Supplementary exact checks for the R3 boundary and T.2 replacements.

The interval arguments are written in the manuscript. This script checks
their formal identities and scalar rational arithmetic without sampling.
"""

from fractions import Fraction as F
from pathlib import Path
import json
from rational_algebra import R

checks = []


def check(name, condition):
    checks.append({"name": name, "passed": bool(condition)})


# Polynomials in y, with exact rational functions of a formal parameter
# as coefficients. This keeps both variables formal.
def add(*polynomials):
    return [sum((p[j] for p in polynomials if j < len(p)), R(0))
            for j in range(max(map(len, polynomials)))]


def scale(polynomial, scalar):
    return [R(scalar) * x for x in polynomial]


def mul(p, q):
    result = [R(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            result[i + j] = result[i + j] + x * y
    return result


def diff(p):
    return [j * p[j] for j in range(1, len(p))] or [R(0)]


def zero(p):
    return all(x.zero() for x in p)


c = R((0, 1))
one = [R(1)]
y = [R(0), R(1)]
y2 = mul(y, y)
one_plus_y = add(one, y)

# W_eta'(y) and W_eta''(y), for both eta values used in the proof.
for label, eta in [("1", R(1)), ("2-c", 2-c)]:
    denominator = add([eta], scale(y2, -c))
    first_numerator = add(mul(diff(y2), denominator),
                          scale(mul(y2, diff(denominator)), -1))
    check(f"W_{label} first derivative", zero(add(first_numerator, scale(y, -2*eta))))
    second_numerator = add(mul(diff(first_numerator), denominator),
                           scale(mul(first_numerator, diff(denominator)), -2))
    expected = add([2*eta**2], scale(y2, 6*eta*c))
    check(f"W_{label} second derivative", zero(add(second_numerator, scale(expected, -1))))

head = mul(one_plus_y, add(one, scale(y2, -1)))
decomposed_head = add(mul(one_plus_y, add(one, scale(y2, -c))),
                      scale(mul(one_plus_y, y2), -(1-c)))
check("concave head decomposition", zero(add(head, scale(decomposed_head, -1))))
tail_left = scale(add(one, y2), c*(2-c))
tail_right = add(scale(add([2-c], scale(y2, -c)), c), scale(y2, 2*c))
check("convex reciprocal tail decomposition", zero(add(tail_left, scale(tail_right, -1))))
check("compact-coordinate head numerator",
      zero(add(mul(add(one, scale(y, -1)), mul(one_plus_y, one_plus_y)), scale(head, -1))))

Y = F(2, 3)
endpoint = (1+Y)*(1-Y*Y)/(1-c*Y*Y)-F(1, 3)-3*c*(1+Y*Y)/(5*(2-c-c*Y*Y))
endpoint_formula = 25/(3*(9-4*c))-F(1, 3)-39*c/(5*(18-13*c))
check("container endpoint formula", (endpoint-endpoint_formula).zero())
check("endpoint head increases with c",
      ((25/(3*(9-4*c))).diff()-100/(3*(9-4*c)**2)).zero())
check("endpoint tail increases with c",
      ((39*c/(5*(18-13*c))).diff()-F(702, 5)/(18-13*c)**2).zero())
check("weaker upper bound on c", F(13, 15)<F(7, 8))
check("positive first denominator threshold", 1-F(7, 8)*Y*Y==F(11, 18)>0)
check("positive second denominator threshold", 2-F(7, 8)*(1+Y*Y)==F(53, 72)>0)
check("container endpoint zero margin", F(2, 3)-F(3, 5)*F(7, 9)==F(1, 5)>F(1, 8))
check("container endpoint two-thirds head bound", F(25, 3)/(9-4*F(6, 7))==F(175, 117))
check("container endpoint two-thirds tail bound", F(39, 5)*F(7, 8)/(18-13*F(7, 8))==F(273, 265))
check("container full interval margin", F(175, 117)-F(1, 3)-F(273, 265)==F(4099, 31005)>F(1, 8))

# The gain is affine in A; the parameter c here is used formally as A.
gain_numerator = [12-3*c, -28+8*c, 6-5*c]
star_numerator = [R(12), R(-28), R(6)]
expected_difference = scale(mul(add(one, scale(y, -1)), add([R(-3)], scale(y, 5))), c)
check("full gain minus J_star",
      zero(add(gain_numerator, scale(star_numerator, -1), scale(expected_difference, -1))))
gain_at_half = (12-3*c)/20-(7-2*c)/10+(6-5*c)/80
check("gain endpoint at p=1/2", (gain_at_half+(2+c)/80).zero())
check("gain derivative upper numerator", (-(12-3*c)+(6-5*c)+(6+2*c)).zero())
p = R((0, 1))
f = 3/(4*(1+2*p)**2)
star = 3/(10*p)-F(7, 10)+3*p/20
tangent = F(3, 8)-3*p/8
check("reciprocal function second derivative", (f.diff().diff()-18/(1+2*p)**4).zero())
check("tangent value", f.at(F(1, 2))==F(3, 16))
check("tangent slope", f.diff().at(F(1, 2))==-F(3, 8))
check("tangent payment identity",
      (tangent-p*star-(F(3, 40)+p*(13-6*p)/40)).zero())
check("positive tangent margin on p interval", 13-6*F(1, 2)>0)

# The T.2 ratio is increasing by its exact logarithmic derivative.
h = R((0, 1))
ratio = h**2*(h+2)/((h+1)*(51*h+82)**2)
log_derivative = (113*h**2+410*h+328)/(h*(h+1)*(h+2)*(51*h+82))
check("T2 logarithmic derivative identity", (ratio.diff()/ratio-log_derivative).zero())
check("T2 ratio endpoint", ratio.at(4)==F(24, 102245))
check("T2 ratio endpoint bound", F(24, 102245)<F(1, 4225))
check("T2 energy scaling", F(2961, 100)*25==F(2961, 4))
check("T2 final radicand ratio", F(2961, 4*4225)==F(2961, 16900)<F(30, 169))

report = {
    "scope": "Supplementary formal identities and exact rational comparisons; no parameter sampling.",
    "official_qmd_prover_run": False,
    "proof_relies_on_execution": False,
    "check_count": len(checks),
    "all_passed": all(c["passed"] for c in checks),
    "checks": checks,
}
Path(__file__).with_name("r3_boundary_exact_checks.json").write_text(json.dumps(report, indent=2)+"\n")
print(json.dumps({k:v for k,v in report.items() if k!="checks"}, indent=2))
raise SystemExit(0 if report["all_passed"] else 1)
