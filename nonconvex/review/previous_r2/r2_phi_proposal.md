# R2 proposal: a convex reciprocal bound for the Phi terminal curve

Date: 2026-10-12

## Outcome

The proposed reciprocal comparison and convexity argument gives a complete replacement for the degree-six positive factorization in `lem-phi-payment`. The route was proposed by the parent agent and independently rederived here. No correction to its mathematical argument is needed.

The existing quantities and conclusion can be retained. In fact, the argument proves the quantitative bound

$$
Z_\Phi>\frac3{500},\qquad
H_1(k)+\mathcal L_h\!\left(\frac{987}{100}h^2e\right)
>\frac{3}{500h}\ge\frac3{2000}
$$

throughout the original interval $\sqrt3-1<h\le4$. No coefficient list, interval sampling, or global numerical sign check is used. The replacement requires no change to the downstream terminal theorem, and the two positive gain terms remain available there as an additional positive remainder.

This is an analysis-only proposal. No `workspace` file, canonical goal, lock, or configuration file was edited.

## Complete replacement proof

Retain the notation of `lem-phi-payment`:

$$
L=1+h,\qquad
e=\frac{3(13h-2)}{13hL(h+2)},\qquad
z=\frac{13h-2}{15h(h+2)},\qquad
k=e-\frac{z^2}{2},\qquad r=\frac{15e}{16}.
$$

Let $\Pi_+=987/100$, and use $s,v,\mathcal L_h$ from `lem-common-tail-line`. Thus

$$
Z_\Phi=s+h\left(1-\frac{2r}{1-r}-\frac{3r}{2}\right)
-v\Pi_+h^2e.
$$

### 1. The head and tail comparisons retain their original hypotheses

Since $\sqrt3>19/11$, the assumed height satisfies $h>8/11>2/3$. We have

$$
0<\frac{z^2}{2e}
=\frac{13(13h-2)L}{1350h(h+2)}
<\frac{169}{1350}<1,
$$

so $e,k>0$. Also, with $e_0=3/[L(h+2)]$,

$$
e_0-e=\frac6{13hL(h+2)}>0.
$$

Consequently $0<\Pi_+h^2e<T_0$, and `lem-common-tail-line` applies with all its positive denominators.

The identity

$$
\frac{z^2}{2e}-\frac1{16}
=\frac{677h^2-206h-208}{10800h(h+2)}
$$

has positive numerator for $h\ge8/11$: its value at $8/11$ is $32/121$, and its derivative is at least $8566/11$. Hence $k<r$. Furthermore,

$$
\frac{27}{52}-e
=\frac{3(h+4)(3h-2)(3h-1)}{52hL(h+2)}>0.
$$

Thus $0<k<r<405/832<1/2$. The function

$$
H_1(t)=1-\frac{2t}{1-t}-\frac{129t}{100(1-t/4)}
$$

is strictly decreasing on this interval, and

$$
\frac{129}{100(1-r/4)}<\frac{258}{175}<\frac32.
$$

Therefore

$$
H_1(k)>J_\Phi(r):=1-\frac{2r}{1-r}-\frac{3r}{2}.
$$

### 2. Replace the nonlinear head loss by one reciprocal function

Put

$$
Q=208h^3+624h^2-169h+90
=208hL(h+2)(1-r)>0,
$$

and denote the nonlinear head loss by

$$
S(h)=\frac{2hr}{1-r}=\frac{90h(13h-2)}{Q}.
$$

The exact comparison identity is

$$
\frac{45}{8(h+3)}-S(h)
=\frac{45(32h^2-73h+90)}{8(h+3)Q}>0.
$$

Indeed, its numerator follows directly from

$$
Q-16h(h+3)(13h-2)=32h^2-73h+90,
$$

and the remaining quadratic is strictly positive by completing the square:

$$
32h^2-73h+90
=32\left(h-\frac{73}{64}\right)^2+\frac{6191}{128}>0.
$$

Define three positive constants

$$
c_1=\frac{174393}{139360},\qquad
c_2=\frac{54705}{6968},\qquad
c_3=\frac{45}{8},
$$

and the reciprocal comparison function

$$
G(h)=\frac{389h}{3350}-\frac{277649}{435500}
-\frac{c_1}{h+1}+\frac{c_2}{h+2}-\frac{c_3}{h+3}.
$$

Then $Z_\Phi>G(h)$. For a transparent verification of this partial-fraction step, use

$$
s=\frac{1381}{500}-\frac{21}{10(h+2)},
$$

$$
\frac{13h-2}{L(h+2)}=-\frac{15}{h+1}+\frac{28}{h+2},
$$

$$
\frac{h(h+7)(13h-2)}{L(h+2)}
=13h+50+\frac{90}{h+1}-\frac{280}{h+2}.
$$

Substitution into $s+h-3hr/2-v\Pi_+h^2e$ gives

$$
\frac{389h}{3350}-\frac{277649}{435500}
-\frac{c_1}{h+1}+\frac{c_2}{h+2}.
$$

The preceding strict upper bound for $S(h)$ now proves $Z_\Phi>G(h)$.

### 3. Convexity follows from a sum of positive reciprocal powers

The comparison function is strictly convex on $[8/11,4]$. To see this, set

$$
x=\frac1{h+2}\in\left[\frac16,\frac{11}{30}\right],\qquad
f(x)=\frac{c_1}{(1-x)^3}+\frac{c_3}{(1+x)^3}.
$$

Direct differentiation gives

$$
\frac{G''(h)}2
=\frac1{(h+2)^3}\bigl(c_2-f(x)\bigr),
$$

and

$$
f''(x)=\frac{12c_1}{(1-x)^5}+\frac{12c_3}{(1+x)^5}>0.
$$

Thus the maximum of $f$ on the compact interval occurs at an endpoint. Both endpoints can be bounded with small rational comparisons. First, $c_1<21/16$ and $c_2>15/2$. At $x=1/6$,

$$
\left(\frac65\right)^3<2,\qquad
\left(\frac67\right)^3<\frac23,
$$

so

$$
f(1/6)<2\frac{21}{16}+\frac23\frac{45}{8}
=\frac{51}{8}<\frac{15}{2}.
$$

At $x=11/30$,

$$
\left(\frac{30}{19}\right)^3<4,\qquad
\left(\frac{30}{41}\right)^3<\frac25,
$$

and therefore

$$
f(11/30)<4\frac{21}{16}+\frac25\frac{45}{8}
=\frac{15}{2}.
$$

Consequently $f(x)<15/2<c_2$ throughout the interval, proving $G''(h)>0$ without expanding a polynomial numerator.

### 4. A single tangent proves a positive lower bound

At $h_*=9/4$, exact evaluation gives

$$
G(h_*)=\frac{9786437}{673718500}>\frac7{500},
$$

$$
0<G'(h_*)=\frac{209699639}{52112125975}<\frac1{200}.
$$

Convexity and $h\ge8/11$ imply

$$
\begin{aligned}
G(h)
&\ge G(h_*)+G'(h_*)(h-h_*)\\
&\ge G(h_*)-\frac{67}{44}G'(h_*)\\
&>\frac7{500}-\frac{67}{8800}
=\frac{281}{44000}>\frac3{500}.
\end{aligned}
$$

The sign $G'(h_*)>0$ is used in the second line. The final margin is $17/44000$.

### 5. Reassemble the original shared-energy comparison

Both comparisons use the same $e$. The retained head estimate and `lem-common-tail-line` give

$$
\begin{aligned}
H_1(k)+\mathcal L_h(\Pi_+h^2e)
&>J_\Phi(r)+\frac{s-v\Pi_+h^2e}{h}\\
&=\frac{Z_\Phi}{h}
>\frac3{500h}\ge\frac3{2000}>0.
\end{aligned}
$$

This proves the existing lemma statement, with an additional explicit positive margin. The downstream `lem-terminal` continues to add $\mathcal B(A,w)>0$, so both original gain terms remain untouched.

## Independent checks and implementation boundary

The project-specific preflight was performed on the R2 copy. The configuration remains `backend: codex`, `model: gpt-6.1-sol`, `effort: xhigh`, with strict citations, rigor, and disproof rigor, and `assumptions: forbid`. The external-policy file is absent. No official verification verdict is claimed.

The reciprocal identity, partial fractions, differential identities, and interval directions were checked by direct algebra. A separate exact rational-arithmetic calculation reproduced both tangent values and the useful margins:

$$
G(9/4)-\frac7{500}=\frac{177189}{336859250}>0,
$$

$$
\frac1{200}-G'(9/4)=\frac{406887927}{416897007800}>0,
$$

$$
c_2-\frac{15}{2}=\frac{2445}{6968}>0,
\qquad
\frac{21}{16}-c_1=\frac{8517}{139360}>0.
$$

Implementation can retain the existing semantic ID, definitions of $J_\Phi$ and $Z_\Phi$, and lemma conclusion. Only the degree-six common-denominator passage needs replacement, together with an updated human-readable lemma name. The original degree-six factorization happened to prove positivity on the larger interval $[2/3,4]$; this replacement proves it on $[8/11,4]$, which contains the entire stated terminal range. No use of that unused larger interval is needed downstream.
