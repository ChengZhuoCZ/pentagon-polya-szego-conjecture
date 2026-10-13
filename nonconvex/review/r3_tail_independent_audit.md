# Independent audit of the R3 regular-tail construction and comparison

Scope: independent mathematical review of `review/r3_tail_proposal.md`, including the entire range $a>1$, $T>0$ for construction and uniqueness, the conditional pole-free positivity assertion, the exact recurrence, and the direct tail bound. The reviewer independently read the current R3 AGENTS contract, strict configuration, and absent external-basis policy. No QMD source was changed by this audit. This is not an official qmd-prover verification.

## Verdict

The proposed mathematical argument is correct. The integral construction removes the regular power series, differential intertwining proves the exact recurrence, and the single positive comparison function proves the same algebraic tail bound, with strict inequality under the existing hypotheses.

One statement-level clarification was sent to the author and has been addressed in the proposal before integration: if $L_a$ denotes the Friedrichs operator with a Dirichlet condition at $1$, the regular function should be stated to solve the differential equation

$$
-u_a''+a(a-1)z^{-2}u_a=T u_a
$$

on $(0,1]$. It generally has nonzero trace at $1$, so an operator-domain assertion $L_a u_a=T u_a$ would be inappropriate. The author now distinguishes the differential expression from its Friedrichs realization explicitly. The proof already handled their domains correctly.

## 1. Volterra construction and normalization

Reversing the order of integration gives exactly

$$
(\mathcal K_av)(z)=\frac1{2a-1}\int_0^z
\eta\left[1-(\eta/z)^{2a-1}\right]v(\eta)\,d\eta.
$$

For $0\le\eta\le z\le1$ and $a>1$, the kernel is nonnegative and at most $\eta/(2a-1)$. It tends to zero at the origin on the triangular integration region. The operator therefore maps $C[0,1]$ into itself and its value at zero is zero.

With $\beta=T/(2a-1)$, the weighted norm is equivalent to the usual complete supremum norm. The integral estimate yields the exact Lipschitz bound

$$
\|T\mathcal K_a(v-w)\|_\beta
\le\frac12\|v-w\|_\beta.
$$

Thus the fixed point exists globally for every $T>0$; no unmentioned small-energy assumption or interval subdivision is present.

Differentiation of the integral equation gives

$$
v'(z)=-Tz^{-2a}\int_0^z\eta^{2a}v(\eta)\,d\eta.
$$

Boundedness first gives $v'=O(z)$ and $v=1+O(z^2)$. Substituting that estimate in the same integral gives

$$
v'(z)=-\frac{Tz}{2a+1}+O(z^3).
$$

The resulting asymptotics of $u_a=z^av$ and of $u_a'-a u_a/z$ are correct. Differentiation on positive compact subintervals is justified by the continuous integrands, and the differential equation supplies further local regularity.

The uniqueness proof checks the potentially missing singular-endpoint condition. For another normalized solution, $p=z^{2a}\widetilde v'$ has an integrable derivative and a finite limit $\ell$. If $\ell\ne0$, integration of $\widetilde v'=\ell z^{-2a}+O(z)$ creates a nonzero diverging term $\ell z^{1-2a}/(1-2a)$, contradicting $\widetilde v\to1$. Hence $\ell=0$, and the second solution obeys the same Volterra equation. This establishes uniqueness from the stated normalization alone.

## 2. Form domains, positivity, and minimizing extensions

The Hardy inequality is first proved on the smooth core and then extended by density. Nonnegativity of $a(a-1)$ and this inequality give the exact common domain $H_0^1(0,1)$ and equivalence of form norms. The finite interval gives compact embedding and an attained positive first eigenvalue. Monotonicity of $a(a-1)$ for $a>1$ proves spectral ordering on that common domain.

The regular estimates make both $|u_a'|^2$ and $z^{-2}|u_a|^2$ of order $O(z^{2a-2})$, which is integrable. At a hypothetical first zero, extension by zero is a legitimate $H_0^1$ test. The boundary product at the singular end is $O(z^{2a-1})\to0$, so the Rayleigh-quotient contradiction is valid.

For the trace-one minimizer, the normalized regular solution has finite energy. Its weak equation extends from smooth zero-trace tests using form continuity and Hardy's inequality. Every competing $H^1$ function with the same traces differs by an element of $H_0^1$. This also shows that every competitor in the stated affine trace class has finite potential energy. The shifted form is strictly coercive on the difference space when $T<\lambda_D(a)$. Orthogonality cancels the mixed term, proving uniqueness of the minimizing extension. The response identity follows from integration by parts with the already controlled endpoint product.

## 3. Differential recurrence

For $A_a=\partial_z-a/z$ and $B_a=\partial_z+a/z$, direct composition gives

$$
-B_aA_a=-\partial_z^2+a(a-1)z^{-2},\qquad
-A_aB_a=-\partial_z^2+a(a+1)z^{-2}.
$$

The intertwining identity follows as an identity of differential expressions. The proof correctly refrains from asserting preservation of Dirichlet operator domains by these first-order factors.

The normalized leading term of $A_a u_a$ is $-Tz^{a+1}/(2a+1)$. Uniqueness of the order-$a+1$ regular solution gives the first recurrence identity; applying $B_a$ gives the second. Positivity of both interface values is established using spectral ordering before division. Therefore the denominator in

$$
D_s=s-\frac{T}{s+D_{s+1}}
$$

is strictly positive. All functions in each identity use the same energy $T$, and the proof covers every real $s>1$, including the larger orders used in the noncrossing high proof.

## 4. Direct rational-Riccati barrier

The parameter identities are exact:

$$
T=c(2a+5-c),\qquad C=M-c,\qquad
H(1)=AM-Ac-T=CD>0.
$$

Since $B=Ac+T>0$, the denominator $H(z)=AM-Bz^2$ is at least $CD$ on $[0,1]$. Also $M-cz^2\ge C>0$. Thus the comparison function is positive and its defining integral is smooth; no additional pole-free assumption is introduced.

Writing $x=z^2$ and $f(x)=T(M-cx)/(AM-Bx)$, independent differentiation confirms

$$
f'(x)=\frac{T^2M}{H^2},\qquad Af-T=\frac{T^2x}{H}.
$$

The logarithmic derivative $w'/w=a/z-zf(z^2)$ consequently gives

$$
\frac{(L_a-T)w}{w}
=\frac{T^2x}{H^2}\left[H+2M-(M-cx)^2\right].
$$

The constant term in the bracket is $M(A+2-M)=0$. Its linear coefficient is $(2M-A)c-T=c^2$, and its quadratic coefficient is $-c^2$. This proves the stated factorization

$$
\frac{(L_a-T)w}{w}
=\frac{T^2c^2z^4(1-z^2)}{H(z)^2}>0
\qquad(0<z<1).
$$

The regular asymptotics cancel the leading Wronskian terms and give zero limit at the singular endpoint. Positivity of the residual and of both functions therefore gives the strict response comparison. Its interface value is exactly $a-T/D$, preserving the existing $\mathsf T$.

The optional closed form was also checked. Its logarithmic derivative simplifies because

$$
cH+MT=(Ac+T)(M-cz^2)=B(M-cz^2).
$$

It is therefore the same normalized barrier as the integral form, with all real powers applied to strictly positive bases.

## Conclusion

The proposal preserves the original parameter ranges and spectral assumptions and proves both the required recurrence and the original tail comparison. The direct comparison is stronger than its retained non-strict statement. The differential-equation wording clarification has been addressed. No mathematical gap or integration blocker was found.
