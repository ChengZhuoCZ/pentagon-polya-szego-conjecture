from fractions import Fraction as F
import json

# Exact rational-function algebra used only to check displayed identities.
def trim(a):
 a=list(map(F,a))
 while len(a)>1 and a[-1]==0:a.pop()
 return tuple(a)
def add(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def neg(a):return tuple(-x for x in a)
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def divmodp(a,b):
 a=list(trim(a));b=trim(b);q=[F(0)]*max(1,len(a)-len(b)+1)
 while not(len(a)==1 and a[0]==0) and len(a)>=len(b):
  d=len(a)-len(b);c=a[-1]/b[-1];q[d]+=c
  for j,x in enumerate(b):a[d+j]-=c*x
  a=list(trim(a))
 return trim(q),trim(a)
def gcdp(a,b):
 while b!=(F(0),):a,b=b,divmodp(a,b)[1]
 return tuple(x/a[-1] for x in a)
def der(a):return trim([i*a[i] for i in range(1,len(a))] or [0])
def val(a,x):
 s=F(0)
 for c in reversed(a):s=s*x+c
 return s
class R:
 def __init__(self,n=0,d=(1,)):
  if isinstance(n,R):self.n,self.d=n.n,n.d;return
  n=trim((n,) if isinstance(n,(int,F)) else n);d=trim(d)
  assert d!=(F(0),)
  c=gcdp(n,d);n=divmodp(n,c)[0];d=divmodp(d,c)[0];c=d[-1]
  self.n=tuple(x/c for x in n);self.d=tuple(x/c for x in d)
 def __add__(self,o):
  o=R(o);return R(add(mul(self.n,o.d),mul(o.n,self.d)),mul(self.d,o.d))
 __radd__=__add__
 def __neg__(self):return R(neg(self.n),self.d)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):
  o=R(o);return R(mul(self.n,o.n),mul(self.d,o.d))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=R(o);return R(mul(self.n,o.d),mul(self.d,o.n))
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,k):
  if k<0:return (1/self)**(-k)
  ans=R(1);p=self
  while k:
   if k%2:ans=ans*p
   p=p*p;k//=2
  return ans
 def diff(self):return R(add(mul(der(self.n),self.d),neg(mul(self.n,der(self.d)))),mul(self.d,self.d))
 def at(self,x):return val(self.n,F(x))/val(self.d,F(x))
 def zero(self):return self.n==(F(0),)

