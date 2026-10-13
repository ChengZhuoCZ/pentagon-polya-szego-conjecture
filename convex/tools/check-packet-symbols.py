"""Exact comparison of original weighted kernel Taylor coefficients and moment packets."""
import sympy as S
from math import comb,factorial
from collections import defaultdict
import json
A,R,K=S.symbols('a r k'); I=S.I
X=A*A*(3-4*R)
def norm(x):
 n,d=S.fraction(S.cancel(x));return S.cancel(S.rem(n,R*R+R-1,R)/d)
C=[(2+R)/(4*A)];SS=[(C[0]-R/2)/2]
for j in range(1,4):
 C.append(norm(X**j*C[0]-j*SS[j-1]));SS.append(norm(-X**j*R/4+S.Rational(2*j+1,2)*C[j]))
def integ(p,q,shift):
 out=0
 for j in range(p+1):
  for h in range(q+1):
   b=j+h;v=comb(p,j)*comb(q,h)*(-1)**(q-h)*I**b*A**(p+q-b)
   if shift==0:m=0 if b%2 else X**(b//2)/S.Integer(b+1)
   else:m=C[b//2] if b%2==0 else shift*I*SS[(b-1)//2]
   out+=v*m
 return norm(out)
# Terms in (1+k(cn+cbar/n)/2)*(1+cn+rdn^2-(rcn+dn^2)e^-2ib).
base=[((0,0,0,0),0,S.Integer(1)),((1,0,0,0),0,S.Integer(1)),((0,0,1,0),0,R),((1,0,0,0),-1,-R),((0,0,1,0),-1,S.Integer(-1))]
weights=[((0,0,0,0),S.Integer(1)),((1,0,0,0),K/2),((0,1,0,0),K/2)]
raw=[]
for spin in (0,1):
 d=defaultdict(lambda:0)
 for v,sh,cf in base:
  for w,wcf in weights:
   v0=tuple(vv+ww for vv,ww in zip(v,w));maxn=7-sum(v0)
   for n in range(maxn+1):
    for p in range(n+1):
     q=n-p;vv=(v0[0]+p,v0[1]+q,v0[2],0)
     root=vv[0]-vv[1]+2*vv[2]+2*spin
     if root%5:continue
     rootcf=(-1)**(root//5) if root//5>=0 else S.Integer(-1)**(root//5)
     term=cf*wcf*rootcf*(K/2)**n*(1 if spin else (-1)**n)/S.Integer(factorial(p)*factorial(q))*integ(p,q,sh+spin)
     d[vv]+=term
 if not spin:
  e=defaultdict(lambda:0)
  for v,cf in d.items():
   e[v]+=cf/2;e[(v[1],v[0],v[3],v[2])]+=cf/2
  d=e
 raw.append({v:norm(cf) for v,cf in d.items() if cf!=0})
def mom(k,l,shift):
 n=abs(k);sgn=1 if k>=0 else -1;out=0
 for h in range(n+1):
  for j in range(l+1):
   b=h+2*j;cf=comb(n,h)*comb(l,j)*I**h*sgn**h*A**(n-h+2*(l-j))
   if shift:m=C[b//2] if b%2==0 else I*SS[(b-1)//2]
   else:m=0 if b%2 else X**(b//2)/S.Integer(b+1)
   out+=cf*m
 return norm(out)
def mode(k,l):
 cf=S.Rational((-1)**(l+(abs(k) if k<0 else 0)),2**(abs(k)+2*l)*factorial(l)*factorial(abs(k)+l));d=mom(k,l,0);h=mom(k,l,1)
 return tuple(norm(v) for v in (cf*h,cf*(R*d+h),cf*(d+R*h)))
Ae=[(-1)**j*K**(2*j)*mom(0,j,0)/S.Integer(4**j*factorial(j)**2)+K**(2*j-1)*mode(1,j-1)[2] for j in range(1,4)]
G=[K**(2+2*l)*mode(2,l)[1] for l in range(3)]
Q=[-K**(3+2*l)*mode(-3,l)[1] for l in range(2)]
P=[K**(2+2*l)*mode(-2,l)[0]+(K**(2*l+1)*mode(-3,l-1)[1] if l else 0) for l in range(3)]
J=[K**(3+2*l)*mode(3,l)[0]+K**(2+2*l)*mode(2,l)[1] for l in range(3)]
M=[K**(1+2*l)*mode(1,l)[2] for l in range(3)]
F=[-K**(4+2*l)*mode(-4,l)[2] for l in range(2)]
jminus=K**7*mode(-7,0)[0];jplus=-K**6*mode(6,0)[2];Ao=[F[0],F[1]+jplus]
expected=[defaultdict(lambda:0),defaultdict(lambda:0)];expected[0][(0,0,0,0)]=1
for l,cf in enumerate(Ae):expected[0][(l+1,l+1,0,0)]+=cf
for l,cf in enumerate(Ao):
 expected[0][(l+5,l,0,0)]+=cf/2;expected[0][(l,l+5,0,0)]+=cf/2
for l,cf in enumerate(G):
 expected[0][(l,l+2,1,0)]+=cf/2;expected[0][(l+2,l,0,1)]+=cf/2
for l,cf in enumerate(Q):
 expected[0][(l+3,l,1,0)]+=cf/2;expected[0][(l,l+3,0,1)]+=cf/2
for l,cf in enumerate(P):expected[1][(l,l+2,0,0)]-=cf
for l,cf in enumerate(J):expected[1][(l+3,l,0,0)]+=cf
for l,cf in enumerate(M):expected[1][(l+1,l,1,0)]+=cf
for l,cf in enumerate(F):expected[1][(l,l+4,1,0)]+=cf
expected[1][(0,7,0,0)]+=jminus;expected[1][(6,0,1,0)]+=jplus
checks={}
for spin in (0,1):
 for v in sorted(set(raw[spin])|set(expected[spin])):
  delta=norm(raw[spin].get(v,0)-expected[spin].get(v,0))
  assert delta==0,(spin,v,delta)
  checks[('Z' if spin else 'A')+'_'+str(v)]=True
print(json.dumps({'all_pass':True,'count':len(checks),'scope':'Exact polynomial identities for symbolic real k; original full weighted kernel degree <=7 vs eight-moment packet formulas, including all zero modes and both phase signs. Uses only r^2+r=1 and alpha^2=a^2(3-4r).','checks':checks},indent=2))
