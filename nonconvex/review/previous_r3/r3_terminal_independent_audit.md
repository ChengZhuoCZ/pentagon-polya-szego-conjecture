# Independent audit of the final R3 single-majorant T.3 proof

## Scope and verdict

The selected version uses the global curvature correction

$$
F(h)=G(h)+\frac1{2(h+2)}
$$

and proves the strict lower bound

$$
Z_\Psi(h)>\frac{289}{136800}>\frac{27}{16000}
\qquad\left(\frac38\le h\le4\right).
$$

This final coarse-constant version passes independent mathematical audit. The original $Z_\Psi$, its full parameter range, and the declared margin $27/16000$ are preserved. The preliminary stronger correction by $2/[5(h+2)]$ is unnecessary and is not the selected version.

The review covers the exact reciprocal identity, the squared polynomial remainder, all normalized-curvature signs and interval implications, the scalar comparisons, and the corrected tangent argument. Exact rational calculations independently reconstructed the original $Z_\Psi$ from `def-terminal-rationals` and confirmed its retained partial fractions. No sampled parameters, floating-point estimates, or numerical spectral values were used to infer a sign. No manuscript source was edited by this audit, and no official qmd-prover verdict is claimed.

## 1. The single reciprocal majorant is valid on the complete interval

The unchanged introductory proof supplies $0<k=N/D<1/L<1$, so $D-N>0$. All factors in the denominator of

$$
M-S=\frac{P}{90h(h+2)^2(D-N)}
$$

are therefore positive. Independent rational-function subtraction confirms both this identity and the proposed product expression for $P$.

The squared-remainder identity was checked as an exact polynomial identity:

$$
P=\frac{17937}{32}-\frac{51717}{8}(h-1/2)+(h-1/2)^2H(h).
$$

On $3/8\le h\le4$, the last part of $H$,

$$
h^2(4-h)(6600h^2+39410h+52858),
$$

is nonnegative, including at the endpoint $h=4$. The remaining quadratic has positive derivative for $h>0$ and value $12935259/128>100000$ at $3/8$. Thus $H>100000$ everywhere in the required interval.

The minimum of the resulting quadratic in the unrestricted real variable $h-1/2$ gives

$$
P\ge\frac{17937}{32}-\frac{(51717/8)^2}{400000}
=\frac{11674951911}{25600000}>450.
$$

This proves $S<M$ and hence $Z_\Psi=R_0-S>R_0-M=G$ on the entire original height range. No sign condition on $h-1/2$ was assumed.

## 2. Normalized curvature and its monotonicity

With $x=1/(h+2)$, the height interval maps exactly to

$$
\frac16\le x\le\frac8{19}.
$$

Independent differentiation of the retained partial fractions confirms

$$
\frac{(h+2)^3G''(h)}2
=Q(x)=b_4-\frac92+3Cx-f(x)
-\frac{b_5}{(1+7x/60)^3}-\frac{\epsilon}{(1-2x)^3},
$$

where $C=b_3-6/5<0$, $\epsilon=407/5760000>0$, and

$$
f(x)=\frac{b_2(1-x)-3b_1x}{(1-x)^4}.
$$

All denominators are positive. The displayed formulas for $f'$ and $f''$ are correct. In particular, the numerator governing the sign of $f''$ is decreasing and affine. Thus $f'$ is monotone or increases and then decreases, so its minimum on $[1/6,2/5]$ occurs at an endpoint.

The selected coarse endpoint comparisons hold:

$$
f'(1/6)>\frac{3}{(5/6)^5}>3,
$$

using $b_2>3$ and $b_1<1$, and

$$
f'(2/5)>
\frac{625}{81}\left(3\frac{637}{200}-11\frac{21}{25}\right)
=\frac{175}{72}>\frac{12}{5},
$$

using $b_2>637/200$ and $b_1<21/25$. All four coefficient bounds follow directly from the retained exact constants.

Consequently $f'>12/5$ on the complete interval. Differentiating $Q$, the $3C$ and $\epsilon$ contributions are negative, while the derivative of its shifted reciprocal loss is less than $(7/20)b_5$. Since $b_5<61/10$,

$$
Q'<-\frac{12}{5}+\frac7{20}\frac{61}{10}
=-\frac{53}{200}<0
\qquad\left(\frac16\le x\le\frac25\right).
$$

## 3. The coarse curvature bounds require no exact curvature endpoint values

On $2/5\le x\le8/19$, replacing $b_2$ by $319/100$ and $b_1$ by $67/80$ increases the numerator of $f$. The exact scalar maximum formula

$$
\max_{x<1}\frac{a-(a+3b)x}{(1-x)^4}
=\frac{(a+3b)^4}{256b^3}
$$

is valid for every $a,b>0$: its derivative is positive before $(a-b)/(a+3b)$ and negative afterwards. At the selected rational values its maximum is strictly below $176/25$.

The remaining bounds were checked against the retained exact constants:

$$
\begin{aligned}
b_4-\frac92+3Cx
&\ge b_4-\frac92+\frac{24C}{19}>\frac{119}{10},\\
\frac{b_5}{(1+7x/60)^3}
&\le b_5\left(\frac{150}{157}\right)^3<\frac{16}{3},\\
\frac{\epsilon}{(1-2x)^3}
&\le\epsilon\left(\frac{19}{3}\right)^3<\frac1{50}.
\end{aligned}
$$

The signs in these substitutions are correct: $C<0$ puts the affine minimum at $8/19$, the first reciprocal loss decreases with $x$, and the second increases with $x$. Therefore

$$
Q>\frac{119}{10}-\frac{176}{25}-\frac{16}{3}-\frac1{50}
=-\frac{37}{75}>-\frac12
$$

on the cap interval, including $x=2/5$. Since $Q$ decreases on $[1/6,2/5]$, this same lower bound extends to that entire interval. An exact evaluation of $Q(2/5)$ is unnecessary.

The stronger sign needed at large heights follows from one coarse comparison at $x=2/7$:

$$
f(2/7)<\frac{343}{625}
\left(5\frac{319}{100}-6\frac{67}{80}\right)
=\frac{149891}{25000}<6,
$$

and

$$
\frac{b_5}{(1+7(2/7)/60)^3}
<\frac{61}{10}\left(\frac{30}{31}\right)^3<\frac{28}{5}.
$$

The affine and $\epsilon$ bounds above hold there as well. Hence

$$
Q(2/7)>\frac{119}{10}-6-\frac{28}{5}-\frac1{50}
=\frac7{25}>\frac14.
$$

Monotonicity of $Q$ now gives $Q>0$ on $[1/6,2/7]$. In height coordinates this is precisely $3/2\le h\le4$.

## 4. The convex correction and final strict margin

For $F=G+1/[2(h+2)]$,

$$
F''=\frac{2}{(h+2)^3}(Q+1/2)>0.
$$

The tangent at $h=1$ rearranges exactly to

$$
G(h)\ge G(1)+G'(1)(h-1)
-\frac{(h-1)^2}{18(h+2)}.
$$

The retained exact values satisfy

$$
G(1)=\frac{208251137}{16401600000}>\frac1{80},
\qquad
-\frac1{400}<G'(1)=-\frac{42620371163}{18402595200000}<0.
$$

For $3/8\le h\le3/2$, the linear term is greater than $-1/800$: it is nonnegative below $1$ and $h-1\le1/2$ above $1$. Also

$$
\frac{(h-1)^2}{18(h+2)}
\le\frac{(5/8)^2}{18(19/8)}=\frac{25}{2736}.
$$

Thus

$$
G(h)>\frac1{80}-\frac1{800}-\frac{25}{2736}
=\frac{289}{136800}>\frac{27}{16000}.
$$

For $3/2\le h\le4$, the established $Q>0$ gives $G''>0$. Independent exact differentiation confirms

$$
G'(3/2)=\frac{5115313959269}{1118040013125000}>0.
$$

Consequently $G$ increases on this upper interval, and its lower bound at $3/2$ extends throughout. Combining with $Z_\Psi>G$ proves the unchanged target margin over the full original range.

## Final assessment

The selected single-majorant proof closes without a gap. The change preserves all initial head, gain, and shared-energy comparisons and requires no new hypothesis. Its interval arguments are explicit analytic curvature arguments, and its remaining polynomial is controlled by the displayed squared remainder and upper-endpoint factor. The final source should use the coarse $1/2$ correction and margin $289/136800$ consistently; the earlier $2/5$ correction belongs only to route history. No additional tuning or numerical investigation is needed.
