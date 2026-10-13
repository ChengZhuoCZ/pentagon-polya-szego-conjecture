# Independent audit of the R4 H.6 comparison and R.4 denominator replacement

## Result and scope

**Pass: no mathematical correction is required in either proposed replacement.** This audit independently checks `review/r4_noncrossing_proposal.md` against the current declaration and operator definition in `workspace/high.qmd`, and checks the root agent's proposed uniform denominator argument against the current pole-free proof in `workspace/robin.qmd`. No QMD source was edited.

The R4 project instructions, strict configuration, and absent external-basis file were independently checked. The configured verifier is Codex / `gpt-6.1-sol` / `xhigh`, with strict citations, rigor and disproof rigor and assumptions forbidden. qmd-prover and Quarto are unavailable on PATH. The conclusions below are mathematical review, not an official verifier verdict. Exact scalar arithmetic was independently recomputed using Python's `Fraction`; the proof does not depend on that execution.

## 1. H.6 declaration and domain

The proposal preserves every part of the current `lem-no-crossing-sturm` statement:

- For every real $2\le a\le3$, the function $\Lambda_a(\delta)=(1+\delta)^2\lambda_1(K_{a;1,\delta})$ is nonincreasing on all $\delta\ge0$.
- The two strict bounds for the orders $a=2,3$ hold throughout $0\le\delta\le1/4$ with the same constants $625/32$ and $1525/48$.
- No assertion at an interpolated energy for an intermediate order is introduced.

Under $v(z)=(1+\delta)^{1/2}u((1+\delta)z)$, the potential in the form of $(1+\delta)^2K_{a;1,\delta}$ becomes
$$
a(a-1)z^{-2}\mathbf 1_{\{z<1/(1+\delta)\}}.
$$
All forms have domain exactly $H_0^1(0,1)$ by the existing Hardy estimate. The cutoff shrinks as $\delta$ increases and $a(a-1)>0$, so the potential decreases pointwise. The Rayleigh comparison therefore has the correct monotonicity direction. In particular, a strict bound at $\delta=1/4$ gives the same strict bound for every smaller $\delta$, including zero.

## 2. Independent derivation of the singular residual

Retain the proposal's notation
$$
A=2a+1,\quad \alpha=E/A,\quad
\beta=\alpha^2/(A+2),\quad
\gamma=2\alpha/(A+4),\quad c=1/23,
$$
$$
H(t)=1-\gamma t-ct^2,\qquad Y(t)=\alpha+\beta t/H(t),
\qquad \theta=E/((A+2)(A+4)).
$$
For the explicitly defined function $w=z^a\exp[-\tfrac12\int_0^{z^2}Y(t)\,dt]$, direct logarithmic differentiation gives
$$
\frac{(-\partial_z^2+a(a-1)z^{-2}-E)w}{w}
=AY+2tY'-tY^2-E,\qquad t=z^2.
$$
To check the factorization independently, use $Y'=\beta(1+ct^2)/H^2$ and write $d=\alpha\gamma-\beta$. Multiplying the residual by $H^2$ gives
$$
t\{A\beta H+2\beta(1+ct^2)-\alpha^2H^2-2\alpha\beta tH-\beta^2t^2\}.
$$
The constant and linear terms inside braces vanish because $(A+2)\beta=\alpha^2$ and $(A+4)\gamma=2\alpha$. The remainder is exactly
$$
t^3\{\beta c(A+6)-(d+\alpha ct)^2\}.
$$
Also $d=\alpha^2 A/((A+2)(A+4))=\alpha\theta$. This proves the stated factored residual, with its powers of $t$, signs and constants unchanged.

At the two parameter pairs, $\gamma=5/9$ or $122/231\le5/9$. Since $0\le t\le1$,
$$
H(t)\ge1-5/9-1/23=83/207>0.
$$
The maximum of the two values of $\theta$ is $61/297$, while the minimum of $c(A+6)/(A+2)$ is $13/207$. The exact gaps are
$$
1/4-61/297-1/23=31/27324>0,
\qquad 13/207-1/16=1/3312>0.
$$
Thus the bracket in the residual is strictly greater than $1/3312$ throughout $0\le t\le1$, and the full residual is positive for $z>0$. The endpoint asymptotics of $w$ follow directly from the bounded smooth function $Y$ near $t=0$; no existence, uniqueness or positivity claim about an exact ODE solution is being imported.

## 3. Free polynomial, physical energy and interface sign

For $p_q(x)=x(1-qx^2/12)^2$, independent differentiation gives
$$
-p_q''-qp_q=\frac{q^2x^3}{144}(4-qx^2),
\qquad \frac{p_q'(1)}{p_q(1)}=1-\frac{q}{3-q/4}.
$$
Both values $q=25/32,61/48$ are in $(0,4)$, so the polynomial is positive for $0<x\le1$ and its differential residual is strictly positive there.

The coordinate $x=5-4z$ maps the free physical interval $(1,5/4)$ to $(1,0)$. Therefore $\partial_z=-4\partial_x$, $-\partial_z^2=-16\partial_x^2$, and the energy must be $q=E/16$. This is exactly the proposal's scaling. At the interface the free physical derivative is negative:
$$
g'(1^+)=-4p_q'(1)/p_q(1).
$$
The singular derivative is $g'(1^-)=a-\alpha-\beta/H(1)$. Independently recomputed endpoint values are:

| Order and energy | Singular derivative $D_a$ | Free outward derivative $F_a=-g'(1^+)$ | Sum $D_a+F_a$ |
| --- | --- | --- | --- |
| $a=2$, $E=25/2$ | $-6337/2324$ | $1036/359$ | $132681/834316>0$ |
| $a=3$, $E=61/3$ | $-128635/61452$ | $1084/515$ | $366943/31647780>0$ |

The proposal's smaller componentwise margins also check exactly: $27/1162$, $195/1436$, $2071/307260$ and $1/206$. Hence $J=g'(1^-)-g'(1^+)>0$, with the correct sign for a positive contribution to the quadratic form.

## 4. Form domain, identity and strictness

The glued function is continuous with common trace one at the interface, positive in the interior, and zero at both outer endpoints. Its behavior is $O(z^a)$ at the singular endpoint and linear at the free endpoint. Consequently it belongs to $H_0^1(0,5/4)$ and has finite potential energy. Its nonzero derivative jump does not prevent form-domain membership. The proposal correctly avoids placing it in the operator domain, whose interface derivatives must match.

On each open piece, put $\rho=(-g''+(V-E)g)/g$. The singular formula extends boundedly to zero with value zero. On the free piece, direct division yields
$$
\rho=\frac{q^2x^2(4-qx^2)}{9(1-qx^2/12)^2}.
$$
This is also bounded, positive in the open piece, and zero at its outer endpoint. Thus $\rho\in L^\infty$ and $\rho>0$ almost everywhere on the complete interval.

For a compactly supported smooth test function, separate integration by parts gives the interface term
$$
\frac{g'(1^-)}{g(1)}|u(1)|^2-
\frac{g'(1^+)}{g(1)}|u(1)|^2=J|u(1)|^2.
$$
This confirms the plus sign in the proposed ground-state identity. After dropping its nonnegative square integral, Hardy form-core density, the bounded residual, and continuity of the one-dimensional trace extend the inequality to the whole form domain. No endpoint quotient limit for an arbitrary $H_0^1$ function is required.

For every nonzero function, $\int\rho|u|^2>0$. The compact form embedding supplies an actual minimizing first eigenfunction, so applying the inequality to that function yields a strict spectral bound. The proposal explicitly includes this attainment step and does not incorrectly infer a strict infimum merely from pointwise positivity of all individual Rayleigh quotients.

Separate Dirichlet spectral bounds, exact regular solutions and pole-free response assumptions are genuinely unnecessary in this whole-interval argument. Multiplication by $25/16$ gives the original constants. The final differences $1/32$ and $37/1200$ are correct.

**Integrated-source follow-up.** The completed H.6 proof in `workspace/high.qmd` was subsequently read directly. It preserves the audited factorization, parameter inequalities, physical gluing, positive jump, bounded residual, core extension and compact-attainment argument. Its remaining direct semantic dependency on `def-high-operator` supplies the stated operator, common form domain and compactness. The unused recurrence import can be removed without affecting H.5, which retains its separate imports. The transfer introduces no mathematical gap.

## 5. Uniform R.4 denominator replacement

The current pole-free proof has already established, without using $D>0$,
$$
\sigma>1,\qquad r>3,\qquad C>\sigma+2,
\qquad 0<\theta\le4/5,
$$
$$
T=3\Pi R\theta,\qquad
\sigma(\sigma-1)=\Pi R^2/2,\qquad \Pi<10.
$$
Because $R>0$ and $\sigma>1$,
$$
\Pi R=\sqrt{2\Pi}\sqrt{\sigma(\sigma-1)}
<\frac92\left(\sigma-\frac12\right).
$$
Here $\sqrt{2\Pi}<\sqrt{20}<9/2$, and the second square-root comparison follows from $(\sigma-1/2)^2-\sigma(\sigma-1)=1/4$. All factors are positive. Therefore
$$
T<\frac{54}{5}\left(\sigma-\frac12\right).
$$
Multiplying $C>\sigma+2$ by $2\sigma+1>0$ and using $CD=(2\sigma+1)C-T$ gives
$$
\begin{aligned}
CD&>(2\sigma+1)(\sigma+2)-\frac{54}{5}(\sigma-1/2)\\
&=2\sigma^2-\frac{29}{5}\sigma+\frac{37}{5}\\
&=2\left(\sigma-\frac{29}{20}\right)^2+\frac{639}{200}>0.
\end{aligned}
$$
Since $C>0$, this proves $D>0$ uniformly. The completion of the square checks exactly. The proof is not circular: the preceding proof of $r>3$ uses the already established energy bound $T<\Pi(2\sigma+1)/3$ and $\sigma>1$, not positivity of $D$.

This replacement therefore removes the two order cases without changing any declaration, domain, endpoint convention, or pole-free spectral conclusion.

## 6. Integrated M.3 reciprocal reductions

**Pass.** The current `lem-m34-identity` and `lem-q-branch-monotone` proofs in `workspace/monotonicity.qmd` were checked directly against `review/r4_pole_and_head_proposal.md`. Both new estimates are valid on the full ranges where the source uses them.

For every $h>3/8$, $L=1+h>11/8$ and $h+2>L$. Therefore
$$
0<\frac3{2L^2}-\frac1{2(h+2)^2}
<\frac3{2L^2}<\frac32\left(\frac8{11}\right)^2
=\frac{96}{121}<1.
$$
This directly supplies both the sign of $v_h$ and the strict positivity of $1-v_h$. It also covers $h=\sqrt2$, which belongs to the closed upper endpoint of the auxiliary lemma. The existing bound $y=L^{-2}<4/5$ separately keeps the denominator $1-5y/4$ positive. No fourth-degree numerator estimate is needed for either denominator.

For the other height branch, $h\ge\sqrt2>4/3$ implies $L>7/3$, hence
$$
1-L^{-2}>1-\frac9{49}=\frac{40}{49}>0.
$$
Using $h(h+2)=L^2-1$ and the unchanged definition of $R_1$,
$$
\frac{6R_1}{h+2}
=\frac{3L^4}{5h^2(h+2)^2}
=\frac3{5(1-L^{-2})^2}
<\frac3{5(40/49)^2}
=\frac{7203}{8000}<1.
$$
Every reciprocal comparison uses a positive denominator. Multiplication by $(h+2)/6>0$ therefore gives exactly the required $R_1<1/3+h/6$, with strictness also at $h=\sqrt2$.

These changes leave the small-height derivative comparison, the selection between $R_1$ and $R_2$, the admissible interval of $q$, and the left-derivative assertion at $q=p$ intact. They add no external premise and do not change either declaration. No source correction is needed.
