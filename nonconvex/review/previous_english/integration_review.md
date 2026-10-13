# English analytic edition: integration review

Date: 12 October 2026.

## Outcome and scope

The mathematical chapters, rendered main statement, manuscript, project introduction, and supporting documentation are in English. The main conclusion remains nonconvex exclusion for fixed-area simple polygons with at most five active sides, with an exactly-five-active-side competitor when required. The appendix retains the existence argument and an explicitly conditional bridge to a separate convex-pentagon extremal theorem.

The canonical `goals.qmd`, statement lock, `AGENTS.md`, and strict verifier configuration are unchanged from the supplied project. The English goal is a presentation layer with the same ID, quantifiers, fixed-area class, strict inequality, and conditional minimizer conclusion. It is stored outside semantic QMD and does not declare a second main target. The renderer checks the canonical goal's SHA-256 before using this translation.

## Four new analytic replacements

| Location in the PDF | New argument | Mathematical result |
|---|---|---|
| Lemma 2.5, pp. 5–7 | Pull back to a fixed form domain; compare Rayleigh quotients and prove strong convergence of normalized ground states | The two-sided polygonal eigenvalue derivative, followed by the retained corner and stress-tensor argument |
| Lemma 10.3, pp. 30–31 | Affine boundary lifting, exact resolvent energy identity, and projection onto two Dirichlet modes | The same rational cotangent bound, strengthened to a strict inequality with a positive operator defect |
| Lemma 12.1, pp. 47–49 | Uniform curvature of the original continued fraction and an exact reciprocal chord remainder | The denominator gap exceeds `1/2000` throughout the full height and energy range |
| Lemma 13.8, pp. 64–66 | Gaussian supersolutions, adjacent-order recurrence, one factored quintic, and a positive common-interface response | Direct first-eigenvalue bounds on the whole noncrossing interval; the old three trace-polynomial evaluations and the `delta=1/9` split are removed |

### Variational derivative

The root review checked uniform coefficient expansions on the common domain, fixed `L2` normalization, eigenvalue continuity, the weak-to-strong convergence argument, the Rayleigh lower remainder, and both signs of the variation parameter. No derivative of the moving eigenfunction or rate of its convergence is required. Kato's analytic perturbation theorem remains in the separate finite-parameter Steiner argument; its closed-form representation theorem is a distinct retained foundational input.

### Cotangent response

The exact identity is

$$
\sqrt K\cot\sqrt K=1-\frac K3-K^2\langle f,R_Kf\rangle,
\qquad f(y)=y,
\quad R_K=(\mathcal A-K)^{-1}.
$$

The two projection coefficients are `sqrt(2)/pi` and `-sqrt(2)/(2*pi)`; the remainder norm squared is `1/3-5/(2*pi^2)`. The complementary operator begins at `9*pi^2`. The strict defect is justified by the kernel of the positive resolvent difference and the remainder's continuous boundary value. An independent review checked the operator domain, boundary integration, algebraic regrouping into the unchanged rational function, and strictness. The separate trigonometric inequality in the pole-free lemma now follows from the derivatives of two elementary functions.

### Common tail

The root review and independent high-module review rederived the transformed continued fraction, the sign of its denominator and curvature, the convex tangent estimate, the exact chord remainder, both endpoint comparisons, and the final uniform gap. The supplementary exact rational checker passes all 25 checks. Its small rational-function module is included for reproducibility; no program output is an input to the mathematical proof.

### Noncrossing high branch

Independent review rederived the Gaussian residuals, positive recurrence denominators, free comparison residual, outward derivative orientation, and physical map `x=5-4z`. Both pieces use the same energy, divided by 16 under that map; both outward responses are divided by four. The final margins and scaling-monotonicity direction hold on the complete closed parameter interval.

The new lemma bounds the first eigenvalue itself. The old auxiliary assertions concerned an inverse-third-trace surrogate. Those redundant assertions were removed and their needed downstream role was replaced; the new argument is not presented as a proof of the old surrogate assertions.

## Inherited arguments and remaining finite algebra

The earlier analytic edition's degree-thirteen replacement, M.6.7 simplification, continuous-parameter 945 envelope, explicit truncated-square competitor, tensor isotropy, and shared-energy comparison remain in the proof. They are distinguished from this edition's new work in `ANALYTIC_CHANGES.md`.

The explicit T.3 and T.4 positive factorizations and the crossing branch's coefficient-sign proof of a single minimum remain. Their identities, variable ranges, and sign arguments are written in the proof. The current manuscript is independent of finite-element output, parameter boxes, interval-program certificates, and runtime numerical sign decisions. It is not described as eliminating every finite algebraic identity or every classical external theorem.

## Structural and presentation checks

The custom source audit covers all 18 QMD files, 61 declarations, and 57 linked proof blocks. It finds no duplicate semantic IDs, unmatched proofs, unresolved or out-of-scope semantic references, missing exports, dependency cycles, missing book chapters, duplicate equation tags, or unexpected assumed/draft/status markers. The original protected file hashes agree. No Chinese prose or punctuation remains in the noncanonical QMD chapters.

The English goal filter was exercised directly with Pandoc. Its output is in English and preserves the original goal ID and classes. The standalone renderer includes all 61 declarations and 57 proof blocks, checks the protected goal hash, and embeds the bibliography. The source goal itself remains untouched.

The final 81-page PDF was compiled with XeLaTeX. The last compilation reports no errors, warnings, overfull or underfull boxes, missing glyphs, or unresolved references. All pages were rendered for a layout overview. Detailed image inspection covered the title, contents, main statement, new analytic sections, final theorem assembly, conditional corollary, and bibliography. The independent visual reviewers covered pp. 5–8, 30–32, 47–50, and 64–70. No clipping, equation-number collisions, or header/footer overlaps were found. The final title and contents occupy separate pages without changing the mathematical page sequence.

## Verification status

The retained configuration is the `codex` backend, `gpt-6.1-sol`, effort `xhigh`, strict citations, strict rigor, strict refutation rigor, and forbidden assumed dependencies under the main goal. The official qmd-prover and Quarto executables were unavailable in this environment. No official local verdict, global composition, or proof-assistant certification is claimed. The included reports are mathematical review, exact arithmetic, source audit, and PDF production records.

Relevant detailed records are `geometry_english_review.md`, `terminal_english_review.md`, `high_english_review.md`, `cot_resolvent_independent_audit.md`, `high_sturm_independent_audit.md`, `source_check.json`, `tail_curvature_exact_checks.json`, and `pdf_check.json` in this directory.
