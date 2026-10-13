from fractions import Fraction as F
from pathlib import Path
import json
from rational_algebra import R
HERE=Path(__file__).resolve().parent
x=R((0,1));h=2*x/(1-x);L=1+h
checks=[]
def check(name,value):
 ok=value.zero() if isinstance(value,R) else bool(value)
 checks.append({'name':name,'pass':ok});assert ok,name
s=(1381*h+1712)/(500*(h+2));v=2*(h+7)/67
T=F(2961,100)*h*h/(L*(h+2));oldB=2*s+5;C=2*s+3-F(13,10)*T/oldB;D=2*s+1-T/C
kappa=F(2961,50);gamma=F(13,10)*kappa
b=F(803,125)+F(21,10)*x;c=F(1053,125)+F(21,10)*x
W=(1+x)*b-gamma*x*x/c;Dh=F(553,125)+F(21,10)*x-kappa*x*x/W
check('transformed energy',T-kappa*x*x/(1+x))
check('transformed common denominator',W-(1+x)*C)
check('transformed original tail response',Dh-D)
check('transformed affine threshold',1/v-F(67,2)*(1-x)/(7-5*x))
c0=F(1053,125);cstar=F(1228,125)
check('upper c endpoint',c.at(F(2,3))==cstar)
check('first rational comparison',gamma/cstar==F(38493,4912) and gamma/cstar>F(39,5))
check('second rational comparison',gamma*c0/cstar**2==F(40533129,6031936) and gamma*c0/cstar**2>F(33,5))
check('third rational comparison',c0/cstar==F(1053,1228) and c0/cstar>F(4,5))
check('W tangent numerator derivative',W-x*W.diff()-(F(803,125)+x*x*(gamma*c0/c**2-F(21,10))))
check('W curvature',W.diff().diff()-(F(21,5)-2*gamma*c0*c0/c**3))
check('negative curvature numerical threshold',F(33,5)*F(4,5)>F(21,10))
U=F(32,5)+F(9,2)*x*x;V=F(13,2)+F(43,5)*x-F(57,10)*x*x
check('tangent quadratic remainder',F(22,3)+F(22,5)*x-V-F(57,10)*(x-F(7,19))**2-F(17,285))
check('convex-function tangent anchor',F(32,5)+F(9,2)*F(16,45)==8)
check('sqrt5 lower bound',F(11,5)**2<5)
Q=kappa*x*x/W
check('quadratic-over-denominator curvature',Q.diff().diff()-kappa*(2*(W-x*W.diff())**2/W**3-x*x*W.diff().diff()/W**2))
check('uniform curvature threshold',16*kappa/125==F(23688,3125) and 16*kappa/125>F(15,2))
a=F(3,19);z=F(2,3);g=F(67,2)*(1-x)/(7-5*x)
lg=g.at(a)+(g.at(z)-g.at(a))*(x-a)/(z-a)
omega=(x-a)*(z-x)
check('exact chord remainder',g-lg-335*omega/((7-5*a)*(7-5*z)*(7-5*x)))
check('chord coefficient bound',335/((7-5*a)*(7-5*z)**2)==F(57285,14278)<F(201,50))
check('left endpoint response',Dh.at(a)-F(4561,1000)==F(23710670971,60245409817000))
check('right endpoint response',Dh.at(z)-F(307,100)==F(3931,146701500))
check('threshold endpoints',g.at(a)==F(268,59) and g.at(z)==F(67,22))
check('left endpoint gap',F(4561,1000)-F(268,59)==F(1099,59000)>F(37,2000))
check('right endpoint gap',F(307,100)-F(67,22)==F(27,1100)>F(37,2000))
check('interval chord length bound',(z-a)**2/4==F(841,12996)<F(1,15))
check('uniform gap arithmetic',F(37,2000)+(F(15,4)-F(201,50))*F(1,15)==F(1,2000))
result={'all_passed':all(c['pass'] for c in checks),'count':len(checks),'checks':checks,'verification_type':'Supplementary exact rational algebra; not qmd-prover certification.'}
(HERE/'tail_curvature_exact_checks.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
