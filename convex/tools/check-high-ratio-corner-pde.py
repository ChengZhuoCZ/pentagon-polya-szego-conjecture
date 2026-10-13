"""Fifth-round exact checks. Python 3 + SymPy; run from any directory."""
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

# Append to phase_model.py for a self-contained replay.
B=[red(sum(p[l]/3**l*sum(S.binomial(l,k)*S.binomial(j,k)/S.binomial(7,k)*2**k for k in range(min(j,l)+1)) for l in range(8))) for j in range(8)]
DD=red(4*p[0]*ef-p[1]**2)
Fs=[red(p[3]+t*t),red(p[4]/t**2+3),red(p[5]/t**2+4)]
q2=red(154*g*h*(Q('.309')-Q('.231')*t*t)-6*theta*(1+8*h)*r*r+Q('2.16')*phi*r*r*t*t-Q('1.2')*g*ee*r*r*t-g*g/2*(4*Q('.6')*X*X+9*(Q('.78')-Q('.26')*X-Q('.48')*X*X)))
def coeffs(pol,a):
 poly=S.Poly(pol.subs(t,t+a).expand(),t)
 return [red(poly.nth(i)) for i in range(poly.degree()+1)]
def tail(co,R,k):return sum(max(abs(low(c)),abs(high(c)))*R**(j-k) for j,c in enumerate(co) if j>=k)
# Entries: name, polynomial, center, radius, L0, U1, L2 (optional), tail order, tail upper, method, target.
# All decimals are exact rational values. Methods: endpoint absolute bound, square, or omit nonnegative quadratic.
rows=[]
for j in range(8):
 rows.append((f'beta{j}a',B[j],Q('.135'),Q('.135'),*[Q(v) for v in [
 ['.07298','.08977','1.45015'],['.12924','.17574','2.15057'],['.21545','.33562','2.86432'],['.33639','.60991','3.64357'],
 ['.49610','1.04877','4.57266'],['.69755','1.71649','5.78167'],['.94233','2.69518','7.45577'],['1.23029','4.08747','9.84334']][j][:2]],None,2,Q([
 '1.45015','2.15057','2.86432','3.64357','4.57266','5.78167','7.45577','9.84334'][j]),'absolute',Q('.02') if j<7 else Q('.0104')))
for j,vals in enumerate([
 ['.02793','.10313','.75039','3.05701'],['.05155','.17419','1.24696','4.43415'],['.08952','.26933','1.93714','6.00968'],
 ['.13529','.42368','2.86970','7.79904'],['.17847','.68179','4.11424','9.85277'],['.20406','1.09215','5.79948','12.28381'],['.19302','1.69090','8.17290','15.26102']]):
 L,U,C,E=map(Q,vals);rows.append((f'beta{j}b',B[j],Q('.405'),Q('.135'),L,U,C,3,E,'square',Q('.02')))
for name,pol,a,R,L,U,C,k,E,method,target in [
 ('beta7b',B[7],'.345','.075','.31082','3.65771','8.03753',3,'21.27347','drop','.0104'),
 ('beta7c',B[7],'.48','.06','.01313','.39829','15.90717',3,'18.27986','square','.0104'),
 ('F3a',Fs[0],'.135','.135','.68724','3.05813',None,2,'1.93001','absolute','.06'),
 ('F3b',Fs[0],'.405','.135','.08636','.75799','7.38034',3,'7.48856','square','.06'),
 ('F4',Fs[1],'.27','.27','1.32832','.72478',None,2,'5.61014','absolute','.72'),
 ('F5prime',S.diff(Fs[2],t),'.27','.27','4.84833','4.88526',None,2,'21.33958','absolute','1.97'),
 ('D1',DD,'.04','.04','.018935','.006360',None,2,'4.887956','absolute','.0099'),
 ('D2',DD,'.145','.065','.011783','.016155','.909679',3,'3.538201','square','.0099'),
 ('D3',DD,'.30','.09','.019587','.030679',None,2,'.848580','absolute','.0099'),
 ('D4',DD,'.465','.075','.013270','.007884','1.604993',3,'14.950219','square','.0099')]:
 rows.append((name,pol,Q(a),Q(R),Q(L),Q(U),Q(C) if C else None,k,Q(E),method,Q(target)))

import json,re
from pathlib import Path
checks={};details={}
def ck(n,v):
 assert bool(v),n
 checks[n]=True
def eq(n,a,b=0):ck(n,red(a-b)==0)
root=Path(__file__).resolve().parent.parent
old=(root/'archive/before-fifth-replacement/workspace__ps-pressure-opposite-corner-entire-amplitude-1011.qmd.txt').read_text()
def bern(pol,n,i,L=T):
 co=S.Poly(pol,t)
 return red(sum(S.binomial(i,j)/S.binomial(n,j)*L**j*co.nth(j) for j in range(i+1)))
spec=[('$F3$ 的实际正基系数：',Fs[0],9),('$F4$ 的实际正基系数：',Fs[1],9),('$F5$ 的实际正基系数：',Fs[2],7),('$q_2-13/2$ 的实际正基系数：',q2-Q(13,2),3),('$\\mathscr D$ 的实际正基系数：',DD,18)]
spec += [(f'$\\mathfrak B_{{11,i}}[\\beta_{j}]$ 的实际系数：',B[j],11) for j in range(7)]
source_count=0
for header,pol,n in spec:
 chunk=old.split(header)[1].split('\n\n')[1]
 matches=re.findall(r'^\|(\d+)\|(-?\d+)\|(-?\d+)\|(\d+)\|(\d+)\|$',chunk,re.M)
 ck(header+'_row_count',len(matches)==n+1)
 for idx,ns,ms,ds,js in matches:
  i=int(idx);source_count+=1
  eq(header+'_identity_'+idx,bern(pol,n,i),(S.Integer(ns)+S.Integer(ms)*r)/S.Integer(ds))
ck('original_integer_coefficients_matched',source_count==135)
# Remaining six endpoint H comparisons and the two printed exact constants.
b7x=red(B[7].subs(t,T*(1-t)));b0=b7x.subs(t,0);b1=S.diff(b7x,t).subs(t,0)
eq('beta7_original_constant',b0,Q(3535493713,1875000000)*r-Q(1045312703014233853,937500000000000000))
eq('beta7_original_linear',b1,Q(935910999,5000000000)*r-Q(80725270955784337,78125000000000000))
H=red((b7x-b0-b1*t)/t**2)
for i,bnd in enumerate(map(Q,['5.543','5.022','4.451','3.832','3.171','2.470'])):ck('beta7_original_H_bound_'+str(i),low(bern(H,5,i,Q(1)))>bnd)
ck('root_isolation',rL*rL+rL-1<0<rU*rU+rU-1)
for name,pol,a,R,L,U,C,k,E,method,target in rows:
 co=coeffs(pol,a);v0=low(co[0]);v1=max(abs(low(co[1])),abs(high(co[1])));err=tail(co,R,k)
 ck(name+'_constant',v0>L);ck(name+'_linear',v1<U);ck(name+'_tail',err<E)
 if C is not None:ck(name+'_quadratic',low(co[2])>C)
 if method=='square':
  kap=C-E*R;ck(name+'_positive_quadratic',kap>0);value=L-U*U/(4*kap)
 elif method=='drop':
  ck(name+'_nonnegative_quadratic',C>0);value=L-U*R-E*R**3
 else:value=L-U*R-E*R**2
 ck(name+'_payment',value>target)
 details[name]={'polynomial_degree':int(S.degree(pol,t)),'center':str(a),'radius':str(R),'constant_lower_exact':str(v0),'linear_absolute_upper_exact':str(v1),'quadratic_lower_exact':str(low(co[2])),'tail_order':k,'tail_upper_exact':str(err),'proven_strict_lower_bound':str(value),'claimed_strict_lower_bound':str(target),'method':method}
# Coverage is an exact closed-interval property, not sampling.
for family,selected in [('betas0to6',rows[:1]+[rows[8]]),('beta7',[rows[7],rows[15],rows[16]]),('F3',[rows[17],rows[18]]),('D',rows[-4:])]:
 intervals=sorted((row[2]-row[3],row[2]+row[3]) for row in selected)
 ck(family+'_coverage',intervals[0][0]==0 and intervals[-1][1]==T and all(intervals[i][1]>=intervals[i+1][0] for i in range(len(intervals)-1)))
ck('F5_initial_positive',low(Fs[2].subs(t,0))>Q('.238'))
ck('q2_derivative_convex',S.diff(q2,t,3)==Q('75.559176'))
ck('q2_derivative_left',high(S.diff(q2,t).subs(t,0))<-15)
ck('q2_derivative_right',high(S.diff(q2,t).subs(t,T))<-18)
ck('q2_endpoint',low(q2.subs(t,T))>Q('6.5516')>Q(13,2))
ck('p0_initial_positive',low(p[0].subs(t,0))>Q('.033'))
eq('p6_identity',p[6],-r*t*t*S.Poly(cs[1],s).nth(4)+r*r*t**4*S.Poly(cs[2],s).nth(2))
eq('p7_identity',p[7],r*r*t**4*S.Poly(cs[2],s).nth(3))
eq('b4_identity',S.Poly(cs[1],s).nth(4),-Q(3,2)*phi*r**4*t*t)
eq('d3_identity',S.Poly(cs[2],s).nth(3),Q('.17405')*(Q('6.3')-Q('.9')*X-Q('3.54')*X*X))
eq('d2_identity',S.Poly(cs[2],s).nth(2),q2+154*g*h*(Q('.00077')*t*t+Q('.0677')*t**4-Q('.005')*t**6))
ck('d3_positive_bracket',Q('6.3')-Q('.9')-Q('3.54')>0)
ck('d2_nonnegative_correction',Q('.0677')-Q('.005')*T*T>0)
y=S.symbols('y');eq('sigma_Bernstein_identity',QQ.subs(s,(1+2*y)/3),sum(S.binomial(7,j)*B[j]*y**j*(1-y)**(7-j) for j in range(8)))
# Differential algebra only: weak testing and H2 membership are prose arguments.
lam,nu=S.symbols('lambda nu',positive=True)
eq('harmonic_lift_factor',-lam+S.sqrt(lam)**2)
bb=lam/(4*(nu+1));eq('barrier_factor',bb*((nu+2)**2-nu**2)-lam)
eq('corner_H2_radial_exponent',2*(nu-2)+1,2*nu-3)
eq('corner_H2_integral_denominator',2*nu-3+1,2*(nu-1))
# Bind every displayed budget row back to the exact checked constants.
active=(root/'workspace/ps-pressure-opposite-corner-entire-amplitude-1011.qmd').read_text()
table_rows=[line for line in active.splitlines() if line.startswith('| $') and len(line.split('|'))==10]
ck('active_table_row_count',len(table_rows)==len(rows))
for row,line in zip(rows[17:21]+rows[-4:]+rows[:8]+rows[8:15]+rows[15:17],table_rows):
 name,pol,a,R,L,U,C,k,E,method,target=row
 cells=[v.strip().strip('$') for v in line.split('|')[1:-1]]
 actual=[Q(x) for x in cells[1:5]]
 ck(name+'_active_qmd_constants',actual==[a,R,L,U] and (cells[5]=='—' if C is None else Q(cells[5])==C) and cells[6].startswith('E_'+str(k)+'<') and Q(cells[6].split('<')[1])==E and cells[7]=={'absolute':'(T1)','square':'(T2)','drop':'(T3)'}[method])
ck('beta7_degree',S.degree(B[7],t)==7)
ck('p4_p5_polynomial_divisions',all(S.Poly(p[j],t).nth(i)==0 for j in [4,5] for i in [0,1]))
ck('high_first_half_prose_bound',all(Q(details[f'beta{j}a']['proven_strict_lower_bound'])>Q('.034') for j in range(7)))
ck('beta7_first_prose_bound',Q(details['beta7a']['proven_strict_lower_bound'])>Q('.499'))
ck('beta0_second_prose_bound',Q(details['beta0b']['proven_strict_lower_bound'])>Q('.02005'))
ck('beta7_middle_prose_bound',Q(details['beta7b']['proven_strict_lower_bound'])>Q('.027'))
for j,v in enumerate(['.01085','.01168','.00995','.01323'],1):ck(f'D{j}_prose_bound',Q(details[f'D{j}']['proven_strict_lower_bound'])>Q(v))
eq('D3_displayed_decimal',Q('.019587')-Q('.030679')*Q('.09')-Q('.848580')*Q('.09')**2,Q('.009952392'))
ck('D3_decimal_present_in_proof','= .009952392'.replace(' ','') in active)
eq('beta0_displayed_kappa',Q('.75039')-Q('.135')*Q('3.05701'),Q('.33769365'))

print(json.dumps({'passed':True,'check_count':len(checks),'checks':checks,'original_exact_coefficients_matched':source_count,'original_endpoint_H_bounds_matched':6,'continuous_Taylor_rows':len(rows),'details':details,'scope':'Exact finite polynomial identities, complete Taylor remainder bounds, interval coverage and PDE algebra only. No sampling proof, independent PDE certification, or formal proof is claimed.'},ensure_ascii=False,indent=2))
