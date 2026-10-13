# Review records for the fourth English analytic edition

This directory records the R4 revision of 12 October 2026. The current integration record is `integration_review.md`, the structural report is `source_check.json`, the exact statement comparison is `r4_statement_preservation.json`, and the dependency summary is `r4_dependency_review.json`.

The source has 18 QMD files, 58 declarations, and 55 linked proof blocks. The R4 manuscript has compiled to 85 pages without XeLaTeX warnings, overfull or underfull boxes, or off-page text spans. Visual inspection is complete: root inspected all 85 pages in contact sheets, with additional close and independent reviews of the revised proofs. No unresolved layout defect remains. The current records are `pdf_check.json`, `r4_pdf_root_qa.md`, `r4_pdf_geometry_qa.md`, `r4_pdf_terminal_qa.md`, and `r4_pdf_noncrossing_qa.md`.

## Integrated R4 derivations and independent mathematical reviews

All current `r4_*_proposal.md` files are integrated derivation records. Planning language retained inside them describes development history. The authoritative statements and proofs are the QMD chapters.

| Subject | Derivation record | Independent review |
|---|---|---|
| M.4: geometry, uniform head and tail bounds, and one convex tangent | `r4_boundary_proposal.md` | `r4_boundary_independent_audit.md` |
| H.6: one singular comparison family, free polynomial, positive jump, and complete form inequality | `r4_noncrossing_proposal.md` | `r4_noncrossing_independent_audit.md`, Sections 1–4 |
| T.3: positive rescaling of the original head gap, negative third derivative, strong convexity, and derivative concavity | `r4_terminal_proposal.md` | `r4_terminal_independent_audit.md` |
| R.4: one uniform positive denominator product | `r4_pole_and_head_proposal.md` | `r4_noncrossing_independent_audit.md`, Section 5 |
| M.3 and M.3.4: reciprocal head-range and large-height estimates | `r4_pole_and_head_proposal.md` | `r4_noncrossing_independent_audit.md`, Section 6 |

The terminal derivation and checker use q for the weighted gap; the manuscript calls the identical function $\mathcal W$ to avoid collision with the geometric coordinate. The comparison is a positive linear rescaling, with no squaring of $M-S$.

The new M.4 proof gives $\mathcal G-\mathcal B>419/2400>1/6$ throughout its original branch, while its declaration retains $1/150$. H.6 retains the complete real-order scaling-monotonicity statement and both exact strict spectral constants on $0\le\delta\le1/4$. T.3 keeps the original majorant and the entire subsequent curvature proof, so the inherited stronger margin $289/136800>27/16000$ remains available on $[3/8,4]$.

Independent review checks full parameter ranges, strict signs, positive factors and denominators, singular endpoint behavior, physical scaling, the interface-jump sign, core-density extension, compact attainment, and unchanged downstream meanings. The final documentation audit is recorded separately in `r4_documentation_audit.md`.

## New exact checks

Run these from the project root. They use the Python standard library and, where required, `rational_algebra.py` in this directory.

| Script | Output | Passing checks | Scope |
|---|---|---:|---|
| `check_r4_boundary.py` | `r4_boundary_exact_checks.json` | 21 | Geometric identities, range and denominator constants, response partial fractions, curvature and tangent margins |
| `check_r4_noncrossing.py` | `r4_noncrossing_exact_checks.json` | 47 | Independent differential residuals, both fixed parameter pairs, free scaling, derivative jumps, and spectral constants |
| `check_r4_terminal.py` | `r4_terminal_exact_checks.json` | 28 | Original-gap rescaling, third derivative, scalar maximum, tangent and endpoint data, and unchanged response/payment |
| `check_r4_pole_and_head.py` | `r4_pole_and_head_exact_checks.json` | 12 | Completed-square denominator identity and reciprocal head bounds |

The four scripts have **108 passing exact checks**. The M.4 independent audit also records 20 separately reconstructed exact arithmetic checks; these are not added to the count of 108. The terminal audit independently differentiates using separate Laurent-polynomial arithmetic, rather than the author's helper.

All interval implications are supplied by the written proofs. The exact scripts corroborate formulas and rational constants; no floating-point grid, numerical spectrum, or executable sign conclusion is used as a proof premise.

## Source and statement preservation

`check_project.py` requires PyYAML. It is a custom structural checker, not the official qmd-prover compiler or a mathematical verifier. Its current report has no findings, duplicate equation tags, unresolved semantic references, import/export defects, dependency cycles, untranslated proof chapters, or protected-file discrepancies.

The source counts are 7 definitions, 48 lemmas, 2 theorems, and 1 corollary. The exact R3 comparison preserves all 58 declaration bodies and their complete metadata. Only six linked proof blocks changed: `lem-m34-identity`, `lem-no-crossing-sturm`, `lem-other-branch`, `lem-pole-free`, `lem-psi-payment`, and `lem-q-branch-monotone`. There are no added or removed declarations. Both parameter-definition files and all four protected files remain byte-identical.

The main goal's dependency closure contains 51 nodes including the goal. The conditional convex bridge is absent. H.6 now has only `def-high-operator` as a direct semantic dependency. M.4 uses only `def-analytic`, `lem-pi-rational`, and `lem-pole-free`; its former dependency on `lem-derivatives` is removed.

## Retained checks and historical archives

These records remain applicable to unchanged parts of the proof:

| Script or record | Retained subject |
|---|---|
| `check_r3_boundaries.py`, `r3_boundary_exact_checks.json` (30 checks), and the R3 boundary derivation/audit | M.5, M.6, and the initial T.2 ratio bound |
| `check_r3_cot.py`, `r3_cot_exact_checks.json` (22 checks), and `r3_cot_proposal.md` | R.7 two-endpoint cotangent proof; its R3 integrated audit is archived at `previous_r3/r3_integration_independent_audit.md` |
| `check_r3_tail.py`, `r3_tail_exact_checks.json` (7 checks), and the R3 tail derivation/audit | R.6 regular solutions, differential factorization, and the direct tail barrier |
| `check_r2_crossing.py`, `r2_crossing_exact_checks.json` (38 checks), and the R2 crossing derivation/audit | The retained real-order H.5 crossing calculation |
| `check_tail_curvature.py` | The inherited common-tail curvature argument, outside the count of 108 new checks |

These inherited checks are identified by their original editions and are not reported as new R4 work. The R3 terminal checker, squared-remainder derivation, terminal audit, and edition-level source/PDF reports are under `previous_r3/`. That archive documents the former T.3 gap proof; its subsequent curvature calculation is retained, but its former gap certificate is superseded.

`previous_r2/` contains the earlier two-chart terminal records and R2 edition-level reports. `previous_english/` contains still earlier English records. Their page counts and structural claims refer to their original checkpoints, not R4.

## Verification limits and theorem scope

No record is an official qmd-prover local or global verdict. qmd-prover and Quarto were unavailable. The manuscript uses the supplied Pandoc/XeLaTeX workflow; successful rendering is separate from mathematical review.

The retained configuration is `codex` / `gpt-6.1-sol` / `xhigh`, with strict citations, strict proof and refutation rigor, fresh context, and assumptions forbidden. The main goal, statement locks, contract, and configuration remain unchanged. Explicit finite algebra and the retained classical geometric inputs remain in the proof.

The central theorem excludes nonconvex minimizers among the stated simple polygons. The final regular-pentagon corollary explicitly assumes a separate convex extremal theorem; this premise is not part of the central theorem's dependency closure.
