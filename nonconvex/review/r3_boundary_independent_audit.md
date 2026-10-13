# Independent audit of the R3 boundary derivative replacements

## Result

**Pass: no mathematical blocker or additional assumption found.** I independently checked both derivations in the boundary proposal and their integrated versions in the proofs of **lem-zero-monotone** and **lem-container-monotone** in monotonicity.qmd. The replacement arguments preserve the full gain derivative, the original parameter ranges, the constant tail order on the relevant branches, and the admissible-interval conclusions.

The R3 AGENTS contract and strict configuration were read independently. The external-basis file is absent. The configured backend is codex with gpt-6.1-sol and xhigh effort; citations, rigor, and refutation rigor remain strict, with assumptions forbidden. No official qmd-prover verdict is claimed. This audit made no changes to the boundary source.

## 1. Vanishing short-tail width

On this boundary, $w=p$. Starting from the complete two-term gain

$$
\mathcal B(A,p)
=\frac{A(1-p)}{2p}
+\frac{A(2-A)(1-p)^2}{20p},
$$

I recomputed

$$
J_0=\mathcal B_A+\frac{p}{2A}\mathcal B_w
=\frac{12-3A}{40p}-\frac{7-2A}{10}
+\frac{6-5A}{40}p.
$$

Thus the proposed simplification uses the full gain and omits no term.

For a fixed value $0<A<1$ and $0<p<1$,

$$
\partial_pJ_0
=-\frac{12-3A}{40p^2}+\frac{6-5A}{40}
<-\frac{6+2A}{40}<0.
$$

The endpoint value is exactly

$$
J_0(1/2,A)=-\frac{2+A}{80}<-\frac1{40}.
$$

The application is pointwise: at any given point on the geometric curve, freeze the value $A=A(p)$ only to compare $J_0(p,A)$ with $J_0(1/2,A)$. The proof does not replace the derivative along that curve by a partial derivative, so there is no missing $A_p$ term.

For $p<1/2$, the identity

$$
J_0-J_*=\frac{A(1-p)(5p-3)}{40p}<0
$$

has the correct sign. At $p=1/2$ the preceding strictly negative bound already applies, so the division into branches leaves no endpoint uncovered.

For the remaining case $1\le h\le4$, $r_0\ge1$, and $p<1/2$, the retained height comparison is also correct. The logarithmic derivative of

$$
B(h)=\frac{h^2(h+2)}{2(1+h)(1+(1+h)p)^2}
$$

satisfies

$$
\frac{B'}B
>\frac2h+\frac1{h+2}-\frac3{1+h}
=\frac{h+4}{h(1+h)(h+2)}>0.
$$

Consequently $r_0hp/6\ge B(1)=3/[4(1+2p)^2]$. For this last reciprocal square, I checked

$$
f''(p)=\frac{18}{(1+2p)^4}>0,\qquad
f(1/2)=\frac3{16},\qquad f'(1/2)=-\frac38.
$$

Its tangent gives

$$
f(p)-pJ_*(p)
\ge\frac3{40}+\frac{p(13-6p)}{40}>\frac3{40}.
$$

Since $p>0$, this proves $r_0h/6>J_0$. In the existing derivative identity

$$
\frac p{2A}\mathcal G_p=(1-r_0)X-r_0hM+J_0,
$$

the first term is nonpositive and $M>1/6$, so the required strict negativity follows. The other two height/order cases retain their original justifications.

## 2. Container equality

Writing $L=1+h$ and $D_h=L^2+1$, the sufficient expression is

$$
\mathcal E_c(h)
=\frac{h(h+2)^2}{L(L^2-c)}
-\frac13-\frac{3cD_h}{5(2L^2-cD_h)}.
$$

Substitution of $y=1/L$ gives exactly

$$
\mathcal F_c(y)
=\frac{(1+y)(1-y^2)}{1-cy^2}
-\frac13-\frac{3c(1+y^2)}{5(2-c-cy^2)}.
$$

For $c=\sqrt3/2$, the bounds $6/7<c<7/8$ follow by squaring. On the closed interval $0\le y\le2/3$, they yield the strict denominator bounds

$$
1-cy^2>\frac{11}{18},\qquad
2-c-cy^2>\frac{53}{72}.
$$

The function therefore extends smoothly to the artificial endpoint $y=0$. Including that endpoint does not change the required range of finite $h$.

The two derivatives

$$
W_a'=\frac{2ay}{(a-cy^2)^2},\qquad
W_a''=\frac{2a(a+3cy^2)}{(a-cy^2)^3}
$$

are correct. Both decomposition identities in the source are exact. They give

$$
\mathcal F_c''
=-(1-c)\bigl(2W_1'+(1+y)W_1''\bigr)
-\frac{6c}{5(2-c)}W_{2-c}''<0
$$

throughout the closed interval, because $W_a'\ge0$, $W_a''>0$, and all displayed multipliers are positive.

At zero,

$$
\mathcal F_c(0)>
\frac23-\frac7{15}=\frac15.
$$

At $y=2/3$, the exact formula and valid opposite choices of the bounds on $c$ give

$$
\begin{aligned}
\mathcal F_c(2/3)
&=\frac{25}{3(9-4c)}-\frac13
-\frac{39c}{5(18-13c)}\\
&>\frac{175}{117}-\frac13-\frac{273}{265}
=\frac{4099}{31005}>\frac18.
\end{aligned}
$$

Both rational functions of $c$ in this endpoint formula increase on the stated range. Thus the first term is bounded below using $c>6/7$, and the subtracted term is bounded above using $c<7/8$. Their comparison directions are correct. The last strict margin is exactly

$$
\frac{4099}{31005}-\frac18
=\frac{1787}{248040}>0.
$$

Concavity places $\mathcal F_c$ above its endpoint chord, proving $\mathcal E_c(h)>1/8$ for every $h\ge1/2$. No cleared degree-five numerator is needed.

Finally, the retained inequalities $r_c>1$, $X>1/3$, $M>1/6$, and the geometric lower bound for $r_c$ imply

$$
(1-r_c)X-r_chM+J_c
<-\mathcal E_c(h)<-\frac18
$$

on the required container branch with $h\ge1/2$. This is the correct sign in the original scaled derivative formula. The proof for $3/8<h<1/2$ and the one-sided interpretation at $q=p$ remain present, as does the argument that the admissible branch is an interval.

Both replacements are complete analytic curvature arguments. The new pointwise comparison and the endpoint-chord comparison do not introduce parameter sampling or numerical sign assumptions.
