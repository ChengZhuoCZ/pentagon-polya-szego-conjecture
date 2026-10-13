#!/usr/bin/env python3
"""Exact supplementary checks for the R4 denominator and head reductions.

Uses the Python standard library. Execution is not a proof premise, and this
is not an official qmd-prover verdict.
"""
from fractions import Fraction as F
import json
from pathlib import Path
from rational_algebra import R

checks = []

def check(name, assertion):
    checks.append({'name': name, 'passed': bool(assertion)})

s = R((0, 1))
h = R((0, 1))
L = 1 + h
check('order_square_identity', (s*(s-1) - ((s-F(1,2))**2-F(1,4))).zero())
check('radical_scalar_gap', F(81,4)-20 == F(1,4))
check('energy_multiplier', 3*F(4,5)*F(9,2) == F(54,5))
check('uniform_denominator_square', ((2*s+1)*(s+2)-F(54,5)*(s-F(1,2))-(2*(s-F(29,20))**2+F(639,200))).zero())
check('positive_denominator_constant', F(639,200) > 0)
check('head_endpoint', F(3,2)/F(11,8)**2 == F(96,121))
check('head_endpoint_gap', 1-F(96,121) == F(25,121))
check('height_threshold', 2-F(4,3)**2 == F(2,9))
R1 = L**4/(10*h**2*(h+2))
check('large_height_reciprocal_identity', (6*R1/(h+2) - 3/(5*(1-L**-2)**2)).zero())
check('large_height_denominator_endpoint', 1-F(3,7)**2 == F(40,49))
check('large_height_ratio_endpoint', 3/(5*F(40,49)**2) == F(7203,8000))
check('large_height_positive_margin', 1-F(7203,8000) == F(797,8000))
result = {
    'description': 'R4 uniform denominator and direct reciprocal head bounds',
    'official_qmd_prover_verdict': False,
    'proof_relies_on_execution': False,
    'check_count': len(checks),
    'all_passed': all(item['passed'] for item in checks),
    'checks': checks,
}
Path(__file__).with_name('r4_pole_and_head_exact_checks.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'check_count': len(checks), 'all_passed': result['all_passed']}))
if not result['all_passed']:
    raise SystemExit(1)
