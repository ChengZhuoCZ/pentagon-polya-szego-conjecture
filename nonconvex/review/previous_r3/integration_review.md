# R3 integration and delivery review

## Mathematical replacements

The third English analytic edition integrates seven related replacements while preserving the original nonconvex-exclusion goal and all 57 pre-existing declaration bodies.

1. **R.6.1:** the new exported regular-tail lemma uses a global Volterra contraction for every real order a > 1 and every positive energy T. It proves uniqueness under the prescribed normalization, the endpoint asymptotics, finite endpoint form energy, positivity below the first Dirichlet eigenvalue, and the trace-one minimizing interpretation. The proof distinguishes a regular solution of the differential equation from a vector in the Dirichlet operator domain.
2. **R.6.2:** first-order differential factorization supplies the exact adjacent-order identity. A single positive comparison function has the exact original endpoint response and a strictly positive residual, so it supplies the original tail bound directly. The recurrence remains available at the higher orders used by the noncrossing argument.
3. **R.7:** an explicit comparison function has exactly the unchanged rational logarithmic derivative. Its residual has one positive-to-negative sign change; the two zero endpoints force a strictly positive Wronskian on the whole open interval. This replaces the finite projection and resolvent proof without changing the response function or range.
4. **M.5:** a pointwise fixed-parameter gain bound removes the obsolete gain split, and a convex tangent removes the quartic comparison in the relevant height/order branch. The proof does not confuse a partial derivative with differentiation along the geometric boundary.
5. **M.6:** reciprocal-coordinate concavity replaces the degree-five numerator and gives a uniform margin greater than 1/8 for every h >= 1/2. The remaining small-height branch is retained.
6. **T.2:** a positive logarithmic derivative and the upper endpoint bound replace the opening polynomial estimate. The subsequent common-tail curvature proof is unchanged.
7. **T.3:** one majorant on 3/8 <= h <= 4 and a single convex correction replace the two response charts. The selected proof gives Z_Psi > 289/136800 > 27/16000. The declared bound, original payment, gain terms, and physical energy are unchanged. The positive squared-remainder identity is displayed and remains ordinary finite algebra.

The regular-tail lemma is explicitly reused in the crossing, Robin, and coupled arguments. The physical scaling is preserved: z = (h-x)/h, T = h^2 E, the normalized shifted form has the physical factor 1/h, and the tail response is u'(1)/(h u(1)). No energy or interface is changed between comparisons.

The second terminal bound remains Z_Phi > 3/500 on its original interval. The retained crossing comparison continues to hold for every real order 2 <= s <= 3 and 0 <= t <= 3/2, with the original geometric constants 39/(2D) and 32/D. The noncrossing constants and adjacent-order inputs are retained. Earlier retired trace-surrogate assertions are not restored or claimed as consequences of the direct Sturm proof.

## Independent mathematical review

The boundary, tail, and first-terminal replacements received independent reviews of their exact identities, derivative signs, positive denominators, endpoint behavior, and full parameter ranges. The final integrated-source audit separately checked R.7, both regular-tail reuse sites, the common-energy scaling, and the shortened T.2 ratio proof. No unresolved mathematical defect was found in those reviews.

The current audit records are r3_boundary_independent_audit.md, r3_tail_independent_audit.md, r3_terminal_independent_audit.md, and r3_integration_independent_audit.md. The four current files named r3_*_proposal.md are explicitly marked as integrated derivation records; retained planning language describes their development history.

## Exact and source checks

The four new exact-check scripts passed all 99 checks: 30 boundary/T.2, 22 cotangent, 7 tail, and 40 terminal checks. The retained crossing script passed all 38 checks. These are exact formal identities and rational scalar comparisons, with no floating-point parameter grids. The written calculus, integral, differential, variational, and Sturm arguments supply the interval conclusions; script execution is not a proof premise.

The final custom source check found 18 QMD files, 58 declarations, and 55 linked proof blocks, with no findings, unresolved semantic references, import/export defects, cycles, duplicate equation tags, untranslated proof chapters, or unexpected assumption/draft markers. The declaration counts are 7 definitions, 48 lemmas, 2 theorems, and 1 corollary.

The statement comparison confirms that every one of the 57 previous declaration bodies is unchanged. The only new declaration is lem-regular-tail. Both parameter-definition files, analytic.qmd and algebra-definitions.qmd, agree byte for byte with R2. The protected main-goal dependency closure has 51 nodes including the goal and the new regular-tail lemma; the conditional convex bridge is absent.

The protected goals.qmd, AGENTS.md, verification configuration, and statement locks agree byte for byte with the preceding project. The goal SHA256 is 14d7b31de04ca7979e4362c08bd276324fd8dc0364b6ff7ab07ec2a2d6ba184f. The English rendering overlay presents this same protected goal.

The README, analytic change record, and review index were checked against the final source for parameter ranges, current and retained bounds, proof counts, historical distinctions, and verification limits.

## Manuscript review

The final English manuscript has 83 pages. The supplied Pandoc renderer and two XeLaTeX passes rendered all 58 declarations and 55 proof blocks. The unchanged bibliography is preserved and embedded in the standalone TeX. The final compile has no warnings, overfull or underfull boxes, missing-glyph warnings, or unresolved references. Automated text-boundary checks found no off-page spans.

All 83 pages were inspected in contact sheets. Root close review covered the title, contents, English main theorem, retained crossing proof's regular-tail reuse, coupled scaling, final conditional corollary, and bibliography. Independent close reviews covered pages 28-33 and 42-47 for the regular tail, cotangent, and boundary arguments, and pages 52-59 for the tail-ratio and terminal arguments. Adjacent continuation pages were examined where needed.

Close review found one stale sentence on page 55 describing the former two-majorant route. It was replaced by the correct single-majorant description, and the PDF was rebuilt twice and reinspected. Only page 55 changed in extracted page text; the page count and all other pages were unchanged. The corrected page is clear. A reported header concern was resolved by the actual PDF spans and raster content: the headers are present. Minor continuations of displays across pages are unambiguous and do not affect readability. No clipping, overlapping formulas, broken glyphs, or unresolved layout defects remain.

The page-specific visual records are r3_pdf_geometry_qa.md and r3_pdf_terminal_qa.md. Current file hashes and exact review locations are recorded in pdf_check.json.

## Limits of the checks and theorem scope

The retained configuration is codex / gpt-6.1-sol / xhigh, with strict citations, strict proof and refutation rigor, and assumptions forbidden. No setting, lock, or assumption was changed to obtain a check result. The external basis remains unrestricted; the current classical inputs and their uses are recorded separately.

The official qmd-prover and Quarto executables were unavailable. Custom source checks are not official local verdicts or global composition, and no proof-assistant certification is claimed. The independent mathematical reviews and exact checks are reported for their actual scope.

The main theorem retains its supplied nonconvex-exclusion scope. A separate convex extremal theorem is an explicit hypothesis only of the appendix corollary. The proof still contains explicit polynomial identities, partial fractions, endpoint arithmetic, and the retained classical corner analysis; this edition does not claim that all finite algebra or all series have disappeared.

Superseded R2 terminal reports and edition-level records are archived under previous_r2/. Earlier English records remain under previous_english/. Current R2 crossing records retain their original names because that calculation is retained. None of the historical records has been relabeled as an R3 check.
