# Analytic replacement for the lower part of the first terminal interval

This derivation concerns the original rational payment (Z_\Psi), with the original (J,G_*,s,v,e,k). It does not replace the shared energy or infer geometric admissibility from rational continuation. Its scope is (3/8\le h\le1/2).

Put

\[
N=300h^3+1295h^2+1349h-96,
\qquad D=2h(1+h)(h+2)^2(60h+127).
\]

The existing head argument proves (k=N/D\in(0,1/(1+h))), so (D-N>0). Write

\[
S=\frac{2hk}{1-k}=\frac{2hN}{D-N},\qquad B=Z_\Psi+S.
\]

## 1. A reciprocal majorant from uniform curvature

We claim

\[
S<M(h):=\frac{199}{40(h+2)}-\frac1{9h}.
\]

Indeed,

\[
M-S=\frac{P(h)}{360h(h+2)(D-N)},
\]

where the product expression

\[
P(h)=(1751h-80)(D-N)-720h^2(h+2)N
\]

has third derivative

\[
P'''(h)=618762+11400720h+7281240h^2-705600h^3.
\]

On the interval in question, (P'''>618762-705600/8=530562>0). Thus

\[
P''(h)\ge P''(3/8)=\frac{18878731}{256}>70000.
\]

At (h_0=1/2),

\[
P(h_0)=\frac{6687}{16}>400,
\qquad 0<P'(h_0)=\frac{33711}{8}<4300.
\]

Integrating the second-derivative lower bound, or completing the quadratic in its second-order tangent bound, gives

\[
\begin{aligned}
P(h)
&\ge P(h_0)+P'(h_0)(h-h_0)+35000(h-h_0)^2\\
&\ge P(h_0)-\frac{P'(h_0)^2}{140000}
>400-\frac{4300^2}{140000}
=\frac{3751}{14}>0.
\end{aligned}
\]

This proves the reciprocal majorant on the entire lower interval. The product expression, its derivative, and one second-order tangent replace a coefficient-sign decomposition; no expanded degree-six polynomial is needed.

## 2. Partial fractions of the remaining payment

Define the positive constants

\[
\begin{gathered}
a=\frac{213469}{1920000},\qquad
b=\frac{225}{268},\qquad
c=\frac{11452440743}{3591200000},\\
d=\frac{1773689}{1600000},\qquad
e_1=\frac{74489644841}{4502400000},\qquad
f=\frac{23869857}{3927875}.
\end{gathered}
\]

Here (e_1) is only a partial-fraction coefficient; it is distinct from the physical energy parameter (e). Direct partial fractions of the original (B) give

\[
\begin{aligned}
B(h)={}&\frac{389h}{3350}-\frac{25913}{33500}-\frac{a}{h}
+\frac{b}{(h+1)^2}-\frac{c}{h+1}\\
&+\frac{d}{(h+2)^2}+\frac{e_1}{h+2}
-\frac{f}{h+127/60}.
\end{aligned}
\]

Consequently (Z_\Psi>G_-(h):=B(h)-M(h)). Put

\[
\epsilon=a-\frac19=\frac{407}{5760000},\qquad
d_1=e_1-\frac{199}{40}=\frac{52090204841}{4502400000}.
\]

The small coefficient of (1/h) in (G_-) is (-\epsilon).

## 3. Convexity of the lower payment

Set (x=1/(h+2)\in[2/5,8/19]). Differentiation of the preceding partial fractions gives

\[
\frac{(h+2)^3G_-''(h)}2
=d_1+3dx
-\frac{c(1-x)-3bx}{(1-x)^4}
-\frac{f}{(1+7x/60)^3}
-\epsilon\left(\frac{h+2}{h}\right)^3.
\]

We use the rational comparisons

\[
c<\frac{16}{5},\quad b>\frac{67}{80},\quad
d>\frac{11}{10},\quad d_1>\frac{23}{2}.
\]

The first negative expression is bounded above by

\[
\frac{16/5-457x/80}{(1-x)^4}.
\]

For positive (A,B), the function

\[
\frac{A-(A+3B)x}{(1-x)^4},\qquad x<1,
\]

has derivative with the sign of ((A-B)-(A+3B)x), and therefore has global maximum

\[
\frac{(A+3B)^4}{256B^3}
\]

at (x=(A-B)/(A+3B)). Taking (A=16/5,B=67/80) gives

\[
\frac{c(1-x)-3bx}{(1-x)^4}
<\frac{457^4}{20480\,67^3}<\frac{71}{10}.
\]

The other negative expressions satisfy

\[
\frac{f}{(1+7x/60)^3}
\le f\left(\frac{150}{157}\right)^3<\frac{16}{3},
\qquad
\epsilon\left(\frac{h+2}{h}\right)^3
\le\epsilon\left(\frac{19}{3}\right)^3<\frac1{50}.
\]

All constants can be checked by single rational multiplications. It follows that

\[
\frac{(h+2)^3G_-''(h)}2
>\frac{23}{2}+\frac{33}{25}-\frac{71}{10}-\frac{16}{3}-\frac1{50}
=\frac{11}{30}>0.
\]

Thus (G_-) is strictly convex throughout the lower interval.

## 4. The endpoint tangent

Direct substitution gives

\[
G_-(1/2)=\frac{105145468}{7396171875}>\frac7{500},
\qquad
G_-'(1/2)=-\frac{357200649213}{5160884375000}<0.
\]

Since (h-1/2\le0), the tangent inequality proves

\[
Z_\Psi(h)>G_-(h)
\ge G_-(1/2)+G_-'(1/2)(h-1/2)
\ge G_-(1/2)>\frac7{500}>0.
\]

The preceding head, gain, and common-tail comparisons in T.3 now give the required strict original response on this interval.

## Exact audit margins

The rational gaps used above include

\[
\begin{gathered}
\frac{71}{10}-\frac{457^4}{20480\,67^3}
=\frac{115441503}{6159626240}>0,\\
\frac{16}{3}-f\left(\frac{150}{157}\right)^3
=\frac{12199946824}{364810943217}>0,\\
\frac1{50}-\epsilon\left(\frac{19}{3}\right)^3
=\frac{318787}{155520000}>0,\\
G_-(1/2)-\frac7{500}=\frac{6396247}{29584687500}>0.
\end{gathered}
\]

The checks reproduce identities and individual rational comparisons. They do not serve as premises in place of the displayed interval proofs, and they are not official qmd-prover verification.
