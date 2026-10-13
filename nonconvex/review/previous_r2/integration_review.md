# R2 integration and delivery review

## Mathematical replacements

The current manuscript contains the complete analytic replacements of T.3, T.4, and the crossing branch of H.5. The original terminal payments satisfy \(Z_\Psi>27/16000\) and \(Z_\Phi>3/500\) on their full original intervals. The crossing estimate is valid for every real order \(2\le s\le3\) and \(0\le t\le3/2\), and gives the exact constants required by the original large-height contradiction.

The lower and upper parts of T.3 were developed independently and checked together after integration. T.4 received independent checks of its reciprocal identity, partial fractions, convexity, tangent data, denominator conditions, and geometric connection. The crossing proof was independently re-derived and then checked again in its integrated form, including the regular series, positive barrier, free response, both curvature identities, endpoint arithmetic, variational minimizing extensions, and the common-energy scaling.

The original terminal energy, two gain terms, head bounds, and common tail comparison are preserved. The old payment factorizations and crossing-only trace constructions are absent from the current semantic sources. The removed auxiliary trace-surrogate assertions are not claimed as consequences of the new Sturm proof. The real-order operator extension has its own Hardy/domain and interface proof. The free comparison function is now one shared lemma, used in both large-height cases.

## Exact and source checks

`check_r2_terminal.py` passed all 63 exact checks. `check_r2_crossing.py` passed all 38 exact checks. The scripts use exact polynomial/rational-function identities and rational arithmetic, with no floating-point grids or parameter sampling. The written calculus and variational arguments supply the interval conclusions.

`check_project.py` found 18 QMD files, 57 declarations, and 54 linked proof blocks, with no source findings, unresolved semantic references, scope/import/export defects, cycles, duplicate equation tags, untranslated proof chapters, or unexpected assumption/draft markers. The declaration counts are 7 definitions, 47 lemmas, 2 theorems, and 1 corollary. The protected goal's dependency closure does not include the conditional convex bridge.

The protected `goals.qmd`, `AGENTS.md`, verification configuration, and statement locks agree byte for byte with the preceding project. The goal SHA256 is `14d7b31de04ca7979e4362c08bd276324fd8dc0364b6ff7ab07ec2a2d6ba184f`. The English rendering overlay still represents this same goal.

The README and change record were reviewed against the source. Their bounds, parameter ranges, historical distinctions, removed auxiliary assertions, and verification limits agree with the integrated mathematics.

## Manuscript review

The final English manuscript has 79 pages. Pandoc and XeLaTeX rendered all 57 declarations and 54 proof blocks. BibTeX regenerated the current bibliography, which is embedded in the standalone TeX. The final compile reports no warnings, overfull/underfull boxes, missing glyphs, or unresolved references. PDF text bounds lie within the page rectangles.

All pages were inspected in contact sheets. Close visual checks covered the title, English main theorem, revised terminal calculations, crossing barrier and curvature argument, endpoint/interface conclusion, and references. The terminal pages also received an independent visual review. No clipping, overlapping formulas, broken glyphs, or disruptive page transitions were found. Exact page locations and file hashes are recorded in `pdf_check.json`.

## Limits of the checks

The retained configuration is `codex` / `gpt-6.1-sol` / `xhigh`, with strict citations, strict proof and refutation rigor, and assumptions forbidden. No setting, lock, or assumption was changed to obtain a check result. The external basis is unrestricted; the current external inputs and their hypotheses are recorded separately.

The official qmd-prover and Quarto executables were unavailable. The source scripts are not substitutes for official local verdicts or global composition, and no proof-assistant certification is claimed. The main theorem retains its supplied nonconvex-exclusion scope; the separate convex extremal theorem is an explicit hypothesis only of the appendix corollary.

Earlier review files under `previous_english/` describe the previous edition and have not been relabeled as new checks. The present reports describe the R2 source and manuscript.
