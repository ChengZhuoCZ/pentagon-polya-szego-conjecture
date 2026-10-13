# R4 noncrossing spectral bounds by one positive comparison family

## Status, scope, and preflight

**Status: integrated into the R4 QMD manuscript and independently reviewed.** The argument
below proves the full existing statement of `lem-no-crossing-sturm` with
the same constants. It replaces the adjacent-order response chains by a
single positive comparison-function family and a direct quadratic-form
identity on the complete interval.

The R4 `AGENTS.md` and configuration were independently read before the
derivation. The external-basis file is absent. Configuration remains
`codex / gpt-6.1-sol / xhigh`, with strict citations, rigor, and
rigor-disprove, fresh context, and assumptions forbidden. Neither
`qmd-prover` nor Quarto is available on PATH. This report is an independent
derivation, not an official verifier verdict.

For real $2\le a\le3$, retain the operator $K_{a;1,\delta}$ and

$$
\Lambda_a(\delta)=(1+\delta)^2\lambda_1(K_{a;1,\delta})
$$

from `def-high-operator` and `lem-no-crossing-sturm`. The claimed
monotonicity for all $\delta\ge0$ is unchanged. The required strict bounds
for $0\le\delta\le1/4$ are

$$
\Lambda_2(\delta)>\frac{625}{32}>\frac{39}{2},\qquad
\Lambda_3(\delta)>\frac{1525}{48}>\frac{1587}{50}.
\tag{N.1}
$$

The same comparison formula, with the fixed constant $c=1/23$, handles
the two pairs

$$
(a,E)=\left(2,\frac{25}{2}\right),\qquad
(a,E)=\left(3,\frac{61}{3}\right).
\tag{N.2}
$$

No spectral assertion at an interpolated energy for other orders is needed
or claimed. The continuous order range remains relevant to the unchanged
monotonicity statement.

## 1. Scaling reduces the problem to one complete interval

Put $L_\delta=1+\delta$. The unitary change of variables
$v(z)=L_\delta^{1/2}u(L_\delta z)$ takes
$L_\delta^2K_{a;1,\delta}$ to the form

$$
\int_0^1\left(|v'|^2+
\frac{a(a-1)}{z^2}\mathbf1_{\{z<1/(1+\delta)\}}|v|^2\right)dz.
\tag{N.3}
$$

All these forms have the common domain $H_0^1(0,1)$ by the Hardy
inequality already proved in `def-high-operator`. Their potential is
pointwise nonincreasing in $\delta$. The Rayleigh principle therefore
shows that $\Lambda_a$ is nonincreasing for every real $2\le a\le3$ and
every $\delta\ge0$.

It is enough to prove

$$
\lambda_1(K_{2;1,1/4})>\frac{25}{2},\qquad
\lambda_1(K_{3;1,1/4})>\frac{61}{3}.
\tag{N.4}
$$

The full physical interval is now $(0,5/4)$, with potential
$a(a-1)/z^2$ on $(0,1)$ and zero potential on $(1,5/4)$.

## 2. A single rational logarithmic derivative on the singular side

For either pair in (N.2), define

$$
A=2a+1,\quad
\alpha=\frac EA,\quad
\beta=\frac{\alpha^2}{A+2},\quad
\gamma=\frac{2\alpha}{A+4},\quad
c=\frac1{23},\quad
\theta=\frac{E}{(A+2)(A+4)}.
\tag{N.5}
$$

For $0\le t\le1$, put

$$
H(t)=1-\gamma t-ct^2,\qquad
Y(t)=\alpha+\frac{\beta t}{H(t)}.
\tag{N.6}
$$

The comparison function is given directly by an ordinary integral of a
positive-denominator rational function:

$$
w(z)=z^a\exp\left[-\frac12\int_0^{z^2}Y(t)\,dt\right]
\qquad(0<z\le1).
\tag{N.7}
$$

At the two parameter pairs, $\gamma$ is respectively $5/9$ and
$122/231$. Hence

$$
H(t)\ge1-\frac59-\frac1{23}=\frac{83}{207}>0.
\tag{N.8}
$$

Thus $w$ is positive, smooth away from zero, and has the explicit regular
behavior

$$
w(z)=z^a(1+O(z^2)),\qquad
w'(z)=a z^{a-1}+O(z^{a+1}).
\tag{N.9}
$$

In particular, $w$ has finite $H^1$ norm and finite inverse-square
potential energy near zero. It is an explicitly constructed comparison
function, not a solution whose existence or positivity needs an ODE
argument.

### Exact differential identity

Writing $t=z^2$, logarithmic differentiation of (N.7) gives

$$
\frac{w'}w=\frac az-zY(t),
$$

and therefore

$$
\frac{(-\partial_z^2+a(a-1)z^{-2}-E)w}{w}
=A Y+2tY'-tY^2-E.
\tag{N.10}
$$

The complete residual factors as

$$
A Y+2tY'-tY^2-E
=\frac{\alpha^2t^3}{H(t)^2}
\left[\frac{c(A+6)}{A+2}-(\theta+ct)^2\right].
\tag{N.11}
$$

Here is a direct derivation without a coefficient-sign calculation.
The identities

$$
H-tH'=1+ct^2,\quad
(A+2)\beta=\alpha^2,\quad
(A+4)\gamma=2\alpha
$$

first cancel the constant, linear, and quadratic terms of
$H^2(AY+2tY'-tY^2-E)$. Put
$d=\alpha\gamma-\beta=A\beta/(A+4)=\alpha\theta$.
The remaining expression is

$$
t^3\{\beta c(A+6)-(d+\alpha ct)^2\},
$$

which is exactly the right side of (N.11) multiplied by $H^2$.
The proof uses the displayed square, rather than signs of an expanded
polynomial.

### One uniform strict sign estimate

At the two pairs, $\theta$ is $25/126$ and $61/297$. Thus

$$
0<\theta+ct\le\frac{61}{297}+\frac1{23}<\frac14,
\qquad
\frac{c(A+6)}{A+2}\ge\frac{13}{207}>\frac1{16}.
\tag{N.12}
$$

The exact gaps are

$$
\frac14-\frac{61}{297}-\frac1{23}=\frac{31}{27324},
\qquad
\frac{13}{207}-\frac1{16}=\frac1{3312}.
$$

Consequently, for every $0<z\le1$,

$$
\frac{(-\partial_z^2+a(a-1)z^{-2}-E)w}{w}
>\frac{\alpha^2z^6}{3312 H(z^2)^2}>0.
\tag{N.13}
$$

This proves the singular-side differential inequality on the whole
interval with the same formula and the same constant for both orders.

## 3. A positive polynomial on the free side

Put $q=E/16$. Thus $q=25/32$ or $61/48$, and in either case
$0<q<4$. Use the same polynomial that underlies
`lem-free-sturm-bound`:

$$
p_q(x)=x\left(1-\frac{qx^2}{12}\right)^2.
\tag{N.14}
$$

It is positive on $(0,1]$, vanishes linearly at zero, and satisfies the
explicit differential identity

$$
-p_q''-q p_q=\frac{q^2x^3}{144}(4-qx^2)>0
\qquad(0<x\le1).
\tag{N.15}
$$

No trigonometric response estimate is needed. On the physical free
interval put $x=5-4z$, so $x$ decreases from $1$ to $0$. Define a single
continuous comparison function on the full physical interval by

$$
g(z)=
\begin{cases}
w(z)/w(1),&0<z\le1,\\[2mm]
p_q(5-4z)/p_q(1),&1\le z<5/4.
\end{cases}
\tag{N.16}
$$

Then $g(1)=1$, $g>0$ in the open interval, $g\in H_0^1(0,5/4)$,
and its inverse-square potential energy is finite. The free-side
residual is positive because

$$
(-\partial_z^2-E)g
=\frac{16}{p_q(1)}\left(-p_q''-q p_q\right)(5-4z)>0.
\tag{N.17}
$$

The physical energy is the same $E$ on both pieces. The factor $16$ and
the reversed coordinate in (N.17) make the scaling explicit.

## 4. The derivative jump is strictly positive

At the interface,

$$
g'(1^-)=a-\alpha-\frac{\beta}{H(1)},\qquad
g'(1^+)=-4\frac{p_q'(1)}{p_q(1)}.
\tag{N.18}
$$

Write $D_a=g'(1^-)$ and
$F_a=-g'(1^+)=4p_q'(1)/p_q(1)$. The polynomial gives directly

$$
F_a=4\left(1-\frac{q}{3-q/4}\right).
\tag{N.19}
$$

There are just two direct scalar comparisons; there is no adjacent-order
chain. For $a=2$, substitution in (N.18) gives

$$
D_2+\frac{11}{4}=\frac{27}{1162}>0,
\qquad
F_2-\frac{11}{4}
=\frac{1036}{359}-\frac{11}{4}
=\frac{195}{1436}>0.
\tag{N.20}
$$

For $a=3$, the corresponding comparisons are

$$
D_3+\frac{21}{10}=\frac{2071}{307260}>0,
\qquad
F_3-\frac{21}{10}
=\frac{1084}{515}-\frac{21}{10}
=\frac1{206}>0.
\tag{N.21}
$$

Therefore the jump with the sign needed for a positive supersolution is

$$
J:=g'(1^-)-g'(1^+)=D_a+F_a>0.
\tag{N.22}
$$

The comparison function deliberately has this derivative jump. It is
not asserted to belong to the operator domain, whose derivatives match
at the interface. Its membership in the form domain is sufficient for
the following direct identity.

## 5. Ground-state identity and strict spectral conclusion

On each open piece set

$$
\rho(z)=\frac{-g''(z)+(V(z)-E)g(z)}{g(z)},\qquad
V(z)=\frac{a(a-1)}{z^2}\mathbf1_{(0,1)}(z).
\tag{N.23}
$$

By (N.13) and (N.17), $\rho>0$ on both open pieces. It is bounded:
the singular-side formula extends to zero with value zero, and on the
free side it is

$$
\rho(z)=\frac{q^2x^2(4-qx^2)}
{9(1-qx^2/12)^2},\qquad x=5-4z,
$$

which also extends to the outer endpoint with value zero. Finite
one-sided values at $z=1$ suffice; no continuity across the potential
jump is required.

For $u\in C_c^\infty(0,5/4)$, integration by parts separately on the two
pieces gives

$$
\begin{aligned}
\mathfrak q_a[u]-E\|u\|_2^2
&=\int_0^{5/4}g^2\left|\left(\frac ug\right)'\right|^2 dz
+\int_0^{5/4}\rho|u|^2\,dz+J|u(1)|^2.
\end{aligned}
\tag{N.24}
$$

The outer boundary terms vanish because $u$ is compactly supported.
The two interface terms add to
$(g'(1^-)-g'(1^+))|u(1)|^2=J|u(1)|^2$, because $g(1)=1$.
This also checks the sign of the derivative jump directly.

Discard the first nonnegative integral. The form-core density and
Hardy inequality in `def-high-operator`, boundedness of $\rho$, and
continuity of the one-dimensional trace at $1$ extend the resulting
inequality to all $u\in H_0^1(0,5/4)$:

$$
\mathfrak q_a[u]-E\|u\|_2^2
\ge\int_0^{5/4}\rho|u|^2\,dz+J|u(1)|^2.
\tag{N.25}
$$

For every nonzero $u$, the first integral on the right is strictly
positive, since $\rho>0$ almost everywhere. Compactness of the form
embedding, already established for `def-high-operator`, means that the
lowest Rayleigh quotient is attained. Applying (N.25) to a nonzero first
eigenfunction gives $\lambda_1(K_{a;1,1/4})>E$. The attainment step is
essential: positivity of every individual shifted Rayleigh quotient
alone would only imply a nonstrict lower bound on its infimum.

This proves (N.4). Multiplying by $(5/4)^2$ and using the monotonicity
in Section 1 gives (N.1), including $\delta=0$. The retained final
scalar margins are

$$
\frac{625}{32}-\frac{39}{2}=\frac1{32},\qquad
\frac{1525}{48}-\frac{1587}{50}=\frac{37}{1200}.
$$

## 6. What this changes, and what it does not change

The inherited R3 argument already proves (N.1) rigorously. The new work
is the direct rational logarithmic derivative (N.6), its positive-square
residual (N.11)–(N.13), and the glued whole-interval argument
(N.16)–(N.25). These replace all of the following within H.6:

- the separate lower bound for the inverse-square Dirichlet spectrum;
- normalized exact regular solutions and their positivity argument;
- two or three adjacent-order recurrence substitutions;
- the Gaussian seed at a higher order;
- the trigonometric free response and the separated-spectrum interface
  criterion.

The common-domain/scaling argument, the full statement of
`lem-no-crossing-sturm`, the geometric high-height assembly, and every
downstream constant remain unchanged. The free polynomial is inherited
from H.4; only its direct use in the complete comparison function is new.
No coefficient-sign table, numerical interval partition, spectral
approximation, or execution of code is part of the proof.

If integrated, `lem-tail-recurrence` is no longer used by `high.qmd`, so
its import there can be removed after a reference search. H.5 still
requires `lem-regular-tail`, `lem-cot-rational`, and `lem-interface`.
The recurrence declaration in `robin.qmd` need not be deleted merely
because this import becomes unnecessary.

The proposal preserves the nonconvex-exclusion scope and all protected
goals and locks. It makes no new claim about the conditional convex
bridge.

## 7. Supplementary exact checks

`check_r4_noncrossing.py` uses Python's standard library and the existing
`rational_algebra.py`. It checks identities in a formal variable and
exact rational scalar comparisons, without floating-point arithmetic,
parameter grids, or sampled differential equations. Its JSON report is
`r4_noncrossing_exact_checks.json`. The derivation above is complete
without running the script. All 47 supplementary exact checks passed.
