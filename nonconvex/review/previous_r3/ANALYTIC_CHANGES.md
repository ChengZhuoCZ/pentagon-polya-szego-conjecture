# R3 analytic replacements — 12 October 2026

## Scope and continuity

This third English analytic edition continues the completed R2 proof. The current replacements are integrated into `workspace/robin.qmd`, `workspace/monotonicity.qmd`, and `workspace/terminal.qmd`, with the new regular-tail lemma explicitly imported where its construction and variational interpretation are needed. The central nonconvex-exclusion theorem, area normalization, allowable side counts, strict competitor construction, and common head and tail energy are preserved.

The main conclusion concerns nonconvex simple polygons. The regular-pentagon conclusion in the appendix still assumes a separate extremal theorem for convex polygons with at most five sides. That conditional premise is not used in the central theorem.

The completed R2 change record is archived at `review/previous_r2/ANALYTIC_CHANGES.md`, and the preceding English record is at `review/previous_english/ANALYTIC_CHANGES.md`. The current files named `r3_*_proposal.md` are integrated and independently reviewed derivation records. Their original planning language, where retained, describes development history rather than unfinished work.

## 1. R.6: a Volterra construction, differential recurrence, and direct tail barrier

**Source:** `workspace/robin.qmd`, `lem-regular-tail` and `lem-tail-recurrence`. **Derivation and audit:** `review/r3_tail_proposal.md` and `review/r3_tail_independent_audit.md`.

### A reusable regular-solution lemma

The new exported `lem-regular-tail` constructs the normalized solution of

$$
-u_a''+\frac{a(a-1)}{z^2}u_a=Tu_a,
\qquad \frac{u_a(z)}{z^a}\longrightarrow1\quad(z\downarrow0),
$$

for every real $a>1$ and every $T>0$. The order range includes all adjacent orders needed later; it is not restricted to the crossing interval $2\le a\le3$.

Writing $u_a=z^av$ gives the Volterra equation

$$
v=1-T\mathcal K_av,\qquad
(\mathcal K_av)(z)=\frac1{2a-1}\int_0^z
\eta\left[1-\left(\frac\eta z\right)^{2a-1}\right]v(\eta)\,d\eta.
$$

Its kernel is nonnegative and at most $\eta/(2a-1)$. In the equivalent norm

$$
\|v\|_\beta=\sup_{0\le z\le1}e^{-\beta z^2}|v(z)|,
\qquad \beta=\frac{T}{2a-1},
$$

the affine map has contraction factor at most $1/2$. This proves existence and uniqueness for every $T>0$, without a small-energy assumption or a regular-solution power series. Differentiation of the integral equation supplies the endpoint asymptotics, including

$$
u_a'-\frac a z u_a=-\frac{T}{2a+1}z^{a+1}+O(z^{a+3}).
$$

The same lemma proves the Hardy form domain $H_0^1(0,1)$, finite singular-endpoint energy, and spectral ordering in the order parameter. If $T<\lambda_D(a)$, a first-zero argument gives $u_a>0$, and its trace-one normalization is the unique shifted-energy minimizing extension. These conclusions are exported explicitly for the Robin, coupled, and crossing proofs.

### The exact recurrence from differential factors

Set $A_a=\partial_z-a/z$ and $B_a=\partial_z+a/z$. The identities

$$
L_a=-B_aA_a,\qquad L_{a+1}=-A_aB_a
$$

and uniqueness of the regular normalization give

$$
A_au_a=-\frac{T}{2a+1}u_{a+1},\qquad
B_au_{a+1}=(2a+1)u_a.
$$

These are identities of differential expressions, with no claim that the separate factors preserve a Dirichlet operator domain. Positivity of both adjacent regular solutions proves the denominator sign before division:

$$
s+D_{s+1}>0,\qquad D_s=s-\frac{T}{s+D_{s+1}}.
$$

The exact recurrence holds for every real $s>1$ and $0<T<\lambda_D(s)$. It remains available to H.6.

### One comparison function gives the original tail response

Assume $a=\sigma>1$ and $0<T<\lambda_D(a)$, together with the original positive-radical and positive-denominator hypotheses. Put

$$
a=\sigma,\quad r=\sqrt{(2a+5)^2-4T},\quad
c=\frac{2a+5-r}{2},\quad A=2a+1,\quad M=2a+3.
$$

Then $T=c(2a+5-c)$, $C=M-c$, and $D=A-T/C$. With $B=Ac+T$ and $H(z)=AM-Bz^2$, the original hypotheses imply $H(z)\ge H(1)=CD>0$. The positive comparison function

$$
w(z)=z^a\exp\left(-\int_0^z
\frac{T\eta(M-c\eta^2)}{H(\eta)}\,d\eta\right)
$$

has exactly the desired endpoint response $w'(1)/w(1)=a-T/D$. Its differential residual factors as

$$
\frac{(L_a-T)w}{w}
=\frac{T^2c^2z^4(1-z^2)}{H(z)^2}>0
\qquad(0<z<1).
$$

A Wronskian comparison with the regular solution therefore gives $D_\sigma>\mathsf T(\sigma,T)$. The existing declaration retains its weaker non-strict inequality. This direct barrier replaces the comparison at a higher order and the two subsequent response substitutions; the recurrence itself remains proved and available independently.

## 2. R.7: a Sturm argument using both endpoints replaces the resolvent proof

**Source:** `workspace/robin.qmd`, `lem-cot-rational`. **Derivation:** `review/r3_cot_proposal.md`.

The rational function $\mathsf H$ is unchanged, and the result retains the complete range

$$
\sqrt K\cot\sqrt K>\mathsf H(K)
\qquad(0<K<\pi^2).
$$

Write $\Pi=\pi^2$, $t=x^2/\Pi$, and $a=3\Pi/2-45/4$. The explicit comparison function

$$
p(x)=x(1-t)(1-t/4)(1-t/9)^a
$$

is smooth on $[0,\pi]$, positive in its interior, and zero at both endpoints. Its logarithmic derivative is exactly $xp'/p=\mathsf H(x^2)$.

Direct differentiation factors $-p''-p$ into a positive factor and a cubic $R_\Pi(t)$. The proof displays that cubic and proves that it is strictly decreasing, positive at $0$, and negative at $1$, using only the inherited rational bounds for $\pi^2$. Thus the residual changes sign exactly once. For

$$
W(x)=\cos x\,p(x)-\sin x\,p'(x),
$$

both endpoint values are zero, and $W'=\sin x(-p''-p)$ is first positive and then negative. Integration from the appropriate endpoint gives $W>0$ throughout $(0,\pi)$, proving the strict response inequality.

This replaces the finite spectral projection, resolvent energy identity, and complementary spectral-defect argument. It preserves the response function and every downstream target. One explicit cubic identity remains, with its full-range sign pattern proved by differentiation; no sampled sign check is used.

## 3. M.5: a fixed-parameter gain estimate and one tangent remove the quartic

**Source:** `workspace/monotonicity.qmd`, `lem-zero-monotone`. **Derivation and audit:** `review/r3_boundary_proposal.md` and `review/r3_boundary_independent_audit.md`.

The declaration still states strict decrease on the admissible boundary $q=0$ for fixed $3/8<h\le4$. Its full gain derivative is

$$
J_0(p,A)=\frac{12-3A}{40p}-\frac{7-2A}{10}
+\frac{6-5A}{40}p.
$$

For each fixed $0<A<1$, direct differentiation shows $\partial_pJ_0<0$ on $0<p<1$. Hence

$$
J_0(p,A)\le J_0(1/2,A)=-\frac{2+A}{80}<-\frac1{40}
\qquad(p\ge1/2).
$$

This is a pointwise estimate for every allowed $A$; it does not assume that $A$ stays constant along the geometric boundary. For $p<1/2$, the retained comparison $J_0<J_*$ applies, where $J_*=3/(10p)-7/10+3p/20$.

In the branch $1\le h\le4$, $r_0\ge1$, and $0<p<1/2$, the retained monotonicity estimate gives $r_0hp/6\ge3/[4(1+2p)^2]$. The latter function is convex, and its tangent at $p=1/2$ gives

$$
\frac3{4(1+2p)^2}-pJ_*(p)
\ge\frac3{40}+\frac{p(13-6p)}{40}>\frac3{40}.
$$

This proves the required derivative sign without the previous quartic numerator. The other height/order branches and the admissible-interval argument remain in force.

## 4. M.6: concavity gives a uniform margin without the degree-five numerator

**Source:** `workspace/monotonicity.qmd`, `lem-container-monotone`, equation (M.6.7).

With $L=1+h$, $D_h=L^2+1$, and $c=\sqrt3/2$, the sufficient expression is

$$
\mathcal E_c(h)=\frac{h(h+2)^2}{L(L^2-c)}
-\frac13-\frac{3cD_h}{5(2L^2-cD_h)}.
$$

The new argument proves the stronger statement $\mathcal E_c(h)>1/8$ for every $h\ge1/2$. In the coordinate $y=L^{-1}$ it becomes

$$
\mathcal F_c(y)=\frac{(1+y)(1-y^2)}{1-cy^2}
-\frac13-\frac{3c(1+y^2)}{5(2-c-cy^2)},
\qquad 0\le y\le\frac23.
$$

The original function extends continuously to $y=0$. The bounds $6/7<c<7/8$ keep both denominators strictly positive. For $\eta>0$, the function $W_\eta(y)=y^2/(\eta-cy^2)$ has $W_\eta'\ge0$ and $W_\eta''>0$ wherever used. Decomposing the first term as $1+y-(1-c)(1+y)W_1(y)$ and the last reciprocal term through $W_{2-c}$ proves $\mathcal F_c''<0$ directly.

The endpoint bounds are

$$
\mathcal F_c(0)>\frac15,\qquad
\mathcal F_c(2/3)>\frac{4099}{31005}>\frac18.
$$

Concavity therefore gives the uniform margin. The degree-five numerator is no longer needed. The branch $3/8<h<1/2$, the full gain, and the admissible-boundary argument are retained, so the original complete monotonicity declaration remains proved.

## 5. T.3: one majorant and one global curvature correction

**Source:** `workspace/terminal.qmd`, `lem-psi-payment`. **Derivation and audit:** `review/r3_terminal_proposal.md` and `review/r3_terminal_independent_audit.md`.

Keep the original payment

$$
Z_\Psi=s+h(J+G_*)-v\Pi_+h^2e,
\qquad S=\frac{2hk}{1-k},\qquad R_0=Z_\Psi+S.
$$

The common partial-fraction identity for $R_0$ is retained. One majorant now works on the entire interval:

$$
S(h)<M(h):=\frac9{2(h+2)}+\frac6{5(h+2)^2}-\frac1{9h}
\qquad\left(\frac38\le h\le4\right).
$$

The proof displays a short squared remainder about $h=1/2$ for the numerator of $M-S$. Its coefficient consists of an increasing quadratic and the nonnegative term

$$
h^2(4-h)(6600h^2+39410h+52858).
$$

An ordinary quadratic minimum proves the numerator greater than $450$. This replaces both previous head-comparison polynomials. An explicit polynomial identity remains, with its sign exposed by the squared remainder and the distance to the upper endpoint.

Set $G=R_0-M$ and $x=1/(h+2)$. Direct reciprocal estimates give

$$
Q(x):=\frac{(h+2)^3G''(h)}2>-\frac{37}{75}>-\frac12
\quad\left(\frac16\le x\le\frac8{19}\right).
$$

The coupled head term has an elementary scalar maximum, and its derivative has a minimum at an endpoint on $[1/6,2/5]$. These facts give $Q'<-53/200$ there and the coarse positive bound $Q(2/7)>7/25$. Thus $Q>0$ for $x\le2/7$.

The single corrected function

$$
F(h)=G(h)+\frac1{2(h+2)}
$$

is strictly convex on the full height interval. Its tangent at $h=1$ yields

$$
G(h)\ge G(1)+G'(1)(h-1)-\frac{(h-1)^2}{18(h+2)}.
$$

Using $G(1)>1/80$ and $-1/400<G'(1)<0$ gives

$$
G(h)>\frac1{80}-\frac1{800}-\frac{25}{2736}
=\frac{289}{136800}>\frac{27}{16000}
\qquad\left(\frac38\le h\le\frac32\right).
$$

For $h\ge3/2$, the proof has $G''>0$ and $G'(3/2)>0$, extending the same bound to $h=4$. The declared conclusion remains exactly $Z_\Psi>27/16000$. Its proof supplies the stronger lower bound above, while keeping the original $Z_\Psi$, both gain terms, and the shared physical energy.

The old two response charts, the second derivative of their normalized curvature, its zero count, and the interior-extrema argument are removed.

## 6. T.2: a shorter proof of the initial ratio bound

**Source:** `workspace/terminal.qmd`, `lem-common-tail-line`.

Only the opening estimate is changed. For

$$
f(h)=\frac{h^2(h+2)}{(1+h)(51h+82)^2},
$$

the logarithmic derivative is

$$
\frac{f'}f=\frac{113h^2+410h+328}{h(h+1)(h+2)(51h+82)}>0.
$$

Hence $f(h)\le f(4)=24/102245<1/4225$ on $3/8\le h\le4$, giving the same bound

$$
\frac{T_0}{B^2}<\frac{2961}{4}f(h)
<\frac{2961}{16900}<\frac{30}{169}.
$$

This replaces the opening cubic/quadratic comparison. The subsequent common-tail curvature proof, positive denominators, uniform gap $\mathcal D(\tau)>1/v+1/2000$, and affine response lower bound are retained.

## Retained terminal and large-height estimates

These results were established in preceding editions and are not presented as new R3 bounds:

| Result | Exact retained range | Retained conclusion |
|---|---|---|
| T.4, second terminal payment | $\sqrt3-1<h\le4$ | $Z_\Phi>3/500$ |
| H.5, crossing comparison | Every real $2\le s\le3$, $0\le t\le3/2$ | $\lambda_1(K_{s;1,t})>(25s-11)/(2F_0(t))$; the geometric specializations are $39/(2D)$ and $32/D$ |
| H.6, noncrossing comparison | $0\le\delta\le1/4$ | $\Lambda_2(\delta)>625/32>39/2$ and $\Lambda_3(\delta)>1525/48>1587/50$ |

Here $\Lambda_\sigma(\delta)=(1+\delta)^2\lambda_1(K_{\sigma;1,\delta})$, with the operators and $F_0$ defined in `workspace/high.qmd`. The nonincrease of $\Lambda_\sigma$ is retained for every real $2\le\sigma\le3$ and every $\delta\ge0$. H.5 now cites the exported Volterra solution construction and the new R.7 proof; H.6 retains the exact adjacent-order recurrence. Their spectral constants, physical scaling, and common-energy interface comparisons are unchanged.

T.4 retains its positive quadratic remainder and convex reciprocal-sum tangent argument. The earlier geometric reductions, variational Hadamard formula, common-tail curvature gap, explicit truncated-square competitor, and energy-tensor argument remain in force.

The old crossing trace polynomials, Green trace calculation, characteristic trace identity, stronger trace-surrogate assertions, and continuous 945 envelope remain retired. The new direct arguments do not claim those stronger auxiliary trace conclusions. R3's replacement of the cotangent resolvent proof is additional to R2's removal of the crossing trace machinery.

## What was checked and what remains in the proof

The four new R3 exact-check scripts contain 99 passing checks: 30 boundary/T.2, 22 cotangent, 7 tail, and 40 terminal checks. The retained crossing script contains 38 passing checks. Independent mathematical audits examine the full parameter ranges, positive denominators, endpoint behavior, strict inequalities, variational domains, shared energy, and downstream uses. The scripts corroborate selected identities and rational arithmetic; their execution is not a proof premise.

The current custom source report records 18 QMD files, 58 declarations, and 55 linked proof blocks, with no reported source findings or protected-file discrepancy. The new declaration is `lem-regular-tail`. The protected main goal, locks, contract, and strict configuration are preserved. The supplied 83-page PDF and standalone TeX use the R3-20261012 filename and are rendered through Pandoc and XeLaTeX. The PDF has compiled without XeLaTeX warnings or overfull/underfull boxes, and an automated scan found no off-page text spans. Final visual QA is complete: all pages were inspected in contact sheets and the revised proof pages received close review. The single stale two-majorant sentence was corrected and its rebuilt page confirmed; no unresolved layout defects remain.

Explicit finite polynomial identities, partial fractions, elementary squares, derivative calculations, and scalar endpoint or tangent comparisons remain. Their signs and interval implications are explained in the manuscript. The proof does not rely on finite-element results, floating-point grids, parameter-box programs, or executable sign certificates.

The retained configuration is `codex` / `gpt-6.1-sol` / `xhigh`, with strict citations, strict proof and refutation rigor, and assumptions forbidden. The external-basis file is absent. The official qmd-prover and Quarto executables were unavailable, so no official local verdict, global composition, or proof-assistant certification is claimed. Standard PDF rendering and custom source checks are separate from those unavailable verification layers.

Current review records are indexed in `review/README.md`. Superseded R2 terminal scripts and reports are archived under `review/previous_r2/`; earlier English records are under `review/previous_english/`. The R2 crossing derivation, audit, and exact checks remain current because the crossing calculation and its constants are retained.
