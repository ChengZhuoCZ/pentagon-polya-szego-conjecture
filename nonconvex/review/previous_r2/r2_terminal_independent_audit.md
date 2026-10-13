# Independent terminal audit and integration review

## Scope and conclusion

I independently audited `review/r2_psi_low_proposal.md` and the new `lem-phi-payment`, and read the integrated `lem-psi-payment` in `workspace/terminal.qmd`. Both independently reviewed arguments are mathematically correct. The integrated source preserves the original shared-energy comparisons and proves the strengthened conclusions

$$
Z_\Psi(h)>\frac{27}{16000}\qquad(3/8\le h\le4).
$$

$$
Z_\Phi(h)>\frac3{500}\qquad(\sqrt3-1<h\le4).
$$

No substantive mathematical error was found. The review made no QMD source edits. The higher-height curvature argument was authored by this reviewer, so the comments on its integration below are a transcription and composition check rather than an independent authorship claim.

## 1. The lower-height reciprocal majorant

The identity

$$
M_--S=\frac{P_-}{360h(h+2)(D-N)}
$$

has the stated numerator, and its denominator is positive by the already established $0<k=N/D<1$. Direct differentiation gives exactly the displayed third derivative of $P_-$. On $3/8\le h\le1/2$, the positive linear and quadratic terms and $h^3\le1/8$ give $P_-'''>530562>0$. Therefore the lower endpoint controls $P_-''$ throughout the interval.

Both tangent data at $h=1/2$ and the lower bound $P_-''>70000$ are correct. The strong-convexity tangent inequality applies also to points to the left of the tangent point. Completing its quadratic proves $P_->3751/14>0$; no inference from sampled values is used.

## 2. Normalized curvature and the scalar maximum

The small remaining pole coefficient is exactly

$$
b_0-\frac19=\frac{407}{5760000}>0.
$$

Differentiating the partial fractions gives the source's normalized expression for $(h+2)^3G_-''/2$. In particular, the combined terms with denominator $h+1$ have the sign and coefficient

$$
-\frac{b_2(1-x)-3b_1x}{(1-x)^4},\qquad x=\frac1{h+2}.
$$

The stated scalar maximum is valid on the full domain $x<1$. For positive $A,B$,

$$
f(x)=\frac{A-(A+3B)x}{(1-x)^4}
$$

satisfies

$$
f'(x)=\frac{3[(A-B)-(A+3B)x]}{(1-x)^5}.
$$

Its unique critical point $x=(A-B)/(A+3B)$ is less than one, and the derivative is positive before that point and negative after it. Substitution gives the global maximum $(A+3B)^4/(256B^3)$. The specialized value $457^4/(20480\,67^3)$ is therefore correct.

All coefficient comparisons have the required signs on $x\in[2/5,8/19]$. The positive factor $1-x$ and positive $x$ justify replacing $b_2$ from above and $b_1$ from below inside the numerator. The shifted reciprocal is largest at $x=2/5$, and $(h+2)/h$ is largest at $h=3/8$. The resulting lower bound for the normalized curvature is exactly $11/30>0$.

## 3. The lower endpoint tangent

The exact value and derivative of $G_-$ at $1/2$ agree with the proposal. Its derivative is negative. Consequently the supporting tangent lies at least at the value $G_-(1/2)$ for every $h\le1/2$, proving

$$
Z_\Psi>G_->\frac7{500}.
$$

This exceeds the strengthened full-range constant $27/16000$.

## 4. Integrated higher-height argument and downstream composition

The source correctly uses the stronger, restricted curvature bound $P_+''>3800$ on $h\ge1/2$. The two second-order tangent arguments concern different reciprocal majorants and are each used only on their stated intervals.

The normalization $x=1/(h+2)$ reverses the height order. Strict concavity of $Q$, its positive values at $1/6$ and $2/7$, and its negative value at $2/5$ imply one sign change. The source correctly translates this into a change of $G_+''$ from negative to positive as height increases. I also checked the final coarse endpoint bounds now used in the source: $Q(1/6)>9/10$, $Q(2/7)>1/2$, and $Q(2/5)<-1523/1620$. All coefficient substitutions have the correct inequality direction.

The proof first establishes convexity and the positive supporting tangent on $[3/2,4]$. In particular, it obtains $G_+(3/2)>27/16000$ before using that endpoint in the argument on $[1/2,3/2]$. Since $G_+'(3/2)<0$, the derivative's decrease-then-increase pattern allows no interior minimum of $G_+$ on the latter interval. The endpoint minimum argument is therefore valid.

Finally, both height arguments prove positivity of the original $Z_\Psi$, not of a substituted energy or an unrelated response. The retained head, gain, and common-tail inequalities imply the source's strict bound for the original rational response. The downstream use by `lem-terminal` continues to require exactly that conclusion. Removing $D_{\rm pay},N_{\rm pay},Q_4$ introduces no missing dependency in this proof.

## 5. Independent audit of the new Phi payment

The identity for the first reciprocal is correct:

$$
\frac{45}{8(h+3)}-\frac{2hr}{1-r}
=\frac{45(32h^2-73h+90)}{8(h+3)Q}.
$$

The denominator is positive by the preceding $r<1$ proof. The numerator satisfies

$$
32h^2-73h+90
=32\left(h-\frac{73}{64}\right)^2+\frac{6191}{128}>0.
$$

Subtracting the resulting majorant from the original shared-energy payment gives exactly the three-pole partial-fraction function in the source. Differentiation yields the claimed normalized second derivative. Its subtracted reciprocal sum is strictly convex in $x=1/(h+2)$, so its maximum on $[1/6,11/30]$ is controlled by the two endpoints. The four displayed cube comparisons, the coefficient bounds, and the resulting strict $G''>0$ are correct.

The tangent value and derivative at $h=9/4$ also agree exactly with the source. Since the tangent slope is positive and the left endpoint is $8/11$, the largest downward displacement is $67/44$. The resulting lower bound is

$$
\frac7{500}-\frac{67}{8800}
=\frac{281}{44000}>\frac3{500}.
$$

The actual Phi height range lies inside $[8/11,4]$, so the convexity argument applies to every required point. The retained head and common-tail inequalities then transfer this bound to the required original response.

## 6. What has been replaced

The full-range Psi positivity now follows from two reciprocal majorants, uniform curvature bounds for their product differences, concavity of a normalized second derivative, and supporting tangents. The Phi positivity follows from a reciprocal majorant with a positive quadratic remainder and one convexity argument. These replace the former degree-12 four-block payment and degree-six positive decomposition as load-bearing arguments.

The proof still performs explicit rational algebra and evaluates a few exact tangent data. Those operations are finite, written mathematical calculations. The global interval conclusions do not depend on a grid, a numerical sign certificate, or execution of a checker.

## 7. Portable verification record

The consolidated portable script `review/check_r2_terminal.py` uses only the Python standard library and the adjacent `review/rational_algebra.py`. It can be run from the project root with `python review/check_r2_terminal.py` and writes `review/r2_terminal_exact_checks.json` beside itself. It contains no absolute workspace paths, floating-point evaluations, grids, or sampled interval conclusions.

All **63 exact rational checks passed**. They cover both Psi subintervals, their majorant product identities and derivatives, the common partial fractions, the coarse curvature endpoints in the integrated source, the four higher-height tangent data, and the Phi reciprocal identity, completed square, partial fractions, normalized curvature, and tangent. These checks corroborate displayed identities and isolated rational constants; the analytic arguments establish the interval conclusions without running the script.

The configured verification settings remain Codex, model `gpt-6.1-sol`, effort `xhigh`, strict citations/rigor/rigor-disprove, and assumptions forbidden. This is a mathematical audit and exact-arithmetic corroboration, not an official `qmd-prover` verdict.
