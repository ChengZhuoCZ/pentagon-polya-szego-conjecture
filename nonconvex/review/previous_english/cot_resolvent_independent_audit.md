# Independent audit of the cotangent resolvent bound

**Scope.** This audit checks `lem-cot-rational` (R.7) and the elementary trigonometric argument inside `lem-pole-free` in `workspace/robin.qmd`, against the definition of \(\mathsf H\) in `workspace/analytic.qmd`. It also records the requested clarification in `workspace/terminal.qmd`. The review found no substantive mathematical error in these replacements.

## 1. Boundary lifting and the exact energy identity

The Dirichlet Laplacian has operator domain
\[
D(\mathcal A)=H^2(0,1)\cap H_0^1(0,1).
\]
For \(0<K<\Pi\), the function \(w=KR_Kf\) lies in this domain even though the forcing \(f(y)=y\) has nonzero right boundary trace. Thus \(g=f+w\in H^2\), \(g(0)=0\), and \(g(1)=1\). The equation \((\mathcal A-K)w=Kf\) gives \(-g''=Kg\). The displayed sine solution and its endpoint derivative follow because \(\sin\sqrt K>0\).

The integration by parts is legitimate on these domains. More explicitly,
\[
\begin{aligned}
\int_0^1 (|g'|^2-Kg^2)
&=1-\frac K3+\int_0^1(|w'|^2-Kw^2)-2K\langle f,w\rangle\\
&=1-\frac K3-K\langle f,w\rangle\\
&=1-\frac K3-K^2\langle f,R_Kf\rangle.
\end{aligned}
\]
Here \(\int f'w'=w(1)-w(0)=0\), and testing the resolvent equation against \(w\) gives the second line. Multiplying \(-g''=Kg\) by \(g\) identifies this energy with \(g'(1)\). All signs and factors in (R.7.1) are correct.

## 2. Finite projection, coefficients, and regrouping

Direct integration gives
\[
\langle y,\sqrt2\sin(n\pi y)\rangle
=\frac{\sqrt2(-1)^{n+1}}{n\pi}.
\]
Consequently the two squared projection weights are
\(a_1=2/\Pi\) and \(a_2=1/(2\Pi)\), and the remainder weight is
\[
a_3=\|\eta\|_2^2=\frac13-\frac5{2\Pi},\qquad
a_1+a_2+a_3=\frac13.
\]
The orthogonal complement of the first two eigenfunctions is reducing for the self-adjoint resolvent. Its Dirichlet spectral lower bound is \(9\Pi\), so its resolvent upper bound is exactly \((9\Pi-K)^{-1}\). This proves the stated bound for \(\langle f,R_Kf\rangle\), with all three displayed coefficients correct.

For an explicit check of the subsequent collection of terms, use
\[
-Ka-\frac{K^2a}{\lambda-K}
=-\frac{Ka\lambda}{\lambda-K}
\]
with \((a,\lambda)=(a_1,\Pi),(a_2,4\Pi),(a_3,9\Pi)\). The first two resulting numerators are both \(2K\); the last term is
\[
-\frac{Ka_3}{1-K/(9\Pi)}
=-\frac{2K(1/6-5/(4\Pi))}{1-K/(9\Pi)}.
\]
This is precisely \(\mathsf H(K)\) in (M.1.5). An independent exact rational-function calculation also verified the identity after setting \(t=K/\Pi\), separately for its constant coefficient and its coefficient of \(\Pi\). No numerical value of \(\pi\) was substituted.

## 3. Strictness and the kernel argument

On this reducing complement, the operator
\[
M_K=(9\Pi-K)^{-1}I-R_K
\]
is nonnegative. Its kernel is precisely the eigenspace of \(\mathcal A\) at \(9\Pi\), namely \(\operatorname{span}\{\phi_3\}\). This follows directly either from the spectral theorem or from \(R_K\eta=(9\Pi-K)^{-1}\eta\), which forces \(\eta\in D(\mathcal A)\) and \(\mathcal A\eta=9\Pi\eta\).

For a nonnegative bounded operator, vanishing of \(\langle\eta,M_K\eta\rangle\) is equivalent to kernel membership. Here \(\eta=y-(\sqrt2/\pi)\phi_1+(\sqrt2/(2\pi))\phi_2\) is continuous on the closed interval and has \(\eta(1)=1\). If it were equal in \(L^2\) to a multiple of \(\phi_3\), continuity would make the two representatives equal everywhere, including at the endpoint. Their boundary values disagree. Therefore (R.7.2) is strictly positive for every \(0<K<\Pi\), and the strengthened statement with \(>\) is justified.

This argument uses ordinary compact Dirichlet spectral theory, a projection onto two explicitly integrated modes, and an operator order bound. It does not require the cotangent partial-fraction identity, an infinite reciprocal-square sum, or an evaluated infinite spectral expansion.

## 4. The elementary trigonometric inequality and the singular tail

The derivatives in the new argument are exact:
\[
J'(x)=x\sin x,\qquad
F'(x)=\frac{x}{3}(\sin x-x\cos x)=\frac{xJ(x)}3.
\]
Both functions vanish at zero. Positivity of \(\sin x\) on \((0,\pi)\) therefore gives \(J(x)>0\), then \(F(x)>0\), and division by \(\sin x\) gives
\[
1-x\cot x>\frac{x^2}{3}.
\]
No series expansion is needed. Differentiating \(g(z)=z^{\sigma-1}\sin(\pi z/h)\) gives exactly the displayed potential identity. Since \(\sigma>1\), the trigonometric estimate implies the claimed lower bound \(\Pi(2\sigma+1)/(3h^2)\).

The domain argument is also sound. Hardy's inequality makes the nonnegative inverse-square potential form bounded by the Dirichlet energy, so its Friedrichs form has domain \(H_0^1(0,h)\), and smooth compactly supported functions are a form core. On that core, \(u/g\) is a legitimate smooth compactly supported function because \(g>0\) in the open interval; Picone's identity has no endpoint term. Only the resulting quadratic-form lower bound is extended by density, so no unproved assertion about extending the full weighted identity is needed. Together with the previously proved strict inequality for \(T=h^2E\), this gives a first tail eigenvalue strictly above \(E\).

## 5. Terminal clarification and verification status

The opening polynomial comparison in `lem-common-tail-line` was clarified to display
\[
\frac{T_0}{B^2}<\frac{3(987/100)}{169}
=\frac{2961}{16900}<\frac{30}{169}.
\]
Indeed, the preceding inequalities give
\(B^2>(51h+82)^2/[25(h+2)^2]\) and
\((51h+82)^2(1+h)>4225h^2(h+2)\). Substitution in the definition of \(T_0\), using \(4225=25\cdot169\), gives the stated ratio. The two rational constant checks passed exactly.

This is an independent mathematical audit plus exact rational algebra checks. No official `qmd-prover` verification is claimed; that executable remains unavailable. The audit changed no statement, proof, or import in `workspace/robin.qmd`, and the terminal change only makes an already established bound explicit.
