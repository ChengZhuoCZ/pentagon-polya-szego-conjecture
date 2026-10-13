# R3 proposal: one reciprocal majorant and a global curvature correction for T.3

**Current status:** the selected derivation has been integrated into the R3 manuscript and independently reviewed. Historical proposal wording below records its development; it is not pending work.
## Recommendation and exact scope

Replace the two reciprocal comparisons and the two response arguments in the proof of `lem-psi-payment` with the argument below. Preserve the declaration, its full height interval $3/8\le h\le4$, the original rational function $Z_\Psi$, and its stated strict margin $27/16000$. The new proof actually obtains the stronger intermediate bound

$$
Z_\Psi>\frac{289}{136800}>\frac{27}{16000}.
$$

The introductory estimates of $e,k,H_2$ and the gain, the shared head and tail energy, and the concluding comparison to the original response remain unchanged. The common partial-fraction identity (T.3.1) is retained. Its six constants are used explicitly; no new auxiliary definition or import is needed.

The substantial change is a single reciprocal majorant on the entire height interval, followed by one global convex correction and one tangent. This removes the old lower-chart curvature calculation, the upper-chart second derivative of the normalized curvature, its zero count, and the interior-extrema argument. It also replaces the two old head-comparison polynomials with one short squared-remainder identity. The new head calculation does retain an auxiliary polynomial, so this should not be described as eliminating every polynomial identity. Its sign follows from the displayed endpoint factor and an ordinary quadratic minimum, without a coefficient table.

No manuscript has been edited for this proposal.

## Preflight and verification limits

I independently read this R3 project's `AGENTS.md` and `.qmd-prover/config.yml`. The external-basis file is absent, so external mathematics is unrestricted subject to checking its hypotheses. Only elementary one-variable differentiation, the second-order tangent inequality, and convexity are used here. The configured backend remains Codex, model `gpt-6.1-sol`, effort `xhigh`, with strict citations, rigor, and disproof rigor, and assumptions forbidden. No protected statement, lock, configuration, or frozen R2 file is changed.

The official qmd-prover workflow remains unavailable in this environment. The proof below and the exact algebraic corroboration do not constitute an official local or global verification verdict.

## 1. Existing objects and one majorant

Let $3/8\le h\le4$, $L=1+h$, and retain the definitions from `def-terminal-rationals`. Write

$$
N=300h^3+1295h^2+1349h-96,\qquad
D=2hL(h+2)^2(60h+127),\qquad
S=\frac{2hN}{D-N},\qquad R_0=Z_\Psi+S.
$$

The unchanged opening of T.3 proves $0<k=N/D<1/L<1$, so $D-N>0$. The existing exact identity is

$$
\begin{aligned}
R_0(h)={}&\frac{389h}{3350}-\frac{25913}{33500}
-\frac{b_0}{h}+\frac{b_1}{(h+1)^2}-\frac{b_2}{h+1}\\
&+\frac{b_3}{(h+2)^2}+\frac{b_4}{h+2}
-\frac{b_5}{h+127/60},
\end{aligned}
$$

where

$$
\begin{gathered}
b_0=\frac{213469}{1920000},\quad b_1=\frac{225}{268},\quad
b_2=\frac{11452440743}{3591200000},\\
b_3=\frac{1773689}{1600000},\quad
b_4=\frac{74489644841}{4502400000},\quad
b_5=\frac{23869857}{3927875}.
\end{gathered}
$$

Use the single majorant

$$
M(h)=\frac9{2(h+2)}+\frac6{5(h+2)^2}-\frac1{9h},\qquad G(h)=R_0(h)-M(h).
$$

Its comparison with the actual head loss is

$$
M-S=\frac{P(h)}{90h(h+2)^2(D-N)},
$$

where the numerator is defined by the unexpanded product

$$
P=(395h^2+878h-40)(D-N)-180h^2(h+2)^2N.
$$

Set $z=h-1/2$. The following identity exposes a squared remainder and the distance to the upper endpoint:

$$
P=\frac{17937}{32}-\frac{51717}{8}z+z^2H(h),
$$

$$
\begin{aligned}
H(h)={}&\frac{302595}{2}h^2+294165h-\frac{244251}{8}\\
&+h^2(4-h)(6600h^2+39410h+52858).
\end{aligned}
$$

The last term is nonnegative on the whole interval. The first line is strictly increasing for $h>0$, because its derivative is $302595h+294165>0$, and at $h=3/8$ it is $12935259/128>100000$. Consequently,

$$
P\ge\frac{17937}{32}-\frac{51717}{8}z+100000z^2
\ge\frac{17937}{32}-\frac{(51717/8)^2}{400000}
=\frac{11674951911}{25600000}>450>0.
$$

All comparison denominators are positive. Hence $S<M$ and $Z_\Psi>G$ throughout $[3/8,4]$.

## 2. A uniform curvature bound

Put

$$
x=\frac1{h+2}\in\left[\frac16,\frac8{19}\right],\qquad
\epsilon=b_0-\frac19=\frac{407}{5760000}>0,\qquad C=b_3-\frac65<0.
$$

Differentiating the retained partial fractions gives

$$
\frac{(h+2)^3G''(h)}2=Q(x),
$$

$$
Q(x)=b_4-\frac92+3Cx-f(x)
-\frac{b_5}{(1+7x/60)^3}-\frac{\epsilon}{(1-2x)^3},
\qquad
f(x)=\frac{b_2(1-x)-3b_1x}{(1-x)^4}.
$$

All denominators are positive on this interval. We will prove

$$
Q(x)>-\frac12\quad\left(\frac16\le x\le\frac8{19}\right),
\qquad
Q(x)>0\quad\left(\frac16\le x\le\frac27\right).
$$

First consider $1/6\le x\le2/5$. We have

$$
f'(x)=\frac{3\{(b_2-b_1)-(b_2+3b_1)x\}}{(1-x)^5},
\qquad
f''(x)=\frac{12\{(b_2-2b_1)-(b_2+3b_1)x\}}{(1-x)^6}.
$$

The numerator controlling $f''$ is decreasing and affine. Thus $f'$ either is monotone or first increases and then decreases; its minimum on a compact interval occurs at an endpoint. The bounds $b_2>3$ and $b_1<1$ give

$$
f'(1/6)>\frac{3}{(5/6)^5}>3.
$$

At the other endpoint, use $b_2>637/200$ and $b_1<21/25$:

$$
f'(2/5)=\frac{625}{81}(3b_2-11b_1)
>\frac{625}{81}\left(3\frac{637}{200}-11\frac{21}{25}\right)
=\frac{175}{72}>\frac{12}{5}.
$$

Consequently $f'>12/5$ on the whole interval. Since $C<0$, $\epsilon>0$, and $b_5<61/10$, differentiation of $Q$ yields

$$
Q'(x)<-\frac{12}{5}+\frac7{20}b_5
<-\frac{12}{5}+\frac{427}{200}=-\frac{53}{200}<0.
$$

For $2/5\le x\le8/19$, bound the coupled head term by its elementary scalar maximum. For positive $a,b$,

$$
\frac{d}{dx}\frac{a-(a+3b)x}{(1-x)^4}
=\frac{3\{a-b-(a+3b)x\}}{(1-x)^5},\qquad x<1.
$$

It increases up to $x=(a-b)/(a+3b)$ and decreases afterwards, so its global maximum for $x<1$ is $(a+3b)^4/(256b^3)$. Use

$$
b_2<\frac{319}{100},\qquad b_1>\frac{67}{80}.
$$

Since $0<x<1$, these inequalities increase the numerator defining $f$. They give

$$
f(x)<\frac{2281^4}{12800000\,67^3}<\frac{176}{25}.
$$

The other three bounds are

$$
\begin{aligned}
b_4-\frac92+3Cx
&\ge b_4-\frac92+\frac{24C}{19}
=\frac{1020466792283}{85545600000}>\frac{119}{10},\\
\frac{b_5}{(1+7x/60)^3}
&\le b_5\left(\frac{150}{157}\right)^3
=\frac{644486139000}{121603647739}<\frac{16}{3},\\
\frac{\epsilon}{(1-2x)^3}
&\le\epsilon\left(\frac{19}{3}\right)^3
=\frac{2791613}{155520000}<\frac1{50}.
\end{aligned}
$$

Thus

$$
Q(x)>\frac{119}{10}-\frac{176}{25}-\frac{16}{3}-\frac1{50}
=-\frac{37}{75}>-\frac12.
$$

In particular this holds at $x=2/5$. Since $Q$ is decreasing on $[1/6,2/5]$, the same lower bound extends to the full interval $[1/6,8/19]$.

To obtain positive curvature in the upper height range, it remains to bound $Q(2/7)$. The affine contribution and the small-pole bound above hold on all of $[1/6,8/19]$. In addition,

$$
\begin{aligned}
f(2/7)&=\frac{343}{625}(5b_2-6b_1)
<\frac{343}{625}\left(5\frac{319}{100}-6\frac{67}{80}\right)
=\frac{149891}{25000}<6,\\
\frac{b_5}{(1+7(2/7)/60)^3}
&=b_5\left(\frac{30}{31}\right)^3
<\frac{61}{10}\left(\frac{30}{31}\right)^3<\frac{28}{5}.
\end{aligned}
$$

Therefore

$$
Q(2/7)>\frac{119}{10}-6-\frac{28}{5}-\frac1{50}
=\frac7{25}>\frac14.
$$

Monotonicity gives $Q>0$ on $[1/6,2/7]$, as required.

## 3. One convex correction and one tangent

Define

$$
F(h)=G(h)+\frac1{2(h+2)}.
$$

The uniform bound just proved gives

$$
F''(h)=\frac{2}{(h+2)^3}\left(Q(x)+\frac12\right)>0
\quad\left(\frac38\le h\le4\right).
$$

Convexity and the tangent at $h=1$ imply

$$
G(h)\ge G(1)+G'(1)(h-1)-\frac{(h-1)^2}{18(h+2)}.
$$

The scalar data are

$$
G(1)=\frac{208251137}{16401600000}>\frac1{80},
\qquad
-\frac1{400}<G'(1)=-\frac{42620371163}{18402595200000}<0.
$$

For $3/8\le h\le3/2$, the negative contribution from the linear term is at most $1/800$: it is nonnegative for $h\le1$, while $0\le h-1\le1/2$ otherwise. Also $|h-1|\le5/8$ and $h+2\ge19/8$, so

$$
\frac{(h-1)^2}{18(h+2)}\le\frac{(5/8)^2}{18(19/8)}=\frac{25}{2736}.
$$

It follows that

$$
G(h)>\frac1{80}-\frac1{800}-\frac{25}{2736}
=\frac{289}{136800}>\frac{27}{16000}.
$$

For $h\ge3/2$, we have $x\le2/7$ and therefore $G''(h)>0$. Moreover,

$$
G'(3/2)=\frac{5115313959269}{1118040013125000}>0.
$$

Hence $G$ is strictly increasing on $[3/2,4]$, and the same strict lower bound extends to that entire interval. Together with $Z_\Psi>G$, this proves the original strict margin on the full original range.

The unchanged concluding head, gain, and common-tail comparison gives the exact declaration of `lem-psi-payment`.

## Audit and route history

The complete displayed derivation is mathematically independent of computation. The portable supplementary script `review/check_r3_terminal.py` uses only the Python standard library and the adjacent `rational_algebra.py`. It reports 40 passing exact checks in `review/r3_terminal_exact_checks.json`, covering the retained partial-fraction identity, product identity, squared-remainder identity, derivative formulas, normalized curvature, all scalar inequalities, and the convex tangent correction. It uses rational arithmetic only and does not infer an interval sign from samples. Run it from the project root with `python review/check_r3_terminal.py`.

During discovery I also considered replacing $6/5$ by $5/4$ in the majorant. That candidate gives an apparently increasing compensated response but requires a less economical derivative proof and reduces the useful low-end response margin. I also established a tighter curvature floor $Q>-2/5$ and the stronger lower bound $G>2353/684000$, but that choice needs closer scalar estimates. Neither route is used in this proposal. The selected route uses the coarser floor $Q>-1/2$, which supplies a simpler reciprocal correction and preserves the exact original declared margin.

The important qualification is that the short polynomial remainder remains ordinary finite algebra. The claimed improvement is its structural sign proof and the removal of the two-chart response machinery, not a claim that the original R2 finite identities were nonanalytic.
