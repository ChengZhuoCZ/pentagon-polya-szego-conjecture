# R4 noncrossing manuscript visual QA

## Result and scope

**Pass: no clipping, overlap, missing mathematical glyph, numbering defect,
incorrect formula transfer, or unreadable continuation was found on pages
70–74.** No manuscript or renderer change is requested.

The reviewer individually inspected the rendered page images
`page-70.png` through `page-74.png` in
`/workspace/scratch/037b125b4db9/tmp/r4_render/pages/` and compared the
displayed H.6 formulas and downstream constants with the independently
audited source. This is close visual and source-transfer review of these
five pages, not a claim to have visually reviewed every page.

The corresponding manuscript is
`manuscript/Nonconvex-Pentagon-Analytic-Proof-English-R4-20261012.pdf`:

- 85 A4 pages;
- 490549 bytes;
- SHA256: `882ad81a0e6ce7f351d3f785983515b37878df70423e1369566cccb9bcc81d5a`.

## Page-specific findings

| Page | Material inspected | Finding |
| --- | --- | --- |
| 70 | End of the crossing comparison; Lemma 13.6 declaration; scaling and common form domain; H.6.1–H.6.2 | The crossing conclusion and proof ending are clear. The H.6 declaration retains both strict constants and the full interval. The scaled inverse-square potential, indicator, real-order range, and two physical energy pairs are readable. The page ends after a complete energy-pair display, giving a natural continuation into the construction. |
| 71 | Singular comparison family; H.6.3–H.6.5; free polynomial; H.6.6–H.6.7 | The two-line parameter definitions, integral defining the comparison function, long residual factorization, positive-square estimate, and explicit interval $0<z\le1$ fit cleanly. Fractions, primes, exponents, and inequality signs are intact. The free residual and piecewise gluing display are complete and separated from the footer. |
| 72 | Common physical energy; interface calculations; H.6.8–H.6.9; strict spectral conclusion; start of Lemma 13.7 | The free scaling factor 16, the derivative-jump orientation, all four exact endpoint comparisons, and the positive interface term in the form identity match the source. The two-line form identity fits within the text block. Bounded-residual/core-density continuation and compact-attainment strictness are readable, and the concluding margins are unchanged. The next lemma begins with enough accompanying text to identify its setup. |
| 73 | High-height weight and area normalization; full-operator comparison; crossing and noncrossing constants | The coordinate reversal, unitary scaling, potential domination, and Rayleigh comparison are readable. The crossing constants $39/2$ and $32$ and the noncrossing order-three constant $1587/50$ are transferred correctly. The final scalar display is complete before the page break. |
| 74 | Noncrossing assembly and final contradiction; complete Robin response; transition to Section 14 | The first display uses the exact chain $E_\tau h^2<B_\sigma/(1+\delta)^2<\Lambda_\sigma(\delta)/(1+\delta)^2\le h^2\mu_\tau$, with the middle equality to the comparison eigenvalue visible. The range $0\le\delta\le1/4$ is explicit. The complete-response conclusion ends cleanly before Section 14. The following true-tail definition, derivative-response notation, and next lemma are readable and show no collision or clipping. |

All H.6 equation labels from H.6.1 through H.6.9 appear in order. No H.6
display is split across pages. The crossing-to-noncrossing and
high-height-to-coupled-response transitions preserve their mathematical
meaning.

## Limits

This review corroborates presentation and transfer of the already audited
proof. The mathematical derivation and integrated-source audit are
recorded separately in `r4_noncrossing_proposal.md` and
`r4_noncrossing_independent_audit.md`. It does not assert an official
qmd-prover local or global verdict or proof-assistant certification.
