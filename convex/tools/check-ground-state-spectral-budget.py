"""Exact finite checks for round 6; this does not verify infinite-dimensional arguments."""
from pathlib import Path
import sympy as S
import json
Q=S.Rational
s,a,R,x,y=S.symbols('s a R x y',positive=True)
checks={}
def ck(name,value):
 assert bool(value),name
 checks[name]=True
def eq(name,left,right=0):ck(name,S.simplify(S.expand(left-right))==0)
pp=sum((-a*s)**k/S.factorial(k)**2 for k in range(6));aa=Q(289,200);cc=Q(289,50)
for k in range(5):eq(f'polynomial_recurrence_{k}',4*(k+1)**2*(-a)**(k+1)/S.factorial(k+1)**2+4*a*(-a)**k/S.factorial(k)**2)
eq('polynomial_radial_residual',-4*(s*S.diff(pp,s,2)+S.diff(pp,s))-4*a*pp,a**6*s**5/3600)
eq('polynomial_endpoint',pp.subs({s:1,a:aa}),Q(502163101517,1536000000000000))
ck('polynomial_endpoint_positive',pp.subs({s:1,a:aa})>0)
U=-a+a*a/2+a**4/144
eq('derivative_upper_difference',U-S.diff(pp,s),a*a*(1-s)/2+a**3*s*s/12+a**4*(1-s**3)/144+a**5*s**4/2880)
eq('derivative_upper_exact',U.subs(a,aa),-Q(85411762559,230400000000))
ck('derivative_upper_negative',U.subs(a,aa)<0)
phi=pp.subs(s,(x*x+y*y)/(R*R))
eq('cartesian_residual',-S.diff(phi,x,2)-S.diff(phi,y,2)-4*a*phi/R**2,a**6*(x*x+y*y)**5/(3600*R**12))
eq('residual_coefficient',aa**6/3600,Q(582622237229761,230400000000000000))
f,F,fx,fy,Fx,Fy=S.symbols('f phi fx fy phix phiy',real=True,nonzero=True)
eq('weighted_square_identity',fx*fx+fy*fy-F*F*((fx/F-f*Fx/F**2)**2+(fy/F-f*Fy/F**2)**2),2*f*(fx*Fx+fy*Fy)/F-f*f*(Fx*Fx+Fy*Fy)/F**2)
eq('constant_c',4*aa,cc)
ck('explicit_threshold_improved',cc>Q(144,25))
eq('q_squared_upper',1/cc,Q(50,289))
eq('q_upper_square',(5*S.sqrt(2)/17)**2,Q(50,289))
eq('q_squared_margin',Q(25,144)-Q(50,289),Q(25,41616))
ck('q_strict_comparison',Q(50,289)<Q(25,144))
# Bind the old six-term endpoint identity, while the new argument uses no Bessel facts.
eq('old_six_term_endpoint',sum((-Q(36,25))**k/S.factorial(k)**2 for k in range(6)),Q(608149,244140625))
# Exact differential/algebraic steps of the heat-product and level-set proofs.
h,rho=S.symbols('h rho',positive=True)
mult=(1-S.exp(-h*rho))/h
eq('form_multiplier_derivative',S.diff(mult,rho),S.exp(-h*rho))
eq('form_multiplier_at_zero',mult.subs(rho,0))
eq('form_multiplier_limit',S.limit(mult,h,0),rho)
eq('form_multiplier_h_sign_numerator',h*h*S.diff(mult,h),S.exp(-h*rho)*(h*rho+1)-1)
eq('log_remainder_derivative',S.diff(-S.log(1-s)-s,s),s/(1-s))
eq('log_remainder_upper_derivative',S.diff(s*s+S.log(1-s)+s,s),s*(1-2*s)/(1-s))
eq('product_bound_maximum_derivative',S.diff(s*s*S.exp(-s),s),s*(2-s)*S.exp(-s))
eq('product_bound_tail_derivative',S.diff(s*S.exp(-s),s),(1-s)*S.exp(-s))
th=S.symbols('theta',real=True)
u1,u2,v1,v2=S.symbols('u1 u2 v1 v2',real=True)
eq('gaussian_convexity_identity',(1-th)*(u1*u1+u2*u2)+th*(v1*v1+v2*v2)-((1-th)*u1+th*v1)**2-((1-th)*u2+th*v2)**2,th*(1-th)*((u1-v1)**2+(u2-v2)**2))
GG,rad,area,per=S.symbols('G radius area perimeter',positive=True)
eq('radial_energy_layer_change',2*S.pi*rad*(2*S.pi*rad/GG)**2*(GG/(2*S.pi*rad)),4*S.pi*(S.pi*rad*rad)/GG)
eq('layer_cake_mass',S.integrate(2*s,(s,0,rho)),rho*rho)
eq('isoperimetric_constant_squared',(Q(1,2))**2*(per**3/(4*S.pi**2))*per,(per*per/(4*S.pi))**2)
eq('area_scaling',cc/(area/S.pi),cc*S.pi/area)
# These bindings guard transcription; they are not proof checks for the analytic limits.
root=Path(__file__).resolve().parent.parent
source=(root/'workspace/analytic-replacements-1012/area-spectral-budget.qmd').read_text()
foundation=(root/'workspace/ps-convex-geometric-tensor-switch-1011g/pressure-foundations.qmd').read_text()
ck('endpoint_value_in_qmd',r'\frac{502163101517}{1536000000000000}' in source)
ck('derivative_bound_in_qmd',r'\frac{85411762559}{230400000000}' in source)
ck('residual_formula_in_qmd',r'\frac{a^6s^5}{3600R^2}' in source)
ck('q_new_bound_in_statement',r'0<q:=I/J_R<\frac{5\sqrt2}{17}<\frac5{12}.' in foundation)
ck('q_new_proof_dependency','@lem-arc-levelset-spectral-budget-1012' in foundation)
ck('log_concavity_new_dependency','@lem-arc-ground-state-log-concavity-1012' in foundation)
ck('old_zero_not_used_in_foundation','j_{0,1}' not in foundation and 'J_0(' not in foundation and 'J_1(' not in foundation)
print(json.dumps({'passed':True,'check_count':len(checks),'checks':checks,'constants':{'c':'289/50','polynomial_parameter':'289/200','endpoint_exact':str(pp.subs({s:1,a:aa})),'derivative_upper_exact':str(U.subs(a,aa)),'q_new_upper':'5*sqrt(2)/17','q_squared_margin_over_old':'25/41616'},'scope':'Finite exact algebra and transcription bindings only. L2 limits, spectral theory, integral inequalities, Sobolev and PDE arguments are justified in QMD prose, not certified by these checks.'},ensure_ascii=False,indent=2))
