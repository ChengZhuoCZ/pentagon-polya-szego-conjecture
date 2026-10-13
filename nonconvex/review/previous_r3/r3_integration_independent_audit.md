# Independent audit of the final R3 analytic integrations

## Result and scope

**Pass: no correction is needed.** I independently checked the integrated R.7 proof in robin.qmd, the reuse of **lem-regular-tail** in **lem-robin** and coupled.qmd, and the replacement ratio estimate at the start of **lem-common-tail-line** in terminal.qmd.

The R3 project contract and strict configuration were read independently and remain in force. The external-basis file is absent. The configured backend is codex, model gpt-6.1-sol, with xhigh effort and strict citations, rigor, and refutation rigor; assumptions are forbidden. This report is an independent mathematical source review, not an official qmd-prover verdict. No source file was changed during this audit.

## 1. R.7: the same response from a comparison using both endpoints

The proof sets

$$
\Pi=\pi^2,\qquad t=x^2/\Pi,\qquad
a=\frac{3\Pi}{2}-\frac{45}{4},\qquad
p(x)=x(1-t)(1-t/4)(1-t/9)^a.
$$

For $0\le x\le\pi$, the base of the real power is at least $8/9$. Thus $p$ and its derivatives extend smoothly to both endpoints, $p(0)=p(\pi)=0$, and $p>0$ in the open interval. The real exponent introduces no endpoint singularity.

The logarithmic derivative is exactly the original response:

$$
\frac{xp'}p
=1-\frac{2t}{1-t}-\frac{t/2}{1-t/4}
-\frac{2at/9}{1-t/9}
=\mathsf H(x^2).
$$

The coefficient identity needed here is $a/(9\Pi)=1/6-5/(4\Pi)$. All denominators are positive for $0<x<\pi$.

### Independent residual calculation

I re-derived the residual from $Q(t)=(1-t)(1-t/4)$, $w(t)=1-t/9$, and $f(t)=Q(t)w(t)^a$, rather than assuming the proposed cubic identity. Since $p(x)=xf(t)$,

$$
p''+p=\frac{x}{\Pi}(6f'+4tf''+\Pi f).
$$

Using $Q'=-5/4+t/2$, $Q''=1/2$, and $w'=-1/9$ gives

$$
\begin{aligned}
-\frac{6f'+4tf''+\Pi f}{w^{a-2}}
={}&-\left(\Pi Q-\frac{15}{2}+5t\right)w^2\\
&+\frac a9\left(6-\frac{35t}{2}+\frac{11t^2}{2}\right)w
-\frac{4a(a-1)}{81}tQ.
\end{aligned}
$$

The constant coefficient vanishes because $2a/3=\Pi-15/2$. Substitution of the stated $a$ gives exactly

$$
-p''-p=\frac{xt}{\Pi}(1-t/9)^{a-2}R_\Pi(t),
$$

with

$$
\begin{aligned}
R_\Pi(t)&=c_0+c_1t+c_2t^2-\frac{\Pi t^3}{324},\\
c_0&=\frac{665}{72}+\frac{5\Pi}{27}-\frac{\Pi^2}{9},\\
c_1&=\frac{175}{432}-\frac{239\Pi}{162}+\frac{5\Pi^2}{36},\\
c_2&=-\frac{1295}{1296}+\frac{131\Pi}{324}-\frac{\Pi^2}{36}.
\end{aligned}
$$

All coefficient formulas and the overall residual sign agree with the source.

### Full-interval sign and endpoint Wronskians

For $49/5<\Pi<99/10$, the derivatives of $c_0$ and $c_2$ are negative. Their displayed endpoint values are exact:

$$
c_0>\frac{323}{1800}>0,\qquad
c_2>\frac{4553}{16200}>0.
$$

Also,

$$
c_1+2c_2
=\frac{\Pi^2}{12}-\frac{2\Pi}{3}-\frac{2065}{1296},
$$

whose derivative is $(\Pi-4)/6>0$. Consequently

$$
c_1+2c_2<-\frac{419}{16200}<0.
$$

The deduction

$$
R_\Pi'(t)=c_1+2c_2t-\frac{\Pi t^2}{108}
<c_1+2c_2<0
$$

holds everywhere on $[0,1]$. For $t<1$, the first comparison is strict because $c_2>0$; at $t=1$, the last quadratic term makes it strict. The exact endpoint formula

$$
R_\Pi(1)=\frac{700}{81}-\frac{8\Pi}{9}<-\frac{28}{405}<0
$$

together with $R_\Pi(0)>0$ establishes exactly one sign change.

For $W=\cos x\,p-\sin x\,p'$, both endpoint values are zero, and

$$
W'=\sin x\,(-p''-p).
$$

Thus $W$ strictly increases from zero before the residual's unique sign change and strictly decreases to zero afterward. Equivalently, integration from zero on the first part and backward from $\pi$ on the second part gives $W>0$ everywhere in $(0,\pi)$. Dividing by $p\sin x>0$ proves the required strict inequality, with the correct orientation:

$$
x\cot x-\mathsf H(x^2)=\frac{xW}{p\sin x}>0.
$$

The endpoint argument is essential and is fully present in the integrated proof. It avoids requiring the residual to have a single sign throughout the interval.

## 2. Reuse of the regular-tail lemma and physical scaling

In both consumers, the physical model tail is

$$
V_m(1+x)=\frac{A_0}{m^2(1-x/h)^2},
\qquad 0<x<h.
$$

The coordinate change $z=(h-x)/h$ sends the interface $x=0$ to $z=1$ and the singular outer endpoint $x=h$ to $z=0$. The normalized equation has

$$
T=h^2E,\qquad \sigma(\sigma-1)=\frac{A_0h^2}{m^2}.
$$

In **lem-robin**, $E$ here is the quantity denoted $\overline E$. The pole-free lemma supplies the same physical energy bound before the change of coordinates, and the Dirichlet spectrum scales by $h^{-2}$. Thus $T$ lies strictly below $\lambda_D(\sigma)$, exactly as required by **lem-regular-tail**. The order satisfies $\sigma>1$.

For a trace-one function $v$ on the normalized interval, put $g(1+x)=v((h-x)/h)$. A direct change of variables gives

$$
\begin{aligned}
&\int_0^h\left(|g_x|^2+
\frac{A_0}{m^2(1-x/h)^2}|g|^2-E|g|^2\right)\,dx\\
&\qquad=\frac1h\int_0^1
\left(|v'|^2+\frac{\sigma(\sigma-1)}{z^2}|v|^2-T|v|^2\right)\,dz.
\end{aligned}
$$

The positive factor $1/h$ preserves the minimizing extension. This is the trace-preserving coordinate change used in the source. The outward derivative at the physical tail's left endpoint is

$$
-g'(1)=\frac{v'(1)}h
=\frac{u_\sigma'(1)}{h\,u_\sigma(1)}
=\frac{D_\sigma(T)}h.
$$

Thus the shifted energy and outward response acquire exactly the same factor, with the stated positive sign.

The new lemma supplies positivity, finite energy, regular asymptotics, and the unique minimizing-extension identification. The consumer proofs retain the common physical interface trace and the original energy throughout. Their potential comparison is made on the same affine domain: a common smooth lifting near the interface plus $H_0^1(1,L)$. The true and model potentials are both bounded above by a constant times $(L-y)^{-2}$; Hardy's inequality gives the asserted common form domains.

Since $f_k(1+x)\le m(1-x/h)$, the true potential is at least the model potential. Comparing shifted energies on this common domain therefore makes the true tail response no smaller. The direction is correct even when the responses themselves are negative. The head comparison is at the same physical $E$, with $K=E-A_0$.

The explicit import of **lem-regular-tail** is present in coupled.qmd; uses inside robin.qmd are same-file dependencies. No new dependency cycle or omitted physical normalization was found.

## 3. The initial T.2 ratio estimate

The identities and strict preliminary bound are correct:

$$
s=\frac{331}{500}+\frac{21}{10}\frac{h+1}{h+2},
\qquad
B-\frac{51h+82}{5(h+2)}
=\frac{81h+112}{250(h+2)}>0.
$$

For

$$
f(h)=\frac{h^2(h+2)}{(h+1)(51h+82)^2},
$$

the logarithmic derivative simplifies to

$$
\frac{f'}f
=\frac{164}{h(51h+82)}-\frac1{(h+1)(h+2)}
=\frac{113h^2+410h+328}{h(h+1)(h+2)(51h+82)}>0.
$$

It is positive for every $h>0$, covering the entire required interval $[3/8,4]$. The endpoint comparison is exactly

$$
f(4)=\frac{24}{102245}<\frac1{4225},
$$

because $24\cdot4225=101400<102245$. Therefore

$$
0<\frac{T_0}{B^2}
<\frac{2961}{4}f(h)
<\frac{2961}{16900}<\frac{30}{169}.
$$

This gives precisely the ratio bound needed by the subsequent positive-denominator estimates. No endpoint or strictness is lost. The R.7 rational constants and the T.2 endpoint arithmetic were also checked independently using exact fractions, without floating-point evaluation.

All requested integrated changes are mathematically consistent with their unchanged downstream conclusions.
