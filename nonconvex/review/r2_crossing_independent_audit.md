# Independent audit of the R2 crossing Sturm replacement

## Result and scope

**Pass: no mathematical blocker or additional assumption was found.** I independently audited the complete argument in `review/r2_crossing_proposal.md` and then compared the integrated `workspace/high.qmd`, including `def-high-operator`, `lem-free-sturm-bound`, `lem-crossing-sturm`, and its use in `lem-high`. The integrated source contains the regular-solution and variational details needed to justify the interface argument for every real order $2\le s\le3$.

The proved comparison is

\[
\lambda_1(K_{s;1,t})>\frac{C_s}{F_0(t)},
\qquad C_s=\frac{25s-11}{2},
\qquad 2\le s\le3,\quad0\le t\le\frac32.
\]

This supplies exactly the two constants $C_2=39/2$ and $C_3=32$ required downstream. It does not claim the discarded auxiliary Green-trace inequalities. The main theorem remains nonconvex exclusion, with no new convex extremal theorem.

The R2 project instructions and strict configuration were read independently; there is no external-basis restriction file. No workspace source or protected statement was edited in this audit. The official qmd-prover executable is unavailable, so this report records an independent mathematical and source-transfer review, not formal or official certification.

## 1. Singular barrier, regular solution, and separated spectrum

Logarithmic differentiation of

\[
v_s(y)=y^s(1-y^2)e^{-sy^2/2}
\]

gives precisely

\[
-\frac{v_s''}{v_s}+\frac{s(s-1)}{y^2}
=s^2+5s+s^2(1-y^2)+\frac2{1-y^2}.
\]

AM--GM therefore gives the lower bound $B_s=s^2+5s+2\sqrt2\,s$. The ground-state identity is first applied on the smooth compactly supported core. The Hardy inequality in `def-high-operator` then extends the resulting quadratic-form inequality to $H_0^1(0,1)$. This avoids imposing any extra classical condition at the singular endpoint.

The strict energy margin is correct:

\[
B_s-C_s>
s^2-\frac{75s}{16}+\frac{11}{2}
=\left(s-\frac{75}{32}\right)^2+\frac7{1024}>0,
\]

using $\sqrt2>45/32$. It proves the $t=0$ case directly. For $t>0$, $F_0(t)>1$, so $E=C_s/F_0(t)<B_s\le\lambda_D(s)$.

The integrated regular series

\[
u(z)=z^s\sum_{n\ge0}a_nz^{2n},\qquad
a_0=1,\qquad
a_n=-\frac{Ea_{n-1}}{2n(2s+2n-1)}
\]

has the correct recurrence. Its convergence and its asymptotics give finite form energy for all $2\le s\le3$. A first zero at or before $z=1$ would yield, by extension by zero, a nonzero element of $H_0^1(0,1)$ with Rayleigh quotient $E<\lambda_D(s)$. The integration-by-parts boundary product is $O(z^{2s-1})\to0$. Consequently $u>0$ throughout $(0,1]$, so its interface logarithmic derivative has no pole.

For

\[
g(z)=z^s\left(1-\frac{z^2}{F}\right)e^{-sz^2/(2F)},
\]

the effective potential is the displayed barrier expression at $y=z/\sqrt F$, divided by $F$. It strictly exceeds $E$, while $g>0$ on $(0,1]$. The Wronskian orientation is correct:

\[
(u'g-ug')'=u(L_s-E)g>0,
\qquad u'g-ug'=O(z^{2s+1})\longrightarrow0.
\]

Thus

\[
D_s(E)>s(1-F^{-1})-\frac2{F-1}.
\]

This is a lower bound for the singular side's outward response at its right endpoint, with the sign needed in the common-interface sum.

## 2. Free response and the first interval

The two definitions of $F_0$ agree at $t=1/4$, with value $29/16$. On either quadratic piece $F=a+bt+ct^2$,

\[
\left(\frac{t^2}{F}\right)'=\frac{t(2a+bt)}{F^2}>0.
\]

The endpoint values $t^2/F=1/29$ at $t=1/4$ and $1/5$ at $t=3/2$ therefore give

\[
q=Et^2\le\frac{32}{29}<4
\quad\hbox{or}\quad
q\le\frac{32}{5}<\pi^2,
\]

respectively. The free side is consequently below its first separated Dirichlet eigenvalue throughout the full range.

I rechecked the shared elementary comparison:

\[
p_q(z)=z(1-qz^2/12)^2,
\qquad -p_q''-qp_q=\frac{q^2z^3}{144}(4-qz^2)\ge0.
\]

The Wronskian with the positive sine solution gives the stated lower bound

\[
\sqrt q\cot\sqrt q\ge1-\frac{q}{3-q/4}.
\]

For $0<t\le1/4$, every estimate leading to the concave quadratic is valid:

\[
1-\frac2{3+t}\ge\frac13+\frac{8t}{39},\quad
\frac{st(F-1)}F\ge\frac{48s}{29}t^2,\quad
3F-C_st^2/4\ge3.
\]

Since

\[
\frac{C_s}{3}-\frac{48s}{29}
=\frac{437s-319}{174}\le\frac{496}{87},
\]

the resulting lower bound is

\[
t(D_s+D_{\rm free})>
P(t)=\frac13+\frac{8t}{39}-\frac{496t^2}{87}.
\]

The exact endpoints $P(0)=1/3$ and $P(1/4)=32/1131$, together with concavity, prove positivity on this entire interval. No division by $t=0$ occurs in the argument.

## 3. Rational free bound and the second-interval curvature argument

The use of `lem-cot-rational` is valid at the same $q=Et^2$. Its current source is a finite-mode resolvent proof. With $k=q/\pi^2$, its response function satisfies

\[
\mathsf H(q)
>1-\frac{2k}{1-k}-\frac{129k}{100(1-k/4)}.
\]

Here $0<\pi^2/3-5/2<79/100$ and $1-k/9>1-k/4>0$. The last expression decreases in $k$; using $\pi^2>49/5$ and $129/100<13/10$ gives

\[
\sqrt q\cot\sqrt q>
1-\frac{2q}{49/5-q}-\frac{13q/10}{49/5-q/4}.
\]

All denominator replacements have the correct direction. They remain positive for $0<q\le32/5$.

On $1/4\le t\le3/2$, the source defines $G_s=A_s-B_{C_s}$ using $F=a+bt+ct^2$, where $a=9/25,b=138/25,c=29/25$. I independently differentiated both quotient identities:

\[
\left(\frac tQ\right)''
=-\frac{2(ab+3act-c^2t^3)}{Q^3},
\qquad
\left(\frac{t^2}{Q}\right)''
=\frac{2(a^2-3act^2-bct^3)}{Q^3}.
\]

For $H=b+3ct>0$ and $X=c^2t^3>0$, first discarding the negative $X$ terms and then using $F>F-1>0$ gives

\[
A_s''<\frac{[2sa+4(a-1)]H}{(F-1)^3}
\le-\frac{2H}{5(F-1)^3}<0.
\]

This comparison does not require $aH-X$ to be positive.

For the two terms of $B_C$, the source's constants satisfy

\[
d\ge\frac{2033}{50}>40,
\qquad
0<\frac{421}{25}\le e\le\frac{6493}{200}<33,
\]

so $d>e>0$. Also $Q_-<Q_+$, and the uniform energy bound gives the stronger explicit positivity $Q_-\ge17F>0$, $Q_+\ge41F>0$. With $\alpha=10C>\beta=13C/2$, $M=A^2>0$, and $N=3At^2+Bt^3>0$,

\[
\frac{B_C''}{2}
=\frac{\alpha(M+dN)}{Q_-^3}
+\frac{\beta(M-eN)}{Q_+^3}
\ge\frac{\alpha M}{Q_-^3}+\frac{\beta M}{Q_+^3}
+\frac{(\alpha d-\beta e)N}{Q_+^3}>0.
\]

The estimate is valid even if $M-eN<0$. Hence $G_s''<0$ over the whole second interval, with no coefficient table or numerical subdivision. At a fixed $t$, each free fraction is an increasing convex function $uC/(A-vC)$ on its positive-denominator range. Since $C_s$ is affine, $G_s(t)$ is also concave in $s$.

## 4. Endpoint arithmetic and interface conclusion

The endpoint evaluations and coarse strict bounds are correct:

| Endpoint | Checked lower bound |
|---|---:|
| $t=1/4$, every $2\le s\le3$ | $G_s(1/4)>5/87$ |
| $t=3/2,s=2$ | $G_2(3/2)>9/10$ |
| $t=3/2,s=3$ | $G_3(3/2)=39/1394$ |

In particular, the tight endpoint is exactly

\[
\frac{1971}{410}-\frac{64}{17}-\frac{208}{205}
=\frac{39}{1394}>0.
\]

Concavity in $s$ and then in $t$ proves $G_s(t)\ge39/1394>0$ throughout the second rectangle. These values were also checked with exact rational arithmetic; the proof uses only the displayed identities and strict rational comparisons.

Both ODE solutions are evaluated at the same physical energy $E$ and normalized to the same interface trace. The integrated source identifies the regular solution with the minimizing trace-one extension: finite form energy, the weak ODE, Hardy density, and $E<\lambda_D(s)$ make the shifted form strictly coercive on the zero-trace subspace. The corresponding free-side statement follows from its ordinary interval equation.

The orientation change

\[
x=\frac{1+t-z}{t}
\]

sends the free interval to $(0,1)$, the singular interval to $(1,1+1/t)$, and their interface to $x=1$. Both energies become $q=t^2E$. Both outward responses are multiplied by the same positive factor $t$: the new right-side outward derivative is $-\partial_x=t\partial_z$, and the new left-side outward derivative is $\partial_x=-t\partial_z$. The separated spectra scale by $t^2$ as well. All hypotheses of `lem-interface` therefore hold in its stated orientation, giving the strict full-operator spectral inequality.

Finally,

\[
\lambda_1(K_{s;\ell,b})
=\ell^{-2}\lambda_1(K_{s;1,b/\ell})
>\frac{C_s}{\ell^2F_0(b/\ell)}
\ge\frac{C_s}{D}
\]

has the correct comparison direction because $D\ge\ell^2F_0$. The use in `lem-high` preserves the original physical scaling and the strict candidate contradiction.

## Source-transfer findings

The integrated text includes the real-order definition, the Hardy/domain and interface-matching proof, the explicit regular series, the variational minimizer identification, and the common-energy orientation check. The shared `lem-free-sturm-bound` is available to both Sturm arguments. Explicit imports include `def-analytic`, `lem-cot-rational`, `lem-pi-rational`, and `lem-interface`; the new dependency on `robin.qmd` creates no cycle. The draft's two missing `\qquad` backslashes have been corrected. No remaining transfer discrepancy affecting the proof was found.
