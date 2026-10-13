# A structural replacement for the higher-height Psi payment

## Result and integration scope

The argument below proves

$$
Z_\Psi(h)>\frac{27}{16000}\qquad\left(\frac12\le h\le4\right)
$$

for the existing rational quantity in `def-terminal-rationals`. It retains the existing shared energy, the functions $J,G_*$, and the common affine tail bound. In particular, neither a stronger tail estimate nor a changed spectral comparison is required.

Together with the lower-height argument in `review/r2_psi_low_proposal.md`, this replaces the four-block degree-12 numerator on the entire interval $[3/8,4]$. The proposed integration is to retain the initial denominator, head, and gain estimates in `lem-psi-payment`, replace its final polynomial payment by the two calculus arguments, and delete the unused $D_{\rm pay},N_{\rm pay},Q_4$ definitions. No source QMD file was edited during this analysis.

The project preflight was read independently. The external-basis file is absent. The configured backend remains Codex, model `gpt-6.1-sol`, effort `xhigh`, with citations, rigor, and rigor-disprove all strict and assumptions forbidden. The official `qmd-prover` executable is unavailable; this report does not assert official verification.

## 1. Separate the first head pole

Retain the original proof that $0<k<1/(1+h)<1$. Put

$$
N=300h^3+1295h^2+1349h-96,\qquad
D=2h(1+h)(h+2)^2(60h+127),\qquad k=\frac ND.
$$

In particular, $D-N>0$. Define

$$
S(h)=\frac{2hk}{1-k},\qquad R_0(h)=Z_\Psi(h)+S(h).
$$

Taking partial fractions in the original definition of $Z_\Psi$ gives the exact identity

$$
\begin{aligned}
R_0(h)={}&\frac{389}{3350}h-\frac{25913}{33500}
-\frac{b_0}{h}-\frac{b_2}{h+1}+\frac{b_1}{(h+1)^2}\\
&+\frac{b_4}{h+2}+\frac{b_3}{(h+2)^2}
-\frac{b_5}{h+127/60},
\end{aligned}
$$

where all six constants are positive:

$$
\begin{gathered}
b_0=\frac{213469}{1920000},\qquad
b_1=\frac{225}{268},\qquad
b_2=\frac{11452440743}{3591200000},\\
b_3=\frac{1773689}{1600000},\qquad
b_4=\frac{74489644841}{4502400000},\qquad
b_5=\frac{23869857}{3927875}.
\end{gathered}
$$

This identity is only a change in the representation of the rational payment. Positivity will come from a reciprocal majorant, concavity of a normalized derivative, and one supporting tangent.

## 2. A reciprocal majorant on $h\ge1/2$

Define

$$
P(h)=5(D-N)-2h\left(h+\frac{231}{100}\right)N.
$$

Then

$$
\frac5{h+231/100}-S(h)
=\frac{P(h)}{(h+231/100)(D-N)}.
$$

No expansion of $P$ is needed. Differentiating its defining product gives

$$
P''(h)=3528h^2+\frac{29073}{5}h+\frac{2231}{25}.
$$

This is increasing on the positive half-line. Thus, for $h\ge1/2$,

$$
P''(h)\ge P''(1/2)=\frac{193927}{50}>3800.
$$

The two tangent data are

$$
P(1/2)=\frac{7971}{400}>19,\qquad
P'(1/2)=-\frac{60607}{200},\qquad |P'(1/2)|<304.
$$

The strong-convexity inequality and completion of the square imply

$$
P(h)>19-304\left|h-\frac12\right|
+1900\left(h-\frac12\right)^2
\ge19-\frac{304^2}{7600}
=\frac{3249}{475}>6.
$$

Consequently

$$
S(h)<\frac5{h+231/100}.
$$

It remains to prove positivity of the simpler function

$$
G_+(h)=R_0(h)-\frac5{h+231/100},\qquad
Z_\Psi(h)>G_+(h).
$$

## 3. Concavity of the normalized second derivative

Set

$$
x=\frac1{h+2}\in\left[\frac16,\frac25\right],\qquad
Q(x)=\frac{(h+2)^3}{2}G_+''(h).
$$

Differentiation of the partial fractions gives

$$
Q(x)=b_4+3b_3x-\mathcal R(x),
$$

where

$$
\mathcal R(x)=
\frac{b_0}{(1-2x)^3}
+\frac{b_2}{(1-x)^3}
+\frac{b_5}{(1+7x/60)^3}
+\frac5{(1+31x/100)^3}
-\frac{3b_1x}{(1-x)^4}.
$$

Every displayed denominator is positive. The essential identity is

$$
\begin{aligned}
\mathcal R''(x)
={}&\frac{12}{(1-x)^6}
\left[
4b_0\frac{(1-x)^6}{(1-2x)^5}
+b_2(1-x)-b_1(2+3x)
\right]\\
&+\frac{12b_5(7/60)^2}{(1+7x/60)^5}
+\frac{60(31/100)^2}{(1+31x/100)^5}.
\end{aligned}
$$

We prove positivity of the bracket directly. The coefficient bounds

$$
b_0>\frac1{10},\qquad b_1<\frac{17}{20},\qquad
b_2>\frac{19}{6}
$$

follow immediately from their definitions.

If $1/6\le x\le1/4$, then

$$
b_2(1-x)-b_1(2+3x)
>\frac{19}{6}\frac34-\frac{17}{20}\frac{11}{4}
=\frac3{80}>0.
$$

If $1/4\le x\le2/5$, the function

$$
u(x)=\frac{(1-x)^6}{(1-2x)^5}
$$

is increasing, because

$$
\frac{u'(x)}{u(x)}
=\frac{4+2x}{(1-x)(1-2x)}>0.
$$

Thus $u(x)\ge u(1/4)=729/128$. Using also $b_2>3$ and $b_1<1$, the bracket is greater than

$$
\frac25\frac{729}{128}+3(1-x)-(2+3x)
\ge\frac{729}{320}-\frac75
=\frac{281}{320}>0.
$$

Therefore $\mathcal R''>0$, so

$$
Q''(x)<0\qquad\left(\frac16\le x\le\frac25\right).
$$

This proves strict concavity of the normalized curvature without expanding a high-degree derivative numerator.

## 4. Endpoint signs using coarse rational bounds

The additional simple bounds

$$
\begin{gathered}
b_0<\frac9{80},\quad b_1>\frac56,\quad b_2<\frac{319}{100},\\
\frac{11}{10}<b_3<\frac98,\quad
\frac{33}{2}<b_4<17,\quad b_5<\frac{61}{10}
\end{gathered}
$$

suffice to prove the needed signs. At $x=1/6$, discard the decreases in the last two negative reciprocals to obtain

$$
\begin{aligned}
Q(1/6)
&>\frac{33}{2}+\frac{11}{20}+\frac{108}{125}
-\frac{243}{640}-\frac{17226}{3125}-\frac{61}{10}-5\\
&>\frac9{10}>0.
\end{aligned}
$$

At $x=2/7$, use the exact rational comparisons

$$
\frac{61}{10}\left(\frac{30}{31}\right)^3<\frac{28}{5},\qquad
5\left(\frac{350}{381}\right)^3<\frac{39}{10}.
$$

They give

$$
\begin{aligned}
Q(2/7)
&>\frac{33}{2}+\frac{33}{35}+\frac{343}{125}
-\frac{343}{240}-\frac{109417}{12500}-\frac{28}{5}-\frac{39}{10}\\
&>\frac12>0.
\end{aligned}
$$

Finally, at $x=2/5$, omit the last two negative terms from $Q$ and use the upper bounds on its positive terms:

$$
Q(2/5)
<17+\frac{27}{20}+\frac{1275}{162}
-\frac{25}{2}-\frac{2375}{162}
=-\frac{1523}{1620}<0.
$$

These are endpoint evaluations inside a global concavity argument, not samples used to infer a global sign.

## 5. One inflection and one positive tangent

Strict concavity of $Q$, together with the preceding signs, implies that it has exactly one zero $x_*\in(2/7,2/5)$ on $[1/6,2/5]$. To see the uniqueness explicitly, the superlevel set $\{x:Q(x)\ge0\}$ is an interval because $Q$ is concave. It contains $[1/6,2/7]$, and its right endpoint is strictly less than $2/5$. Strict concavity and positivity at $1/6$ imply strict positivity before that right endpoint and strict negativity afterwards.

Set $h_*=1/x_*-2\in(1/2,3/2)$. Since the normalizing factor $(h+2)^3/2$ is positive,

$$
G_+''(h)<0\quad(1/2\le h<h_*),\qquad
G_+''(h)>0\quad(h_*<h\le4).
$$

In particular, $G_+$ is strictly convex on $[3/2,4]$. Direct rational substitution in the displayed partial-fraction formula gives

$$
G_+(17/8)>\frac1{500},\qquad
0<G_+'(17/8)<\frac1{2000}.
$$

Its supporting tangent therefore proves, for $3/2\le h\le4$,

$$
G_+(h)\ge G_+(17/8)+G_+'(17/8)(h-17/8)
>\frac1{500}-\frac58\frac1{2000}
=\frac{27}{16000}>0.
$$

This proves the required bound at $h=3/2$ before that value is used in the remaining interval.

The other two rational evaluations are

$$
G_+(1/2)>\frac1{400},\qquad G_+'(3/2)<0.
$$

On $[1/2,h_*]$ the derivative $G_+'$ decreases, and on $[h_*,3/2]$ it increases. Its value at $3/2$ is negative. Thus $G_+'$ is negative throughout the second interval, and any zero in the first interval is a change from positive to negative. Every interior stationary point of $G_+$ on $[1/2,3/2]$ is therefore a maximum. Its minimum occurs at an endpoint, whence

$$
G_+(h)\ge\min\{G_+(1/2),G_+(3/2)\}
>\frac{27}{16000}.
$$

Combining the two height ranges with $Z_\Psi>G_+$ proves the stated result.

## 6. Exact endpoint data and independent checks

For fully explicit evaluation of the four scalar data used above,

$$
G_+(1/2)=\frac{2433531573}{923699687500},
$$

$$
G_+'(3/2)=-\frac{149796111140233433}{6010955790564375000},
$$

$$
G_+(17/8)=\frac{30400178207917}{13725647553750000},
$$

$$
G_+'(17/8)=
\frac{11525960738983536155737}{32591802711187012605468750}.
$$

Each required comparison follows by multiplying positive integer denominators. These evaluations are not needed at other heights; the global extension is furnished by the concavity and tangent arguments.

The supplementary exact-arithmetic script is
`/workspace/scratch/037b125b4db9/tmp/r2_terminal/high_psi_convexity.py`,
with its record at
`/workspace/scratch/037b125b4db9/tmp/r2_terminal/high_psi_exact_checks.json`.
It independently checks the original partial-fraction identity, the reciprocal majorant, the normalized curvature identity, the decomposition of $\mathcal R''$, and all rational inequalities displayed above. The proof is complete without running this script.

## 7. Routes explored but not used

A bound of the form $k<125/(50h^2+100h+133)$ was found and can be proved by strong convexity of a small quartic. It was not used: replacing the first head pole by the associated quadratic reciprocal loses too much of the middle-height affine-tail margin. Retaining the continued fraction restores that margin but complicates the final payment.

A separate strengthening of the common-tail curvature argument also gives

$$
\mathcal D(T_0)-\frac1v
>\frac1{2000}+3\omega(x)(2/3-x),\qquad
x=\frac h{h+2},\quad \omega=(x-3/19)(2/3-x).
$$

That additional estimate is not a premise of the successful replacement. The final argument preserves the original affine bound and proves positivity of the original $Z_\Psi$ itself.
