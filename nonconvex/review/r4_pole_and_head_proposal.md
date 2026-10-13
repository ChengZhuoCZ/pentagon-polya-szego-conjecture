# R4 uniform denominator and head-range reductions

**Status: integrated and independently reviewed.** These derivations replace only the indicated linked-proof passages. Every declaration, parameter definition, and strict domain remains unchanged. The QMD chapters are authoritative. The R.4 argument has an independent review in `r4_noncrossing_independent_audit.md`; the M.3 calculations are elementary exact reciprocal estimates recorded here for integrated review.

## R.4: one positive product bound for the complete order range

The preceding part of `lem-pole-free` proves, without using the sign of D,

$$
\sigma>1,\quad r>3,\quad C>\sigma+2,\quad
\theta\le\frac45,\quad T=3\Pi R\theta,\quad
\sigma(\sigma-1)=\frac{\Pi R^2}{2},\quad \Pi<10.
$$

Therefore

$$
\Pi R=\sqrt{2\Pi}\sqrt{\sigma(\sigma-1)}
<\frac92\left(\sigma-\frac12\right),
\qquad T<\frac{54}{5}\left(\sigma-\frac12\right),
$$

because $2\Pi<20<81/4$ and the positive square root of $(\sigma-1/2)^2-1/4$ is smaller than $\sigma-1/2$. Both multipliers are positive. Hence

$$
\begin{aligned}
CD&=(2\sigma+1)C-T\\
&>(2\sigma+1)(\sigma+2)-\frac{54}{5}\left(\sigma-\frac12\right)\\
&=2\left(\sigma-\frac{29}{20}\right)^2+\frac{639}{200}>0.
\end{aligned}
$$

Since $C>0$, this proves $D>0$. It removes the split at $\sigma=4/3$ and covers all of the original domain, including $b=0$.

## M.3.4 and M.3: direct reciprocal bounds

For every $h>3/8$, put $L=1+h$. Since $h+2>L>11/8$,

$$
0<v_h=\frac3{2L^2}-\frac1{2(h+2)^2}
<\frac3{2L^2}<\frac{96}{121}<1.
$$

The first inequality follows already from $3/L^2>1/(h+2)^2$. This establishes the same head range in the proofs of `lem-m34-identity` and `lem-q-branch-monotone`, without introducing the fourth-degree numerator of $1-v_h$.

For the large-height branch $h\ge\sqrt2>4/3$, one has $L>7/3$ and

$$
\frac{6R_1}{h+2}
=\frac{3L^4}{5h^2(h+2)^2}
=\frac3{5(1-L^{-2})^2}
<\frac{7203}{8000}<1.
$$

Here $h(h+2)=L^2-1$ and $1-L^{-2}>40/49>0$. Thus

$$
R_1<\frac{h+2}{6}=\frac13+\frac h6,
$$

as required, with no fourth-degree sign calculation. This does not change the small-height derivative comparison in M.3.4 or any one-sided derivative assertion at $q=p$.

## Verification scope

`check_r4_pole_and_head.py` checks the displayed formal identities and rational constants exactly. The interval signs follow from the written square-root and reciprocal arguments, not from executing the script or sampling points. The script is supplementary and is not an official qmd-prover verdict.
