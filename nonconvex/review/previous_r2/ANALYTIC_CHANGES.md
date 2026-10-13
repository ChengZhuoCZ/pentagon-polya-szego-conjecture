# R2 analytic replacements - 12 October 2026

## Scope and continuity

This round continues the English manuscript and replaces the three remaining long terminal/crossing calculations identified at its end. The central nonconvex-exclusion theorem, area normalization, allowable side counts, and strict competitor construction are preserved. The appendix's regular-pentagon conclusion still assumes a separate extremal theorem for convex polygons with at most five sides.

The previous English change record is preserved at `review/previous_english/ANALYTIC_CHANGES.md`. The current file records the additional R2 work. The mathematical proof appears in full in the QMD chapters and generated manuscript.

## 1. T.3: reciprocal majorants and curvature replace the degree-twelve payment

The original payment is unchanged:

\[
Z_\Psi=s+h(J+G_*)-v\Pi_+h^2e,
\qquad \Pi_+=987/100.
\]

The head, gain, and affine-tail comparisons already reduce the first terminal curve to this same payment. Its original four-part numerator factorization and the auxiliary objects \(D_{\rm pay},N_{\rm pay},Q_4\) are removed.

Write

\[
S(h)=\frac{2hk}{1-k},\qquad R_0(h)=Z_\Psi(h)+S(h).
\]

The function \(R_0\) has an elementary partial-fraction decomposition involving the linear part and poles at \(0,-1,-2,-127/60\). The proof displays every coefficient. The nonlinear reciprocal loss is bounded by

\[
S(h)<M_-(h):=\frac{199}{40(h+2)}-\frac1{9h}
\quad\left(\frac38\le h\le\frac12\right),
\]

and

\[
S(h)<M_+(h):=\frac5{h+231/100}
\quad\left(\frac12\le h\le4\right).
\]

These bounds are established from positive denominators and uniform curvature of their numerator product expressions. For the first majorant, the numerator has second derivative greater than 70000 on the lower interval. Its second-order tangent at \(h=1/2\) gives a positive lower bound \(3751/14\). For the second majorant, the second derivative is greater than 3800 and the same tangent method gives a lower bound greater than 6. This uses explicit differentiation and completion of a quadratic, without a coefficient-sign factorization.

### Lower interval

Put \(G_-=R_0-M_-\) and \(x=1/(h+2)\). Its normalized curvature is a sum of simple reciprocal terms. The potentially adverse combination is bounded by the elementary maximum formula

\[
\max_{x<1}\frac{A-(A+3B)x}{(1-x)^4}
=\frac{(A+3B)^4}{256B^3}\qquad(A,B>0).
\]

Coarse rational comparisons give the uniform estimate

\[
\frac{(h+2)^3G_-''(h)}2>\frac{11}{30}>0.
\]

Moreover \(G_-(1/2)>7/500\) and \(G_-'(1/2)<0\). The tangent at the right endpoint therefore proves

\[
Z_\Psi>G_->\frac7{500}
\quad\left(\frac38\le h\le\frac12\right).
\]

### Upper interval

Put \(G_+=R_0-M_+\) and again \(x=1/(h+2)\). The key function is

\[
Q(x)=\frac{(h+2)^3G_+''(h)}2
=b_4+3b_3x-\mathcal R(x).
\]

The constants \(b_j\) are the displayed positive partial-fraction coefficients. A direct reciprocal derivative identity proves \(\mathcal R''>0\), hence \(Q''<0\), on \([1/6,2/5]\). The proof treats the two elementary ranges \(x\le1/4\) and \(x\ge1/4\) by monotone rational bounds. These ranges organize an analytic inequality; no sampled values or numerical boxes are used.

Three coarse rational endpoint comparisons show

\[
Q(1/6)>0,\qquad Q(2/7)>0,\qquad Q(2/5)<0.
\]

Concavity implies exactly one curvature transition for \(G_+\), from negative to positive as \(h\) increases. On \([3/2,4]\), it is convex. Its tangent at \(17/8\), with

\[
G_+(17/8)>\frac1{500},\qquad
0<G_+'(17/8)<\frac1{2000},
\]

gives

\[
G_+(h)>\frac1{500}-\frac{5/8}{2000}
=\frac{27}{16000}.
\]

On \([1/2,3/2]\), the single curvature transition and \(G_+'(3/2)<0\) exclude an interior minimum. The two endpoint values then give the same lower bound. Combining both intervals proves

\[
\boxed{Z_\Psi(h)>\frac{27}{16000}\qquad\left(\frac38\le h\le4\right).}
\]

The original terminal response consequently satisfies

\[
H_2(k)+\mathcal B(A_-,w)+\mathcal L_h(\Pi_+h^2e)
>\frac{Z_\Psi(h)}h>\frac{27}{16000h}>0.
\]

The common physical energy and the two gain terms are retained. This result strengthens the same payment used previously; it does not merely substitute an unrelated positive expression.

## 2. T.4: one positive quadratic and one tangent replace the degree-six factorization

The original quantities \(e,k,r,J_\Phi,Z_\Phi\) are retained. The preliminary head and tail analysis still proves

\[
0<k<r<\frac12,\qquad
Q=208h(1+h)(h+2)(1-r)>0,
\qquad \Pi_+h^2e<T_0.
\]

The new structural identity is

\[
\frac{45}{8(h+3)}-\frac{2hr}{1-r}
=\frac{45(32h^2-73h+90)}{8(h+3)Q}>0,
\]

because

\[
32h^2-73h+90
=32\left(h-\frac{73}{64}\right)^2+\frac{6191}{128}>0.
\]

Substituting this bound into the original payment gives \(Z_\Phi>G\), where

\[
G(h)=\frac{389h}{3350}-\frac{277649}{435500}
-\frac{174393}{139360(h+1)}
+\frac{54705}{6968(h+2)}-\frac{45}{8(h+3)}.
\]

For \(x=1/(h+2)\in[1/6,11/30]\),

\[
\frac{(h+2)^3G''(h)}2
=c_2-\left[\frac{c_1}{(1-x)^3}+\frac{c_3}{(1+x)^3}\right].
\]

The bracket is convex. Simple endpoint estimates give an upper bound \(15/2<c_2\), so \(G''>0\) on the whole interval. At \(h_*=9/4\),

\[
G(h_*)>\frac7{500},\qquad 0<G'(h_*)<\frac1{200}.
\]

The tangent yields

\[
G(h)>\frac7{500}-\frac{67/44}{200}
=\frac{281}{44000}>\frac3{500}.
\]

Since \(\sqrt3-1>8/11\), this covers the original terminal range and proves

\[
\boxed{Z_\Phi(h)>\frac3{500}\qquad(\sqrt3-1<h\le4).}
\]

In particular,

\[
H_1(k)+\mathcal L_h(\Pi_+h^2e)>\frac3{500h}>0.
\]

The original geometric terminal path and both unused positive gain terms remain available. The degree-six payment numerator is removed entirely.

## 3. H.5: direct Sturm comparison replaces the entire crossing trace argument

The comparison operator is now defined for every real \(2\le s\le3\):

\[
K_{s;\ell,b}=-\partial_z^2+
\frac{s(s-1)}{z^2}\mathbf1_{(0,\ell)}
\quad\text{on }(0,\ell+b).
\]

It has the original Friedrichs left endpoint, Dirichlet right endpoint, and continuous value and derivative at the actual interface. Hardy's inequality proves that its common form domain is \(H_0^1\); compact resolvent and interface matching are justified in the definition's proof.

The retained geometric area reduction gives

\[
D\ge\ell^2 F_0(t),\qquad t=b/\ell\in[0,3/2],
\]

where

\[
F_0(t)=
\begin{cases}
1+3t+t^2,&0\le t\le1/4,\\
(9+138t+29t^2)/25,&1/4\le t\le3/2.
\end{cases}
\]

The new spectral statement is

\[
\boxed{\lambda_1(K_{s;1,t})>
\frac{25s-11}{2F_0(t)}
\qquad(2\le s\le3,\ 0\le t\le3/2).}
\]

### A positive singular comparison function

Set \(C_s=(25s-11)/2\). The positive function

\[
v_s(y)=y^s(1-y^2)e^{-sy^2/2}
\]

satisfies

\[
-\frac{v_s''}{v_s}+\frac{s(s-1)}{y^2}
=s^2+5s+s^2(1-y^2)+\frac2{1-y^2}
\ge B_s:=s^2+5s+2\sqrt2\,s.
\]

AM-GM proves the last inequality, and the ground-state identity proves the separated Dirichlet lower bound. The elementary inequality \(\sqrt2>45/32\) gives

\[
B_s-C_s>
\left(s-\frac{75}{32}\right)^2+\frac7{1024}>0.
\]

For \(t>0\), choose the common energy \(E=C_s/F_0(t)\). Rescaling the comparison function by \(\sqrt{F_0(t)}\) and using a Wronskian identity gives the singular outward response bound

\[
D_s(E)>s\left(1-\frac1F\right)-\frac2{F-1},
\qquad F=F_0(t).
\]

The regular solution is supplied explicitly by its convergent series. Positivity, finite form energy, and its identification with the unique variational minimizing extension are checked before applying the interface criterion.

### The free response and its curvature

For \(q=Et^2\), the first interval has \(q\le32/29<4\). The shared positive comparison function

\[
p_q(z)=z(1-qz^2/12)^2
\]

gives \(\sqrt q\cot\sqrt q\ge1-q/(3-q/4)\). Combining the two responses reduces the first interval to the concave quadratic

\[
P(t)=\frac13+\frac{8t}{39}-\frac{496t^2}{87},
\qquad P(0)=\frac13,\quad P(1/4)=\frac{32}{1131}>0.
\]

On the second interval, \(q\le32/5<\pi^2\). The existing finite-mode resolvent estimate gives a two-fraction rational lower bound for the free response. The full lower bound can be written as \(G_s=A_s-B_{C_s}\). Two elementary quotient derivative identities show that \(A_s\) is strictly concave and \(B_C\) is strictly convex in \(t\). The latter sign follows by comparing two quadratic denominators and the signs of their quadratic terms; no expanded high-degree numerator is used.

The function \(G_s(t)\) is also concave in \(s\). Its endpoint estimates are

\[
G_s(1/4)>\frac5{87},\quad
G_2(3/2)>\frac9{10},\quad
G_3(3/2)=\frac{39}{1394}>0.
\]

The two concavity arguments therefore give \(G_s(t)\ge39/1394\) over the entire second rectangle. Both separated spectra remain above \(E\); both outward responses use the same energy and interface. The variational interface criterion proves the spectral statement. The case \(t=0\) follows separately from \(B_s>C_s\).

Scaling and the geometric area cost now give exactly the estimates required by the original large-height contradiction:

\[
\lambda_1(K_{2;\ell,b})>\frac{39}{2D},
\qquad \lambda_1(K_{3;\ell,b})>\frac{32}{D}.
\]

### Removed auxiliary machinery

The current proof removes `def-trace-polynomials`, `lem-green-trace`, `lem-trace-single-valley`, `lem-trace-uniform-envelope`, `lem-trace-endpoints`, and `lem-characteristic-trace-identity`. Their old stronger trace-surrogate bounds and the continuous 945 envelope are not asserted by the new Sturm proof. They are redundant to the nonconvex-exclusion conclusion and survive only in the preceding edition's historical review records. Mercer's theorem is removed from the current external-input list and bibliography.

## What remains and what was checked

The preceding English and Chinese analytic replacements remain in force: the common-tail curvature gap, variational Hadamard formula, finite-projection cotangent response, noncrossing Sturm comparison, the earlier middle-height derivative comparisons, the explicit truncated-square competitor, and energy-tensor isotropy.

The three targeted long factorization/coefficient arguments are gone. Ordinary exact algebra remains: partial fractions, derivatives of low-degree product expressions, positive squares, and a finite number of explicit rational endpoint or tangent comparisons. These are parts of written interval proofs. No finite-element computation, floating-point grid, interval program, or machine-generated sign certificate is a mathematical premise.

The two terminal replacements and the crossing proof were independently cross-reviewed, including all denominator conditions, parameter ranges, strict inequalities, common-energy comparisons, and final assembly. Portable scripts reproduce selected exact identities and rational comparisons. Current source checks report 18 QMD files, 57 declarations, and 54 linked proof blocks, with no dependency or protected-file discrepancy.

The original protected goal, locks, contract, and strict verification configuration are preserved. The official qmd-prover and Quarto executables were unavailable; no official local/global verdict or proof-assistant certification is claimed. Current review reports and the PDF inspection report state precisely what was checked. The earlier review records are explicitly separated under `review/previous_english/`.
