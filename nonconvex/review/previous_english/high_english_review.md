# English translation and new high-height comparison

## Scope and verification status

This review covers `workspace/high.qmd` and `workspace/analytic.qmd` in the English project only. The Chinese analytic project and the original uploaded project were not changed. The project contract, strict configuration, and external-result policy were read before editing. The protected goals and their locks were not edited.

The official qmd-prover, Quarto, and Codex CLI verification commands are unavailable in this environment. The checks reported here are independent mathematical and static checks; they are not an official strict-verification result.

## Translation

All Chinese exposition, headings, semantic names, and table labels in the two owned files were translated into mathematical English. At the translation checkpoint, all inline formulas were identical to those in the Chinese analytic edition. All 114 displayed formula blocks were also identical, except for the English translation of two textual table headings. Semantic IDs, imports, and proof structure were preserved at that checkpoint.

The subsequent mathematical edit intentionally changes one auxiliary statement and its use. Its new semantic ID is `lem-no-crossing-sturm`, replacing the old `lem-no-crossing-endpoints`. The new proof imports the already established adjacent-order recurrence `lem-tail-recurrence` from `robin.qmd`.

## New structural result in this edition

The noncrossing branch now has direct lower bounds for the first eigenvalue. For

\[
\Lambda_\sigma(\delta)=(1+\delta)^2\lambda_1(K_{\sigma;1,\delta}),
\]

one has, uniformly for \(0\le\delta\le1/4\),

\[
\Lambda_2(\delta)>\frac{625}{32}>\frac{39}{2},
\qquad
\Lambda_3(\delta)>\frac{1525}{48}>\frac{1587}{50}.
\]

The proof uses positive comparison functions and the variational interface criterion. It does not evaluate either trace polynomial at an endpoint.

### 1. Monotonicity and absence of poles

Scaling to the unit interval gives the potential

\[
\frac{\sigma(\sigma-1)}{z^2}
\mathbf1_{\{z<1/(1+\delta)\}}.
\]

It decreases with \(\delta\), and Hardy's inequality gives the common form domain \(H_0^1(0,1)\). Thus min--max makes \(\Lambda_\sigma\) nonincreasing, reducing the uniform bound to \(\delta=1/4\).

The elementary inequality \(1-x\cot x>x^2/3\) follows by differentiating \(\sin x-x\cos x-x^2\sin x/3\). The positive function \(z^{a-1}\sin(\pi z)\), together with the displayed ground-state identity, then gives

\[
\lambda_D(a)\ge\frac{(2a+1)\pi^2}{3}.
\]

Consequently the physical energies \(E_2=25/2\) and \(E_3=61/3\) lie strictly below the separated Dirichlet spectra on both pieces. This also justifies positivity of all regular solutions and every adjacent-order recurrence used in the proof.

### 2. Gaussian comparison on the singular side

For \(v(z)=z^j e^{-cz^2/2}\), the exact residual is

\[
\frac{(-\partial_z^2+j(j-1)z^{-2}-E)v}{v}
=c(2j+1)-c^2z^2-E.
\]

The Wronskian comparison therefore gives \(D_j\ge j-c\) when the residual is nonnegative. The two applications are:

| Order \(\sigma\) | Energy \(E\) | Gaussian order \(j\) | \(c\) | Residual lower bound |
|---|---:|---:|---:|---:|
| 2 | \(25/2\) | 4 | \(7/4\) | \(3/16\) |
| 3 | \(61/3\) | 6 | \(11/6\) | \(5/36\) |

Using \(D_a=a-E/(a+D_{a+1})\) yields

\[
D_2\ge-\frac{61}{22},\qquad D_3\ge-\frac{9319}{4478}.
\]

Every substituted denominator has an explicit positive lower bound in the proof. No branch of the recurrence is crossed.

### 3. One factored comparison function on the free side

For \(0<q\le4\), use

\[
p_q(z)=z\left(1-\frac{qz^2}{12}\right)^2.
\]

The key identity is

\[
-p_q''-q p_q=\frac{q^2z^3}{144}(4-qz^2)\ge0.
\]

Wronskian comparison with \(\sin(\sqrt q\,z)/\sqrt q\) proves the continuous-parameter response bound

\[
\sqrt q\cot\sqrt q\ge1-\frac{q}{3-q/4}.
\]

This single inequality supplies both free-side bounds. At length \(1/4\), the energy parameter is \(q=E/16\), and the outward response is four times the unit-interval response. The total response lower bounds are exactly

\[
-\frac{61}{22}+\frac{1036}{359}
=\frac{893}{7898}>0,
\]

\[
-\frac{9319}{4478}+\frac{1084}{515}
=\frac{54867}{2306170}>0.
\]

The reflection and rescaling \(x=5-4z\) maps the operator to the orientation of the existing interface lemma. The energy becomes \(E/16\) on both pieces, and both outward responses are divided by four. Hence positivity is preserved without comparing responses at different physical energies.

### 4. Shorter noncrossing assembly

The order-two energy estimate is already below \(39/2\). For order three, convexity in \(r\), together with \(\pi^2<987/100\), gives throughout \(2/3<r<1\)

\[
2(\pi^2r+6/r)<\max\left\{\frac{779}{25},\frac{1587}{50}\right\}
=\frac{1587}{50}<\frac{1525}{48}.
\]

The same direct spectral comparison now excludes the full noncrossing range \(0\le\delta\le1/4\). The former subdivision at \(\delta=1/9\) is unnecessary.

## Exact distinction from the previous analytic edition

The previous lemma bounded the inverse-third-trace surrogate

\[
M_\sigma(\delta)=(1+\delta)^2
\bigl(\operatorname{Tr}K_{\sigma;1,\delta}^{-3}\bigr)^{-1/3}.
\]

The new lemma bounds \(\Lambda_\sigma\), which uses the first eigenvalue itself. The old assertions about \(M_2(1/4)\), \(M_3(1/9)\), and \(M_3(1/4)\) were redundant auxiliary facts. They have been removed, not purportedly reproved by the new method. The protected conclusion of the large-height theorem and every downstream estimate needed by its proof are retained.

This edit removes all three noncrossing trace-polynomial evaluations and the noncrossing height split. Its new analytic content is the direct Sturm comparison and its positive comparison functions.

The continuous-parameter 945 trace envelope in the crossing branch was obtained in the previous Chinese analytic edition. It is translated here but is not a new result of this English edition. The crossing proof still uses the existing parametric coefficient-sign proof of the single-minimum property in `lem-trace-single-valley`. That proof remains a finite exact algebraic argument. This review does not claim to have replaced it by an integral or operator inequality.

## Checks completed

- All formulas and inline mathematical notation were compared with the Chinese source at the translation checkpoint.
- All coefficients in the Gaussian and factored quintic residuals were differentiated directly and checked independently with exact rational arithmetic.
- Every recurrence value, positive denominator, free response, response sum, scaling factor, and final margin was checked exactly.
- The final owned files contain no Chinese characters or Chinese punctuation.
- The semantic declarations and proof targets are paired, the new import is explicit, and all references to the removed auxiliary ID in the owned files were updated.
- The large-height theorem statement is unchanged. The Chinese project, strict configuration, protected goals, and locks were not edited.

Independent cross-review of the new H.6 argument has been completed without finding a mathematical correction. The separate report is `review/high_sturm_independent_audit.md`; it covers the Dirichlet conditions, recurrence orientation, response signs, scaling, and theorem assembly.


## Independent cross-review of the terminal curvature lemma

The newly rewritten `lem-common-tail-line` in `workspace/terminal.qmd` was independently reviewed after the owned high-height work was completed. No mathematical correction was found.

The change of variable \(x=h/(h+2)\), the formula for \(W\), and the identities for \(W-xW'\) and \(W''\) were rederived. The exact identity

\[
\left(\frac{\kappa x^2}{W}\right)''
=\kappa\left(\frac{2(W-xW')^2}{W^3}-\frac{x^2W''}{W^2}\right)
\]

has the claimed signs on the full interval. The tangent-line argument for \(U^{2/3}\), its coefficient \(2\sqrt5\), and the completed-square remainder \(17/285\) are correct. Together they establish \(\widehat D''<-15/2\).

The Möbius chord remainder for \(g(x)=67(1-x)/(2(7-5x))\) has the claimed positive coefficient. Its maximum is \(57285/14278<201/50\). The endpoint values were independently computed directly from the original formulas in \(h\), and the two stated rational residuals were reproduced exactly. Finally, the strong-concavity contribution is \(+15\omega/4\), so subtraction leaves

\[
\widehat D-g>\frac{37}{2000}-\frac{27}{100}\omega
>\frac1{2000}.
\]

The energy derivative \(\mathcal D'(\tau)=-(2s+3)/\mathcal C(\tau)^2\) and the resulting strict affine response bound are also correct.

The suggested expository addition \(T_0/B^2<2961/16900<30/169\) has been incorporated in the final source. It does not change the argument.
