"""Round 8 finite identities and source bindings; not a certification of infinite-dimensional proofs."""
from pathlib import Path
import json
import sympy as S
checks={}
def ck(n,v):
 assert bool(v),n
 checks[n]=True
def eq(n,a,b=0):ck(n,S.simplify(S.expand(a-b))==0)
x,y,R,alpha,eps,nu,Lambda,B,C=S.symbols('x y R alpha eps nu Lambda B C',positive=True)
a11,a12,a22,b1,b2,c=S.symbols('a11 a12 a22 b1 b2 c',real=True)
r2=x*x+y*y;beta=S.exp(-alpha*r2)-S.exp(-alpha*R*R)
Lbeta=a11*S.diff(beta,x,2)+2*a12*S.diff(beta,x,y)+a22*S.diff(beta,y,2)+b1*S.diff(beta,x)+b2*S.diff(beta,y)-c*beta
rhs=S.exp(-alpha*r2)*(4*alpha**2*(a11*x*x+2*a12*x*y+a22*y*y)-2*alpha*(a11+a22)-2*alpha*(b1*x+b2*y)-c)+c*S.exp(-alpha*R*R)
eq('general_elliptic_barrier_derivative',Lbeta,rhs)
M,D=S.symbols('M D',positive=True);threshold=(2*D+1+C*M)/M
poly=S.expand(threshold**2*M-2*threshold*D-C)
eq('explicit_barrier_threshold_residual',poly,((2*D+1)*(1+C*M)+C**2*M**2)/M)
ck('barrier_threshold_positive_coefficients',all(v>0 for v in S.Poly(S.expand(poly*M),D,C,M).coeffs()))
t=S.symbols('t',positive=True)
eq('hopf_inward_slope',S.limit((S.exp(-alpha*(R-t)**2)-S.exp(-alpha*R*R))/t,t,0),2*alpha*R*S.exp(-alpha*R*R))
eq('barrier_outer_boundary',beta.subs({x:R,y:0}),0)
# Hilbert/parallelogram and bounded symmetric forms in arbitrary two-coordinate blocks.
x1,x2,y1,y2,z1,z2,l1,l2=S.symbols('x1 x2 y1 y2 z1 z2 l1 l2',real=True)
X=S.Matrix([x1,x2]);Y=S.Matrix([y1,y2]);Z=S.Matrix([z1,z2]);A=S.Matrix([[a11,a12],[a12,a22]]);ell=S.Matrix([l1,l2])
def norm2(v):return (v.T*v)[0]
def form(v,w):return (v.T*A*w)[0]
def J(v):return form(v,v)-2*(ell.T*v)[0]
eq('projection_parallelogram',norm2(X-Y),2*norm2(Z-X)+2*norm2(Z-Y)-4*norm2(Z-(X+Y)/2))
eq('quadratic_midpoint_identity',J((X+Y)/2),(J(X)+J(Y))/2-form(X-Y,X-Y)/4)
eq('nonnegative_form_dual_difference',form(X,X)-2*form(X,Y)+form(Y,Y),form(X-Y,X-Y))
eq('weak_plus_norm_identity',norm2(X-Y),norm2(X)+norm2(Y)-2*(X.T*Y)[0])
eq('quadratic_euler_derivative',S.diff(J(X+t*Y),t).subs(t,0),2*(form(X,Y)-(ell.T*Y)[0]))
p=S.symbols('p',real=True)
eq('weighted_cauchy_variance',p*norm2(X)+(1-p)*norm2(Y)-norm2(p*X+(1-p)*Y),p*(1-p)*norm2(X-Y))
h11,h12,h22=S.symbols('h11 h12 h22',real=True)
eq('strict_hessian_source_sign_2d',2*(h11*h11+h12*h12)-2*(h11+h22)*h11,-2*(h11*h22-h12*h12))
sigma=S.symbols('sigma',positive=True)
eq('angular_kernel_operator_identity',2+(2/sigma)*(-sigma),0)
k=S.symbols('k',integer=True,positive=True)
eq('cauchy_subsequence_tail_sum',S.summation(2**(-k),(k,1,S.oo)),1)
# Convolution product/derivative signs and primitive product finite identities.
f=S.Function('f')(x);g=S.Function('g')(x)
eq('smooth_multiplier_test_identity',S.diff(f*g,x),S.diff(f,x)*g+f*S.diff(g,x))
kern=S.exp(-(x-y)**2)
eq('convolution_test_derivative_sign',S.diff(kern,x),-S.diff(kern,y))
phi=x*(1-x);gg=1+x*x;primitive=S.integrate(gg,(x,0,x))
eq('primitive_weak_derivative_identity',S.integrate(primitive*S.diff(phi,x),(x,0,1)),-S.integrate(gg*phi,(x,0,1)))
# Source bindings are transcription checks, not logical verification.
root=Path(__file__).resolve().parent.parent;ar=root/'workspace/analytic-replacements-1012'
bar=(ar/'local-elliptic-barriers.qmd').read_text();hil=(ar/'hilbert-foundations.qmd').read_text();inte=(ar/'integral-foundations.qmd').read_text();dist=(ar/'distribution-foundations.qmd').read_text()
pressure=(root/'workspace/ps-convex-geometric-tensor-switch-1011g/pressure-foundations.qmd').read_text();weights=(root/'workspace/ps-convex-geometric-tensor-switch-1011g/pressure-weights.qmd').read_text()
spec=(ar/'dirichlet-spectral-foundations.qmd').read_text();heat=(ar/'gaussian-ground-state.qmd').read_text()
ck('barrier_explicit_parameter_in_source',r'\alpha=\frac{2D_0+1+CM}{M}' in bar)
ck('barrier_all_three_interfaces','内切球' in bar and '$v\\equiv0$ 或 $v>0$' in bar and '若 $Lf\\ge0$' in bar)
ck('strict_hessian_uses_barrier','@lem-arc-local-elliptic-barrier-1012' in pressure and r'$c=2\operatorname{tr}H\ge0$' in pressure)
ck('hopf_replaced_by_ball_barrier','内切球结论用于 $L=\\Delta$' in pressure and 'Hopf 引理在' not in pressure)
ck('angular_comparison_uses_barrier','有界域正最大值反证' in weights and '@lem-arc-local-elliptic-barrier-1012' in weights)
ck('angular_local_coefficient_scope','不要求这些系数在整个无界楔上一致有界或一致椭圆' in weights)
ck('hilbert_weak_sequence_diagonal','依次抽取再对角化' in hil)
ck('hilbert_projection_parallelogram','平行四边形恒等式' in hil)
ck('quadratic_cauchy_construction',r'c\|v_n-v_k\|^2\le2(J(v_n)-m)+2(J(v_k)-m)' in hil)
ck('spectral_form_uses_quadratic_construction','@lem-arc-coercive-quadratic-1012' in spec)
ck('heat_form_uses_quadratic_construction','@lem-arc-coercive-quadratic-1012' in heat)
ck('hilbert_concrete_completeness_bound',r'\left\|\sum_{k=1}^N|d_k|\right\|_2^2\le1' in dist)
ck('distribution_weak_limit_test_identity',r'\int f\partial_i\phi=\lim_n\int f_n\partial_i\phi' in dist)
ck('zero_distribution_uses_local_l1_limit','其局部 $L^1$ 极限为 $f$' in dist)
ck('zero_gradient_countable_null_union','可数个零例外集之并仍为零集' in dist)
ck('integral_simple_function_monotone_proof',r'E_{i,n}=E_i\cap\{f_n\ge qa_i\}' in inte)
ck('fubini_generating_class_proof','最小此类' in inte and '有理矩形生成欧氏 Borel 集' in inte)
ck('lebesgue_construction_retained','不重建 Lebesgue 外测度' in inte)
ck('prior_q_constant_preserved',r'0<q:=I/J_R<\frac{5\sqrt2}{17}<\frac5{12}.' in pressure)
print(json.dumps({'passed':True,'check_count':len(checks),'checks':checks,'scope':'Finite symbolic derivative/algebra identities and source bindings only. Does not certify the strong principle, Hilbert weak subsequences, measure limits, Fubini, distribution theory or the complete proof.'},ensure_ascii=False,indent=2))
