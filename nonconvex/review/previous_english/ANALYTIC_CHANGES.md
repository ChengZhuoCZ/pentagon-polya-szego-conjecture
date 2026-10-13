# Analytic changes in the English edition — 12 October 2026

## Scope of the conclusion

The central theorem remains nonconvex exclusion in the fixed-area class of simple polygons with at most five sides. Its strict competitor can be chosen with exactly five active sides. The appendix's global conclusion for the regular pentagon retains an explicit hypothesis supplying the separate convex theorem.

Here, an analytic proof consists of definitions, variational principles, differential and integral identities, and exact inequalities that can be checked directly. It does not require running finite elements, parameter subdivisions, interval code, or machine certificates. Ordinary finite algebra remains part of mathematical reasoning.

The English exposition was translated before the new mathematical replacements were made. Formula-preservation records refer to that translation checkpoint. The protected `goals.qmd` and its locks retain their original Chinese bytes; `render/goal-en.json` and `render/english-goal.lua` provide an English presentation of the same semantic goal. There is no duplicate English semantic target.

## New in this English edition

### 1. Curvature replaces the common-tail quintic

The old proof of the common affine tail bound cleared denominators to a polynomial of degree five and then used a derivative table. The replacement works with the original continued fraction and proves the stronger uniform estimate

\[
\mathcal D(\tau)>\frac1{v(h)}+\frac1{2000},
\qquad \frac38\le h\le4,\quad 0\le\tau\le T_0(h).
\]

Use the compact height coordinate \(x=h/(h+2)\in[3/19,2/3]\). With the positive function \(W\) specified in `lem-common-tail-line`, the original maximal-energy denominator is

\[
\widehat D(x)=\mathcal D_h(T_0(h))
=\frac{553}{125}+\frac{21x}{10}-\frac{\kappa x^2}{W(x)},
\qquad \kappa=\frac{2961}{50}.
\]

Elementary rational bounds give

\[
W''<0,\qquad W-xW'>U(x)=\frac{32}{5}+\frac92x^2,
\qquad 0<W<V(x)=\frac{13}{2}+\frac{43}{5}x-\frac{57}{10}x^2.
\]

A tangent to the convex function \(U^{2/3}\), together with one completed square, gives \(V<(5/2)U^{2/3}\). The exact identity

\[
\left(\frac{\kappa x^2}{W}\right)''
=\kappa\left\{\frac{2(W-xW')^2}{W^3}-\frac{x^2W''}{W^2}\right\}
\]

then yields \(\widehat D''<-15/2\). Compare this strong concavity with the exact chord remainder of

\[
g(x)=\frac1v=\frac{67(1-x)}{2(7-5x)}.
\]

The two explicit endpoint gaps exceed \(37/2000\), while the chord correction is at most \((27/100)\omega(x)\), where \(\omega=(x-3/19)(2/3-x)<1/15\). Thus \(\widehat D-g>1/2000\). Monotonicity in the energy variable extends the estimate to every \(0\le\tau\le T_0\).

The same functions, height interval, and energy interval are retained. The strict affine tail bound follows for \(\tau>0\); at \(\tau=0\) its two sides agree. Two direct rational endpoint evaluations remain, but the cleared quintic and its derivative table are removed.

### 2. Rayleigh comparison supplies the polygonal eigenvalue derivative

The pullback of a piecewise affine vertex deformation gives forms on the fixed space \(H_0^1(P)\), with uniform expansions

\[
a_t=a_0+t\dot a_0+O(t^2),\qquad
m_t=m_0+t\dot m_0+O(t^2).
\]

Uniform coefficient comparison gives convergence of the first eigenvalues. Compactness, positivity, and simplicity identify every limit of normalized pulled-back ground states with the original ground state \(U\). Convergence of their energy norms upgrades weak convergence to strong convergence in \(H_0^1(P)\).

Using \(U\) as a fixed trial function gives one Rayleigh bound; using the pulled-back minimizing eigenfunction gives the reverse bound. Together they prove

\[
\lambda_t=\lambda+t\bigl[\dot a_0(U,U)-\lambda\dot m_0(U,U)\bigr]+o(|t|)
\]

for both signs of \(t\). The existing sector estimates, explicit corner truncation, and stress-tensor calculation then give the stated boundary Hadamard formula, including reflex angles.

This first-variation step no longer invokes analytic perturbation of eigenfunctions. Kato's analytic-perturbation theorem is still used for the distinct finite-parameter Steiner argument, where analyticity and the identity theorem rule out an isospectral interval. The standard closed-form representation theorem remains part of the operator foundations.

### 3. A finite resolvent projection replaces the cotangent expansion

Let \(\mathcal A=-d^2/dy^2\) be the Dirichlet Laplacian on \((0,1)\), \(R_K=(\mathcal A-K)^{-1}\), and \(f(y)=y\). The affine lifting and its zero-trace resolvent correction give the exact response identity

\[
\sqrt K\cot\sqrt K
=1-\frac K3-K^2\langle f,R_Kf\rangle,
\qquad 0<K<\pi^2.
\]

Project \(f\) onto just the first two normalized Dirichlet eigenfunctions \(\phi_n=\sqrt2\sin(n\pi y)\):

\[
f=\frac{\sqrt2}{\pi}\phi_1-\frac{\sqrt2}{2\pi}\phi_2+\eta,
\qquad \|\eta\|_2^2=\frac13-\frac5{2\pi^2}.
\]

The complement has spectral lower bound \(9\pi^2\). Bounding the resolvent on this complement reproduces exactly the original rational function \(\mathsf H(K)\). In fact the defect has the exact form

\[
\sqrt K\cot\sqrt K-\mathsf H(K)
=K^2\left\langle\eta,
\bigl[(9\pi^2-K)^{-1}I-R_K\bigr]\eta\right\rangle>0.
\]

The bracketed operator is nonnegative, and its kernel on the complement is the third eigenspace. The continuous remainder satisfies \(\eta(1)=1\), so it is not a multiple of \(\phi_3\), which vanishes there. This proves strictness. The rational response used downstream is unchanged.

The separate inequality needed for the inverse-square Dirichlet lower bound is also elementary. For

\[
J(x)=\sin x-x\cos x,
\qquad F(x)=(1-x^2/3)\sin x-x\cos x,
\]

one has \(J(0)=F(0)=0\), \(J'=x\sin x>0\), and \(F'=xJ/3>0\) on \((0,\pi)\). Hence \(1-x\cot x>x^2/3\). Neither the cotangent partial-fraction formula nor the Basel reciprocal-square sum is used by these replacements.

### 4. Direct Sturm bounds replace all noncrossing trace evaluations

Define

\[
\Lambda_\sigma(\delta)=(1+\delta)^2\lambda_1(K_{\sigma;1,\delta}).
\]

Hardy's inequality gives a common \(H_0^1\) form domain after scaling, and min--max shows that \(\Lambda_\sigma\) is nonincreasing. The new lemma `lem-no-crossing-sturm` proves, throughout \(0\le\delta\le1/4\),

\[
\Lambda_2(\delta)>\frac{625}{32}>\frac{39}{2},
\qquad
\Lambda_3(\delta)>\frac{1525}{48}>\frac{1587}{50}.
\]

At the endpoint \(\delta=1/4\), choose the physical energies \(25/2\) and \(61/3\). Positive Gaussian comparison functions in orders four and six start the adjacent-order recurrence, whose denominators are checked to be positive. The free interval uses the single positive comparison function

\[
p_q(z)=z\left(1-\frac{qz^2}{12}\right)^2,
\qquad
-p_q''-qp_q=\frac{q^2z^3}{144}(4-qz^2)\ge0
\quad(0<q\le4).
\]

Its Wronskian comparison gives \(\sqrt q\cot\sqrt q\ge1-q/(3-q/4)\). Both total interface responses are strictly positive, with exact lower bounds \(893/7898\) and \(54867/2306170\). The same physical energy is used on both sides, and the interface lemma gives the required strict eigenvalue bounds.

The earlier auxiliary assertions concerned the smaller trace surrogate

\[
M_\sigma(\delta)=(1+\delta)^2
\bigl(\operatorname{Tr}K_{\sigma;1,\delta}^{-3}\bigr)^{-1/3}.
\]

Those redundant assertions have been removed, not claimed as consequences of the new proof. All three corresponding polynomial evaluations disappear. The direct bound for order three also makes the old subdivision at \(\delta=1/9\) unnecessary: the candidate energy is uniformly below \(1587/50<1525/48\).

## Retained results from the preceding Chinese analytic edition

The following changes had already been made before this English revision:

- **M.3.4:** a change of variable and a derivative comparison replace the degree-thirteen positive-coefficient polynomial, giving the uniform strict margin \(321929/15162000\) on the original interval \(3/8<h\le\sqrt2\).
- **M.6.7:** positivity of a second derivative and two endpoint values replace the shifted quintic coefficient list.
- **H.5:** the continuous-parameter estimate
  \[
  \frac{\mathcal N_s(t)}{F_0(t)^3(1+st)^3}\le945,
  \qquad 2\le s\le3,\quad 0\le t\le3/2,
  \]
  with equality only at \(t=0\), replaces six large integer endpoint differences and strengthens the crossing spectral bounds to \(\sqrt[3]{7875}/D\) and \(\sqrt[3]{33957}/D\).
- **The truncated-square competitor:** the explicit choice \(\varepsilon=1/32\) is valid; the proof gives
  \[
  F(Q_\varepsilon)<2\pi^2-\frac{\pi^2}{3}\varepsilon^2-\frac{\pi^2}{3}\varepsilon^4
  \quad(0<\varepsilon\le1/32).
  \]
- **Energy-tensor isotropy:** two Rayleigh comparisons using the same ground state establish \(\int_P\nabla U\otimes\nabla U=(\lambda/2)I\) under the stated criticality assumption.
- **The comparison preserving shared energy:** the middle-height response proof checks radicals and denominators before moving along the permitted order-and-energy path. It retains the real interface, the Hardy form domain, and the physical factor \(1/h\).

These are inherited analytic results, not new claims of this English edition. The previous edition's simplified three noncrossing trace comparisons have now been superseded by the direct Sturm argument described above.

## Explicit finite algebra that remains

The T.3 four-part positive factorization and the T.4 positive factorization of degree six remain in the proof. So does the crossing branch's parametric coefficient-sign proof of the single-minimum property. They were already explicit analytic identities and inequalities; this edition does not claim to have replaced them by an integral or operator argument.

Short rational comparisons, the two endpoint values in the new curvature proof, and the displayed polynomial identities remain ordinary finite calculations. Their formulas and sign arguments are in the manuscript. Supplementary scripts reproduce selected identities but are not premises of the proof.

## Completeness, references, and verification limits

The proof treats lower side counts, two reflex angles, noncritical single-reflex polygons, and low-spectrum critical candidates with one reflex angle. The last class is excluded in the small-, middle-, and large-height regimes. Domains above the square threshold use the explicit truncated pentagon as a competitor. Approximation with exactly five active sides preserves the strict spectral gap.

The module reviews distinguish translated material, new derivations, inherited results, and cross-review. Exact rational calculations supplement the displayed arguments. For precise source counts, declaration/proof links, import/export checks, dependency checks, and protected-file comparisons, consult the completed reports in `review/`.

**These checks are not official qmd-prover verification.** The qmd-prover and Quarto executables were unavailable for this revision. No official strict local verdicts or global composition results are claimed. The strict configuration and original goal locks are preserved; no assumption node, reduced-rigor setting, or manually asserted `verified` result was introduced.

The manuscript is built separately by `render/build_manuscript.py`, using Python, Pandoc, and XeLaTeX. The generated English TeX embeds its bibliography. Build completion and any rendering checks should be read from the delivery record rather than inferred from semantic source checks.

The external inputs and their hypotheses are documented in `external-inputs.md`. The detailed original-text checks of Steiner equality, zero-trace rearrangement, Henrot's boundedness construction, and planar spectral continuity were recorded in the preceding Chinese analytic edition. They are preserved as earlier review records, not described as fresh original-source reading in this English revision.
