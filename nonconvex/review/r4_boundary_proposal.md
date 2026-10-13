**Integration status:** This derivation is integrated into the linked proof of `lem-other-branch` in the R4 manuscript and has passed independent review. Any proposal language below records its development; the QMD source is authoritative.

# R4 proposal: a uniform convexity proof for M.4

## Scope and preflight

This proposal replaces the proof of `lem-other-branch` in `workspace/monotonicity.qmd`. Its declaration remains exactly unchanged:

> On $\mathcal D_*\cap\{q>p\}$, one has $\mathcal G>1/150+\mathcal B(A,w)>1/150$.

The replacement proves the stronger estimate
$$
\mathcal G-\mathcal B(A,w)>\frac{419}{2400}>\frac16
$$
throughout that entire domain. The stronger bound need not be exported. The proof removes the old height threshold $7/3$, the response split at $h=3$, the two separate evaluations of the tail response, and their parameter-path checks. Its only height reduction is the elementary geometric necessity $h>2$. A single reciprocal-function convexity argument then treats the complete interval $2<h\le4$.

The current project `AGENTS.md`, configuration, and external-basis policy were read independently. The external-basis file is absent. The configured backend remains Codex, model `gpt-6.1-sol`, effort `xhigh`, with strict citations, rigor and disproof rigor, and assumptions forbidden. Neither qmd-prover nor Quarto is available on PATH. This is a written analytic derivation and supplementary exact arithmetic, not an official verifier verdict. No QMD source, protected statement, configuration or lock has been changed.

Only the existing declarations `def-analytic`, `lem-pole-free`, and `lem-pi-rational` are needed. No new external mathematical input is introduced; no numerical sampling is used as a premise.

## Proposed complete replacement proof

Use the definitions in @def-analytic, the pole-free conclusions in @lem-pole-free, and the rational bounds in @lem-pi-rational. In particular,
$$
\frac{49}{5}<\Pi<\frac{99}{10}<10,
\qquad 0<A<1,\qquad 0<K<\Pi.
$$
Suppose $q>p$. All the estimates below use only $\mathcal D_*$; the additional container restriction defining $\mathcal D$ is not used.

### 1. The geometric branch forces $h>2$

Write $L=1+h$ and $D_h=h^2+2h+2$. The area condition is equivalent to
$$
p(1-q)>j(h):=\frac{h(h+2)}{LD_h}.
\tag{B.1}
$$
If $h\le1$, then $q\le h/L\le1/2$. The function $q(1-q)$ is increasing on $[0,1/2]$, so
$$
p(1-q)<q(1-q)\le\frac{h}{L^2}<j(h),
$$
where the last difference is $j(h)-h/L^2=h^2/(L^2D_h)>0$. This contradicts (B.1), and hence $h>1$.

For $1\le h\le2$, the identity
$$
h^3-h^2-4h+2=(h-2)(h-1)(h+2)-2\le-2
$$
gives $j(h)>1/4$. This again contradicts
$p(1-q)<q(1-q)\le1/4$. Therefore
$$
2<h\le4.
\tag{B.2}
$$

### 2. A common order and energy range

Since $m=q$ on this branch, (B.1) gives
$$
R=\frac{Lp}{(h+2)q}
>\frac{h}{D_hq(1-q)}
\ge\frac{4h}{D_h}\ge\frac8{13}.
$$
The last inequality follows because $(4h/D_h)'=4(2-h^2)/D_h^2<0$ on $[2,4]$. Consequently,
$$
\sigma(\sigma-1)=\frac{\Pi R^2}{2}
>\frac{1568}{845}
>\frac{741}{400}
=\frac{39}{20}\frac{19}{20}.
$$
As $\sigma>1$, this implies
$$
\sigma>\frac{39}{20}.
\tag{B.3}
$$

Also $S_0=Lp+(1-q)^{-1}>Lp+(1-p)^{-1}$. Therefore
$$
E<\frac{3\Pi L}{h(h+2)}
\frac{p(1-p)}{1+Lp(1-p)}
\le\frac{3\Pi L}{h(h+2)(h+5)}.
\tag{B.4}
$$
Here $0<p<1$, $p(1-p)\le1/4$, and $t/(1+Lt)$ is increasing for $t\ge0$.

Set
$$
e(h)=\frac{3L}{h(h+2)(h+5)},\qquad
u(h)=h^2e(h)=\frac{3hL}{(h+2)(h+5)}.
$$
The logarithmic derivatives are
$$
\frac{e'}e=\frac1L-\frac1h-\frac1{h+2}-\frac1{h+5}<0,
$$
$$
\frac{u'}u=\frac1h+\frac1L-\frac1{h+2}-\frac1{h+5}>0.
$$
In the second line, pair $1/h$ with $-1/(h+2)$ and $1/L$ with $-1/(h+5)$. Thus (B.2) and (B.4) imply
$$
\frac K\Pi<e(h)<e(2)=\frac9{56}<\frac16,
\qquad
T<\Pi u(h)\le\Pi u(4)=\frac{10\Pi}{9}<11.
\tag{B.5}
$$

### 3. One affine lower bound for the tail response

By (B.3) and (B.5),
$$
r^2=(2\sigma+5)^2-4T
>\frac{3521}{100}>\left(\frac{59}{10}\right)^2.
$$
It follows that
$$
C=\sigma+\frac12+\frac r2>\frac{27}{5},
$$
$$
D=2\sigma+1-\frac TC
>\frac{49}{10}-\frac{55}{27}
=\frac{773}{270}>\frac{20}{7}.
$$
All the quantities used in these divisions are strictly positive. Hence the same estimate holds throughout the branch:
$$
\mathsf T(\sigma,T)=\sigma-\frac TD
>\frac{39}{20}-\frac{7T}{20}.
\tag{B.6}
$$
This step uses direct denominator bounds; it needs no tail-response differentiation, auxiliary parameter path or evaluation at another height.

### 4. Reduce the whole response to one rational function

Let $x=K/\Pi$. The three coefficients
$$
\frac2\Pi,\qquad \frac1{2\Pi},\qquad
\frac13-\frac5{2\Pi}
$$
are positive and sum to $1/3$. Applying their common denominator bound in the formula for $\mathsf H$ gives
$$
\mathsf H(K)\ge1-\frac{K}{3(1-x)}
>1-\frac{2K}{5}>1-\frac{2E}{5},
$$
where (B.5) was used. Combining this with (B.6) and $T=h^2E$ yields
$$
\mathcal G-\mathcal B(A,w)
>1+\frac{39}{20h}-\frac{8+7h}{20}E.
$$
Use (B.4) and $\Pi<10$ in this expression. The exact partial-fraction identity gives
$$
\begin{aligned}
\mathcal G-\mathcal B(A,w)
&>1+\frac{39}{20h}
-\frac{3(8+7h)L}{2h(h+2)(h+5)}\\
&=F(h):=1+\frac3{4h}+\frac3{2(h+2)}-\frac{54}{5(h+5)}.
\end{aligned}
\tag{B.7}
$$

### 5. A single tangent proves the uniform positive margin

For $2\le h\le4$,
$$
\frac{(h+5)^3}{2}F''(h)
=\frac34\left(\frac{h+5}{h}\right)^3
+\frac32\left(\frac{h+5}{h+2}\right)^3-\frac{54}{5}.
$$
The first ratio is at least $9/4>2$, and the second is at least $3/2$. Therefore
$$
\frac{(h+5)^3}{2}F''(h)
>6+\frac{81}{16}-\frac{54}{5}
=\frac{21}{80}>0.
$$
Thus $F$ is strictly convex on this full interval. At the single interior point $h=3$,
$$
F(3)=\frac15,\qquad F'(3)=\frac{61}{2400}>0.
$$
Its supporting tangent gives, for every $2<h\le4$,
$$
F(h)\ge\frac15+\frac{61}{2400}(h-3)
>\frac{419}{2400}>\frac16>\frac1{150}.
$$
Substitution into (B.7) proves the unchanged stated inequality. Finally, $0<A<1$ and $0<w<1$ imply $\mathcal B(A,w)>0$, giving its last strict inequality as well.

## Integration notes

The above proof can replace only the linked proof of `lem-other-branch`. Preserve its ID, name, date, export, and declaration body. None of the equations labelled M.4.2–M.4.5 in the old proof are cited outside that proof; the new proof can use a fresh local sequence or omit explicit equation tags. The old proof's citation of `lem-derivatives` is no longer needed at this declaration, but the result remains used elsewhere in the same file.

The short low-height contradictions in Section 1 establish geometric emptiness. They are not separate response estimates. Once the branch exists, Sections 2–5 use the same bounds and one convexity argument at every admissible point, including all points without the container restriction.

The pole-free section and the retained M.3, M.5 and M.6 arguments were inspected for alternative targets. Their current differential and geometric reductions remain intact. This proposal concentrates on M.4 because it replaces a full response case split and eliminates two separate radical-tail comparisons, rather than changing a scalar constant or repeating the R3 improvements.
