"""Checks the preserved fine means after changing their coefficient source.
The phase-square inequality itself remains an analytic argument in the QMD.
"""
import sympy as S
from fractions import Fraction as F
import json,runpy,contextlib,io
from pathlib import Path
here=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):env=runpy.run_path(str(here/'check-moment-packets.py'))
expected=env['expected'];t,s,g,cp,cm=S.symbols('t s gamma Cp Cm');checks={}
def check(n,c):
 assert c,n
 checks[n]=True
D=S.Integer(10)**8
for label,data in expected.items():
 lo={k:[S.Rational(v,D) for v in a] for k,a in data.items()};hi={k:[S.Rational(v+1,D) for v in a] for k,a in data.items()}
 # Uniform analytic sign bounds for 0<=zeta<=3/10.
 for name in ['Ao','F']:check(label+'_'+name+'_negative',hi[name][0]+hi[name][1]*S.Rational(3,10)<0)
 for name in ['J','P','M','Q']:check(label+'_'+name+'_positive',lo[name][0]+lo[name][1]*S.Rational(3,10)>0)
 for name in ['jplus','jminus']:check(label+'_'+name+'_positive',lo[name][0]>0)
 check(label+'_G_error',S.Rational(1,D)*(1+S.Rational(3,10)+S.Rational(9,100))<S.Rational(2,D))
 pure=[lo['Ae'][0],0,lo['Ae'][1],lo['Ao'][0],lo['Ae'][2],lo['Ao'][1]]
 base=sum(v*t**j for j,v in enumerate(pure))
 ee=S.Rational(2,D)+hi['Q'][0]*t+hi['Q'][1]*t**3
 P=sum(v*t**(2*j) for j,v in enumerate(hi['P']))
 M=sum(v*t**(2*j) for j,v in enumerate(hi['M']))
 # Full adverse spin envelope preserves the favorable coefficient signs.
 zp=P+t*(hi['J'][0]+hi['J'][1]*t*t+(hi['J'][2]+hi['jminus'][0])*t**4)+g**7*cp*t**6
 zm=M+t**3*(-lo['F'][0]+(-lo['F'][1]+hi['jplus'][0])*t*t)+g**7*cm*t**6
 targets={
 'U':[
 '.34559582-.04819280*t**2-.00081178*t**3+.00188004*t**4+.00003797*t**5',
 '.00000002+.01947940*t-.00105669*t**3',
 '.10980168+.05734980*t-.02767112*t**2-.00343686*t**3+.00129011*t**4+.00007469*t**5+gamma**7*Cp*t**6',
 '.56546698-.06049508*t**2+.00081178*t**3+.00219163*t**4-.00001753*t**5+gamma**7*Cm*t**6'],
 'C':[
 '.36194590-.07902548*t**2-.00168330*t**3+.00452310*t**4+.00011338*t**5',
 '.00000002+.03366040*t-.00262939*t**3',
 '.15811441+.08164883*t-.05064676*t**2-.00701394*t**3+.00332636*t**4+.00021835*t**5+gamma**7*Cp*t**6',
 '.67856037-.10453551*t**2+.00168330*t**3+.00545347*t**4-.00005238*t**5+gamma**7*Cm*t**6']}
 for name,v,src in zip(['base','mixed_scalar','spin_pure','spin_mixed'],[base,ee,zp,zm],targets[label]):
  target=S.sympify(src,locals={'t':t,'gamma':g,'Cp':cp,'Cm':cm},rational=True)
  check(label+'_'+name+'_exact_envelope',S.expand(v-target)==0)
 check(label+'_pure_spin_remainder_positive',hi['J'][0]+hi['J'][1]*S.Rational(3,10)>0)
 check(label+'_mixed_spin_remainder_positive',-lo['F'][0]+(-lo['F'][1]+hi['jplus'][0])*S.Rational(3,10)>0)
# The phase credit has exactly this amplitude, with no loss of a factor t or s.
P,M,u=S.symbols('P M u',real=True)
L=t*t*P+t*s*M
sq=t**4*P**2+t*t*s*s*M**2-2*t**3*s*P*M*u
check('exact_phase_square_amplitude',S.expand(L**2-sq-2*P*M*t**3*s*(1+u))==0)
print(json.dumps({'all_pass':True,'count':len(checks),'scope':'Fine-mean sign conditions, exact unchanged adverse envelopes, and phase-square amplitude; continuous triangle/square proof is in QMD.','checks':checks},indent=2))
