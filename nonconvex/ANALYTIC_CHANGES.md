# R4 analytic replacements — 12 October 2026

## Scope and continuity

This fourth English analytic edition continues the completed R3 proof. The replacements are integrated into `workspace/high.qmd`, `workspace/monotonicity.qmd`, `workspace/robin.qmd`, and `workspace/terminal.qmd`. All 58 R3 declarations, their metadata, the parameter definitions, the main goal, and the strict verification settings are preserved.

The central theorem concerns nonconvex simple polygons with at most five active sides, with the same area normalization and strict competitor conclusion. The separate convex-pentagon extremal theorem remains an explicit hypothesis only of the final appendix corollary. The head and tail continue to use the same physical energy and interface.

The R3 edition-level records and superseded first-terminal remainder calculation are archived under `review/previous_r3/`. Earlier records remain under `review/previous_r2/` and `review/previous_english/`. Files named `r4_*_proposal.md` are integrated derivation records, not pending alternatives. The QMD sources are authoritative.

## 1. M.4: one convex lower bound for the complete short-tail-dominant branch

**Source:** `workspace/monotonicity.qmd`, `lem-other-branch`. **Derivation and audit:** `review/r4_boundary_proposal.md` and `review/r4_boundary_independent_audit.md`.

The unchanged declaration is

$$
\mathcal G>\frac1{150}+\mathcal B(A,w)>\frac1{150}
\qquad\text{on }\mathcal D_*\cap\{q>p\}.
$$

### Geometry and uniform response ranges

With $L=1+h$ and $D_h=h^2+2h+2$, the strict area condition gives

$$
p(1-q)>j(h):=\frac{h(h+2)}{LD_h}.
$$

For $h\le1$, the bounds $p<q\le h/L\le1/2$ contradict this inequality because $q(1-q)\le h/L^2<j(h)$. For $1\le h\le2$, the identity

$$
h^3-h^2-4h+2=(h-2)(h-1)(h+2)-2\le-2
$$

implies $j(h)>1/4$, impossible since $p(1-q)<q(1-q)\le1/4$. Thus $2<h\le4$ throughout the branch.

Here $m=q$, so

$$
R>\frac{h}{D_hq(1-q)}\ge\frac{4h}{D_h}\ge\frac8{13}.
$$

Using $\Pi=\pi^2>49/5$ and $\sigma(\sigma-1)=\Pi R^2/2$ gives $\sigma>39/20$. The original energy satisfies

$$
E<\frac{3\Pi(1+h)}{h(h+2)(h+5)}.
$$

The normalized right side decreases with $h$, while its product with $h^2$ increases. Their endpoint values yield

$$
\frac K\Pi<\frac9{56}<\frac16,\qquad T=h^2E<11.
$$

Hence the original radical and denominators obey

$$
r>\frac{59}{10},\quad C>\frac{27}{5},\quad
D>\frac{773}{270}>\frac{20}{7},
$$

and therefore

$$
\mathsf T(\sigma,T)>\frac{39}{20}-\frac{7T}{20}.
$$

The three positive head coefficients sum to $1/3$. Bounding their reciprocal denominators by the smallest one gives

$$
\mathsf H(K)\ge1-\frac{K}{3(1-K/\Pi)}>1-\frac{2E}{5}.
$$

These are pointwise estimates at the original parameters. The proof does not move along a comparison path requiring a new pole-free check.

### A single tangent

Adding the response estimates gives

$$
\mathcal G-\mathcal B(A,w)>1+\frac{39}{20h}-\frac{8+7h}{20}E>F(h),
$$

where exact partial fractions give

$$
F(h)=1+\frac3{4h}+\frac3{2(h+2)}-\frac{54}{5(h+5)}.
$$

On $2<h\le4$,

$$
\frac{(h+5)^3}{2}F''(h)
=\frac34\left(\frac{h+5}{h}\right)^3
+\frac32\left(\frac{h+5}{h+2}\right)^3-\frac{54}{5}
>\frac{21}{80}>0.
$$

The value and slope at $h=3$ are $F(3)=1/5$ and $F'(3)=61/2400>0$. Consequently

$$
F(h)\ge\frac15+\frac{61}{2400}(h-3)>\frac{419}{2400}>\frac16>\frac1{150}.
$$

Finally, $0<A,w<1$ makes the original gain strictly positive. This proves the entire declaration with a stronger internal margin. It removes the old geometric cutoff at $7/3$, the response split at $h=3$, the two separate tail evaluations, and their path checks.

## 2. H.6: glue positive comparison functions and use the complete form

**Source:** `workspace/high.qmd`, `lem-no-crossing-sturm`. **Derivation and audit:** `review/r4_noncrossing_proposal.md` and `review/r4_noncrossing_independent_audit.md`.

### Full scaling range

The unitary scaling to $(0,1)$ transforms $(1+\delta)^2K_{a;1,\delta}$ into a form with potential

$$
a(a-1)z^{-2}\mathbf1_{\{z<1/(1+\delta)\}}.
$$

The Hardy inequality supplies the common form domain $H_0^1(0,1)$. The potential decreases as $\delta$ increases, proving that $\Lambda_a(\delta)$ is nonincreasing for every real $2\le a\le3$ and all $\delta\ge0$. It suffices to treat the physical interval $(0,5/4)$ at

$$
(a,E)=\left(2,\frac{25}{2}\right),\qquad
(a,E)=\left(3,\frac{61}{3}\right).
$$

No interpolated energy bound at other orders is asserted.

### One singular comparison family

Put

$$
A=2a+1,\quad \alpha=\frac EA,\quad
\beta=\frac{\alpha^2}{A+2},\quad
\gamma=\frac{2\alpha}{A+4},\quad c=\frac1{23},\quad
\theta=\frac{E}{(A+2)(A+4)}.
$$

Define

$$
H(t)=1-\gamma t-ct^2,\quad
Y(t)=\alpha+\frac{\beta t}{H(t)},\quad
w(z)=z^a\exp\left[-\frac12\int_0^{z^2}Y(t)\,dt\right].
$$

At both pairs, $H\ge83/207>0$ on $[0,1]$. Direct logarithmic differentiation gives

$$
\frac{(-\partial_z^2+a(a-1)z^{-2}-E)w}{w}
=\frac{\alpha^2z^6}{H(z^2)^2}
\left[\frac{c(A+6)}{A+2}-(\theta+cz^2)^2\right].
$$

The same two rational comparisons work for both orders:

$$
\theta+cz^2\le\frac{61}{297}+\frac1{23}<\frac14,
\qquad
\frac{c(A+6)}{A+2}\ge\frac{13}{207}
=\frac1{16}+\frac1{3312}.
$$

Thus the residual is strictly positive for $0<z\le1$. The endpoint behavior $w=z^a(1+O(z^2))$ gives finite form energy directly.

### The free piece and positive interface jump

Set $q=E/16$ and $p_q(x)=x(1-qx^2/12)^2$. On $0<x\le1$, $p_q>0$ and

$$
-p_q''-qp_q=\frac{q^2x^3}{144}(4-qx^2)>0.
$$

Glue the trace-one functions:

$$
g(z)=
\begin{cases}
w(z)/w(1),&0<z\le1,\\
p_q(5-4z)/p_q(1),&1\le z<5/4.
\end{cases}
$$

The coordinate $x=5-4z$ fixes the energy factor $q=E/16$, so both pieces use the same physical energy. The derivative jump is positive:

$$
J=g'(1^-)-g'(1^+)>0.
$$

Its exact values are $132681/834316$ for $a=2$ and $366943/31647780$ for $a=3$. The source proves each sign by two simpler positive rational margins. The comparison belongs to the form domain; no matching-derivative operator-domain assertion is made for it.

### Strictness on the full form domain

Let $V=a(a-1)z^{-2}\mathbf1_{(0,1)}$ and $\rho=[-g''+(V-E)g]/g$ on each open piece. The formulas give bounded $\rho>0$ almost everywhere. Piecewise integration by parts for a smooth compactly supported test function gives

$$
\begin{aligned}
\int_0^{5/4}(|u'|^2+(V-E)|u|^2)
={}&\int_0^{5/4}g^2|(u/g)'|^2\\
&+\int_0^{5/4}\rho|u|^2+J|u(1)|^2.
\end{aligned}
$$

After dropping the nonnegative square, form-core density, boundedness of $\rho$, and continuity of the interface trace extend the inequality to $H_0^1$. Its right side is positive for every nonzero function. Compact attainment then permits application to the first eigenfunction, yielding a strict spectral bound. Individual strict Rayleigh inequalities alone would not imply a strict infimum.

Scaling gives, on all $0\le\delta\le1/4$,

$$
\Lambda_2(\delta)>\frac{625}{32}>\frac{39}{2},\qquad
\Lambda_3(\delta)>\frac{1525}{48}>\frac{1587}{50}.
$$

The exact comparison margins are $1/32$ and $37/1200$. H.6 now cites only `def-high-operator`. Exact regular solutions, higher-order Gaussian seeds, adjacent-order chains, separated-spectrum estimates, and the cotangent interface response are no longer dependencies of H.6. H.5 retains its distinct required premises.

## 3. T.3: differentiate a positive rescaling of the original gap

**Source:** `workspace/terminal.qmd`, `lem-psi-payment`. **Derivation and audit:** `review/r4_terminal_proposal.md` and `review/r4_terminal_independent_audit.md`.

Keep the original head loss, majorant, and payment:

$$
S=\frac{2hN}{D-N},\quad
M=\frac9{2(h+2)}+\frac6{5(h+2)^2}-\frac1{9h},\quad
G=R_0-M,\quad R_0=Z_\Psi+S,
$$

with

$$
N=300h^3+1295h^2+1349h-96,\quad
D=2h(h+1)(h+2)^2(60h+127).
$$

The preceding proof gives $0<k=N/D<1/(h+1)<1$, so $D-N>0$. Define the positive linear rescaling

$$
\mathcal W(h)=\frac{15(h+2)^2(D-N)}{2h}(M-S).
$$

The report and checker call this same quantity $q(h)$; the manuscript uses $\mathcal W$ to distinguish it from the geometric short-tail coordinate. There is no squaring of the gap or loss of sign. Its unexpanded formula is

$$
\mathcal W=\frac{(395h^2+878h-40)(D-N)}{12h^2}-15(h+2)^2N.
$$

Three derivatives give

$$
\mathcal W'''(h)=\frac{7680}{h^5}-\frac{48804}{h^4}
+58071-12820h-33000h^2.
$$

For $h\ge3/8$, put $y=h^2$. Then

$$
h^4\mathcal W'''<-28324+y^2(59000-33000y).
$$

The scalar cubic has its global maximum at $y=118/99$:

$$
y^2(59000-33000y)\le\frac{821516000}{29403}<28000.
$$

Consequently $\mathcal W'''<-324/h^4<0$. On $[3/8,2]$,

$$
\mathcal W''(h)\ge\mathcal W''(2)=\frac{140594}{3}>45000.
$$

With $z=h-1/2$, the strong-convexity tangent yields

$$
\mathcal W(h)\ge\frac{5979}{32}-\frac{11609}{4}z+22500z^2
\ge\frac{134286119}{1440000}>90.
$$

On $[2,4]$, $\mathcal W'$ is strictly concave and $\mathcal W'(2)=537851/4>0$. Its positive superlevel set is an interval beginning at the left endpoint. Thus $\mathcal W$ first increases and may then decrease; its minimum is attained at an endpoint. The endpoint values $113604$ and $227460$ are positive, proving positivity on the remaining interval.

The positive rescaling gives $S<M$ everywhere on $[3/8,4]$. Since $M$ and $R_0$ are unchanged, the subsequent curvature proof is unchanged. In particular,

$$
Z_\Psi-G=M-S>0,\qquad
Z_\Psi>G>\frac{289}{136800}>\frac{27}{16000}
\quad\left(\frac38\le h\le4\right).
$$

This replaces the degree-seven squared-remainder identity and its degree-five auxiliary remainder. It is a longer calculus passage, but exposes the interval sign through derivatives. The original energy, both gains, the correction $1/[2(h+2)]$, and the final tangent are preserved.

## 4. R.4: one positive product bound removes the order split

**Source:** `workspace/robin.qmd`, `lem-pole-free`. **Derivation and audit:** `review/r4_pole_and_head_proposal.md` and Section 5 of `review/r4_noncrossing_independent_audit.md`.

Before checking $D>0$, the proof establishes $\sigma>1$, $r>3$, $C>\sigma+2$, $\theta\le4/5$, $T=3\Pi R\theta$, and $\sigma(\sigma-1)=\Pi R^2/2$. Since $\Pi<10$,

$$
\Pi R=\sqrt{2\Pi}\sqrt{\sigma(\sigma-1)}
<\frac92\left(\sigma-\frac12\right),\qquad
T<\frac{54}{5}\left(\sigma-\frac12\right).
$$

Thus

$$
\begin{aligned}
CD&=(2\sigma+1)C-T\\
&>(2\sigma+1)(\sigma+2)-\frac{54}{5}\left(\sigma-\frac12\right)\\
&=2\left(\sigma-\frac{29}{20}\right)^2+\frac{639}{200}>0.
\end{aligned}
$$

Because $C>0$, this proves $D>0$ without the split at $\sigma=4/3$. The argument is noncircular and includes the original domain, including $b=0$.

## 5. M.3: direct reciprocal estimates remove two fourth-degree sign arguments

**Source:** `workspace/monotonicity.qmd`, `lem-m34-identity` and `lem-q-branch-monotone`. **Derivation and audit:** `review/r4_pole_and_head_proposal.md` and Section 6 of `review/r4_noncrossing_independent_audit.md`.

For $h>3/8$, $L=1+h>11/8$ and $h+2>L$, so

$$
0<v_h=\frac3{2L^2}-\frac1{2(h+2)^2}<\frac3{2L^2}<\frac{96}{121}<1.
$$

This replaces the fourth-degree numerator proof of $1-v_h>0$ at both former occurrences. For $h\ge\sqrt2>4/3$, $L>7/3$ gives

$$
\frac{6R_1}{h+2}=\frac3{5(1-L^{-2})^2}<\frac{7203}{8000}<1,
$$

and hence $R_1<1/3+h/6$, replacing the other fourth-degree sign argument. The small-height derivative comparison and the one-sided assertion at $q=p$ are unchanged.

## Retained scope and verification

R3's regular-tail construction, direct tail and cotangent comparisons, M.5 and M.6 boundary arguments, common-tail curvature bound, and second terminal estimate remain in force. H.5 retains its full real-order crossing interval and exact constants. The retired trace-surrogate assertions are not reinstated. No additional external theorem has been introduced.

The four new R4 scripts contain 108 exact checks: 21 boundary, 47 noncrossing, 28 terminal, and 12 denominator/head checks. Each selected replacement has independent mathematical review of its interval implications and connection to the unchanged conclusion. The scripts check identities and scalar arithmetic without floating-point grids; execution is not a proof premise.

The current source has 18 QMD files, 58 declarations, and 55 linked proof blocks. All R3 declaration bodies and metadata, the parameter-definition files, and the four protected files are preserved. Current structural and rendering reports, statement comparison, and mathematical reviews are indexed in `review/README.md`.

Explicit rational identities, finite polynomial calculations, positive squares, and endpoint comparisons remain. The common-tail curvature proof and geometric foundations retain their stated analytic and classical inputs. R4 removes the particular constructions identified above, not all algebra from the project.

The strict settings remain `codex` / `gpt-6.1-sol` / `xhigh`, with assumptions forbidden. The official qmd-prover and Quarto executables were unavailable, so no official local verdict, global composition, or formal certification is claimed. The Pandoc/XeLaTeX manuscript and custom source checks are separate from that unavailable verification layer.
