# English translation and analytic review: foundations and geometric reduction

Date: 2026-10-12

## Scope and outcome

The four assigned chapters have been translated completely into mathematical English:

| Chapter | Semantic declarations | Linked proof blocks |
| --- | ---: | ---: |
| `workspace/foundations.qmd` | 5 | 4 |
| `workspace/geometry.qmd` | 6 | 6 |
| `workspace/candidate.qmd` | 5 | 5 |
| `workspace/small.qmd` | 1 | 1 |
| Total | 17 | 16 |

The translation covers titles, semantic names, statements, proof prose, and the two Chinese textual annotations inside mathematical expressions. All IDs, exports, classes, proof targets, dates, and explicit cross-file imports are unchanged. The translation preserves all assumptions and proof steps; the subsequent mathematical replacement is described separately below. The terms “active sides,” “area-critical,” “strict competitor,” and “longest connected section” are used consistently with the source definitions.

After finishing the translation, the initial differentiability subsection of `lem-hadamard-corners` was replaced by a direct variational proof. This is a new mathematical simplification: the Hadamard argument now derives the eigenvalue derivative without an analytic eigenpair branch, a spectral-gap inverse, the Banach implicit function theorem, or a differentiated eigenfunction. The existing formula, corner estimates, and boundary-flux argument remain intact.

The theorem's scope is unchanged. These chapters reduce and exclude nonconvex low-energy critical candidates. They do not establish the separate global minimization theorem for convex pentagons.

## New direct proof of the first variation

Pullback by $F_t=I+tV$ puts all variational problems in the fixed space $H_0^1(P)$, with energy and mass forms $a_t,m_t$. Boundedness of $DV$ gives expansions in the appropriate bounded bilinear-form norms:

$$
a_t=a_0+t\dot a_0+O(t^2),\qquad
m_t=m_0+t\dot m_0+O(t^2).
$$

The energy remainder is bounded by $Ct^2\|\nabla u\|_2^2$, and the mass remainder by $Ct^2\|u\|_2^2$. Thus the estimates apply uniformly to varying trial functions, including the unknown minimizers.

Uniform comparison of the forms yields $\lambda_t\to\lambda$. Choose their nonnegative minimizers $u_t$ with the single fixed normalization

$$
m_0(u_t,u_t)=1.
$$

The minimizing identity and coefficient comparison give boundedness in $H_0^1(P)$ and $a_0(u_t,u_t)\to\lambda$. Rellich compactness gives weak $H_0^1$ and strong $L^2$ subsequential limits. The Rayleigh principle and lower semicontinuity identify every limit as a normalized nonnegative ground state. Connectedness and simplicity identify it with $U$. Equality of the limiting energy norms then gives strong convergence $u_t\to U$ in $H_0^1(P)$.

Set $D=\dot a_0(U,U)-\lambda\dot m_0(U,U)$. The fixed trial function gives

$$
\lambda_t-\lambda\le tD+O(t^2).
$$

For the other direction, expand the quotient at the actual minimizer:

$$
\lambda_t-\lambda
=\frac{(a_0-\lambda m_0)(u_t,u_t)}{m_t(u_t,u_t)}
+t\frac{(\dot a_0-\lambda\dot m_0)(u_t,u_t)}{m_t(u_t,u_t)}
+O(t^2)
\ge tD+o(|t|).
$$

The first numerator is nonnegative; strong convergence makes the second quotient converge to $D$. Both inequalities hold for both signs of $t$, without a quantitative rate for $u_t\to U$. Hence $\lambda_t=\lambda+tD+o(|t|)$. The explicit coefficient derivatives recover the original volume formula, which the unchanged stress-tensor and corner argument converts to the original Hadamard boundary formula.

This replacement is local to the Hadamard differentiability step. Kato's analytic form theorem remains in the finite-parameter strictness argument for continuous Steiner deformation in `geometry.qmd`. It would be inaccurate to claim that the entire manuscript has eliminated analytic perturbation theory.

## Mathematical audit of the translated chapters

### Foundations

The square-corner competitor retains the explicit cutoff, not a numerical eigenvalue calculation. With $C_0=16\pi^5/3$ and $0<\varepsilon\le1/32$, the mass loss is at most $C_0\varepsilon^6$ and the added cutoff energy at most $C_0\varepsilon^4$. The elementary comparisons using $\pi<4$ establish the strict deficit in $F=|P|\lambda_1(P)$ after area normalization.

The energy-tensor identity retains its two-sided affine Rayleigh proof. It uses the actual planar area-criticality and the area-preserving family $\exp(tM)P$ for symmetric trace-free $M$. It introduces no criticality assumption for a one-dimensional comparison operator.

The corner argument retains $\alpha=\pi/\omega>1/2$ for every permitted interior angle $\omega<2\pi$. The series bounds imply $|\nabla U|\le Cr^{\alpha-1}$, so the squared edge flux is integrable and the artificial circular-boundary contribution is $O(\varepsilon^{2\alpha-1})\to0$. Reflex angles are therefore covered explicitly. The compatible-mesh construction for vertex velocities still interpolates every additional boundary mesh point from the prescribed original vertex velocities, preserving the side count.

### Geometric reductions

The unique-reflex fan proof does not assume a quadrilateral convex hull. The two-reflex classification retains both placements of the reflex vertices, strict determinant inequalities, full height orderings, and the verification of every single-interval section hypothesis.

Continuous Steiner cancellation retains the exact cancellation parameter and the side-count argument, including horizontal top or bottom sides. The rearrangement steps are performed in the original Euclidean metric; oblique coordinates are used only for determinant signs and height orderings. Brock's monotonicity input and Capriani's equality input remain explicit, with their function-space, critical-set, connected-projection, and boundary-normal hypotheses checked. Finite-parameter strictness still uses the analytic dependence argument described above.

The ear reflection argument retains the geometric inclusion of the reflected half-ear, strict positivity on the reflected boundary, the spectral maximum principle below $\lambda_1(T_-)$, Hopf's lemma, and the strict squared-flux moment. The two endpoint relabelings and the second ear are accounted for explicitly. The approximation lemma retains a bi-Lipschitz realization, a bijection of the two $H_0^1$ spaces, two-sided Rayleigh bounds, exact area normalization, and the exact count of five active sides.

### Candidate reduction and actual section widths

The slicing lemma uses the longest connected component of each open section. It proves measurability, membership of the slice norm in $H_0^1$, zero traces on every component, and finiteness of the induced weighted energy. The density subsequence is chosen once for almost every height and works for every component at that height.

The geometric normalization is a Euclidean similarity. The normalized vertices, area, completed-square ear bound, and physical height are preserved. Above the reflex vertex the two ear intervals have an actual positive gap

$$
\frac{x(\beta\gamma-st)}{hk}>0\qquad(0<x<k).
$$

Thus the profile is exactly the maximum of the two component lengths. It is not the sum of disconnected widths. At the single interface height, the value assigned to the potential has no effect on the quadratic form.

The weighted comparison uses the isotropic energy tensor of the planar ground state to obtain the necessary inequality for every positive weight. It does not assume the spectral necessary condition while proving it. The triangular container proof retains both regimes $d\le1/L$ and $d\ge1/L$, the strict relation $p+q>k/(1+k)$, and the open sector omitted near the reflex vertex, which makes domain monotonicity strict.

### Small heights

The small-height exclusion remains an exact chain of rational inequalities. It uses the positive sign of $d$ when multiplying the lower bound for $S$, strict monotonicity in $v$, the decreasing function $R(h)$, and

$$
R(3/8)=\frac{12287}{14060}>\frac{13}{15}>\frac{\sqrt3}{2}.
$$

The final comparison is justified by $(13/15)^2-3/4=1/900$. No sampling or interval computation is used.

No new load-bearing gap was found in these four chapters during this audit. Beyond the Hadamard differentiability replacement, further geometric shortening was not made where it would remove needed checks of actual sections, side count, or admissibility.

## Checks performed and verification limits

The project instructions and strict configuration were read. There is no `.qmd-prover/.external.qmd` restriction file in this copy. The source Chinese project was not edited during this English task.

Local structural checks established the following:

- All 17 semantic declaration headers and 16 linked proof headers match the Chinese analytic copy after ignoring the translated `name` attributes.
- All explicit import lists are identical, and all semantic block delimiters are balanced.
- None of the four assigned chapter files contains Chinese characters.
- At the translation checkpoint, all inline and displayed mathematical expressions were retained, allowing only the English translation of the two textual annotations in `geometry.qmd`.
- After the new analytic replacement, all mathematical-expression multisets and the sequence of displayed equations outside the initial Hadamard differentiability subsection still match the Chinese analytic source. The comparison covers 153 mathematical fragments in `foundations.qmd`, 325 in `geometry.qmd`, 247 in `candidate.qmd`, and 22 in `small.qmd`; English prose can reorder adjacent inline expressions while preserving their mathematical content.
- The strict `.qmd-prover/config.yml` and protected canonical `goals.qmd` remain byte-identical to the Chinese analytic copy.

The protected canonical goal has SHA-256:

```text
14d7b31de04ca7979e4362c08bd276324fd8dc0364b6ff7ab07ec2a2d6ba184f
```

These checks establish translation completeness, structural preservation, and the stated manual mathematical review. They are not official QMD-Prover verification. QMD-Prover, Quarto, and the configured Codex CLI are unavailable in this environment; no official strict-verification or rendering result is claimed here.
