# R4 terminal comparison: a differential proof of the unchanged majorant

**Status:** Integrated into `workspace/terminal.qmd` and independently reviewed. The manuscript denotes the weighted gap by `\mathcal W`; the equivalent symbol `q` is retained in this derivation record and its checker. Only the authorized proof passage for `S < M` was replaced. The declaration, original majorant, and subsequent curvature argument are unchanged. The R3 edition remains frozen.

## Scope and recommendation

The integrated change replaces only the proof of the strict head comparison `S < M` inside `lem-psi-payment` in `workspace/terminal.qmd`. It keeps the declaration, the height interval, the original variables and energies, the reciprocal majorant, and all subsequent curvature estimates unchanged. This replacement preserves the original conclusion

\[
Z_\Psi(h)>\frac{27}{16000},\qquad \frac38\le h\le4.
\]

The new argument uses a positive linear rescaling of the head gap, a negative third derivative, strong convexity on the lower interval, and concavity of the first derivative on the upper interval. It removes the current degree-seven numerator's squared-remainder identity and the associated degree-five remainder `H`. It is somewhat longer than that short algebraic identity, but its global sign mechanism is differential and independently auditable. Explicit finite algebraic identities still occur; no sampled signs or executable certificate is a premise.

## 1. Hypotheses and the exact positive rescaling

Throughout, let

\[
\frac38\le h\le4,\qquad L=h+1,
\]

and retain the original head quantities

\[
N=300h^3+1295h^2+1349h-96,
\qquad D=2hL(h+2)^2(60h+127),\qquad k=\frac ND.
\]

The opening part of `lem-psi-payment` has already established

\[
0<k<\frac1L<1.
\]

Thus `D > 0` and `D-N = D(1-k) > 0`. In particular, all denominators below are positive. Keep precisely the same head loss and majorant as in R3:

\[
S(h)=\frac{2hk}{1-k}=\frac{2hN}{D-N},
\qquad
M(h)=\frac9{2(h+2)}+\frac6{5(h+2)^2}-\frac1{9h}.
\]

Define the weighted gap directly by

\[
q(h)=\frac{15(h+2)^2(D-N)}{2h}\,[M(h)-S(h)].
\tag{R4.T.1}
\]

This is a **positive linear rescaling**, not a square. There is no sign ambiguity, and the exact inverse relation is

\[
M-S=\frac{2h}{15(h+2)^2(D-N)}q.
\tag{R4.T.2}
\]

For direct differentiation, combining the three terms of `M` gives the unexpanded formula

\[
q(h)=\frac{(395h^2+878h-40)(D-N)}{12h^2}
-15(h+2)^2N.
\tag{R4.T.3}
\]

Formula (R4.T.3) is rational and smooth for `h > 0`. Neither an expanded degree-seven numerator nor the old auxiliary polynomial `H` is needed.

## 2. A global negative third derivative

Differentiating (R4.T.3) three times gives

\[
q'''(h)=\frac{7680}{h^5}-\frac{48804}{h^4}
+58071-12820h-33000h^2.
\tag{R4.T.4}
\]

For `h >= 3/8`, the reciprocal term obeys `7680/h <= 20480`. Therefore

\[
\begin{aligned}
h^4q'''(h)
&=\frac{7680}{h}-48804
+h^4(58071-12820h-33000h^2)\\
&<-28324+h^4(59000-33000h^2).
\end{aligned}
\tag{R4.T.5}
\]

The strict inequality uses `58071-12820h < 59000`. Set `y=h^2`. The scalar cubic

\[
g(y)=y^2(59000-33000y),\qquad y\ge0,
\]

has derivative

\[
g'(y)=y(118000-99000y).
\]

Hence it increases up to `y=118/99` and decreases afterwards, so

\[
g(y)\le \frac{4\cdot59000^3}{27\cdot33000^2}
=\frac{821516000}{29403}<28000.
\tag{R4.T.6}
\]

Equations (R4.T.5) and (R4.T.6) imply

\[
q'''(h)<-\frac{324}{h^4}<0
\qquad(h\ge3/8).
\tag{R4.T.7}
\]

In particular, `q''` is strictly decreasing and `q'` is strictly concave throughout the required height interval.

## 3. Strong convexity on the lower interval

On `3/8 <= h <= 2`, monotonicity of `q''` gives

\[
q''(h)\ge q''(2)=\frac{140594}{3}>45000.
\tag{R4.T.8}
\]

The exact value and slope at `h=1/2` are

\[
q(1/2)=\frac{5979}{32},\qquad
q'(1/2)=-\frac{11609}{4}.
\tag{R4.T.9}
\]

The function `q(h)-22500(h-1/2)^2` is strictly convex on this interval. Its tangent at `1/2` lies below its graph, so, with `z=h-1/2`,

\[
\begin{aligned}
q(h)
&\ge\frac{5979}{32}-\frac{11609}{4}z+22500z^2\\
&\ge\frac{5979}{32}-\frac{(11609/4)^2}{90000}
=\frac{134286119}{1440000}>90.
\end{aligned}
\tag{R4.T.10}
\]

This proves positivity on the entire lower interval, including both endpoints.

## 4. Concavity of the derivative on the upper interval

The exact initial slope is

\[
q'(2)=\frac{537851}{4}>0.
\tag{R4.T.11}
\]

Since `q'` is concave on `[2,4]`, its positive superlevel set is an interval containing `2`. More explicitly, if `2 < u < v <= 4` and `q'(v)>0`, concavity applied to `u` as a convex combination of `2` and `v` yields `q'(u)>0`. Once `q'` becomes nonpositive, it therefore cannot become positive again. Consequently `q` first increases and may then decrease; it cannot have an interior minimum below both endpoint values.

The exact endpoint values are

\[
q(2)=113604>0,\qquad q(4)=227460>0.
\tag{R4.T.12}
\]

Thus

\[
q(h)\ge\min\{q(2),q(4)\}=113604>0,
\qquad 2\le h\le4.
\tag{R4.T.13}
\]

Together with (R4.T.10), this proves `q>0` on `[3/8,4]`. The positive factor in (R4.T.2) now gives

\[
S(h)<M(h),\qquad \frac38\le h\le4.
\tag{R4.T.14}
\]

## 5. Preservation of the original payment and strict margin

Retain the original response `R_0=Z_\Psi+S` and the same function `G=R_0-M`. Their identity is unchanged:

\[
Z_\Psi-G=M-S>0.
\]

No head energy or shared tail energy has been changed. In particular, the six partial-fraction constants in (T.3.1), the subsequent normalized curvature function `Q`, and the gain and affine-tail bounds retain their exact meanings.

The unchanged remainder of the R3 proof establishes

\[
G''(h)>-\frac1{(h+2)^3}\quad(3/8\le h\le4),
\qquad G''(h)>0\quad(3/2\le h\le4),
\]

using the same majorant `M`. It also has the exact scalar bounds

\[
G(1)=\frac{208251137}{16401600000}>\frac1{80},\qquad
-\frac1{400}<G'(1)=-\frac{42620371163}{18402595200000}<0,
\]

\[
G'(3/2)=\frac{5115313959269}{1118040013125000}>0.
\]

For clarity, the global propagation is as follows. The function `G+1/[2(h+2)]` is strictly convex, so its tangent at `h=1` gives

\[
G(h)\ge G(1)+G'(1)(h-1)-\frac{(h-1)^2}{18(h+2)}.
\]

On `[3/8,3/2]`, the linear loss is at most `1/800`. The derivative of `(h-1)^2/(h+2)` is `(h-1)(h+5)/(h+2)^2`, so its maximum on this interval occurs at an endpoint, and its contribution after division by `18` is at most `25/2736`. Thus

\[
G(h)>\frac1{80}-\frac1{800}-\frac{25}{2736}
=\frac{289}{136800}>\frac{27}{16000}.
\]

Above `3/2`, the positive second derivative and the positive slope at `3/2` make `G` increasing, extending that strict margin to `h=4`. Hence the new differential comparison proves precisely the needed full-range conclusion

\[
Z_\Psi(h)>G(h)>\frac{289}{136800}>\frac{27}{16000},
\qquad \frac38\le h\le4.
\]

The declaration of `lem-psi-payment` can remain unchanged. Its earlier strict head and gain comparisons still imply the displayed terminal bound with `Z_\Psi/h`.

## 6. Exact corroboration, remaining scope, and unsuccessful routes

`check_r4_terminal.py` uses the existing `rational_algebra.py` and Python `Fraction` to verify the displayed rescaling and derivative identities, the scalar cubic maximum and comparisons, the tangent data, the upper endpoint data, and compatibility with the original response. Its output is `r4_terminal_exact_checks.json`. These calculations corroborate the written formulas; they do not prove the interval sign by sampling and are not proof premises.

The global curvature argument for `G` is intentionally retained. This candidate does not claim to remove all rational coefficients or every finite polynomial identity in T.3. The result is a structural replacement of the remaining high-degree sign argument for the actual head-majorant gap.

Exploration of a simpler majorant of the form `5h/(h^2+b h+c)` did not produce a usable replacement: choices close enough to the original head at low heights consumed the existing payment margin in the middle heights. An inversion of `S` exposed a rational response with suggestive convexity, but its available lower bounds introduced more poles and scalar comparisons than the present derivative proof. Neither route is asserted as a theorem or used in this derivation.

The complete R4 `AGENTS.md` and strict configuration were read before this work. The external-basis file is absent. No configuration, protected declaration, original parameter definition, or frozen earlier edition has been changed. Official `qmd-prover` and Quarto are unavailable in this environment; this report makes no official semantic or formal-verification claim.
