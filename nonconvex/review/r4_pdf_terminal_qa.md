# R4 PDF terminal close review

**Result: PASS. No correction required.**

## Coverage and method

Independently inspected each full-resolution rendered image for printed pages **54–60**, inclusive, of the 85-page R4 PDF. The inputs were `page-54.png` through `page-60.png` in `/workspace/scratch/037b125b4db9/tmp/r4_render/pages/`, each 983 by 1390 pixels. This is a close review of these seven pages; it does not claim independent visual coverage of the other pages.

The review checked mathematical transfer, fraction bars and signs, derivative primes, subscripts and superscripts, missing glyphs, formula widths, clipping, overlaps, vertical spacing, page continuity, running headers, and page-number clearance. The mathematical content of the new weighted-gap passage was also compared with the already audited derivation. No source or renderer file was edited.

## Page-by-page findings

| Printed page | Material inspected | Finding |
|---|---|---|
| 54 | End of the terminal comparison; T.3 declaration; opening positivity and head bounds | All displays and the strict declared margin are readable. The lemma heading stays with its statement and opening proof. The bottom head-comparison display fits above the footer. |
| 55 | Retained gain bound; common head loss and response; six partial-fraction constants; majorant `M` | The aligned gain and response formulas, tag `(T.3.1)`, and large rational constants are distinct and unclipped. The majorant heading and its defining display remain together at the foot of the page. |
| 56 | New weighted-gap definition, product formula, third derivative, scalar maximum, lower-interval tangent, and upper endpoint data | The calligraphic weighted-gap symbol, all derivative orders, strict signs, and displayed constants transferred correctly. Long fractions and the two-line tangent estimate remain legible. No formulas overlap. |
| 57 | Completion of the derivative-concavity argument; positive rescaling; beginning of the retained curvature proof | The conclusion `M-S > 0` displays the correct positive factor. The curvature heading is separated clearly from the completed comparison. The definitions of `Q` and `f` and the paired derivative formulas fit within the text area. |
| 58 | Retained scalar-maximum bounds; uniform and positive curvature estimates; convex correction | Fraction numerators, denominators, and exponents remain clear. The lower bound `Q > -37/75 > -1/2`, the estimate at `2/7`, and the positive second derivative of the corrected response display correctly. |
| 59 | Retained tangent payment; propagation above `3/2`; original response; T.4 declaration and opening proof | The strict payment `289/136800 > 27/16000` and the bound for the original response are readable and unchanged in meaning. T.3 closes visibly before T.4 begins. The new lemma heading stays with its statement and proof. |
| 60 | Retained T.4 head comparison, reciprocal majorant, partial fractions, curvature, and tangent data | The positive quadratic decomposition, tagged response `(T.4.7)`, endpoint estimates, and final tangent values are unclipped and consistently spaced. The last display has adequate clearance above the page number. |

## New argument: specific transfer checks

The rendered passage on pages 56–57 correctly shows the positive linear rescaling

\[
\mathcal W=\frac{15(h+2)^2(D-N)}{2h}(M-S),
\qquad
M-S=\frac{2h}{15(h+2)^2(D-N)}\mathcal W>0.
\]

The third-derivative coefficients `7680`, `48804`, `58071`, `12820`, and `33000`, the scalar maximum `821516000/29403 < 28000`, and the resulting bound `\mathcal W''' < -324/h^4` are rendered without ambiguity. The lower-interval curvature value `140594/3`, tangent data `5979/32` and `-11609/4`, minimum bound `134286119/1440000 > 90`, and upper endpoint data `537851/4`, `113604`, and `227460` match the audited derivation.

## Page continuity and layout

The derivative-concavity paragraph continues from page 56 to page 57 as ordinary prose; the continuation is clear and does not separate an equation from a necessary sign condition. The scalar-maximum setup at the end of page 57 is completed by the display at the top of page 58. This break is readable. The transition from the completed T.3 proof to T.4 on page 59 is clean.

Across all seven inspected pages, running headers, horizontal rules, proof-end squares, and page numbers remain clear of the mathematical content. No missing glyph, clipped text, overlapping display, footer collision, or unreadable page break was found.

This record is a visual and mathematical-transfer review. It does not constitute an official `qmd-prover` verdict or a new global proof audit.
