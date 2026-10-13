"""Exact corroboration of the proposed R3 one-chart Psi argument.
No floating-point evaluations, sample grids, or interval-sign certificates.
The global implications are the calculus proof in r3_terminal_proposal.md.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sys
PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / 'review'))
from rational_algebra import R
checks = []
def check(name, expression):
    result = expression.zero() if isinstance(expression, R) else bool(expression)
    checks.append({'name': name, 'passed': result})
    if not result:
        raise AssertionError(name)
h = R((0, 1)); L = h + 1
b0 = F(213469, 1920000); b1 = F(225, 268); b2 = F(11452440743, 3591200000)
b3 = F(1773689, 1600000); b4 = F(74489644841, 4502400000); b5 = F(23869857, 3927875)
N = 300*h**3 + 1295*h**2 + 1349*h - 96
D = 2*h*L*(h+2)**2*(60*h+127)
S = 2*h*N/(D-N)
R0 = F(389,3350)*h - F(25913,33500) - b0/h + b1/(h+1)**2 - b2/(h+1) + b3/(h+2)**2 + b4/(h+2) - b5/(h+F(127,60))
s = (1381*h+1712)/(500*(h+2)); v = 2*(h+7)/67
e = 3*(60*h**2+127*h-8)/(h*L*(h+2)*(60*h+127))
k = e-1/(2*(h+2)**2)
A = 493/(100*(h+2)**2)
J = 1-2*k/(1-k)-(F(129,100)+1/(4*L))*k
Gstar = A*(26*h-5)/(60*h**2)*(1+33/(400*L))
Z = s+h*(J+Gstar)-v*F(987,100)*h**2*e
check('original head identity', k-N/D)
check('retained partial-fraction identity', R0-(Z+S))
M = F(9,2)/(h+2) + F(6,5)/(h+2)**2 - 1/(9*h)
G = R0 - M
P = (395*h**2+878*h-40)*(D-N) - 180*h**2*(h+2)**2*N
check('one majorant product identity', M-S-P/(90*h*(h+2)**2*(D-N)))
z = h-F(1,2)
Hbase = F(302595,2)*h**2 + 294165*h - F(244251,8)
H = Hbase + h**2*(4-h)*(6600*h**2+39410*h+52858)
check('global squared remainder identity', P-F(17937,32)+F(51717,8)*z-z**2*H)
check('remainder base increases', Hbase.diff()-(302595*h+294165))
check('remainder base endpoint bound', Hbase.at(F(3,8))==F(12935259,128)>100000)
check('global quadratic minimum', F(17937,32)-F(51717,8)**2/400000>450)

epsilon=b0-F(1,9); C=b3-F(6,5)
check('small positive pole', epsilon==F(407,5760000)>0)
check('negative square coefficient', C<0)
x=R((0,1)); alpha=F(7,60)
f=(b2*(1-x)-3*b1*x)/(1-x)**4
Q=b4-F(9,2)+3*C*x-f-b5/(1+alpha*x)**3-epsilon/(1-2*x)**3
xh=1/(h+2)
Qh=b4-F(9,2)+3*C*xh-(b2*(1-xh)-3*b1*xh)/(1-xh)**4-b5/(1+alpha*xh)**3-epsilon/(1-2*xh)**3
check('normalized curvature identity', (h+2)**3*G.diff().diff()/2-Qh)
check('first derivative of head group', f.diff()-3*((b2-b1)-(b2+3*b1)*x)/(1-x)**5)
check('second derivative of head group', f.diff().diff()-12*((b2-2*b1)-(b2+3*b1)*x)/(1-x)**6)
check('left endpoint derivative coefficients', b2>3 and b1<1)
check('head group left derivative', f.diff().at(F(1,6))>3/F(5,6)**5>3)
check('right endpoint derivative coefficients', b2>F(637,200) and b1<F(21,25))
check('head group right derivative identity', f.diff().at(F(2,5))==F(625,81)*(3*b2-11*b1))
check('head group right derivative lower bound', F(625,81)*(3*F(637,200)-11*F(21,25))==F(175,72)>F(12,5))
check('reciprocal derivative estimate', b5<F(61,10) and -F(12,5)+F(7,20)*F(61,10)==-F(53,200)<0)
maxf=(b2+3*b1)**4/(256*b1**3)
check('head group scalar maximum', f.at((b2-b1)/(b2+3*b1))==maxf)
check('head group maximum bound', maxf<F(176,25))
a = F(319,100); b = F(67,80)
fc = (a-(a+3*b)*x)/(1-x)**4
check('coarse head coefficients', b2<a and b1>b)
check('coarse maximum derivative', fc.diff()-3*(a-b-(a+3*b)*x)/(1-x)**5)
check('coarse pointwise difference', fc-f-((a-b2)*(1-x)+3*(b1-b)*x)/(1-x)**4)
check('coarse maximum identity', fc.at((a-b)/(a+3*b))==F(2281**4,12800000*67**3))
check('coarse maximum strict bound', F(176,25)-F(2281**4,12800000*67**3)==F(31552288479,3849766400000)>0)
check('affine positive contribution', b4-F(9,2)+3*C*F(8,19)>F(119,10))
check('shifted loss bound', b5*F(150,157)**3<F(16,3))
check('small pole loss bound', epsilon*F(19,3)**3<F(1,50))
check('uniform curvature margin', F(119,10)-F(176,25)-F(16,3)-F(1,50)==-F(37,75)>-F(1,2))
check('positive curvature head value', f.at(F(2,7))==F(343,625)*(5*b2-6*b1))
check('positive curvature head bound', F(343,625)*(5*F(319,100)-6*F(67,80))==F(149891,25000)<6)
check('positive curvature shifted loss', b5*F(30,31)**3<F(61,10)*F(30,31)**3<F(28,5))
check('positive curvature coarse margin', F(119,10)-6-F(28,5)-F(1,50)==F(7,25)>F(1,4))
Fcurved=G+F(1,2)/(h+2)
check('convex compensation', Fcurved.diff().diff()-2*(Qh+F(1,2))/(h+2)**3)
check('tangent compensation identity', F(1,2)*(F(1,3)-(h-1)/9-1/(h+2))+(h-1)**2/(18*(h+2)))
check('tangent height value', G.at(1)==F(208251137,16401600000)>F(1,80))
check('tangent height slope', -F(1,400)<G.diff().at(1)==-F(42620371163,18402595200000)<0)
check('right-hand positive slope', G.diff().at(F(3,2))==F(5115313959269,1118040013125000)>0)
check('maximum tangent correction', F(5,8)**2/(18*F(19,8))==F(25,2736))
check('improved full-range margin', F(1,80)-F(1,800)-F(25,2736)==F(289,136800)>F(27,16000))
output={'kind':'exact algebraic corroboration only','checks':checks,'passed':all(c['passed'] for c in checks),'count':len(checks)}
path=Path(__file__).with_name('r3_terminal_exact_checks.json')
path.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'passed':output['passed'],'count':output['count'],'output':str(path)}))
