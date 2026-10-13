# R2 crossing replacement: a direct Sturm comparison for the full range

Status: integrated and independently reviewed. The argument below is now `lem-crossing-sturm` in `workspace/high.qmd`. The author edited only that semantic QMD file; the parent coordinates the companion algebra-definition and documentation changes. The R2 AGENTS contract, strict configuration, and absent external-basis restriction were read independently. The configuration remains `codex` / `gpt-6.1-sol` / `xhigh`, with strict citations, proof rigor, and refutation rigor and with assumptions forbidden. The official qmd-prover executable is unavailable; no certification is claimed.

The independent mathematical and source-transfer audit is recorded in `review/r2_crossing_independent_audit.md`. The portable supplementary checker `review/check_r2_crossing.py` passed all 38 exact identity and rational-arithmetic checks, with results in `review/r2_crossing_exact_checks.json`. It performs no parameter sampling; the proof does not require executing it. The final source supplies additional details on the regular series, its finite form energy, the trace-one minimizing extensions, and the real-order operator domain.

## Integrated result

Extend the notation $K_{s;\ell,b}$ to real $2\le s\le3$ by the same Friedrichs quadratic form as the existing comparison operator:

$$
-\partial_z^2+s(s-1)z^{-2}\mathbf1_{(0,\ell)}
\quad\hbox{on }(0,\ell+b),
$$

with the shared interface and the right Dirichlet condition. Hardy's inequality gives the common form domain $H_0^1$ and compact resolvent exactly as in the existing operator proof.

Put

$$
C_s=\frac{25s-11}{2},\qquad
F(t)=F_0(t)=
\begin{cases}
1+3t+t^2,&0\le t\le1/4,\\
(9+138t+29t^2)/25,&1/4\le t\le3/2.
\end{cases}
$$

Then the stronger continuous-order comparison is

$$
\lambda_1(K_{s;1,t})>\frac{C_s}{F(t)}
\qquad(2\le s\le3,\ 0\le t\le3/2).
\tag{R2.H.1}
$$

For the original crossing geometry, the already established concave area-cost reduction gives $D\ge\ell^2F(t)$ and $t=b/\ell$. Scaling then yields

$$
\lambda_1(K_{2;\ell,b})>\frac{39/2}{D},\qquad
\lambda_1(K_{3;\ell,b})>\frac{32}{D}.
$$

These are exactly the constants needed by the protected large-height theorem. No Green trace, trace numerator, coefficient-sign argument, or numerical parameter subdivision occurs in the proof below.

## 1. A positive comparison function and a uniform pole-free bound

For the stated range $2\le s\le3$, use the positive function

$$
v_s(y)=y^s(1-y^2)e^{-s y^2/2}\qquad(0<y<1).
$$

Direct logarithmic differentiation gives

$$
-\frac{v_s''}{v_s}+\frac{s(s-1)}{y^2}
=s^2+5s+s^2(1-y^2)+\frac{2}{1-y^2}
\ge B_s:=s^2+5s+2\sqrt2\,s.
\tag{R2.H.2}
$$

The inequality is AM--GM applied to the last two terms. The ground-state identity, first for compactly supported smooth functions and then by Hardy's inequality and form-core density, gives the Friedrichs--Dirichlet lower bound $\lambda_D(s)\ge B_s$ on $(0,1)$.

The inequality $\sqrt2>45/32$ follows by squaring. Hence, for $2\le s\le3$,

$$
B_s-C_s>
 s^2-\frac{75s}{16}+\frac{11}{2}
=\left(s-\frac{75}{32}\right)^2+\frac7{1024}>0.
\tag{R2.H.3}
$$

The case $t=0$ of (R2.H.1) follows immediately.

For $t>0$, set $E=C_s/F(t)$, so $F(t)>1$ and $0<E<C_s<B_s\le\lambda_D(s)$. The regular left solution $u$ at this energy is positive on $(0,1]$: a first zero would give a Dirichlet test function of Rayleigh quotient $E$, contradicting the separated spectral bound. Write $D_s(E)=u'(1)/u(1)$.

Use the rescaled comparison function

$$
g(z)=z^s\left(1-\frac{z^2}{F}\right)e^{-s z^2/(2F)}\qquad(0<z\le1).
$$

Its effective potential is the right-hand side of (R2.H.2), at $y=z/\sqrt F$, divided by $F$. It therefore strictly exceeds $E$. The Wronskian identity

$$
(u'g-ug')'=u\left[-g''+\left(\frac{s(s-1)}{z^2}-E\right)g\right]>0
$$

and the regular asymptotics at zero give

$$
D_s(E)>\frac{g'(1)}{g(1)}
=s\left(1-\frac1F\right)-\frac2{F-1}.
\tag{R2.H.4}
$$

All functions have positive value at the interface. The singular endpoint is handled by the same regular asymptotics already used in the project's Sturm comparison; the Wronskian tends to zero there.

Let $q=Et^2=C_st^2/F$. The quantity $t^2/F(t)$ increases on either quadratic piece, since its derivative is $t(2a+bt)/F^2$ when $F=a+bt+ct^2$. Thus

$$
0<q\le\frac{32}{29}<4\quad(0<t\le1/4),
\qquad
0<q\le\frac{32}{5}<\pi^2\quad(1/4\le t\le3/2).
\tag{R2.H.5}
$$

In particular, $E<\pi^2/t^2$, so the free segment also stays below its first separated Dirichlet eigenvalue. Its outward response at the shared physical energy is

$$
D_{\mathrm{free}}(E,t)=\sqrt E\cot(\sqrt E\,t)
=\frac1t\sqrt q\cot\sqrt q.
$$

It remains to prove that the sum of the two outward responses is positive.

## 2. The first interval: a single concave quadratic bound

For $0<q\le4$, the already established positive comparison function

$$
p_q(z)=z\left(1-\frac{qz^2}{12}\right)^2
$$

satisfies

$$
-p_q''-qp_q=\frac{q^2z^3}{144}(4-qz^2)\ge0.
$$

Its Wronskian comparison with $\sin(\sqrt q\,z)/\sqrt q$ gives

$$
\sqrt q\cot\sqrt q\ge1-\frac{q}{3-q/4}.
\tag{R2.H.6}
$$

This is the same continuous-parameter inequality used in the previous edition's noncrossing Sturm proof.

For $0<t\le1/4$, put $F=1+3t+t^2$. Combining (R2.H.4) and (R2.H.6) gives

$$
\begin{aligned}
t(D_s+D_{\mathrm{free}})
&>1-\frac2{3+t}+\frac{s t(F-1)}F
-\frac{C_s t^2}{3F-C_st^2/4}.
\end{aligned}
$$

Here $F\le29/16$, while $3F-C_st^2/4\ge3+9t-5t^2\ge3$. Therefore

$$
\begin{aligned}
t(D_s+D_{\mathrm{free}})
&>\frac13+\frac{8t}{39}
-\left(\frac{C_s}{3}-\frac{48s}{29}\right)t^2\\
&\ge P(t):=\frac13+\frac{8t}{39}-\frac{496t^2}{87}.
\end{aligned}
\tag{R2.H.7}
$$

The last step uses

$$
\frac{C_s}{3}-\frac{48s}{29}
=\frac{437s-319}{174}\le\frac{496}{87}.
$$

The quadratic $P$ is concave. Its endpoint values are

$$
P(0)=\frac13,\qquad P(1/4)=\frac{32}{1131}>0.
$$

Consequently the total interface response is strictly positive on the entire first interval, uniformly in $2\le s\le3$.

## 3. A simple rational lower bound for the free response

For the second interval we use the proved finite-mode resolvent estimate `lem-cot-rational`, together with $493/50<\Pi=\pi^2<987/100$. Put $k=q/\Pi\in(0,1)$. Its original rational function satisfies

$$
\begin{aligned}
\mathsf H(q)
&=1-\frac{2k}{1-k}-\frac{k/2}{1-k/4}
-\frac{(\Pi/3-5/2)k}{1-k/9}\\
&>1-\frac{2k}{1-k}-\frac{129k}{100(1-k/4)}.
\end{aligned}
$$

Indeed, $0<\Pi/3-5/2<79/100$ and $1-k/9>1-k/4>0$. The last rational function decreases strictly in $k$. Since $\Pi>49/5$ and $129/100<13/10$, it follows that

$$
\sqrt q\cot\sqrt q>
1-\frac{2q}{49/5-q}-\frac{13q/10}{49/5-q/4}
\qquad\left(0<q\le\frac{32}{5}\right).
\tag{R2.H.8}
$$

All denominators are positive. This is a consequence of the finite resolvent projection already proved in the English edition, not an appeal to a partial-fraction expansion.

## 4. The second interval: concavity of the response lower bound

Throughout $1/4\le t\le3/2$, write

$$
F=a+bt+ct^2,\qquad a=\frac9{25},\ b=\frac{138}{25},\ c=\frac{29}{25}.
$$

Define

$$
A_s(t)=1+s t-\frac{s t}{F}-\frac{2t}{F-1},
$$

$$
B_C(t)=\frac{10C t^2}{49F-5Ct^2}
+\frac{(13C/2)t^2}{49F-(5C/4)t^2},
\qquad G_s(t)=A_s(t)-B_{C_s}(t).
\tag{R2.H.9}
$$

Equations (R2.H.4) and (R2.H.8) give $t(D_s+D_{\mathrm{free}})>G_s(t)$.

### 4a. The singular-side expression is strictly concave

For a quadratic $Q=a+bt+ct^2$,

$$
\left(\frac tQ\right)''
=-\frac{2[ab+3ac t-c^2t^3]}{Q^3}.
$$

Put $H=b+3ct>0$ and $X=c^2t^3>0$. Then

$$
A_s''=
\frac{2s(aH-X)}{F^3}
+\frac{4((a-1)H-X)}{(F-1)^3}.
$$

Since $F>F-1>0$, $2\le s\le3$, and

$$
2sa+4(a-1)\le10a-4=-\frac25,
$$

we obtain

$$
A_s''<-
\frac{2H}{5(F-1)^3}<0.
\tag{R2.H.10}
$$

The omitted $X$ terms have negative signs. This sign comes from the constant term $a=9/25$, not from a high-degree numerator expansion.

### 4b. The sum of the two free fractions is strictly convex

For $39/2\le C\le32$, put

$$
A=49a,\quad B=49b,\quad
d=5C-49c,\quad e=49c-\frac{5C}{4},
$$

$$
Q_-=A+Bt-dt^2,\qquad Q_+=A+Bt+et^2.
$$

The bounds on $q=Ct^2/F$ give $Q_->0$ and $Q_+>Q_-$. Moreover

$$
d\ge\frac{2033}{50}>40,\qquad
0<\frac{421}{25}\le e\le\frac{6493}{200}<33.
$$

In particular, $d>e>0$. Set $\alpha=10C$ and $\beta=13C/2$, so $\alpha>\beta>0$.

The second elementary identity is

$$
\left(\frac{t^2}{a+bt+ct^2}\right)''
=\frac{2[a^2-3ac t^2-bc t^3]}{(a+bt+ct^2)^3}.
$$

With $M=A^2>0$ and $N=3At^2+Bt^3>0$, it gives

$$
\frac12 B_C''
=\frac{\alpha(M+dN)}{Q_-^3}
+\frac{\beta(M-eN)}{Q_+^3}.
$$

Using $Q_-<Q_+$ and $\alpha d>\beta e$ yields

$$
\frac12 B_C''
\ge\frac{\alpha M}{Q_-^3}+\frac{\beta M}{Q_+^3}
+\frac{(\alpha d-\beta e)N}{Q_+^3}>0.
\tag{R2.H.11}
$$

Thus $G_s''<0$ for every $2\le s\le3$ on the entire second interval.

## 5. The endpoint comparisons are short and uniform

At $t=1/4$, $F=29/16$. The function $B_C$ increases in $C$, so $C\le32$ gives

$$
B_C(1/4)\le\frac{320}{1261}+\frac{208}{1381}
<\frac13+\frac16=\frac12.
$$

Since $s\ge2$,

$$
A_s(1/4)=1+\frac{13s}{116}-\frac8{13}
>\frac13+\frac{13}{58}.
$$

Therefore

$$
G_s(1/4)>\frac5{87}>0.
\tag{R2.H.12}
$$

At each fixed $t$, $A_s$ is affine in $s$. Both terms in $B_C$ are strictly convex increasing functions of $C$ wherever their denominators are positive. Since $C_s$ is affine, $G_s(t)$ is concave in $s$. It is therefore enough to bound its two order endpoints at $t=3/2$.

There $F=45/4$. For $s=2$, $C_2=39/2$, and

$$
A_2(3/2)=\frac{2116}{615}>3,
\qquad
B_{39/2}(3/2)=\frac{78}{59}+\frac{1014}{1765}
<\frac32+\frac35=\frac{21}{10}.
$$

Hence $G_2(3/2)>9/10$.
For $s=3$, $C_3=32$, and the exact comparison is

$$
G_3(3/2)=\frac{1971}{410}-\frac{64}{17}-\frac{208}{205}
=\frac{39}{1394}>0.
\tag{R2.H.13}
$$

Concavity in $s$ gives $G_s(3/2)\ge39/1394$. Concavity in $t$, (R2.H.12), and $5/87>39/1394$ consequently imply

$$
G_s(t)\ge\frac{39}{1394}>0
\qquad\left(2\le s\le3,\ \frac14\le t\le\frac32\right).
\tag{R2.H.14}
$$

These reductions follow from analytic curvature inequalities on the full intervals. They are not numerical parameter boxes or a coefficient-sign table.

## 6. The common-interface conclusion

For every $t>0$, the energy $E=C_s/F(t)$ lies strictly below the first separated Dirichlet eigenvalue on both sides. The total outward response at the same physical interface and the same physical energy is strictly positive by Sections 2 and 4–5. The existing variational common-interface criterion therefore gives $\lambda_1(K_{s;1,t})>E$.

To match its stated orientation explicitly, use $x=(1+t-z)/t$. This sends the free interval to $(0,1)$, the singular interval to $(1,1+1/t)$, and the interface to $x=1$. The energy becomes $t^2E=q$ on both pieces, and each outward response is multiplied by $t$. Thus the sign and the separated spectral hypotheses are preserved. The case $t=0$ was established directly in Section 1.

This proves (R2.H.1) and hence the required crossing comparison for the original geometric parameters.

## Completed integration and exact scope

1. The geometric lemmas `lem-high-area-cost` and `lem-high-cost-reduction` are retained. The operator definition now explicitly covers real $2\le s\le3$, with its linked Hardy inequality, common $H_0^1$ form domain, compact-resolvent, and interface-matching proof placed immediately after it.
2. The new `lem-crossing-sturm` states and proves the full continuous-order comparison, followed by its two required geometric scaling consequences. The displayed labels (R2.H.1)–(R2.H.14) in this report correspond to (H.5.4)–(H.5.17) in the integrated source.
3. The invocation of `lem-trace-endpoints` in `lem-high` is replaced by `lem-crossing-sturm`. The constants $C_2=39/2$, $C_3=32$ and the large-height theorem statement are unchanged.
4. The five crossing-only trace lemmas are removed from `high.qmd`: `lem-green-trace`, `lem-trace-single-valley`, `lem-trace-uniform-envelope`, `lem-trace-endpoints`, and `lem-characteristic-trace-identity`. Their polynomial definition `def-trace-polynomials` has no remaining high-module consumer; its companion deletion is handled by the parent. The former $945$ trace envelope and stronger trace-surrogate assertions are redundant auxiliary results, not conclusions established by this new argument.
5. The inherited elementary free comparison (R2.H.6) is factored into `lem-free-sturm-bound` and cited by both crossing and noncrossing proofs. This factoring is editorial; the inequality itself was proved in the previous English edition. The noncrossing Sturm estimates are retained.
6. The new crossing proof imports and cites the inherited finite-mode response bound `lem-cot-rational`, its defining response function from `def-analytic`, the rational constants, and the common-interface criterion. Thus it also inherits the finite two-mode resolvent argument in the previous English edition, without reintroducing a cotangent partial-fraction expansion.

The new mathematical step is the singular comparison function $y^s(1-y^2)e^{-s y^2/2}$ together with the concavity of $A_s$ and convexity of $B_C$ on the complete second interval. These inequalities bypass the trace-ratio single-minimum assertion itself. The only endpoint arithmetic is the short evaluation at the natural break $t=1/4$ and at the geometric extreme $t=3/2$, justified uniformly by the proved curvature inequalities. No coefficient-sign table or numerical parameter subdivision remains in the high module.

`high.qmd` decreased from 1096 to 820 lines. Its seven declarations each have one linked proof. This is a source description, not an official verification verdict. Full-project structural checks and protected-file checks are handled separately by the parent.

The main conclusion remains nonconvex exclusion in the original fixed-area simple-polygon class. No convex extremal theorem is introduced, and no additional assumption is needed.
