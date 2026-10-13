"""Generate BOTH source packets from eight exact angular moments.
All assertions use rational intervals; no sinc coefficient table is evaluated.
"""
from pathlib import Path
import runpy,io,contextlib,json
from fractions import Fraction as F
from math import factorial,comb
p=Path(__file__).resolve().parent/'check-nine-constants.py'
if not p.exists():p=Path(__file__).resolve().parent/'凸五边形-双核与均值解析替换-20261012/tools/check-nine-constants.py'
with contextlib.redirect_stdout(io.StringIO()):env=runpy.run_path(str(p))
R=env['R'];a=env['a'];r=env['r'];X=env['X'];al=env['al']
# Use only the explicitly stated coarse geometric intervals in the QMD.
a=R('.8648062659772','.8648062659773')
r=R('.6180339887498','.6180339887499')
X=R('.3947841760435','.3947841760436')
C=[(2+r)/(4*a)];SS=[(C[0]-r/2)/2]
for j in range(1,4):
 C.append(X**j*C[0]-j*SS[j-1])
 SS.append(-X**j*r/4+F(2*j+1,2)*C[j])
def poly(k,l,imag=False):
 n=abs(k);sgn=1 if k>=0 else -1;out={}
 for h in range(n+1):
  if (h%2==1)!=imag:continue
  for j in range(l+1):
   key=(n-h+2*(l-j),h+2*j)
   out[key]=out.get(key,F())+F(comb(n,h)*comb(l,j)*(-1)**(h//2)*sgn**h)
 return out
def moment(k,l,shift=False):
 ans=R()
 for (ap,bp),cf in poly(k,l).items():
  v=C[bp//2] if shift else X**(bp//2)/F(bp+1)
  ans+=cf*a**ap*v
 if shift:
  for (ap,bp),cf in poly(k,l,True).items():ans-=cf*a**ap*SS[(bp-1)//2]
 return ans
def mode(k,l):
 cf=F((-1)**(l+(abs(k) if k<0 else 0)),2**(abs(k)+2*l)*factorial(l)*factorial(abs(k)+l))
 d=moment(k,l);h=moment(k,l,True)
 return cf*h,cf*(r*d+h),cf*(d+r*h)
def coeff(k):
 values={}
 values['Ae']=[(-1)**j*k**(2*j)*moment(0,j)/F(4**j*factorial(j)**2)+k**(2*j-1)*mode(1,j-1)[2] for j in range(1,4)]
 values['G']=[k**(2+2*l)*mode(2,l)[1] for l in range(3)]
 values['Q']=[-k**(3+2*l)*mode(-3,l)[1] for l in range(2)]
 values['P']=[k**(2+2*l)*mode(-2,l)[0]+(k**(2*l+1)*mode(-3,l-1)[1] if l else 0) for l in range(3)]
 values['J']=[k**(3+2*l)*mode(3,l)[0]+k**(2+2*l)*mode(2,l)[1] for l in range(3)]
 values['jminus']=[k**7*mode(-7,0)[0]]
 values['M']=[k**(1+2*l)*mode(1,l)[2] for l in range(3)]
 values['F']=[-k**(4+2*l)*mode(-4,l)[2] for l in range(2)]
 values['jplus']=[-k**6*mode(6,0)[2]]
 values['Ao']=[values['F'][0],values['F'][1]+values['jplus'][0]]
 return values
expected={
 'U':{'Ae':[34559582,-4819280,188004],'Ao':[-81178,3797],'G':[6059592,-370871,8245],'Q':[1947939,-105670],'P':[10980167,-2767113,129010],'J':[5734979,-343687,7422],'jminus':[45],'M':[56546697,-6049509,219162],'F':[-81178,2775],'jplus':[1021]},
 'C':{'Ae':[36194590,-7902548,452310],'Ao':[-168330,11338],'G':[8725812,-769038,24621],'Q':[3366039,-262940],'P':[15811440,-5064677,332635],'J':[8164882,-701395,21670],'jminus':[163],'M':[67856036,-10453552,545346],'F':[-168330,8288],'jplus':[3049]}}
checks={};rows=[]
for label,k in [('U',F(1)),('C',F(6,5))]:
 vals=coeff(k)
 for name,ints in expected[label].items():
  for j,n in enumerate(ints):
   v=vals[name][j]
   assert F(n,10**8)<v.l<=v.h<F(n+1,10**8),(label,name,j,v.obj())
   checks[f'{label}_{name}_{j}']=True
   rows.append({'source':label,'coefficient':name,'degree':j,'integer_lower':n,'interval':v.obj()})
# Real integral moments also agree with directly integrated Taylor series.
for j in range(4):
 for name,recur,power,odd in [('C',C[j],2*j,0),('S',SS[j],2*j+1,1)]:
  exact=env['moment'](power,odd)
  assert max(recur.l,exact.l)<min(recur.h,exact.h)
  checks[f'angular_moment_{name}{j}']=True
# Same original weighted Taylor remainder, uniform for both 1<=k<=6/5.
g=F(3,4);cp=F(51543,917504);cm=F(22815,458752)
f=lambda n:F(3,2)**n/F(factorial(n))
assert f(8)+F(71,24)*f(7)+F(13,6)*f(6)==F(4,5)*cp
assert F(13,8)*(f(7)+F(4,3)*f(6))==F(4,5)*cm
checks['full_Taylor_pure_constant']=True;checks['full_Taylor_mixed_constant']=True
print(json.dumps({'all_pass':True,'count':len(checks),'scope':'46 packet intervals from 8 angular moments, direct moment crosschecks, and uniform complete Taylor tail constants','checks':checks,'rows':rows},indent=2))
