"""Independent rational audit. No author code, imports, numerical sampling or CAS.
The trigonometric moments are integrated from their defining Taylor series,
rather than taken from the candidate's moment recurrence.
"""
from fractions import Fraction as F
from math import factorial, comb
from pathlib import Path
import json, hashlib

class R:
    def __init__(self,l=0,h=None):
        if isinstance(l,R): self.l,self.h=l.l,l.h
        else: self.l,self.h=F(l),F(l if h is None else h)
        assert self.l<=self.h
    def __add__(self,x):
        x=R(x); return R(self.l+x.l,self.h+x.h)
    __radd__=__add__
    def __neg__(self): return R(-self.h,-self.l)
    def __sub__(self,x): return self+-R(x)
    def __rsub__(self,x): return R(x)+-self
    def __mul__(self,x):
        x=R(x); u=[a*b for a in [self.l,self.h] for b in [x.l,x.h]]; return R(min(u),max(u))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=R(x); assert x.l>0 or x.h<0
        return self*R(1/x.h,1/x.l)
    def __pow__(self,n):
        assert n>=0
        if n==0:return R(1)
        if self.l>=0:return R(self.l**n,self.h**n)
        if self.h<=0:return (-self)**n*((-1)**n)
        return R(0,max(-self.l,self.h)**n) if n%2==0 else R(self.l**n,self.h**n)
    def cut(self,n=25):
        d=10**n
        return R((self.l*d).__floor__()/F(d),(self.h*d).__ceil__()/F(d))
    def obj(self): return dict(lo=str(self.l),hi=str(self.h),decimal_lo=float(self.l),decimal_hi=float(self.h))

out={'method':'Independent Fraction interval arithmetic and integrated alternating Taylor series; no author code executed','checks':{},'constants':{}}
def claim(name,v,lo,hi):
    v=R(v);lo,hi=F(lo),F(hi)
    ok=lo<=v.l<=v.h<=hi
    out['checks'][name]={'value':v.obj(),'target':[str(lo),str(hi)],'pass':ok}
    assert ok,(name,v.obj(),lo,hi)
    return v

def atanrec(k,N):
    s=sum((F((-1)**j,(2*j+1)*k**(2*j+1)) for j in range(N)),F(0))
    t=F((-1)**N,(2*N+1)*k**(2*N+1));return R(min(s,s+t),max(s,s+t))
pi=(16*atanrec(5,48)-4*atanrec(239,16)).cut(30)
al=pi/5

def trig(x,odd,N=25):
    s=sum(((-1)**j*x**(2*j+odd)/factorial(2*j+odd) for j in range(N)),R())
    rem=x**(2*N+odd)/factorial(2*N+odd)
    return (s+(R(0,rem.h) if N%2==0 else R(-rem.h,0))).cut()
a=(al*trig(al,0)/trig(al,1)).cut()
r=R('0.6180339887498948482045868','0.6180339887498948482045870')
assert r.l*r.l+r.l<1<r.h*r.h+r.h
X=(al**2).cut()
for key,val in [('pi',pi),('alpha',al),('a',a),('r',r),('alpha2',X)]:out['constants'][key]=val.obj()

# Moments are evaluated directly under the integral, using the positive omitted term bound.
def moment(p,odd,N=25):
    terms=[(-1)**j*2**(2*j+odd)*al**(p+2*j+odd)/(factorial(2*j+odd)*(p+2*j+odd+1)) for j in range(N)]
    rem=(2**(2*N+odd)*al**(p+2*N+odd)/(factorial(2*N+odd)*(p+2*N+odd+1))).h
    return (sum(terms,R())+(R(0,rem) if N%2==0 else R(-rem,0))).cut()
C=[moment(2*j,0) for j in range(3)]
S=[moment(2*j+1,1) for j in range(3)]
# Generate Re (a+ib)^n (a^2+b^2)^ell and Im thereof as exact formal monomials in a,b.
def poly(n,ell,imag=False):
    v={}
    for k in range(n+1):
        if (k%2==1)!=imag:continue
        for j in range(ell+1):
            e=(n-k+2*(ell-j),k+2*j)
            v[e]=v.get(e,F())+F(comb(n,k)*comb(ell,j)*((-1)**(k//2)))
    return v

def integral(n,ell,kind,sign=1):
    v=R()
    for (ap,bp),coef in poly(n,ell).items():
        m=al**bp/F(bp+1) if kind=='D' else C[bp//2]
        v+=coef*a**ap*m
    if kind=='H':
        for (ap,bp),coef in poly(n,ell,True).items():v-=sign*coef*a**ap*S[(bp-1)//2]
    return v
D=lambda n,l:integral(n,l,'D')
H=lambda n,l,sgn=1:integral(n,l,'H',sgn)
vals={
'f0':(a*a+X/3)/4,
'e0':(D(1,0)+r*H(1,0))/2,
'e1':(D(1,1)+r*H(1,1))/16,
'p0':H(2,0,-1)/8,
'b0':(r*D(2,0)+H(2,0))/8,
'd0':(r*D(3,0)+H(3,0,-1))/48,
'b1':(r*D(2,1)+H(2,1))/96,
'v0':H(3,0)/48,
'v1':H(3,1)/768}
bounds={'f0':('.21987115','.21987116'),'e0':('.56546697','.56546698'),'e1':('.06049508','.06049510'),'p0':('.10980167','.10980168'),'b0':('.06059592','.06059593'),'d0':('.01947939','.01947940'),'b1':('.00370870','.00370872'),'v0':('-.00324613','-.00324612'),'v1':('-.00027185','-.00027183')}
for name,v in vals.items():claim(name,v,*bounds[name])
# Independently check the IBP recurrence that prints the compact nine constants.
M=(2+r)/(4*a)
claim('C0_matches_M',C[0]-M,'-1e-22','1e-22')
claim('S0_endpoint_formula',S[0]-(M-r/2)/2,'-1e-22','1e-22')
for j in range(1,3):
    claim('C_recurrence_'+str(j),C[j]-(X**j*M-j*S[j-1]),'-1e-22','1e-22')
    claim('S_recurrence_'+str(j),S[j]-(-X**j*r/4+F(2*j+1,2)*C[j]),'-1e-22','1e-22')
Q=F(81,125);T=F(27,50);L=F(107,100);rh=F(619,1000);y=Q*L/2
claim('R_upper',a*a+X,0,L*L)
claim('radial_argument',Q*Q*L*L/4,0,F(121,1000))
claim('angle_derivative',3*a/(L*L)-2,F(1,4),1)
claim('E_density_positive',a-r*al,F(47,100),1)
# Exact positive geometric majorants for all omitted radial orders and aliases.
rad=((1+rh)*L**6/F(3072)+F(6,5)*L**7/F(30720))/(1-Q*Q*L*L/F(60))
aliasE=2*(1+rh)*(L/2)**4/F(24)/(1-y/5)
aliasB=2*(1+rh)*(L/2)**7/F(5040)/(1-y/8)
aliasZ=2*(1+T*(1+rh))*(L/2)**7/F(5040)/(1-y/8)
for name,val,up in [('radial_tail_div_q4',rad,F(1,1000)),('E_alias_div_q4',aliasE,F(3,250)),('B_alias_div_q7',aliasB,F(1,100000)),('Z0_alias_div_q7',aliasZ,F(1,100000))]:claim(name,val,0,up)
claim('P_lower_div_q2',F(3,10)*F(74,100)/8*(1-Q*Q*L*L/12)-T*Q*(1+rh)*L**3/48,F(1,100),1)
claim('B2_lower_div_q2',F('.06059592')-Q*Q*F('.00370872')-Q**4/F(1000),F(58,1000),1)
claim('B2_upper_correction',F('.00370870')-Q*Q/F(1000),F(3,1000),1)
for label,k,s,jcap,zcap,ecap in [('U',F(1),F(5,8),F('.05735'),F('.144'),F('.570')),('C',F(6,5),T,F('.056701'),F('.206'),F('.685'))]:
    j0=vals['b0']+k*vals['v0'];j1=vals['b1']+k*vals['v1']
    claim('j0_'+label,j0,F('.0567'),jcap)
    claim('j1_'+label,j1,F('.0033'),F('.0038'))
    claim('J_lower_'+label,F('.0567')-Q**2*F('.0038')-Q**4/F(1000),F('.0549'),1)
    claim('J_upper_correction_'+label,F('.0033')-Q**2/F(1000),F('.0028'),1)
    g=k*F('.56546697')-k*k*F('.21987116')-k**3*F('.06049510')*T*T-F(3,250)*k**4*T**3-s*(k*k*F('.06059593')+k**3*F('.01947940')*T+k**7*T**5/F(100000))
    e=k*F('.56546698')+F(3,250)*k**4*T**3
    z=k*k*(F('.10980168')+T*jcap)+k**7*T**5/F(100000)
    claim('A_gain_'+label,g,F('.26'),1)
    claim('E_div_t_'+label,e,0,ecap)
    claim('Z0_div_t2_'+label,z,0,zcap)
# Q[eta]/(eta^4+eta^3+eta^2+eta+1): verify the endpoint gluing exactly.
def cyc(p):
    p=list(map(F,p))+[F()]*(5-len(p))
    while len(p)>4:
        k=len(p)-1;x=p.pop()
        for j in range(4):p[k-4+j]-=x
    return tuple(p)
def add(p,q):return cyc([x+y for x,y in zip(p,q)])
def scale(p,s):return cyc([x*s for x in p])
def mul(p,q):
    z=[F()]*7
    for i,x in enumerate(p):
        for j,y in enumerate(q):z[i+j]+=x*y
    return cyc(z)
one=cyc([1]);eta=cyc([0,1]);zero=cyc([0])
poweta=[one]
for i in range(1,6):poweta.append(mul(poweta[-1],eta))
rfield=add(eta,poweta[4])
uplus=add(one,scale(mul(rfield,poweta[4]),-1))
uminus=mul(eta,add(one,scale(mul(rfield,eta),-1)))
dplus=add(rfield,scale(poweta[4],-1))
dminus=mul(poweta[2],add(rfield,scale(eta,-1)))
for name,v in [('cyclotomic_eta5',add(poweta[5],scale(one,-1))),('r_quadratic',add(add(mul(rfield,rfield),rfield),scale(one,-1))),('P_c_endpoint',add(uplus,scale(uminus,-1))),('P_d_endpoint',add(dplus,scale(dminus,-1))),('spin_endpoint',add(eta,scale(mul(poweta[2],poweta[4]),-1)))]:
    assert v==zero,(name,v);out['checks'][name]={'exact_coefficients':[str(x) for x in v],'pass':True}
# Formal symbols: A=a, X=alpha^2, r, C_j, S_j. Reconstruct all nine
# displayed formulas from the binomial integrands, and compare coefficientwise.
def sadd(*ps):
    ans={}
    for p in ps:
        for e,v in p.items():ans[e]=ans.get(e,F())+v
    return {e:v for e,v in ans.items() if v}
def ss(p,k=1,rshift=0):return {(ae,xe,re+rshift,kind,j):v*F(k) for (ae,xe,re,kind,j),v in p.items() if v*k}
def mon(ae=0,xe=0,re=0,kind='1',j=0,coef=1):return {(ae,xe,re,kind,j):F(coef)}
def ds(n,l):
    return sadd(*[mon(ae,bp//2,coef=coef/F(bp+1)) for (ae,bp),coef in poly(n,l).items()])
def hs(n,l,sgn=1):
    return sadd(*[mon(ae,kind='C',j=bp//2,coef=coef) for (ae,bp),coef in poly(n,l).items()],
                *[mon(ae,kind='S',j=(bp-1)//2,coef=-sgn*coef) for (ae,bp),coef in poly(n,l,True).items()])
built={
'f0':ss(sadd(mon(2),mon(xe=1,coef=F(1,3))),F(1,4)),
'e0':ss(sadd(ds(1,0),ss(hs(1,0),rshift=1)),F(1,2)),
'e1':ss(sadd(ds(1,1),ss(hs(1,1),rshift=1)),F(1,16)),
'p0':ss(hs(2,0,-1),F(1,8)),
'b0':ss(sadd(ss(ds(2,0),rshift=1),hs(2,0)),F(1,8)),
'd0':ss(sadd(ss(ds(3,0),rshift=1),hs(3,0,-1)),F(1,48)),
'b1':ss(sadd(ss(ds(2,1),rshift=1),hs(2,1)),F(1,96)),
'v0':ss(hs(3,0),F(1,48)),
'v1':ss(hs(3,1),F(1,768))}
# Each line is the printed numerator in candidate (8), with denominator separate.
printed={
'f0':(4,[mon(2),mon(xe=1,coef=F(1,3))]),
'e0':(2,[mon(1),mon(1,re=1,kind='C'),mon(re=1,kind='S',coef=-1)]),
'e1':(16,[mon(3),mon(1,1,coef=F(1,3)),mon(3,re=1,kind='C'),mon(1,re=1,kind='C',j=1),mon(2,re=1,kind='S',coef=-1),mon(re=1,kind='S',j=1,coef=-1)]),
'p0':(8,[mon(2,kind='C'),mon(kind='C',j=1,coef=-1),mon(1,kind='S',coef=2)]),
'b0':(8,[mon(2,re=1),mon(xe=1,re=1,coef=F(-1,3)),mon(2,kind='C'),mon(kind='C',j=1,coef=-1),mon(1,kind='S',coef=-2)]),
'd0':(48,[mon(3,re=1),mon(1,1,1,coef=-1),mon(3,kind='C'),mon(1,kind='C',j=1,coef=-3),mon(2,kind='S',coef=3),mon(kind='S',j=1,coef=-1)]),
'b1':(96,[mon(4,re=1),mon(xe=2,re=1,coef=F(-1,5)),mon(4,kind='C'),mon(kind='C',j=2,coef=-1),mon(3,kind='S',coef=-2),mon(1,kind='S',j=1,coef=-2)]),
'v0':(48,[mon(3,kind='C'),mon(1,kind='C',j=1,coef=-3),mon(2,kind='S',coef=-3),mon(kind='S',j=1)]),
'v1':(768,[mon(5,kind='C'),mon(3,kind='C',j=1,coef=-2),mon(1,kind='C',j=2,coef=-3),mon(4,kind='S',coef=-3),mon(2,kind='S',j=1,coef=-2),mon(kind='S',j=2)])}
for name,(den,ps) in printed.items():
    diff=sadd(built[name],ss(sadd(*ps),-F(1,den)))
    assert not diff,(name,diff)
    out['checks']['symbolic_formula_'+name]={'difference_monomials':len(diff),'pass':True}
u=F(1,5);u=2*u/(1-u*u);u=2*u/(1-u*u)
assert (u-F(1,239))/(1+u/F(239))==1
out['checks']['Machin_tangent_identity']={'exact_value':'1','pass':True}
out['all_pass']=all(x['pass'] for x in out['checks'].values())
print(json.dumps(out,indent=2,ensure_ascii=False,sort_keys=True))
