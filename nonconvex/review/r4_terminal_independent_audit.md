# Independent audit of the R4 terminal calculus replacement

## Verdict and scope

**Pass: no mathematical correction is required.** The proposal in `review/r4_terminal_proposal.md` was checked against the current `lem-psi-payment` statement and complete proof in `workspace/terminal.qmd`. The replacement concerns only the comparison of the actual head loss with the existing majorant. It preserves the entire interval $3/8\le h\le4$, all response definitions, the shared energy, and the strict declared margin $27/16000$.

No QMD source was edited during this audit. The project remains under its existing strict configuration; qmd-prover and Quarto are unavailable on PATH, so this review is not an official verifier verdict. For independent corroboration, the third derivative and endpoint data were recomputed with a separate standard-library Laurent-polynomial implementation using `Fraction`, rather than the author's `rational_algebra.py`. The interval arguments below are analytic and do not rely on executing that computation.

## 1. Positive rescaling and the exact original gap

The current proof has already established $0<k=N/D<1/L<1$, with $h>0$ and $D>0$. Thus $D-N>0$. The prefactor
$$
\frac{15(h+2)^2(D-N)}{2h}
$$
is strictly positive throughout the closed height interval. The definition of $q(h)$ is linear in $M-S$, so its positivity proves the sign of the actual gap without squaring or changing the majorant.

Combining the three terms of the unchanged $M$ gives
$$
\frac{15(h+2)^2}{2h}M
=\frac{405h(h+2)+108h-10(h+2)^2}{12h^2}
=\frac{395h^2+878h-40}{12h^2}.
$$
Also, multiplication of $S=2hN/(D-N)$ by the prefactor gives exactly $15(h+2)^2N$. This independently verifies the unexpanded formula for $q$. Equivalently, the new $q$ is the old gap numerator divided by $12h^2$, which is positive. The exact inverse relation
$$
M-S=\frac{2h}{15(h+2)^2(D-N)}q
$$
has the correct factor and sign.

## 2. Third derivative and the global maximum bound

Independent differentiation recovers exactly
$$
q'''(h)=\frac{7680}{h^5}-\frac{48804}{h^4}
+58071-12820h-33000h^2.
$$
For $h\ge3/8$, $7680/h\le20480$ and $58071-12820h<59000$. Multiplication by $h^4>0$ therefore gives
$$
h^4q'''<-28324+h^4(59000-33000h^2).
$$
With $y=h^2\ge0$, the remaining term is $g(y)=y^2(59000-33000y)$. Its derivative $g'(y)=y(118000-99000y)$ changes from positive to negative at $118/99$, so this is the global maximum on $y\ge0$. Its exact value and gap are
$$
g(118/99)=\frac{821516000}{29403},\qquad
28000-g(118/99)=\frac{1768000}{29403}>0.
$$
Thus $q'''<-324/h^4<0$ for every $h\ge3/8$. This is a global differential estimate; it does not use a finite sampling grid or a sign table for the former degree-seven numerator.

## 3. Strong convexity for $3/8\le h\le2$

Because $q'''<0$, the function $q''$ decreases. The independently checked endpoint value is
$$
q''(2)=\frac{140594}{3}>45000.
$$
It follows that $q(h)-22500(h-1/2)^2$ has positive second derivative everywhere on the lower interval. The tangent point $h=1/2$ lies inside that interval, and its exact data are
$$
q(1/2)=\frac{5979}{32},\qquad q'(1/2)=-\frac{11609}{4}.
$$
Consequently the proposed quadratic lower bound follows from ordinary convexity. Completing its square gives
$$
q(h)\ge\frac{134286119}{1440000}>90,
$$
with exact excess over $90$ equal to $4686119/1440000$. The same estimate covers both endpoints $3/8$ and $2$; no omitted endpoint limit is needed.

## 4. Concavity of the derivative for $2\le h\le4$

The independently recovered values are
$$
q'(2)=\frac{537851}{4}>0,
\qquad q(2)=113604,
\qquad q(4)=227460.
$$
Since $(q')''=q'''<0$, the derivative $q'$ is concave. The proposal correctly uses concavity of the derivative, rather than asserting that $q$ itself is concave on this interval.

For an explicit check of the no-minimum implication, suppose $2<u<v\le4$ and $q'(v)>0$. Writing $u$ as a strict convex combination of $2$ and $v$ gives $q'(u)>0$. Therefore a nonpositive derivative at an interior point cannot be followed by a positive derivative later. The derivative is positive from the left endpoint until a possible transition, and is nonpositive thereafter. The function first increases and may then decrease, so its minimum is attained at an endpoint. This proves
$$
q(h)\ge\min\{q(2),q(4)\}=113604>0
\qquad(2\le h\le4).
$$
Combined with the preceding interval, $q>0$ holds on the full required range. The positive inverse factor now proves $S<M$ everywhere on that range.

## 5. Preservation of the terminal payment

The proposal uses exactly the same $S$, $M$, $R_0=Z_\Psi+S$, and $G=R_0-M$ as the current proof. Hence
$$
Z_\Psi-G=M-S>0.
$$
No energy substitution or coefficient in the retained reciprocal form changes. The previously established curvature bounds for $G$ consequently remain applicable without modification.

The retained convex correction $G+1/[2(h+2)]$ yields
$$
G(h)\ge G(1)+G'(1)(h-1)-\frac{(h-1)^2}{18(h+2)}.
$$
The reciprocal remainder has the correct sign and coefficient. On $[3/8,3/2]$, the linear loss is at most $1/800$, and the remainder is at most $25/2736$. Together with $G(1)>1/80$, this gives
$$
G(h)>\frac{289}{136800}>\frac{27}{16000}.
$$
The retained inequalities $G''>0$ and $G'(3/2)>0$ make $G$ increasing on $[3/2,4]$, extending the same strict lower bound. Thus the new head-gap proof preserves the full original declaration and the final comparison with $Z_\Psi/h$.

## Integration note

The proposal currently uses backslash-bracket display delimiters. These should be converted to the project's required double-dollar display delimiters during QMD integration. This is a formatting issue in the proposal, not a mathematical gap, and was reported to the author before integration. The surrounding strict head and gain estimates and the subsequent curvature proof should remain unchanged.

## Integrated-source follow-up

**Pass.** The integrated passage in `workspace/terminal.qmd`, from the weighted-gap definition after $M$ through the conclusion preceding “A uniform curvature bound,” was read directly. The manuscript symbol $\mathcal W$ replaces the proposal's $q$ consistently. Its positive rescaling and inverse relation, third derivative, global cubic maximum, strong-convexity tangent, all exact scalar data, upper-interval concave-derivative argument, and final implication $S<M$ are the audited formulas and arguments.

The source uses the required double-dollar display delimiters. The unchanged $G=R_0-M$ is linked explicitly by $Z_\Psi>G$, and the retained curvature proof begins immediately afterward. The transfer introduces no altered hypothesis, sign ambiguity, omitted endpoint, or mathematical gap. No source correction is required.
