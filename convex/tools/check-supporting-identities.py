"""Exact local checks for the analytic replacement. Requires SymPy.
This is not a proof checker; continuous inequalities remain in the QMD proofs.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import contextlib,io,json,runpy
import sympy as S
here=Path(__file__).resolve().parent
mean_path=here/'check-nine-constants.py'
if not mean_path.exists():mean_path=here/'凸五边形-解析接口替换-20261012/tools/check-nine-constants.py'
with contextlib.redirect_stdout(io.StringIO()): env=runpy.run_path(str(mean_path))
R=env['R'];aa=env['a'];rr=env['r'];XX=env['X'];al=env['al']
checks={}
def ok(name,cond):
 assert cond,name
 checks[name]=True
def eq(name,x,y):ok(name,S.cancel(S.expand(x-y))==0)
def bound(name,v,l,h):
 v=R(v);ok(name,F(l)<=v.l<=v.h<=F(h))
a,b,q,x,alpha=S.symbols('a b q x alpha',real=True);i=S.I;z=a+i*b;zb=a-i*b;R2=a*a+b*b
p2=zb*(zb-2)/8;p21=zb**2*(-R2+2*a+4*i*b)/96
p3=z*z*(z+3)/48;p31=z**3*(-R2-3*a+5*i*b)/768
radials={
 (1,1):(z+1)/2,
 (1,3):z*(-R2-a+3*i*b)/16,
 (1,5):z*R2*(R2+a-5*i*b)/384,
 (2,2):z*(z+2)/8,
 (2,4):z*z*(-R2-2*a+4*i*b)/96,
 (-3,3):zb*zb*(3-zb)/48,
 (-2,2):p2,(-2,4):p21,(3,3):p3,(3,5):p31,
 (-4,4):zb**3*(zb-4)/384,
 (-4,6):zb**4*(-R2+4*a+6*i*b)/7680}
for (k,degree),value in radials.items():
 n=abs(k);l=(degree-n)//2
 psi=(-1)**l*(z if k>=0 else zb)**n*R2**l/(2**degree*factorial(l)*factorial(n+l))
 if k<0:psi*=(-1)**n
 eq(f'full_weight_radial_{k}_{degree}',psi-i*S.diff(psi,b),value)
def d(p,e):return (2-2*e)*p-i*S.diff(p,b)
def dprime(p,e):return S.expand(2*i*d(p,e)+S.diff(d(p,e),b))
eq('V_p2_dplus_derivative',dprime(p2,1),-b/2+i*(3-2*a)/4)
eq('V_p3_dplus_derivative',dprime(p3,1),-b*(2*a+3)/8+i*(a*a+3*a+1-b*b)/8)
eq('V_p21_dplus_derivative',dprime(p21,1),b*(9*a+2*b*b-6)/24+i*(a**3-3*a+(3*a-9)*b*b)/24)
FF=-4*a**3+21*a-6+(14-4*a)*b*b;PP=2*a**4-7*a**3+3*a+21*(1-a)*b*b-2*b**4
eq('V_p21_dminus_derivative',dprime(p21,-1),(b*FF-i*PP)/24)
Q=F(81,125);T=F(27,50);L=F(107,100)
radR=(7-4*a)/2-S.Rational(81,125)*(12*a*a+42*a+21-4*b*b)/24
radT=-(4*a*a-14*a+7-4*b*b)/4+S.Rational(81,125)*(4*a**3+21*a*a+21*a+3-(12*a+21)*b*b)/24
eq('V_combined_leading_derivative',-dprime(p2,-1)+S.Rational(81,125)*dprime(p3,-1),b*radR+i*radT)
N=4*a**5+15*a**4+4*a**3+(-8*a**3+30*a*a+36*a)*b*b-(12*a+25)*b**4
MM=3*a**4+5*a**3-3*a*a+(2*a*a+15*a+5)*b*b-b**4
Np=3*a**4+4*a**3+(6*a*a+36*a)*b*b-5*b**4
Mp=a**3-3*a*a+(3*a+5)*b*b
eq('V_p31_dminus',d(p31,-1),-N/768-i*b*MM/192)
eq('V_p31_dplus',d(p31,1),-Np/768-i*b*Mp/192)
Y=a*a+alpha*alpha
cp2=- (Y+a)/(16*Y)
cp3=(10*a**4+12*a**3-20*a*a*alpha*alpha-9*a*a-12*a*alpha*alpha+3*a+2*alpha**4+3*alpha*alpha)/(192*Y)
cp21=(2*Y*Y+3*a*Y-3*a-3*alpha*alpha)/(192*Y)
p31num=10*a**6+10*a**5-10*a**4*alpha*alpha+2*a**4+20*a**3*alpha*alpha-24*a**3-18*a*a*alpha**4-52*a*a*alpha*alpha+33*a*a-22*a*alpha**4+48*a*alpha*alpha-15*a+2*alpha**6+10*alpha**4-15*alpha*alpha
cp31=-p31num/(3072*Y)
for name,p,expected in [('p2',p2,cp2),('p3',p3,cp3),('p21',p21,cp21),('p31',p31,cp31)]:
 hp=sum((-1)**j*S.diff(p,b,j)/(2*i)**(j+1) for j in range(S.degree(p,b)+1))
 exact=S.re(((a*a-alpha*alpha+2*i*a*alpha)/Y)*hp.subs(b,alpha)-hp.subs(b,0))/alpha
 eq('endpoint_integral_'+name,exact,expected)
# Evaluate exact endpoint formulas by directed rational arithmetic.
def iv(expr,**kwargs):
 expr=S.Poly(S.expand(expr),a,alpha)
 out=R()
 for (ae,be),coef in expr.terms():out+=F(int(S.numer(coef)),int(S.denom(coef)))*aa**ae*al**be
 return out
def rat(expr):
 num,den=S.fraction(S.cancel(expr));return iv(num)/iv(den)
C2=rat(cp2);C3=rat(cp3);C21=rat(cp21);C31=rat(cp31)
bound('V_Aplus_zero',(1-aa)/4+2*C2,'-1','-1/6')
bound('V_leading_joint_zero',-((2*aa**2-5*aa+1)/4-2*C2)+Q*((4*aa**3+15*aa**2+6*aa)/48-2*C3),'.48962','.48972')
bound('V_A1minus_zero',aa**3*(5-2*aa)/48-2*C21,'1/40','1/16')
bound('V_A1plus_zero',aa**3/48+2*C21,'1/40','1/16')
bound('V_Cp31',C31,'-1/2000','1/2000')
Sa=(2+rr)/(4*aa);Ca=rr/2
Hplus=(1+rr*(2*(1+aa)+1-((2*aa+1)*(1-Sa)+1-Ca)))/2
Hminus=(1+rr*(2*(1+aa)+1+((2*aa+1)*(1-Sa)+1-Ca)))/2
bound('Hplus_zero',Hplus,'1.542','1.543');bound('Hminus_zero',Hminus,'2.380','2.381')
# Correct simple geometric majorants for the full integer alias tail.
y=Q*L/2;E=lambda n:y**n/F(factorial(n))/(1-y/F(n+1));B=lambda n:E(n)+Q/2*(E(n-1)+E(n+1))
ok('alias_d0',2*B(6)/Q**6<F('.000458')<F(1,2000))
ok('alias_d1',Q*(B(5)+B(7))/Q**6<F('.002238')<F(1,400))
# All remaining radial tails: exact rational first term and positive ratio.
fall=lambda n,j:F(factorial(n),factorial(n-j))
def opJ(ds):
 d0,d1,d2=ds
 return d1+F(2,15)*d2+F(619,1000)*(d1+2*d0+F(2,15)*(d2+4*d1+4*d0))
def opP(ds):
 d0,d1,d2=ds
 return (2+F(8,15))*d0+(1+F(619,1000)+F(8,15))*d1+(1+F(619,1000))*F(2,15)*d2
Jds=[F(60,59)*(fall(7,j)*L**(7-j)/18432+fall(6,j)*L**(6-j)*(F(1,4608)+F(1,6144))) for j in range(3)]
ok('J_all_radial_tail',Q**4*opJ(Jds)<F(1,400))
Pds=[F(32,31)*(fall(6,j)*L**(6-j)/3072+fall(5,j)*L**(5-j)*(F(1,768)+F(1,1536))) for j in range(3)]
Qds=[F(16,15)*(fall(5,j)*L**(5-j)/768+fall(4,j)*L**(4-j)*(F(1,192)+F(1,768))) for j in range(3)]
ok('P_all_radial_tail',Q**4*opP(Pds)<F(1,100))
ok('Q_all_radial_tail',F(7,120)+Q**2*opP(Qds)<F(1,8))
ok('PQ_final_gap',F(4,25)-F(4,5)*Q*Q/7-F(1,100)-Q/8>F(21,1000))
def gamma(n):
 ds=[(fall(n+4,j)*L**(n+4-j)+(n+4)*fall(n+3,j)*L**(n+3-j))/F(2**(n+5)*factorial(n+2)) for j in range(3)]
 return F(32,31)*(ds[1]+2*ds[0]+F(2,15)*(ds[2]+4*ds[1]+4*ds[0]))
ok('V_all_radial_tail',Q**4*gamma(2)+Q**5*gamma(3)<F(1,125))
ok('V_final_gain',Q*F(9,250)<F(1,40) and F(49,100)+F(1,125)==F(249,500))
ok('J_final_gain',F(13,100)+F(42,100)/50+F(1,400)<F(1,7))
ok('high_mode_final_gain',F(11,384)+Q*Q/200+F(1,5000)<F(1,32))
# Actual angular measure identity, preserved amplitude orders, and four budgets.
V,Wp,H,G,e=S.symbols('V Wp H G e',real=True)
eq('measure_decomposition',sum((V/2-sign*Wp/4)*(H+2*sign*G) for sign in [-1,1]),V*H-Wp*G)
k,t,s,TT,LL=S.symbols('k t s TT LL',nonnegative=True)
raw=k*k*t*t/2+(S.Rational(4,5)*k*t*t+s)*k*t*LL+s*k**4*t**4/32
cap=(k*k/2+S.Rational(4,5)*k*k*TT*LL)*t*t+(k*LL+k**4*TT**3/32)*t*s
eq('low_mode_amplitude_gap',cap-raw,S.Rational(4,5)*k*k*LL*t*t*(TT-t)+s*k**4*t*(TT**3-t**3)/32)
rows=[]
for label,kap,ma,mb,ta,tb in [('U',F(1),F('.144'),F('.570'),F('.322'),F('.850')),('C',F(6,5),F('.206'),F('.685'),F('.464'),F('1.024'))]:
 LK=F(2381,1000)+kap**2*T*T/7
 DK=kap**6*T**4*(11+F(133,8)*T)/2000
 EK=kap**6*T**5*F(127,8)/2000
 UK=kap**2/2+F(4,5)*kap**2*T*LK+DK
 VK=kap*LK+kap**4*T**3/32+EK
 ca=ma+F(23,200)*UK;cb=mb+F(23,200)*VK
 ok('actual_spin_'+label,ca<ta and cb<tb)
 rows.append({'branch':label,'t2_coefficient':str(ca),'ts_coefficient':str(cb)})
ok('moment_constant',F(44671,20000)**2<5 and F(63,100)*F(73,100)/4<F(23,200))

# Generate the J-radial alternating coefficient identity for a symbolic n>=2.
n=S.symbols('n',integer=True,positive=True)
A0=-a*a*(a+1);A1=-(a+3);B0=2*a-a*a;B1=-1
rat1=-(2*n+1)*(2*n)/4;rat2=rat1*(-(2*n-1)*(2*n-2)/4)
Un=(2*n+1)*B0+(2*n-1)*rat1*B1+2*A0+2*rat1*A1
Gn=-((2*n+1)*A0+(2*n-1)*rat1*A1)+2*(rat1*B0+rat2*B1)
Mplus=3*n*n+(2*a+S.Rational(9,2))*n+2*a-a*a
Mminus=4*n**3+(4*a+9)*n*n+(-4*a*a+8*a+S.Rational(1,2))*n-4*a**3-5*a*a+2*a
eq('J_derivative_series_all_n_plus',Un+2*Gn/(2*n+1),Mplus)
eq('J_derivative_series_all_n_minus',Un-2*Gn/(2*n+1),Mminus)
j=S.symbols('j',real=True)
expectedM=28*j**3+(28*a+219)*j*j+(-28*a*a+160*a+S.Rational(1027,2))*j-28*a**3-87*a*a+210*a+S.Rational(723,2)
eq('J_series_ratio_positive_polynomial',(8*Mminus-Mminus.subs(n,n+1)).subs(n,j+2),expectedM)
# Independent polynomial arithmetic for eight P/Q envelopes (33 coefficients).
r=S.symbols('r',real=True)
CL=1-2*x;CU=CL+S.Rational(2,3)*x*x;SL=1-S.Rational(2,3)*x;SU=SL+S.Rational(2,15)*x*x
Ap=-a**4-2*a**3-6*a*x+x*x;Bp=-2*a**3-(2*a+4)*x
Dp=Bp-S.diff(Ap,x);Np=2*Ap+Bp+2*x*S.diff(Bp,x)
polys=[r*Bp+CU*Bp+2*SU*Ap,r*Bp+CL*Bp+2*SL*Ap,r*S.diff(Ap,x)+CL*Dp+SU*Np,r*S.diff(Ap,x)+CU*Dp+SL*Np]
ranges=[['-5.81,-5.78','-14.61,-14.57','19,19.05','-6.56,-6.51','.26,.27'],['-5.81,-5.78','-14.61,-14.57','20.35,20.41','-1.34,-1.33'],['-4.33,-4.29','-38.54,-38.49','35.14,35.20','-5.03,-4.99','.26,.27'],['-4.33,-4.29','-38.54,-38.49','38.40,38.47','-6.51,-6.46']]
Aq=3*a*a-a**3+(3*a-3)*x;Bq=3*a*a-6*a-x;Dq=Bq-S.diff(Aq,x);Nq=S.expand(2*Aq+Bq+2*x*S.diff(Bq,x));N0=Nq.subs(x,0);N1=Nq.coeff(x,1)
polys += [r*Bq+CU*Bq+2*SL*Aq,r*Bq+CL*Bq+2*SU*Aq,r*S.diff(Aq,x)+CU*Dq+SL*N0+x*SU*N1,r*S.diff(Aq,x)+CL*Dq+SU*N0+x*SL*N1]
ranges += [['-1.58,-1.56','1.32,1.35','.56,.60','-.67,-.66'],['-1.58,-1.56','1.32,1.35','2.94,3.0','-.12,-.10'],['-2.55,-2.53','.09,.12','2.82,2.88','-1.20,-1.15'],['-2.55,-2.53','.09,.12','4.55,4.61']]
def ivar(expr):
 out=R()
 for (ae,re),coef in S.Poly(S.expand(expr),a,r).terms():out+=F(int(S.numer(coef)),int(S.denom(coef)))*aa**ae*rr**re
 return out
for idx,(p,rs) in enumerate(zip(polys,ranges)):
 p=S.Poly(S.expand(p),x)
 ok(f'PQ_polynomial_degree_{idx}',p.degree()==len(rs)-1)
 for k,interval in enumerate(rs):bound(f'PQ_coefficient_{idx}_{k}',ivar(p.nth(k)),*interval.split(','))
# Tight common leading gap at the one real endpoint, in both signs.
Ic=(aa*aa+aa-F(1,2)-XX)*Sa+(aa+F(1,2))*Ca
Pzero_plus=(rr*(aa+1)+rr*XX/3+(aa+F(1,2))+F(1,2)+Ic)/4
Pzero_minus=(rr*(aa+1)-rr*XX/3+(2*aa*aa+3*aa-F(1,2))+(2*aa+F(3,2))-Ic)/4
bound('PQ_H_gap_plus',F(4,5)*Hplus-Pzero_plus,'4/25','1')
bound('PQ_H_gap_minus',F(4,5)*Hminus-Pzero_minus,'4/25','1')

print(json.dumps({'scope':'Fixed identities, constants and tail majorants only; no full mathematical or formal verification','all_pass':True,'check_count':len(checks),'checks':checks,'spin_coefficients':rows},indent=2))
