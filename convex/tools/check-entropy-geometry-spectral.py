"""Exact identities and rational payments for the third analytic replacement.
Requires SymPy. It checks finite formulae, not PDE existence or the root theorem.
"""
import sympy as S
import json
from math import comb
checks={}
def ck(n,v):
 assert bool(v),n
 checks[n]=True
def eq(n,x,y=0):ck(n,S.cancel(S.expand(x-y))==0)
def Q(x):return S.Rational(str(x))
# Universal reciprocal identity and optimal square.
H,h,b,U1,U2,V,m,h0,B0=S.symbols('H h b U1 U2 V m h0 B0',positive=True)
eq('reciprocal_exact_defect',(1-2*(H-h)/b+H*(H-h)/b**2)/h-1/H,(H-h)*(H-b)**2/(h*b*b*H))
eq('optimal_scale_square',(V-2*U1/b+U2/b**2)/h-(V-U1**2/U2)/h,(U2-b*U1)**2/(h*b*b*U2))
S0,V2,V3,F4=S.symbols('S0 V2 V3 F4')
poly=S.Poly(S.expand((1-2*(H-h)/b+H*(H-h)/b**2)/h).subs({H:m+S0,h:m*h0,b:B0*m}),S0)
coef=[(1+(1-h0)*(1-2*B0)/B0**2)/(m*h0),(2-h0-2*B0)/(B0**2*m*m*h0),1/(B0**2*m**3*h0)]
for i,v in enumerate(coef):eq('signed_reciprocal_coefficient_'+str(i),poly.nth(i),v)
u1=m*(1-h0)*V2+V3;u2=m*m*(1-h0)*V2+m*(2-h0)*V3+F4
eq('adaptive_credit_numerator',u2-Q('1.5')*m*u1,F4+m*(Q('.5')-h0)*V3-m*m*(1-h0)*V2/2)
x,y=S.symbols('x y',positive=True)
eq('hellinger_rationalization',(x-y)**2*(x+y)**2,(x*x-y*y)**2)
eq('hellinger_discriminant',(x+y)**2-(x-y)**2,4*x*y)
ck('central_ratio_eta_left',(1-Q('9/23'))/(1+Q('9/23'))==Q('7/16'))
ck('central_ratio_eta_right',Q('1/3')<Q('7/16'))
eq('central_sqrt_square_margin',1-Q('7/16')**2-Q('.899')**2,Q('1571/4000000'))
eq('central_entropy_multiplier',1/(4*(1+Q('.899'))),Q('250/1899'))
ck('unit_ratio_eta',(1-Q('7/20'))/(1+Q('7/20'))==Q('13/27'))
ck('unit_sqrt_square_margin',1-Q('13/27')**2>Q('49/64'))
eq('unit_entropy_multiplier',1/(4*(1+Q('7/8'))),Q('2/15'))
eq('central_sqrt_m_factor',9*m-(m+2)**2,(m-1)*(4-m))
ck('adaptive_whole_multiplier_relaxation',Q('250/633')<Q('21/50'))
# Independent root filtering of the precise entropy moments.
c,cb,d,db,r,de,p,n=S.symbols('c cb d db r delta p n')
xx=(c*n+cb/n)/2;zz=(d*n*n+db/n**2)/2
U=(c*c*db+cb*cb*d)/2;VV=(c*d*d+cb*db*db)/2;QQ=(c**3*d+cb**3*db)/2;WW=(cb*d**3+c*db**3)/2
root=lambda ex: S.expand(sum((term/n**int(term.as_powers_dict().get(n,0))*S.Integer(-1)**(int(term.as_powers_dict().get(n,0))//5) for term in S.expand(ex).as_ordered_terms() if int(term.as_powers_dict().get(n,0))%5==0),S.Integer(0)))
DD=de*xx+2*r*zz;SS=p*xx+r*zz
v2=de**2*c*cb/2+2*r*r*d*db
v3=r*de*(de+4*p)/4*U-r*r*(de+p)*VV
f4=3*de**2*p*p*(c*cb)**2/8-de*r*p*QQ+r*r*(de**2+8*de*p+4*p*p)*c*cb*d*db/4-2*r**3*WW+3*r**4*(d*db)**2/2
eq('five_root_second_moment',root(DD**2),v2)
eq('five_root_third_moment',root(DD**2*SS),v3)
eq('five_root_fourth_moment',root(DD**2*SS**2).subs(de,4-2*p),f4.subs(de,4-2*p))
# Uniform source sharper full entropy budget.
ck('uniform_sqrt_mass',Q('14/15')**2<Q('7/8'))
ck('uniform_sqrt_node_floor',Q('16/25')**2<Q('41/100'))
eq('uniform_denominator_lower',Q('7/8')*Q('14/15')*(1+Q('16/25'))**2,Q('82369/37500'))
eq('uniform_denominator_payment',Q('82369/37500')*Q('57/125'),Q('1565011/1562500'))
ck('uniform_entropy_constant',Q('1565011/1562500')>1)
ck('uniform_r_lower',Q('559/250')**2<5)
v=Q('21/8')*Q('309/500')-Q('57/25')*(Q('1/4')+Q('191/500'))
eq('uniform_delta_lower',v,Q('18129/100000'))
ck('uniform_delta_payment',v>Q('9/50'))
eq('uniform_epsilon_payment',Q('9/50')/12,Q('3/200'))
D,L,q=S.symbols('D L q');eq('deficit_bridge_identity',(1-q)*D-q*L,(7*D-5*L)/12+(Q('5/12')-q)*(D+L))
# Exact geometry amplitude endpoint reductions, now without root counting.
u,y=S.symbols('u y');F=2*u-Q('9/25')*(1+r*(u-r*r*y*y))**2-Q('3/5')*r*r*y*(1+r*(u-r*r*y*y))
def reduce_r(ex):
 num,den=S.fraction(S.cancel(ex));return S.cancel(S.rem(num,r*r+r-1,r)/den)
polys=[(30092031-28022031*r)/S.Integer(156250000)+(3126*r-5313)/S.Integer(12500)*y+(25317*r-9378)/S.Integer(31250)*y*y+(3*r-Q('9/5'))*y**3+(72*r-45)/25*y**4,
 (32-9*r)/25-3*r/5*y+18*(1-r)/25*y*y+(3*r-Q('9/5'))*y**3+(72*r-45)/25*y**4]
rL=Q('.61803');rU=Q('.61804');R0=-26137500000*y**4+70429687500*y**3+261194396250*y**2-352191481250*y+106444124673;R1=-50184*y**4+135225*y**3+687528*y**2-927060*y+2643764
for i,u0 in enumerate([Q('729/2500'),Q(1)]):
 eq('geometry_endpoint_identity_'+str(i),reduce_r(F.subs(u,u0)),polys[i])
 lower=0
 for j in range(5):
  cj=S.Poly(polys[i],y).nth(j);dr=S.diff(cj,r);ck(f'geometry_affine_r_coefficient_{i}_{j}',not dr.has(r))
  lower+=cj.subs(r,rL if dr>=0 else rU)*y**j
 eq('geometry_endpoint_lower_'+str(i),lower,3*R0/S.Integer(3906250000000) if i==0 else R1/S.Integer(2500000))
ck('geometry_r_isolation',rL*rL+rL-1<0<rU*rU+rU-1)
eq('R0_second_derivative',S.diff(R0,y,2),522388792500+y*(422578125000-313650000000*y))
ck('R0_curvature_nonnegative_tail',422578125000-313650000000>0)
ck('R0_curvature_lower',522388792500>500000000000)
eq('R0_center_value',R0.subs(y,Q('3/5')),984611073)
eq('R0_center_derivative',S.diff(R0,y).subs(y,Q('3/5')),14723056750)
ck('R0_center_value_lower',984611073>980000000)
ck('R0_center_derivative_upper',0<14723056750<15000000000)
z=S.symbols('z');eq('R0_completed_square',980000000-15000000000*z+250000000000*z*z,250000000000*(z-Q('3/100'))**2+755000000)
eq('R1_positive_decomposition',R1,1666520+927060*(1-y)+50184*(1-y**4)+687528*y*y+135225*y**3)
# Spectral normalization: the correlated double-amplitude denominator.
t,w=S.symbols('t w');T=Q('27/50');rho=Q('.619');large=Q('31/50');XX=Q('3/10')
ups=[Q('3.1'),Q('1.16'),Q('.215'),Q('.020'),Q('.001')]
for j,up in enumerate(ups,1):ck('spectral_power_slope_term_'+str(j),comb(5,j)*large**j*XX**(j-1)<=up)
ck('spectral_power_slope_sum',sum(ups)<Q('9/2'))
eq('spectral_shape_square',1-w*(2-w),(1-w)**2)
G=Q('423/100')-(2+Q('9/2')*t*t)*(3+rho*t*t)*(Q('141/200')-Q('3/5')*t)
poly=Q('18/5')-Q('1039029/100000')*t+Q('22107/2500')*t*t-Q('785511/400000')*t**3+Q('16713/10000')*t**4
eq('spectral_G_expansion',G,t*poly)
ck('spectral_G_linear_bound',Q('1039029/100000')<Q('52/5'))
ck('spectral_G_quadratic_bound',Q('22107/2500')>Q('44/5'))
ck('spectral_G_cubic_bound',0<Q('785511/400000')<2)
ck('spectral_G_quartic_positive',Q('16713/10000')>0)
eq('spectral_completed_square',Q('18/5')-Q('52/5')*t+Q('44/5')*t*t-2*T**3,Q('44/5')*(t-Q('13/22'))**2+Q('145987/687500'))
ck('spectral_square_margin',Q('145987/687500')>0)
eq('spectral_total_denominator',Q('59/100')*Q('423/100'),Q('24957/10000'))
eq('spectral_central_margin_denominator',30000*Q('24957/10000'),74871)
ck('spectral_central_final',74871<75000)
ck('spectral_unit_final',Q('1/3000')>Q('1/75000'))
ck('spectral_uniform_final',Q('3/200')*Q('4/5')==Q('3/250')>Q('1/75000'))
print(json.dumps({'all_pass':True,'count':len(checks),'checks':checks,'scope':'Exact local entropy identities, all entropy moments, rational full-entropy payments, geometry endpoint/square replacements, and correlated spectral normalization. Does not verify unchanged PDE or geometric foundational theorems.'},indent=2))
