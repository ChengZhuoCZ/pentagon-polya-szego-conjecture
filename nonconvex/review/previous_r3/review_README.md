# Review records for the third English analytic edition

This directory records the completed R3 revision of 12 October 2026. The current integration record is `integration_review.md`, the custom structural report is `source_check.json`, and the manuscript inspection record is `pdf_check.json`. The source report records 18 QMD files, 58 declarations, and 55 linked proof blocks. The current manuscript has 83 pages; historical page counts below refer to earlier editions.

The 83-page PDF has compiled without XeLaTeX warnings or overfull/underfull boxes, and an automated scan found no off-page text spans. Final visual QA is complete. All pages were inspected in contact sheets, and the revised proof pages received close and independent review. The corrected page 55 was rebuilt and rechecked. The page-specific records are `r3_pdf_geometry_qa.md` and `r3_pdf_terminal_qa.md`.

## Integrated R3 derivations and mathematical audits

All four current files named `r3_*_proposal.md` are **integrated and reviewed derivation records**, not pending replacements. Each has an explicit status note. Any retained proposal language or integration instructions inside them describe the route's development history. The authoritative current statements and proofs are the QMD sources.

| Integrated subject | Derivation record | Independent review |
|---|---|---|
| R.6 regular solution, exact adjacent-order recurrence, and direct tail barrier | `r3_tail_proposal.md` | `r3_tail_independent_audit.md` |
| R.7 cotangent inequality from the two-endpoint Sturm argument | `r3_cot_proposal.md` | `r3_integration_independent_audit.md` |
| M.5 full gain/tangent argument and M.6 concavity bound | `r3_boundary_proposal.md` | `r3_boundary_independent_audit.md` |
| T.3 one majorant, curvature correction $1/[2(h+2)]$, and one tangent | `r3_terminal_proposal.md` | `r3_terminal_independent_audit.md` |

The selected T.3 derivation proves $Z_\Psi>289/136800$ on $3/8\le h\le4$. The manuscript deliberately retains its original declared margin $27/16000$. The earlier tighter curvature choice in the derivation history is not the selected proof.

The regular-tail lemma is exported for every real order $a>1$, and supplies construction for all $T>0$, with positivity and the minimizing interpretation below the corresponding Dirichlet spectrum. The cotangent estimate keeps the entire original range $0<K<\pi^2$. The mathematical reviews distinguish these full ranges from the smaller ranges of particular applications.

## Portable exact checks

Run these scripts from the project root. They use the Python standard library and, where needed, the adjacent `rational_algebra.py` helper.

| Script | Output | Passing checks | Scope |
|---|---|---:|---|
| `check_r3_boundaries.py` | `r3_boundary_exact_checks.json` | 30 | M.5 gain and tangent identities, M.6 concavity identities and endpoint arithmetic, and the shorter T.2 ratio proof |
| `check_r3_cot.py` | `r3_cot_exact_checks.json` | 22 | Cotangent comparison function, residual identities, and rational sign comparisons |
| `check_r3_tail.py` | `r3_tail_exact_checks.json` | 7 | Differential factorization and direct tail-barrier identities |
| `check_r3_terminal.py` | `r3_terminal_exact_checks.json` | 40 | Original $Z_\Psi$ and partial fractions, the single majorant, curvature estimates, and the selected tangent margin |
| `check_r2_crossing.py` | `r2_crossing_exact_checks.json` | 38 retained | The crossing Sturm calculation and its unchanged spectral constants |

The four new R3 scripts contain **99 passing checks**. The crossing checker contributes **38 retained checks** and keeps its R2 filename to identify its origin. These checks use exact formal identities and rational arithmetic, with no floating-point grids or sampled interval conclusions. The written calculus, integral, variational, and Sturm arguments prove the interval statements.

`check_project.py` additionally checks source relationships and protected-file consistency; it requires PyYAML. It is a custom structural checker, not the official qmd-prover compiler or a mathematical verifier. `check_tail_curvature.py` remains available for the inherited common-tail curvature calculation and is outside the count of 99 new R3 checks.

## Current retained records and historical archives

The crossing files `r2_crossing_proposal.md`, `r2_crossing_independent_audit.md`, `check_r2_crossing.py`, and `r2_crossing_exact_checks.json` remain current for the retained H.5 calculation. Its regular solution and cotangent premises now come from the integrated R3 proofs. The crossing and noncrossing spectral constants remain those of the preceding edition; the retired stronger trace-surrogate bounds are not restored.

`previous_r2/` contains the superseded R2 terminal calculations, terminal exact checker, and edition-level reports. Those records describe the former two-chart T.3 proof and the R2 checkpoint. Its T.4 derivation remains useful historical evidence for the unchanged second terminal estimate, but the archived terminal script is not the current R3 checker.

`previous_english/` contains records from the earlier English edition. Its source counts, proof structure, and manuscript page counts refer to that earlier checkpoint. Neither archive should be read as the current R3 source or rendering report.

## Verification limits and theorem scope

No record in this directory is an official qmd-prover local or global verdict. The official qmd-prover and Quarto executables were unavailable. The manuscript uses the supplied Pandoc/XeLaTeX publishing workflow; successful rendering is separate from mathematical verification.

The retained configuration is `codex` / `gpt-6.1-sol` / `xhigh`, with strict citations, strict proof and refutation rigor, and assumptions forbidden. The original protected goal, locks, contract, and configuration remain unchanged. Explicit finite polynomial identities and rational comparisons remain in the proof; code execution and numerical grids are not premises.

The central result excludes nonconvex minimizers among the stated simple polygons. Its current dependency closure has 51 nodes including the goal and the new regular-tail lemma. The separate convex extremal theorem is an explicit hypothesis only of the conditional appendix corollary; that bridge is absent from the main theorem's dependency closure.
