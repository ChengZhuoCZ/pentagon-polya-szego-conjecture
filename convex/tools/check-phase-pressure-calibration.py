"""Exact fourth-round checks. Requires SymPy; reads the archived original phase proof."""
import sympy as S
Q=S.Rational
t,s,r,M,z=S.symbols('t sigma r M z')
T=Q(27,50);X=t/T;h=Q('.705')-Q('.6')*t;g=Q('.59');theta=Q(413,3000);phi=Q(413,750);ee=Q(14,15)*(1+h)
mu2=Q('.6')*X**2*(1-s)
mu3=(1-s)*(Q('.78')-Q('.26')*X-Q('.48')*X**2)+s*(Q('.08')-Q('.16')*X+Q('.18')*X**2)
muA=(1-s)*(Q('.26')*X-Q('.06')*X**2)+s*(Q('.82')-Q('.90')*X+Q('3.12')*X**2)
delta=2-Q('1.2')*M;pp=1+Q('.6')*M
alpha=r*delta*(delta+4*pp)/4;beta=r*r*(delta+pp)
FM=3*delta**2*pp**2/8+delta*r*pp*s+r*r/4*(delta**2+8*delta*pp+4*pp**2)*s*s+2*r**3*s**3+3*r**4*s**4/2
KK=(1+r)**2*(-1+Q('1.2')*(Q('2.5')+r/4));HH=Q('.6')*(1+r)**3;LL=(1+r)*(r+2-Q('.6')*(Q('2.5')+r/4)**2)
D=Q('.05292')-Q('.099')*t*t-(Q('.08726002')*t+(Q('.141')+Q('.0555')*t-Q('.046')*t*t)*t*t)*s+(Q('.309')-Q('.23023')*t*t+Q('.0677')*t**4-Q('.005')*t**6)*s*s
ED=7*g*h*(M**5+2*M**4)*D-theta*(1+8*h)*M**3*(delta**2/2+2*r*r*s*s)-phi*t*t*M*FM-g*ee*M*M*t*s*(alpha+s*beta)+muA*(g*M*(LL+s)*t*t+g*g*M*M*KK*t-g**3*M**3*HH)-Q(1,2500)
for l,mu in [(2,mu2),(3,mu3)]:
 ED+=mu*(t*t*(1+l*r*s*s)**2+g*M*t*((r/2+l)*s+(l*r+Q(l*l,2))*s*s)-g*g*M*M*(1+l*l*s*s)/2)
def red(ex):
 return S.Poly(S.expand(ex),r).rem(S.Poly(r*r+r-1,r)).as_expr().expand()
cs=[red(S.diff(ED,M,i).subs(M,1)/S.factorial(i)) for i in range(3)]
QQ=red(sum(cs[i]*(r*t*t*(1-s*s))**i for i in range(3)))
p=[S.Poly(QQ,s).nth(i) for i in range(8)]
ef=p[2]-Q(22,27)*t*t
f=ef-Q('.15')+Q('.2')*t
Ds=red(4*(p[0]+Q(1,200))*f-p[1]**2);Dl=red(4*p[0]*f-p[1]**2)
J0=-Q('.3092')+Q('6.1592')*r-(Q('.44424')+Q('1.50576')*r)*X-(Q('.96')+Q('.24')*r)*X**2
kk=Q('.7')*(Q('4.5')+3*r)-Q('.1')*(Q('4.5')+3*r)*X-(Q('1.77')+Q('.78')*r)*X**2
ap=g*(1+r*t*t);Q0=21*h*(Q('.14095')-Q('.0536')*t*t)+Q(448,375)*r
UU=red(27*kk*Q0*(Q('.15')-Q('.2')*t)-2*ap*J0**3)
rL=Q(309,500);rU=Q(15451,25000);rr=(S.sqrt(5)-1)/2

def low(a):
 a=red(a);u=a.coeff(r,0);v=a.coeff(r,1)
 assert not u.has(r) and not v.has(r)
 return u+v*(rL if v>=0 else rU)
def high(a):return -low(-a)

# Exact replay: finite formulae and local bounds, not an independent PDE proof.
import json,re
from pathlib import Path
checks={};details={}
def ck(name,value):
 assert bool(value),name
 checks[name]=True
def eq(name,a,b=0):ck(name,red(a-b)==0)
def coeffs(pol,center):return [red(S.diff(pol,t,i).subs(t,center)/S.factorial(i)) for i in range(S.degree(pol,t)+1)]
def tail(co,R,k):return sum(max(abs(low(co[i])),abs(high(co[i])))*R**(i-k) for i in range(k,len(co)))
# Original 50 full coefficients identify the reconstructed source polynomials.
archive=Path(__file__).resolve().parent.parent/'archive/before-fourth-replacement/workspace__ps-pressure-low-ratio-rank-one-payment-1011.qmd.txt'
old=archive.read_text()
for name,pol,a,b,N,start,end in [
 ('Ds',Ds,Q(0),Q('.1'),18,'$D_s$ 的 $[0,1/10]$ 十八阶正基：','$D_l$ 的 $[1/10,27/50]$ 三十阶正基：'),
 ('Dl',Dl,Q('.1'),T,30,'$D_l$ 的 $[1/10,27/50]$ 三十阶正基：','特别地，三十阶表')]:
 chunk=old.split(start)[1].split(end)[0]
 rows=re.findall(r'^\|(\d+)\|(-?\d+)\|(-?\d+)\|(\d+)\|(\d+)\|$',chunk,re.M)
 ck(name+'_source_table_row_count',len(rows)==N+1)
 powers=[red(S.diff(pol,t,j).subs(t,a)/S.factorial(j)*(b-a)**j) for j in range(S.degree(pol,t)+1)]
 for idx,ns,ms,ds,js in rows:
  i=int(idx);value=red(sum(S.binomial(i,j)/S.binomial(N,j)*powers[j] for j in range(min(i,len(powers)-1)+1)))
  eq(name+'_source_identity_'+idx,value,(S.Integer(ns)+S.Integer(ms)*r)/S.Integer(ds))
# Also match all nine earlier U lower bounds, and its stated exact row 2.
co=coeffs(UU,0)
ubs=list(map(Q,['.408','.201','.198','.525','1.171','1.943','2.449','2.255','1.626']))
for i,bound in enumerate(ubs):
 val=red(sum(S.binomial(i,j)/S.binomial(8,j)*T**j*co[j] for j in range(i+1)))
 ck('U_original_bound_'+str(i),low(val)>bound)
 if i==2:eq('U_original_exact_row_2',low(val),Q(270879879811020629631,1367187500000000000000))
ck('root_isolation',rL*rL+rL-1<0<rU*rU+rU-1)
ck('source_degrees',S.degree(UU,t)==8 and S.degree(Ds,t)==18 and S.degree(Dl,t)==18)
# New two-segment U and three-segment Dl bounds.
rows=[('U1',UU,Q('.135'),Q('.135'),Q('.42'),Q('3.49'),Q('24.29'),3,Q(42)),
      ('U2',UU,Q('.405'),Q('.135'),Q('2.045'),Q('2.783'),None,2,Q('50.75')),
      ('Dl1',Dl,Q('.16'),Q('.06'),Q('.00645'),Q('.00873'),None,2,Q('.667')),
      ('Dl2',Dl,Q('.31'),Q('.09'),Q('.01048'),Q('.014'),None,2,Q('.721')),
      ('Dl3',Dl,Q('.46'),Q('.08'),Q('.00190'),Q('.0031'),Q('1.589'),3,Q('14.316'))]
for name,pol,a,R,L0,M1,L2,k,E in rows:
 c=coeffs(pol,a);v0=low(c[0]);v1=max(abs(low(c[1])),abs(high(c[1])));err=tail(c,R,k)
 ck(name+'_constant',v0>L0);ck(name+'_linear',v1<M1);ck(name+'_tail',err<E)
 if L2 is not None:ck(name+'_quadratic',low(c[2])>L2)
 details[name]={'center':str(a),'radius':str(R),'constant_lower_exact':str(v0),'linear_abs_upper_exact':str(v1),'tail_exact':str(err),'tail_order':k}
c=coeffs(Ds,0)
ck('Ds_constant',low(c[0])>Q('.003'))
ck('Ds_linear',low(c[1])>Q('.720'))
ck('Ds_quadratic',low(c[2])>-11)
cubic=low(c[3])+sum(min(0,low(c[j]))*Q('.1')**(j-3) for j in range(4,len(c)))
ck('Ds_aggregated_cubic',cubic>45);details['Ds_cubic_lower_exact']=str(cubic)
ck('Ds_bracket_decreasing',-11+90*Q('.1')<0)
eq('Ds_endpoint_bracket',Q('.720')-11*Q('.1')+45*Q('.1')**2,Q('.070'))
ck('U_first_square_payment',Q('.42')-Q('3.49')**2/(4*Q('18.62'))>Q('1/4'))
eq('U_first_quadratic',Q('24.29')-42*Q('.135'),Q('18.62'))
ck('U_second_payment',Q('2.045')-Q('2.783')*Q('.135')-Q('50.75')*Q('.135')**2>Q('1/4'))
eq('Dl_first_payment',Q('.00645')-Q('.00873')*Q('.06')-Q('.667')*Q('.06')**2,Q('.003525'))
eq('Dl_second_payment',Q('.01048')-Q('.014')*Q('.09')-Q('.721')*Q('.09')**2,Q('.0033799'))
ck('Dl_third_quadratic',Q('1.589')-Q('14.316')*Q('.08')>Q('.44'))
ck('Dl_third_square_payment',Q('.00190')-Q('.0031')**2/(4*Q('.44'))>Q('9/5000'))
ck('Dl_other_segments_payment',min(Q('.003525'),Q('.0033799'))>Q('9/5000'))
# Independent algebra for the shared pressure/corner arguments.
a0,s0,h0,rho,lam,nu,rrho=S.symbols('a0 s0 h0 rho lam nu rrho',positive=True)
eq('pressure_reciprocal_gap',1/(4*h0)-1/(4*s0)+(h0-s0)/(4*s0**2),(h0-s0)**2/(4*s0**2*h0))
x0,y0=S.symbols('x0 y0',positive=True)
eq('transport_young_square',x0*x0*y0*y0+1/(4*x0*x0)-y0,(x0*y0-1/(2*x0))**2)
# For rho^(nu+k) cos(nu theta), the polar Laplacian factor is (nu+k)^2-nu^2.
eq('corner_harmonic_factor',nu**2-nu**2)
eq('corner_corrected_factor',(nu+2)**2-nu**2,4*(nu+1))
b0=lam/(4*(nu+1));eq('corner_barrier_cancellation',4*(nu+1)*b0-lam)
# Dilation, equal edge pressures, and normalized boundary integral.
ell,area,mm=S.symbols('ell area mm',positive=True)
eq('regular_edge_pressure',(2*lam/(5*a0))/(lam/(5*a0*ell/2)),ell)
eq('regular_boundary_calibration',S.Rational(1,4)*5*a0*2*S.sqrt(lam)*ell,(5*a0*ell/2)*S.sqrt(lam))
vv=S.symbols('vv',nonnegative=True)
eq('pressure_equation_scaling',(lam+lam*vv)**2/lam**2,(1+vv)**2)
print(json.dumps({'all_pass':True,'count':len(checks),'checks':checks,'exact_bounds':details,'scope':'Exact local phase polynomials and 50 archived coefficient identities, complete Taylor remainder payments, and pressure/corner algebra. Does not certify PDE regularity, existence, or the global root theorem.'},ensure_ascii=False,indent=2))
