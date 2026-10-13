# R3: direct convexity proofs for the two boundary derivatives

**Current status:** the selected derivation has been integrated into the R3 manuscript and independently reviewed. Historical proposal wording below records its development; it is not pending work.
This is a derivation record for two proposed replacements in
workspace/monotonicity.qmd. The statements and parameter domains of
lem-zero-monotone and lem-container-monotone remain unchanged.

## 1. Vanishing short-tail width: remove the quartic and the split at \(p=3/5\)

Retain the notation and derivative identity (M.5.2). Pointwise, with
\(0<A<1\) and \(0<p<1\), the full gain derivative is
\[
J_0(p,A)=\frac{12-3A}{40p}-\frac{7-2A}{10}
       +\frac{6-5A}{40}p.
\]
For fixed \(A\),
\[
\partial_pJ_0=-\frac{12-3A}{40p^2}+\frac{6-5A}{40}
<\frac{-6-2A}{40}<0.
\]
Thus, whenever \(p\ge1/2\),
\[
J_0(p,A)\le J_0(1/2,A)
=-\frac{2+A}{80}<-\frac1{40}.
\]
This argument is pointwise in \(A\); it does not assert that \(A\) is
constant along the original geometric curve. For \(p<1/2\), the inherited
identity
\[
J_0-J_*
=\frac{A(1-p)(5p-3)}{40p}<0,\qquad
J_*(p)=\frac3{10p}-\frac7{10}+\frac{3p}{20},
\]
still applies.

For the branch \(1\le h\le4,\ r_0\ge1,\ 0<p<1/2\), retain the analytic
monotonicity estimate
\[
\frac{r_0hp}{6}
=\frac{h^2(h+2)}{2(1+h)(1+(1+h)p)^2}
\ge\frac3{4(1+2p)^2}.
\]
Define \(f(p)=3/[4(1+2p)^2]\). Since
\[
f''(p)=\frac{18}{(1+2p)^4}>0,
\]
its tangent at \(p=1/2\) gives
\[
f(p)\ge \frac3{16}-\frac38\left(p-\frac12\right)
=\frac38-\frac{3p}{8}.
\]
Consequently,
\[
\frac3{4(1+2p)^2}-pJ_*(p)
\ge\frac3{40}+\frac{p(13-6p)}{40}
>\frac3{40}.
\]
Hence \(r_0h/6>J_0\), exactly the condition needed to make (M.5.2)
strictly negative in this branch. The quartic numerator previously used
here is unnecessary. The other two height/order cases are retained.

## 2. Container equality: remove the degree-five numerator

The sufficient condition in (M.6.7) is positivity of
\[
\mathcal E_c(h)=
\frac{h(h+2)^2}{(1+h)((1+h)^2-c)}
-\frac13
-\frac{3c((1+h)^2+1)}
 {5(2(1+h)^2-c((1+h)^2+1))},
\qquad c=\frac{\sqrt3}{2}.
\]
In fact,
\[
\boxed{\mathcal E_c(h)>\frac18\qquad(h\ge1/2).}
\]

Set \(y=(1+h)^{-1}\), so \(0<y\le2/3\), and extend the transformed
function continuously to \(y=0\):
\[
\mathcal F_c(y)=
\frac{(1+y)(1-y^2)}{1-cy^2}
-\frac13-\frac{3c(1+y^2)}{5(2-c-cy^2)}.
\]
This is exactly \(\mathcal E_c(h)\), and all denominators are positive
on \([0,2/3]\), since \(6/7<c<7/8\). More explicitly,
\[
1-cy^2>\frac{11}{18},\qquad
2-c-cy^2>\frac{53}{72}.
\]

For \(a>0\), put \(W_a(y)=y^2/(a-cy^2)\) wherever its denominator is
positive. Then
\[
W_a'(y)=\frac{2ay}{(a-cy^2)^2},\qquad
W_a''(y)=\frac{2a(a+3cy^2)}{(a-cy^2)^3}>0.
\]
The two nonconstant terms of \(\mathcal F_c\) can be written as
\[
\frac{(1+y)(1-y^2)}{1-cy^2}
=1+y-(1-c)(1+y)W_1(y),
\]
\[
\frac{c(1+y^2)}{2-c-cy^2}
=\frac{c}{2-c}+\frac{2c}{2-c}W_{2-c}(y).
\]
Because \(W_a'\ge0\), \(W_a''>0\), and \(0<c<1\), the first displayed
term is strictly concave and the second strictly convex. Therefore
\[
\mathcal F_c''(y)
=-(1-c)\bigl(2W_1'(y)+(1+y)W_1''(y)\bigr)
-\frac{6c}{5(2-c)}W_{2-c}''(y)<0.
\]

A concave function on a closed interval lies above its endpoint chord.
At the endpoints,
\[
\mathcal F_c(0)=\frac23-\frac{3c}{5(2-c)}
>\frac23-\frac7{15}=\frac15,
\]
and
\[
\begin{aligned}
\mathcal F_c(2/3)
&=\frac{25}{3(9-4c)}-\frac13
-\frac{39c}{5(18-13c)}\\
&>\frac{175}{117}-\frac13-\frac{273}{265}
=\frac{4099}{31005}>\frac18.
\end{aligned}
\]
For the second line, the first rational term increases with \(c\), so
use \(c>6/7\); the subtracted rational term increases with \(c\), so
use \(c<7/8\). Thus \(\mathcal F_c>1/8\) throughout \([0,2/3]\).
This proves (M.6.7) directly and with a uniform margin, without clearing
denominators into a degree-five polynomial.

The proof for \(3/8<h<1/2\), the full gain in (M.6.3), the constancy of
the tail order on the relevant branch, and the admissible-interval
argument are all retained.

The integrated T.2 ratio simplification is also checked by check_r3_boundaries.py and the final independent integration audit: the ratio h^2(h+2)/[(h+1)(51h+82)^2] increases for h>0 and is bounded at h=4.
