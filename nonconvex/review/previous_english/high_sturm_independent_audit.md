# Independent audit of the H.6 Sturm comparison

Date: 2026-10-12

## Result and scope

The new `lem-no-crossing-sturm` in `workspace/high.qmd`, equations H.6.2–H.6.9, and its use in `lem-high` were independently rederived from the source. The imported adjacent-order recurrence and common-interface criterion were also read. No mathematical correction is required.

This review checked the differential identities, signs, endpoint conditions, denominator positivity, coordinate scaling, and theorem assembly. Exact rational arithmetic supplied a secondary check of the displayed constants. It is not official QMD-Prover verification. No proof source, canonical goal, or configuration file was edited during this audit.

## Scaling and Dirichlet positivity

Unitary scaling of $(0,1+\delta)$ to $(0,1)$ gives the potential

$$
\sigma(\sigma-1)z^{-2}\mathbf 1_{\{z<1/(1+\delta)\}}.
$$

Hardy's inequality gives the same form domain $H_0^1(0,1)$ for every finite $\delta\ge0$. Increasing $\delta$ decreases this potential. Thus $\Lambda_\sigma(\delta)$ is nonincreasing, and its value at $\delta=1/4$ is a lower bound throughout $[0,1/4]$. The endpoint $\delta=0$, where the free interval is empty, is covered.

For $f(x)=\sin x-x\cos x-x^2\sin x/3$,

$$
f'(x)=\frac{x}{3}(\sin x-x\cos x)>0\qquad(0<x<\pi).
$$

This proves the claimed strict cotangent inequality. Direct differentiation of $g_a=z^{a-1}\sin(\pi z)$ gives

$$
-\frac{g_a''}{g_a}+\frac{a(a-1)}{z^2}
=\pi^2+\frac{2(a-1)}{z^2}(1-\pi z\cot(\pi z)).
$$

The ground-state identity on the smooth core and Hardy density consequently establish $\lambda_D(a)\ge(2a+1)\pi^2/3$. Hence $E_2=25/2<15<\lambda_D(2)$ and $E_3=61/3<21<\lambda_D(3)$. Potential ordering gives the same strict spectral separation at every higher order used in the recurrence. The free-side Dirichlet eigenvalue is $16\pi^2$, also above both energies. A first zero of any regular solution would give a forbidden zero-trace Rayleigh function, so all response denominators are finite.

## Singular-side comparison and recurrence orientation

For $v=z^j e^{-cz^2/2}$,

$$
\frac{v''}{v}=\frac{j(j-1)}{z^2}-c(2j+1)+c^2z^2.
$$

The residual in H.6.4 follows. With $W=u_j'v-u_jv'$, its derivative is the positive regular solution times that residual and $W(0)=0$. Thus a nonnegative residual gives $D_j\ge j-c$, with the direction stated in the proof.

The adjacent-order identities give

$$
D_a=a-\frac{E}{a+D_{a+1}},\qquad
a+D_{a+1}=(2a+1)\frac{u_a(1)}{u_{a+1}(1)}>0.
$$

The recurrence map is increasing on this branch because its derivative is $E/(a+X)^2>0$. All substitutions and constants were reproduced:

| Order | Minimum Gaussian residual | Successive response lower bounds | Successive denominator lower bounds |
| --- | --- | --- | --- |
| $2$ | $3/16$ | $D_4\ge9/4$, $D_3\ge13/21$, $D_2\ge-61/22$ | $21/4$, $55/21$ |
| $3$ | $5/36$ | $D_6\ge25/6$, $D_5\ge153/55$, $D_4\ge1121/1119$, $D_3\ge-9319/4478$ | $55/6$, $373/55$, $4478/1119$ |

Every lower bound in the last column is positive; no pole or change of recurrence branch is crossed.

## Free response and the physical interface

Expanding $p_q=z-qz^3/6+q^2z^5/144$ gives exactly

$$
-p_q''-qp_q=\frac{q^2z^3}{144}(4-qz^2).
$$

For $0<q\le4$, both $p_q$ and $\sin(\sqrt q\,z)/\sqrt q$ are positive on $(0,1]$. The Wronskian has the same orientation as on the singular side. Moreover,

$$
\frac{p_q'(1)}{p_q(1)}=1-\frac{q}{3-q/4},
$$

with positive denominator. A physical free interval of length $1/4$ therefore has outward response at least $4(1-q/(3-q/4))$, where $q=E/16$. The two free-response lower bounds are $1036/359$ and $1084/515$, giving exactly

$$
\frac{893}{7898}>0,
\qquad
\frac{54867}{2306170}>0
$$

for the total interface responses.

The coordinate change $x=5-4z$ sends the original free interval to $(0,1)$ and the singular interval to $(1,5)$. After division of the differential equation by $16$, the potential is

$$
0\quad(0<x<1),\qquad
\frac{\sigma(\sigma-1)}{(5-x)^2}\quad(1<x<5),
$$

and the energy is $E/16$. The singular-side outward derivative becomes $D_\sigma/4$; the free-side outward derivative becomes $\sqrt E\cot(\sqrt E/4)/4$. Thus both responses use the same transformed energy and the same interface, and both are divided by the same positive factor. The transformed form is compact, its potential is bounded near the interface with one-sided limits, and its outer conditions are precisely those of `lem-interface`. That lemma gives the required strict spectral inequalities.

## Final constants and noncrossing assembly

Multiplication by $(5/4)^2$ gives $625/32$ and $1525/48$. Their margins are exactly

$$
\frac{625}{32}-\frac{39}{2}=\frac1{32},\qquad
\frac{1525}{48}-\frac{1587}{50}=\frac{37}{1200}.
$$

For $2/3<r<1$, the convex endpoint comparison with $\pi^2<987/100$ gives the values $779/25$ and $1587/50$, as stated. For order two, the already established endpoint bounds are below $39/2$. Combining these bounds with $\eta<(1+\delta)^{-2}$ and the unchanged form comparison yields

$$
E_\tau h^2
<\frac{B_\sigma}{(1+\delta)^2}
<\lambda_1(K_{\sigma;1,\delta})
\le h^2\mu_\tau.
$$

This contradicts the required candidate inequality for the chosen positive weight. The monotonicity range includes every $\delta=1/h$ with $h\ge4$. The argument requires no subdivision at $\delta=1/9$ and makes no assertion about the removed inverse-trace surrogate.
