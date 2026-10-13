# English translation and structural terminal comparison

Date: 12 October 2026.

## Scope and verification setting

The assigned files were `workspace/monotonicity.qmd`, `workspace/terminal.qmd`, `workspace/constants.qmd`, and `workspace/algebra-definitions.qmd` in the English working project. The project instructions and current verification configuration were independently read before work. The external-basis file is absent. The preserved configuration is Codex, gpt-6.1-sol, xhigh, with strict citations, strict rigor, strict refutation rigor, and assumptions forbidden.

No qmd-prover, Quarto, or Codex verification executable was available for this work. The checks reported below are mathematical reading and supplementary exact rational calculations, not qmd-prover certification. No protected statement or lock was edited. The earlier Chinese project was left unchanged.

## 1. Translation completed before mathematical revision

All Chinese exposition, titles, and semantic names in the four assigned files were translated into mathematical English. Stable declaration IDs, proof associations, imports, exports, and formulas were preserved during this first phase.

An extraction comparison counted 720 mathematical fragments:

| File | Mathematical fragments | Result of the translation comparison |
|---|---:|---|
| algebra-definitions.qmd | 20 | Identical formulas in identical order |
| constants.qmd | 27 | Identical formulas in identical order |
| terminal.qmd | 237 | Identical formula multiset; local inline order adjusted for English syntax |
| monotonicity.qmd | 436 | Identical formula multiset; local inline order adjusted for English syntax |

The record is `review/translation_formula_checks.json`. A final scan found no remaining Chinese characters in these four files. The formula-preservation record refers to the translation phase; the structural mathematical change described next was made afterwards and is explicitly identified.

## 2. New structural replacement of the common-tail quintic

The original proof of the common affine tail bound cleared denominators to a polynomial of degree five, then used its third derivative and several large endpoint values. That polynomial and its derivative table have now been removed from `lem-common-tail-line`.

The replacement proves a quantitative statement directly for the continued-fraction response:

\[
\mathcal D(\tau)>\frac1{v(h)}+\frac1{2000},
\qquad \frac38\le h\le4,\quad 0\le\tau\le T_0(h).
\]

This is stronger than the denominator comparison previously required for the affine tail estimate. The same height interval, the same energy interval, and the same original functions are retained.

### Compact height coordinate and the original response

Set

\[
x=\frac h{h+2}\in[3/19,2/3],\qquad
\kappa=\frac{2961}{50},\qquad\gamma=\frac{13\kappa}{10},
\]

\[
b(x)=\frac{803}{125}+\frac{21x}{10},\qquad
c(x)=\frac{1053}{125}+\frac{21x}{10},
\]

and

\[
W(x)=(1+x)b(x)-\frac{\gamma x^2}{c(x)}.
\]

The original continued fraction becomes

\[
\widehat D(x)=\mathcal D_h(T_0(h))
=\frac{553}{125}+\frac{21x}{10}-\frac{\kappa x^2}{W(x)}.
\]

Moreover, \(W=(1+x)\mathcal C_h(T_0)>0\). Its positivity has already been proved in the initial common-denominator argument, before any derivative or division is used.

### A curvature estimate without a high-degree expansion

Elementary rational comparisons imply

\[
W''<0,\qquad
W-xW'>U(x):=\frac{32}{5}+\frac92x^2,
\]

\[
0<W(x)<V(x):=\frac{13}{2}+\frac{43}{5}x-\frac{57}{10}x^2.
\]

The function \(U^{2/3}\) is strictly convex. Its tangent at \(x_*=4/(3\sqrt5)\), where \(U(x_*)=8\), gives

\[
\frac52 U(x)^{2/3}\ge\frac{22}{3}+2\sqrt5\,x.
\]

The simple square identity

\[
\frac{22}{3}+\frac{22}{5}x-V(x)
=\frac{57}{10}\left(x-\frac7{19}\right)^2+\frac{17}{285}>0
\]

and \(\sqrt5>11/5\) consequently show

\[
V(x)<\frac52U(x)^{2/3}.
\]

Now use the exact differential identity

\[
\left(\frac{\kappa x^2}{W}\right)''
=\kappa\left\{\frac{2(W-xW')^2}{W^3}-\frac{x^2W''}{W^2}\right\}.
\]

It follows that

\[
\left(\frac{\kappa x^2}{W}\right)''
>\frac{2\kappa U^2}{V^3}
>\frac{16\kappa}{125}
=\frac{23688}{3125}>\frac{15}{2}.
\]

Therefore the actual tail response satisfies the uniform strong-concavity estimate

\[
\widehat D''(x)<-\frac{15}{2}.
\]

This is the structural step: a quadratic divided by a positive concave function is controlled through an exact curvature identity and one convex tangent. No polynomial of degree five, six, or higher is expanded to prove this estimate.

### Comparison with the fractional-linear threshold

The threshold is

\[
g(x)=\frac1v=\frac{67(1-x)}{2(7-5x)}.
\]

Let \(\xi_0=3/19\), \(\xi_1=2/3\), let \(\ell_f\) be the affine endpoint interpolant, and write

\[
\omega(x)=(x-\xi_0)(\xi_1-x).
\]

Strong concavity gives

\[
\widehat D\ge\ell_{\widehat D}+\frac{15}{4}\omega.
\]

The threshold has the exact chord remainder

\[
g-\ell_g
=\frac{335\omega}{(7-5\xi_0)(7-5\xi_1)(7-5x)},
\]

whose coefficient is at most \(57285/14278<201/50\).

Direct substitution into the continued fraction proves

\[
\widehat D(\xi_0)>4561/1000,\qquad
\widehat D(\xi_1)>307/100.
\]

These give endpoint gaps strictly larger than \(37/2000\). Finally,

\[
0\le\omega\le\frac{841}{12996}<\frac1{15},
\]

so throughout the entire interval

\[
\widehat D-g
>\frac{37}{2000}-\frac{27}{100}\omega
>\frac1{2000}.
\]

The already-established monotonicity of \(\mathcal D(\tau)\) in \(\tau\) then gives the asserted uniform denominator gap for every \(0\le\tau\le T_0\). Substitution proves the original strict affine tail bound.

## 3. What was retained

The earlier structural replacement of M.3.4 remains intact in English: its single rational derivative comparison gives the uniform lower bound \(321929/15162000\), without the former degree-thirteen coefficient expansion. The M.6.7 convexity argument and the integral-remainder proof of the rational constants also remain intact.

The T.3 four-part factorization and the T.4 factorization of degree six remain in the proof. They were already explicit purely analytic identities, and this phase does not claim to have replaced them. Their common tail input is now supplied by the new response-curvature argument. In particular, all downstream definitions and both terminal parameter curves keep exactly the same shared-energy coupling.

## 4. Exploratory routes not used

Direct differentiation of the fully cleared rational expressions led to high-degree numerators with mixed coefficients. That route was not used because it would replace one finite polynomial calculation with a larger one.

Attempts to bound the head and tail energies independently were not adopted: such estimates lose the shared-energy information that makes the terminal inequalities sharp. The successful argument works with the original continued fraction at its common maximal comparison energy and compares its curvature with the exact threshold chord remainder.

No numerical curvature observation, sampled sign, or unsuccessful intermediate bound is included as a premise of the final QMD proof.

## 5. Supplementary exact checks

`review/check_tail_curvature.py` uses Python standard-library Fraction arithmetic and an exact rational-function implementation. All 25 checks passed. They include:

- the compact-coordinate transformation of the energy, common denominator, and original response;
- the two exact derivatives of W and the three scalar rational bounds;
- the tangent quadratic remainder;
- the exact second derivative of a quadratic divided by W;
- the fractional-linear chord remainder and its coefficient bound;
- both continued-fraction endpoint differences;
- the interval-length estimate and the final uniform-gap arithmetic.

The detailed output is `review/tail_curvature_exact_checks.json`. These calculations are optional reproductions of identities stated in the proof; the mathematical argument does not depend on running the script. They are not official qmd-prover verification.
