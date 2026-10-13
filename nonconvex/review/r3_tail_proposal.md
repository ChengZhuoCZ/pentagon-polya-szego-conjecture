# R3 proposal: Volterra construction, differential intertwining, and a direct tail barrier

**Current status:** the selected derivation has been integrated into the R3 manuscript and independently reviewed. Historical proposal wording below records its development; it is not pending work.
## Result and project scope

The power-series construction and coefficient comparison in R.6 can be removed completely. A global Volterra contraction constructs the normalized regular solution for every real order $a>1$ and every $T>0$. A first-order differential factorization then proves the exact adjacent-order recurrence, including its positive denominator. Finally, a single positive comparison function proves the same algebraic tail bound $\mathsf T$ directly, without the two response reductions through higher orders.

The direct comparison in fact gives $D_\sigma>\mathsf T(\sigma,T)$ under the current hypotheses. The existing weaker conclusion $D_\sigma\ge\mathsf T(\sigma,T)$ may therefore be retained unchanged. The exact recurrence must remain because H.6 uses it at orders larger than three.

I independently read the R3 AGENTS contract and configuration. The external-basis file is absent. The configured backend is codex, model gpt-6.1-sol, effort xhigh, with strict citations, rigor, and refutation rigor, and assumptions forbidden. The official qmd-prover executable is unavailable. This document is a proposed analytic derivation for independent review, not an official verification result. No QMD source, protected goal, configuration, or statement lock has been edited.

## 1. Proposed reusable lemma: regular inverse-square solutions

Introduce the exported identifier **lem-regular-tail** before R.6. Its statement should make the regular asymptotics and positivity available to downstream proofs, rather than leaving those facts only inside another lemma's proof.

### Proposed statement

For every real $a>1$, write $L_a$ for the differential expression

$$
-\frac{d^2}{dz^2}+\frac{a(a-1)}{z^2}
$$

on $(0,1)$, and write $\lambda_D(a)$ for the first eigenvalue of its Friedrichs realization with a Dirichlet condition at $1$. That realization has form domain $H_0^1(0,1)$, and $\lambda_D(a+1)\ge\lambda_D(a)$. Uses of $L_a$ on the regular solution below mean the differential expression, not membership in the operator domain with a zero trace at $1$.

For every $T>0$, there is a unique solution $u_a\in C^2((0,1])$ of $L_a u_a=Tu_a$ with $u_a(z)/z^a\to1$ as $z\downarrow0$. It has finite form energy near the singular endpoint and satisfies

$$
u_a(z)=z^a(1+O(z^2)),\qquad
u_a'(z)=az^{a-1}+O(z^{a+1}),
$$

and, more precisely,

$$
u_a'(z)-\frac a z u_a(z)
=-\frac{T}{2a+1}z^{a+1}+O(z^{a+3}).
\tag{V.1}
$$

If $0<T<\lambda_D(a)$, then $u_a>0$ on $(0,1]$. Its trace-one normalization $u_a/u_a(1)$ is the unique minimizer of the shifted form

$$
\int_0^1\left(|v'|^2+\frac{a(a-1)}{z^2}|v|^2-T|v|^2\right)\,dz
$$

among $v\in H^1(0,1)$ with $v(0)=0$ and $v(1)=1$. Its outward response at $z=1$ is $D_a=u_a'(1)/u_a(1)$.

### Proof of the common Friedrichs domain

For a real compactly supported smooth function, integration by parts and Cauchy--Schwarz give

$$
\int_0^1\frac{|v|^2}{z^2}\,dz
=2\int_0^1\frac{vv'}z\,dz
\le2\left(\int_0^1\frac{|v|^2}{z^2}\right)^{1/2}
\left(\int_0^1|v'|^2\right)^{1/2}.
$$

Thus

$$
\int_0^1\frac{|v|^2}{z^2}\le4\int_0^1|v'|^2.
\tag{V.2}
$$

Apply the same argument to the real and imaginary parts if complex functions are used. Approximation extends (V.2) to $H_0^1(0,1)$. The potential is nonnegative for $a>1$, and the form norm is equivalent to the $H_0^1$ norm. Its closure therefore has exactly that domain, with the smooth compactly supported functions as a form core. Compact embedding gives compact resolvent and a positive first eigenvalue. Since $a(a-1)$ increases with $a>1$ on this common domain, the variational principle gives $\lambda_D(a+1)\ge\lambda_D(a)$.

### Global Volterra construction

Write $u_a(z)=z^a v(z)$. The differential equation becomes

$$
(z^{2a}v')'=-Tz^{2a}v.
\tag{V.3}
$$

For $v\in C[0,1]$, define

$$
(\mathcal K_a v)(z)
=\int_0^z \xi^{-2a}\int_0^\xi \eta^{2a}v(\eta)\,d\eta\,d\xi,
\qquad (\mathcal K_a v)(0)=0.
$$

Changing the order of integration gives, for $z>0$,

$$
(\mathcal K_a v)(z)
=\frac1{2a-1}\int_0^z
\eta\left[1-\left(\frac\eta z\right)^{2a-1}\right]v(\eta)\,d\eta.
\tag{V.4}
$$

The kernel is nonnegative, is bounded above by $\eta/(2a-1)$, and extends continuously at the origin. In particular, $\mathcal K_a$ maps $C[0,1]$ to itself.

Set $\beta=T/(2a-1)>0$, and use the equivalent complete norm

$$
\|v\|_\beta=\sup_{0\le z\le1}e^{-\beta z^2}|v(z)|.
$$

The kernel bound in (V.4) gives

$$
\begin{aligned}
e^{-\beta z^2}|T\mathcal K_a(v-w)(z)|
&\le \frac{T}{2a-1}\|v-w\|_\beta
e^{-\beta z^2}\int_0^z\eta e^{\beta\eta^2}\,d\eta\\
&=\frac12(1-e^{-\beta z^2})\|v-w\|_\beta\\
&\le\frac12\|v-w\|_\beta.
\end{aligned}
\tag{V.5}
$$

Consequently the affine map $v\mapsto1-T\mathcal K_av$ is a contraction on all of $C[0,1]$, with no smallness condition on $T$. Starting with any continuous function, its successive iterates have geometrically decreasing differences in this norm. They converge uniformly to a unique fixed point

$$
v=1-T\mathcal K_a v.
\tag{V.6}
$$

This is a contraction argument for an integral equation; no power-series expansion, coefficient recurrence, or termwise differentiation is used.

### Differentiability, asymptotics, and uniqueness of the normalization

Differentiating the integral equation at every $z>0$ gives

$$
v'(z)=-Tz^{-2a}\int_0^z\eta^{2a}v(\eta)\,d\eta.
\tag{V.7}
$$

Because $v$ is bounded, (V.7) yields $v'=O(z)$; integrating and using $v(0)=1$ yields $v=1+O(z^2)$. Substituting this estimate back into (V.7) gives the finite asymptotic estimate

$$
v'(z)=-\frac{T}{2a+1}z+O(z^3).
\tag{V.8}
$$

Equation (V.7) is differentiable for $z>0$ and implies (V.3). Thus $u_a=z^av$ solves the required equation. Its ordinary derivative and (V.8) give all the asymptotics in the proposed statement. Local smoothness on $(0,1]$ follows from the differential equation.

It remains to verify that the normalization itself determines this solution, without silently assuming a derivative condition at zero. Suppose another solution has $\widetilde u(z)/z^a\to1$, and put $\widetilde v=\widetilde u/z^a$. This function is bounded near zero, and

$$
p(z):=z^{2a}\widetilde v'(z)
\quad\hbox{satisfies}\quad
p'(z)=-Tz^{2a}\widetilde v(z).
$$

The right-hand side is integrable at zero, so $p(z)$ has a finite limit $\ell$ and

$$
p(z)=\ell+O(z^{2a+1}),\qquad
\widetilde v'(z)=\ell z^{-2a}+O(z).
$$

If $\ell\ne0$, integration gives a nonzero term $\ell z^{1-2a}/(1-2a)$ in $\widetilde v(z)$, contradicting its finite limit because $a>1$. Hence $\ell=0$. Integrating the resulting derivative formula from zero gives exactly (V.6). Uniqueness of its fixed point proves $\widetilde u=u_a$ on the entire interval.

### Endpoint form behavior, positivity, and the variational extension

The regular estimates show that $u_a(0)=0$, $u_a'=O(z^{a-1})$, and

$$
|u_a'|^2+z^{-2}|u_a|^2=O(z^{2a-2}).
$$

These quantities are integrable for every $a>1$. Hence $u_a\in H^1(0,1)$, has finite potential energy, and has the required Friedrichs behavior at the singular endpoint. No zero trace at $z=1$ is imposed unless a zero actually occurs there.

Assume now $T<\lambda_D(a)$. The leading regular term is positive. If $u_a$ had a first zero $z_0\in(0,1]$, extend its restriction to $(0,z_0)$ by zero to $(0,1)$. The result is a nonzero member of $H_0^1(0,1)$ with finite potential energy. Integrating the ODE gives Rayleigh quotient $T$: the boundary term at $z_0$ vanishes, and the term $u_au_a'=O(z^{2a-1})$ tends to zero at the singular endpoint. This contradicts $T<\lambda_D(a)$, proving positivity.

Normalize $g=u_a/u_a(1)$. Integration by parts against compactly supported smooth tests gives its weak equation. The finite energy just proved, together with Hardy's inequality and form-core density, extends that equation to all zero-trace form-domain tests. Every other function with the same endpoint traces is $g+w$, with $w\in H_0^1(0,1)$. Its shifted energy equals the shifted energy of $g$ plus that of $w$, because the mixed term vanishes. Moreover,

$$
q_a(w)-T\|w\|_2^2
\ge\left(1-\frac{T}{\lambda_D(a)}\right)q_a(w)>0
\quad(w\ne0).
$$

This proves the asserted unique minimizing extension. A final integration by parts gives its energy, and therefore its outward response, as $g'(1)=D_a$.

## 2. Exact recurrence from first-order intertwining

Retain the statement and export of **lem-tail-recurrence**. Importing is unnecessary between this lemma and the proposed same-file **lem-regular-tail**, but the proof must cite the new lemma.

For $a>1$, set

$$
A_a=\partial_z-\frac a z,\qquad
B_a=\partial_z+\frac a z.
$$

Direct composition gives the differential identities on $(0,1]$

$$
L_a=-B_aA_a,\qquad L_{a+1}=-A_aB_a,
\qquad L_{a+1}A_a=A_aL_a.
\tag{V.9}
$$

These are identities of differential expressions; they do not assert that either first-order factor preserves a Dirichlet operator domain.

By (V.1),

$$
A_a u_a=-\frac{T}{2a+1}z^{a+1}+O(z^{a+3}).
$$

The intertwining identity shows that $A_a u_a$ solves the order-$a+1$ equation at the same energy $T$. Its leading term and uniqueness in **lem-regular-tail** therefore give

$$
A_a u_a=-\frac{T}{2a+1}u_{a+1}.
\tag{V.10}
$$

Applying $B_a$ and using $B_aA_a u_a=-Tu_a$ gives the second identity

$$
B_a u_{a+1}=(2a+1)u_a.
\tag{V.11}
$$

Now suppose $T<\lambda_D(s)$. Spectral ordering in **lem-regular-tail** implies $T<\lambda_D(s+1)$, so both interface values are strictly positive. Equation (V.11) yields

$$
s+D_{s+1}
=(2s+1)\frac{u_s(1)}{u_{s+1}(1)}>0.
\tag{V.12}
$$

Dividing (V.10) by $u_s(1)$ and using (V.12) gives exactly

$$
D_s=s-\frac{T}{s+D_{s+1}}.
\tag{V.13}
$$

This argument applies to every real $s>1$, and in particular to all orders needed in H.6. Positivity of the recurrence denominator is established before the division. Both adjacent solutions use the same energy $T$ throughout.

## 3. Direct positive comparison giving the original algebraic tail bound

This replaces the Gaussian comparison at order $\sigma+2$ and its two recurrence substitutions. The new proof uses the same original hypotheses:

$$
a=\sigma>1,\quad 0<T<\lambda_D(a),\quad
r=\sqrt{(2a+5)^2-4T}>0,
$$

$$
C=a+\frac12+\frac r2>0,\qquad
D=2a+1-\frac TC>0.
$$

Put

$$
A=2a+1,\qquad M=2a+3,\qquad
c=\frac{2a+5-r}{2}>0.
$$

Then

$$
T=c(2a+5-c),\qquad C=M-c,\qquad D=A-\frac TC.
\tag{V.14}
$$

Let

$$
B=Ac+T>0,\qquad
H(z)=AM-Bz^2.
$$

The original positive denominator hypotheses have the useful exact consequence

$$
H(1)=AM-Ac-T=C D>0.
\tag{V.15}
$$

Thus $H(z)\ge CD>0$ and $M-cz^2\ge C>0$ on $[0,1]$. Define the single positive comparison function

$$
w(z)=z^a\exp\left(
-\int_0^z\frac{T\eta(M-c\eta^2)}{H(\eta)}\,d\eta
\right).
\tag{V.16}
$$

The integral is finite and smooth up to both endpoints. This function has $w=z^a(1+O(z^2))$, $w'=az^{a-1}+O(z^{a+1})$, and

$$
\frac{w'}w=\frac a z-\frac{Tz(M-cz^2)}{H(z)}.
\tag{V.17}
$$

In particular, its interface response is exactly the original rational-radical bound:

$$
\frac{w'(1)}{w(1)}
=a-\frac{T C}{C D}
=a-\frac TD
=\mathsf T(a,T).
\tag{V.18}
$$

### Full residual calculation

For a transparent derivation, put $x=z^2$ and

$$
h(x)=AM-Bx,\qquad
f(x)=\frac{T(M-cx)}{h(x)}.
$$

Then

$$
f'(x)=\frac{T^2M}{h(x)^2},\qquad
A f(x)-T=\frac{T^2x}{h(x)}.
\tag{V.19}
$$

Writing (V.17) as $w'/w=a/z-zf(z^2)$ gives

$$
\begin{aligned}
\frac{(L_a-T)w}{w}
&=A f(x)+2x f'(x)-x f(x)^2-T\\
&=\frac{T^2x}{h(x)^2}
\left[h(x)+2M-(M-cx)^2\right].
\end{aligned}
$$

Here $M=A+2$ and $2M-A=2a+5$. Therefore

$$
\begin{aligned}
h(x)+2M-(M-cx)^2
&=\bigl[(2M-A)c-T\bigr]x-c^2x^2\\
&=c^2x(1-x),
\end{aligned}
$$

where the last equality is precisely $T=c(2a+5-c)$. We obtain the factored differential residual

$$
\boxed{\displaystyle
\frac{(L_a-T)w}{w}
=\frac{T^2c^2z^4(1-z^2)}{H(z)^2}\ge0.}
\tag{V.20}
$$

It is strictly positive for $0<z<1$.

By **lem-regular-tail**, $u_a$ is positive on $(0,1]$. With

$$
W=u_a'w-u_aw',
$$

the ODE and (V.20) give

$$
W'=u_a(L_a-T)w>0\quad(0<z<1).
$$

The regular asymptotics give $W=O(z^{2a+1})\to0$ at zero. Integrating to one and dividing by the positive interface values gives

$$
D_a>\frac{w'(1)}{w(1)}
=\mathsf T(a,T).
\tag{V.21}
$$

The original conclusion with $\ge$ follows. The same energy, the original pole-free hypothesis, and the original positive algebraic denominators have all been retained. No higher-order spectral comparison is needed for this second conclusion.

An entirely elementary closed form for the same barrier, if desired instead of (V.16), is

$$
w(z)=z^a
\exp\left(-\frac{Tc}{2B}z^2\right)
\left(\frac{AM-Bz^2}{AM}\right)^{MT^2/(2B^2)}.
\tag{V.22}
$$

The logarithmic derivative of (V.22) is (V.17). All bases in this real power are strictly positive by (V.15). The integral form is shorter to motivate, whereas the closed form makes the comparison function explicit without an unevaluated integral.

## 4. Integration and dependency notes

1. Add and export **lem-regular-tail** in robin.qmd before **lem-tail-recurrence**. Keep the new lemma's quantified range $a>1$, not merely the order interval $[2,3]$ used in the crossing theorem.
2. Replace the R.6 power-series construction and coefficient proof by (V.9)–(V.13), citing **lem-regular-tail**. Retain the exact recurrence and positive-denominator statement.
3. Replace the Gaussian comparison at order $\sigma+2$ and the two recurrence reductions by (V.14)–(V.21). Preserve the current non-strict lower-bound statement. A short proof sentence may record that the comparison is actually strict for $T>0$.
4. At the first use of $\mathsf T$, cite **def-analytic**, which robin.qmd already imports. If the existing statement continues to write only $\sigma-T/D$, the same definition is needed where the notation $\mathsf T$ is introduced in the proof.
5. Add **lem-regular-tail** to high.qmd's explicit import from robin.qmd. Its H.5 proof can then replace the duplicate regular series and first-zero argument with this lemma at $a=s$, $T=E$. H.6 retains **lem-tail-recurrence** for its adjacent-order identities. The new dependency creates no cycle.
6. The form-minimizer assertion also permits later consolidation of repeated singular-endpoint arguments in the Robin and coupled proofs. Such consolidation is optional and should preserve their separate physical-coordinate and energy transformations.
7. The proof uses Hardy's inequality, contraction of an integral operator, differential factorization, and a single positive comparison function. It uses no Bessel functions, no power-series identity, no infinite continued-fraction limit, and no numerical or coefficient-sign certificate.
