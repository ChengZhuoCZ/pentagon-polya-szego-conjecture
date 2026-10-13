# R3 cotangent response: an elementary two-endpoint Sturm comparison

**Current status:** the selected derivation has been integrated into the R3 manuscript and independently reviewed. Historical proposal wording below records its development; it is not pending work.
Status: complete derivation, independently reviewed by the parent and ready for its R.7 integration. The parent reported that the full-range residual and endpoint Wronskian proof are correct. The author has not edited `robin.qmd`; the separately authorized downstream update in `high.qmd` cites the new regular-tail construction and uses the current Sturm description of R.7. The R3 `AGENTS.md`, `.qmd-prover/config.yml`, and external-basis preflight were read independently. The external-basis file is absent. The existing `codex` / `gpt-6.1-sol` / `xhigh` settings, strict citations and rigor, forbidden assumptions, and protected statements remain unchanged. The official qmd-prover executable is unavailable; this report makes no certification claim.

The supplementary exact checker passed all 22 formal identity and rational-arithmetic checks. Its results are saved in `review/r3_cot_exact_checks.json`; the proof does not depend on running the checker.

## Result and scope

The existing assertion in `lem-cot-rational` is preserved exactly:

$$
\sqrt K\cot\sqrt K>\mathsf H(K)
\qquad(0<K<\pi^2),
$$

where, with $\Pi=\pi^2$,

$$
\mathsf H(K)=1-\frac{2K}{\Pi-K}-\frac{2K}{4\Pi-K}
-\frac{2K(1/6-5/(4\Pi))}{1-K/(9\Pi)}.
$$

The proof below uses elementary differentiation, the known zero endpoints and positivity of $\sin x$ on $(0,\pi)$, and the already proved rational bounds for $\pi^2$. It replaces the finite spectral projection, the resolvent, and the strict-defect operator argument. The definition of $\mathsf H$, its complete parameter range, and all downstream targets are unchanged.

## 1. A positive function with exactly the required logarithmic derivative

Write

$$
t=\frac{x^2}{\Pi},\qquad
a=\frac{3\Pi}{2}-\frac{45}{4},\qquad
p(x)=x(1-t)(1-t/4)(1-t/9)^a
\qquad(0\le x\le\pi).
\tag{R3.R7.1}
$$

The rational bounds in `lem-pi-rational` imply

$$
\frac{49}{5}<\Pi<\frac{99}{10},\qquad
\frac{69}{20}<a<\frac{18}{5}.
$$

On the entire closed interval, $1-t/9\ge8/9>0$. Thus its real power is a smooth function of $x$ there. The remaining factors are polynomials. Consequently $p\in C^\infty[0,\pi]$, with $p(0)=p(\pi)=0$, finite endpoint derivatives, and $p(x)>0$ for $0<x<\pi$. In particular, the real exponent causes no endpoint singularity.

Logarithmic differentiation on the open interval gives

$$
\frac{xp'(x)}{p(x)}
=1-\frac{2t}{1-t}-\frac{t/2}{1-t/4}
-\frac{2at/9}{1-t/9}
=\mathsf H(x^2),
\tag{R3.R7.2}
$$

because $a/(9\Pi)=1/6-5/(4\Pi)$. Every denominator is positive for $0<x<\pi$.

## 2. The differential residual reduces to one explicitly monotone cubic

Define

$$
\begin{aligned}
c_0(\Pi)&=\frac{665}{72}+\frac{5\Pi}{27}-\frac{\Pi^2}{9},\\
c_1(\Pi)&=\frac{175}{432}-\frac{239\Pi}{162}+\frac{5\Pi^2}{36},\\
c_2(\Pi)&=-\frac{1295}{1296}+\frac{131\Pi}{324}-\frac{\Pi^2}{36},\\
R_\Pi(t)&=c_0+c_1t+c_2t^2-\frac{\Pi t^3}{324}.
\end{aligned}
\tag{R3.R7.3}
$$

The exact residual identity is

$$
-p''(x)-p(x)
=\frac{xt}{\Pi}(1-t/9)^{a-2}R_\Pi(t).
\tag{R3.R7.4}
$$

For a direct verification, put $Q(t)=(1-t)(1-t/4)$, $w(t)=1-t/9$, and $f(t)=Q(t)w(t)^a$, so $p(x)=xf(t)$. The chain rule gives

$$
p''(x)+p(x)=\frac{x}{\Pi}\bigl(6f'(t)+4tf''(t)+\Pi f(t)\bigr).
$$

Using $Q'=-5/4+t/2$, $Q''=1/2$, and $w'=-1/9$ yields

$$
\begin{aligned}
&-\frac{6f'+4tf''+\Pi f}{w^{a-2}}\\
&\quad=-\left(\Pi Q-\frac{15}{2}+5t\right)w^2
+\frac a9\left(6-\frac{35t}{2}+\frac{11t^2}{2}\right)w
-\frac{4a(a-1)}{81}\,tQ\\
&\quad=tR_\Pi(t).
\end{aligned}
$$

The constant term cancels because $2a/3=\Pi-15/2$. Substituting $a=3\Pi/2-45/4$ in the remaining cubic gives precisely (R3.R7.3). This supplies a short checkable identity, rather than an unspecified polynomial expansion.

We now prove the residual sign on the full interval using only three quadratic functions of $\Pi$. On $49/5<\Pi<99/10$,

$$
c_0'(\Pi)=\frac{5-6\Pi}{27}<0,\qquad
c_2'(\Pi)=\frac{131-18\Pi}{324}<0.
$$

Evaluation at the single upper constant $99/10$ therefore gives

$$
c_0(\Pi)>c_0(99/10)=\frac{323}{1800}>0,
\qquad
c_2(\Pi)>c_2(99/10)=\frac{4553}{16200}>0.
\tag{R3.R7.5}
$$

Also,

$$
c_1+2c_2=\frac{\Pi^2}{12}-\frac{2\Pi}{3}-\frac{2065}{1296},
\qquad
\frac{d}{d\Pi}(c_1+2c_2)=\frac{\Pi-4}{6}>0.
$$

Consequently

$$
c_1+2c_2<(c_1+2c_2)(99/10)
=-\frac{419}{16200}<0.
\tag{R3.R7.6}
$$

Since $c_2>0$, for every $0\le t\le1$ this proves

$$
R_\Pi'(t)=c_1+2c_2t-\frac{\Pi t^2}{108}
<c_1+2c_2<0.
\tag{R3.R7.7}
$$

The first inequality is strict also at the endpoints: at $t=0$ it follows from $c_2>0$, while at $t=1$ it follows from $\Pi>0$. Finally,

$$
R_\Pi(0)=c_0>0,
\qquad
R_\Pi(1)=\frac{700}{81}-\frac{8\Pi}{9}
<\frac{700}{81}-\frac89\frac{49}{5}
=-\frac{28}{405}<0.
\tag{R3.R7.8}
$$

The intermediate value theorem and strict monotonicity give exactly one $t_*\in(0,1)$ with $R_\Pi(t_*)=0$. Hence $-p''-p$ is strictly positive on $0<x<x_*:=\sqrt{\Pi t_*}$ and strictly negative on $x_*<x<\pi$.

## 3. The two zero endpoints force a strictly positive Wronskian

Let

$$
W(x)=\cos x\,p(x)-\sin x\,p'(x).
$$

The endpoint regularity established in Section 1 makes $W$ continuously differentiable on $[0,\pi]$. Since both $p$ and $\sin$ vanish at both endpoints,

$$
W(0)=W(\pi)=0.
$$

Differentiation gives

$$
W'(x)=\sin x\,[-p''(x)-p(x)].
\tag{R3.R7.9}
$$

Because $\sin x>0$ on the open interval, $W'>0$ before $x_*$ and $W'<0$ after $x_*$. Therefore

$$
W(x)=\int_0^x W'(y)\,dy>0\quad(0<x\le x_*),
$$

and

$$
W(x)=-\int_x^\pi W'(y)\,dy>0\quad(x_*\le x<\pi).
$$

No limit involving a singular quotient is used at either endpoint. Dividing the strictly positive Wronskian by the positive product $p(x)\sin x$ now yields

$$
x\cot x-\mathsf H(x^2)
=\frac{xW(x)}{p(x)\sin x}>0
\qquad(0<x<\pi).
$$

Taking $x=\sqrt K$ proves the required strict inequality on the entire original interval $0<K<\pi^2$.

## 4. Why the direct one-sided Riccati test needed refinement

The Riccati identity for $r(K)=\sqrt K\cot\sqrt K$ is

$$
2Kr'(K)=r(K)-r(K)^2-K.
$$

The same calculation for $\mathsf H(K)=xp'(x)/p(x)$ gives the exact defect

$$
\mathsf H-\mathsf H^2-K-2K\mathsf H'
=\frac{t^2R_\Pi(t)}{(1-t)(1-t/4)(1-t/9)^2},
\qquad t=K/\Pi.
$$

It changes sign once, from positive to negative. Thus the unchanged $\mathsf H$ is not a global one-sided Riccati subsolution. That observation does not obstruct the bound: the known second zero endpoint supplies the missing boundary condition, and the Wronskian argument above uses precisely the resulting one-change residual pattern.

## Integration notes

- Replace only the proof of `lem-cot-rational`; preserve its declaration and `def-analytic`'s definition of $\mathsf H$ verbatim.
- Cite `def-analytic` for the rational response and `lem-pi-rational` for the coarse constants. Both are already imported by `robin.qmd`.
- The former finite-mode resolvent argument and strict operator defect are no longer needed for this lemma.
- The argument contains one explicitly differentiated cubic and elementary monotonicity on the full intervals. It uses no coefficient-sign table, parameter grid, interval subdivision, or numerical spectral estimate.
- The supplementary exact checker is `review/check_r3_cot.py`; its output is `review/r3_cot_exact_checks.json`. It checks the displayed algebra and rational endpoint arithmetic and is not a premise of the proof.
