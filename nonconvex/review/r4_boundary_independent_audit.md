# Independent audit of the R4 M.4 uniform-convexity proposal

## Result and scope

**No mathematical gap found.** The complete argument in
`r4_boundary_proposal.md` proves the unchanged assertion of
`lem-other-branch` on the full domain
$\mathcal D_*\cap\{q>p\}$, including points without the container
restriction. Its stronger internal bound
$\mathcal G-\mathcal B>419/2400>1/6$ follows as stated.

This audit independently compared the proposal with `def-analytic`,
the declaration and inherited proof of `lem-other-branch`, and the
stated pole-free conclusions used by the proposal. The R4 preflight
was completed independently: external basis absent; configuration
`codex / gpt-6.1-sol / xhigh`, strict citations/rigor/disproof rigor,
fresh context, and assumptions forbidden. No qmd-prover or Quarto
execution was available. This is an independent mathematical audit,
not an official verifier verdict. No manuscript source was edited.

## 1. The geometric range is valid with only $h>2$

The area-condition conversion
$p(1-q)>h(h+2)/[(1+h)(h^2+2h+2)]$ follows from the definition using
$p=ha/(1+h)$. The proof uses $q>p$ and $q\le h/(1+h)$ in the
small-height contradiction, both valid on the stated domain. The
identity

$$
h^3-h^2-4h+2=(h-2)(h-1)(h+2)-2
$$

does imply $j(h)>1/4$ on $1\le h\le2$. Thus $h>2$ is sufficient;
the old stronger threshold $h>7/3$ is not being used implicitly.

Since $m=q$ and $q(1-q)\le1/4$,

$$
R>\frac{4h}{h^2+2h+2}\ge\frac8{13}
\qquad(2<h\le4).
$$

The derivative of the middle function is
$4(2-h^2)/(h^2+2h+2)^2<0$ on the entire interval. With
$\Pi>49/5$, the exact product comparison

$$
\frac{\Pi R^2}{2}>\frac{1568}{845}
>\frac{741}{400}=\frac{39}{20}\frac{19}{20}
$$

establishes $\sigma>39/20$ everywhere on the branch. No additional
height split or container assumption is required.

## 2. Energy and denominator hypotheses are complete

The inequality $q>p$ gives
$S_0>Lp+(1-p)^{-1}$. Here $0<p<1$, and the use of
$p(1-p)\le1/4$ in an increasing function is legitimate. The resulting
strict energy bound is exactly

$$
E<\frac{3\Pi(1+h)}{h(h+2)(h+5)}.
$$

The two displayed logarithmic derivatives prove the required
monotonicity, giving $K/\Pi<9/56<1/6$ and $T<11$. The step
$K<E$ uses $A>0$, available from the cited pole-free lemma.

Combining $\sigma>39/20$ and $T<11$ gives the stated bounds

$$
r>\frac{59}{10},\qquad C>\frac{27}{5},\qquad
D>\frac{773}{270}>\frac{20}{7}>0.
$$

Every division has a positive denominator. In particular,
$\mathsf T=\sigma-T/D>39/20-7T/20$ follows directly and needs no
derivative theorem or path through an auxiliary parameter domain.

## 3. The complete response reduction is correct

The three positive coefficients of the losses in $\mathsf H$ sum
exactly to $1/3$. Each denominator is at least $1-K/\Pi>0$.
Consequently the common-denominator bound has the correct direction,
and $K/\Pi<1/6$ yields
$\mathsf H(K)>1-2K/5>1-2E/5$.

Combining this with the affine tail bound and $T=h^2E$ gives the
coefficient $(8+7h)/20$ of the energy loss. Substituting the strict
energy bound and $\Pi<10$ has the correct direction. The resulting
partial-fraction identity is exactly

$$
F(h)=1+\frac{3}{4h}+\frac{3}{2(h+2)}-
\frac{54}{5(h+5)}.
$$

The cancellation of $\mathcal B$ in this reduction is justified by
the definition of $\mathcal G$; no lower estimate for the gain is
needed before the final positivity assertion.

## 4. Curvature, tangent, and strict final margin

Both ratios in the formula for $(h+5)^3F''/2$ attain their minimum
at $h=4$. The proposed coarser ratio bounds imply the positive lower
bound $21/80$. Thus the supporting-tangent argument is valid on the
whole closed interval $[2,4]$.

The exact anchor values are $F(3)=1/5$ and $F'(3)=61/2400>0$.
Since every admissible point has $h>2$, the tangent is strictly
larger than $419/2400$. Hence the stronger response margin is strict
even where the supporting-tangent inequality is an equality.
Finally, $0<A<1$ and $0<w<1$ give $\mathcal B>0$, completing the
unchanged declaration's last inequality.

## Supplementary corroboration and integration scope

An independently written exact calculation using Python `Fraction`
and the existing rational-function algebra checked 20 identities and
scalar comparisons, including the geometric cubic, the derivative of
$4h/D_h$, the order product, both logarithmic derivatives, the
radical/denominator constants, the complete response partial fractions,
the curvature identity, and the tangent data. All 20 passed. There
was no numerical sampling. The written reasoning above, rather than
execution of this calculation, establishes the full parameter ranges.

The new proof may replace the linked proof of `lem-other-branch`
without changing its declaration. Its logical inputs are
`def-analytic`, `lem-pole-free`, and `lem-pi-rational`; the old
`lem-derivatives` dependency is unnecessary for this proof. The
remaining uses of that lemma elsewhere are unaffected.
