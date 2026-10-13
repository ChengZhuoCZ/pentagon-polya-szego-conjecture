# R4 documentation and preservation-report audit

## Scope and result

**The mathematical descriptions, constants, ranges, and statement-preservation
claims agree with the integrated R4 source.** The findings below concern
edition-level completion records and one local interval clarification, not
a change to the theorem or an error in the integrated proofs.

Independently reviewed `README.md`, `ANALYTIC_CHANGES.md`, `index.qmd`, the
abstract and output stem in `render/build_manuscript.py`,
`review/source_check.json`, and `review/r4_statement_preservation.json`.
The review also followed their references into `review/README.md`,
`review/integration_review.md`, `review/pdf_check.json`, the exact-check
reports, and the current H.6, M.4, R.4, M.3, and T.3 proof passages.
The frozen R3 source was used for an independent byte comparison.

This audit was begun before the R4 PDF build. During the review, the parent
editor reported successful R4 TeX generation with 58 declarations and 55
proofs and the start of the XeLaTeX passes. This report does not certify
the R4 PDF's final layout. No source, documentation, renderer, or existing
source-check output was edited by this reviewer.

## Findings and disposition

| Finding | Location and evidence | Disposition |
| --- | --- | --- |
| Historical rendering records were still presented as current | At inspection, `review/README.md` and `review/integration_review.md` still described the completed third English edition and its 83-page PDF/QA. `review/pdf_check.json` explicitly named the R3 PDF. The review index also listed the superseded top-level R3 terminal checker, now archived under `previous_r3/`. | Reported. The parent editor confirmed that these edition-level files are being replaced, with the originals already archived. Final R4 page counts and completed QA claims must come from the new build. |
| Completion wording anticipated the R4 PDF/QA | `README.md` lists the intended complete R4 PDF and says final rendering and visual review are recorded, while the R4 build/QA was still in progress at this review. | This is a pre-delivery status issue. It is resolved when the actual R4 PDF, current rendering report, and current QA records have been produced and checked; it is not evidence that those steps had already completed at this audit. |
| Ambiguous use of “verified” | The initial README said H.6 depends on the “verified comparison operator,” despite the absence of official local/global verifier verdicts. | **Resolved during review.** The parent editor changed this to “the comparison operator and its common form domain,” which matches the intended mathematical dependency without implying an official verdict. |
| Singular comparison interval should be explicit | In `ANALYTIC_CHANGES.md`, Section 2, “the residual is strictly positive for $z>0$” follows bounds that require $0<z\le1$. The source itself states the correct interval explicitly. | Reported the precise wording change to “for $0<z\le1$.” The surrounding derivation is correct on that interval. |

The first README paragraph also calls the two fourth-degree calculations
“repeated,” while its detailed table correctly says that one of the two
arguments occurred twice. This is a minor prose ambiguity only; the detailed
change account and source accurately distinguish the two identities and
the repeated occurrence.

## Mathematical descriptions checked against source

### H.6

The descriptions preserve both exact inequalities
$\Lambda_2>625/32>39/2$ and
$\Lambda_3>1525/48>1587/50$ on $0\le\delta\le1/4$.
They correctly distinguish these two spectral applications from
monotonicity for every real $2\le a\le3$ and every $\delta\ge0$.
No interpolated-energy assertion is made.

The documented singular comparison family, positive residual,
same-energy free rescaling, derivative-jump orientation, bounded residual,
core extension, and compact-attainment strictness agree with the source.
The recorded exact jumps $132681/834316$ and $366943/31647780$ agree with
the direct interface calculations. The current source graph gives H.6
exactly one direct dependency, `def-high-operator`. The documentation
correctly retains regular solutions, the adjacent-order lemma, and
trigonometric comparison elsewhere in the project.

### M.4 and R.4

The M.4 account uses the full $\mathcal D_*\cap\{q>p\}$ domain and
correctly derives $2<h\le4$, $\sigma>39/20$, $K/\Pi<1/6$, and
$T<11$. Its margin $419/2400>1/6$ is an internal strengthening;
the declaration retains $1/150$. The documentation does not import the
container restriction or silently reuse the old cutoff $7/3$.

The R.4 account matches the source's completed-square product estimate

$$
CD>2(\sigma-29/20)^2+639/200>0.
$$

It correctly restricts the claim to the original admissible domain,
including $b=0$, and identifies the prior positive bounds used before
division. It does not claim that all geometric cases elsewhere in the
pole-free proof have been removed.

### M.3 and T.3

The two direct reciprocal bounds, their height ranges, and the constants
$96/121$ and $7203/8000$ agree with the integrated M.3 passages. The
small-height derivative comparison and the one-sided conclusion at
$q=p$ remain unchanged.

The T.3 documentation uses the correct positive multiplier of $M-S$,
the correct third derivative, cubic maximum, lower-interval curvature
constant, tangent data, and positive upper-interval endpoint values.
It explicitly acknowledges that the new calculus passage is longer than
the replaced remainder identity. The original majorant and the subsequent
curvature proof, including the correction $1/[2(h+2)]$ and margin
$289/136800>27/16000$, are preserved. An independent source comparison
confirmed that the text from “A uniform curvature bound” to the end of
`terminal.qmd` is byte-identical to R3.

## Independent verification of counts and preservation reports

Without running or modifying `check_project.py`, the review independently
parsed the current and frozen R3 semantic blocks. The result agrees with
both current JSON reports:

- **18 QMD files, 58 declarations, and 55 linked proof blocks**;
- every declaration body and complete metadata header is unchanged;
- no declaration was added or removed;
- exactly six proof blocks changed: `lem-m34-identity`,
  `lem-q-branch-monotone`, `lem-other-branch`, `lem-pole-free`,
  `lem-psi-payment`, and `lem-no-crossing-sturm`;
- the four protected files are byte-identical to frozen R3;
- the current QMD byte total is 228580, matching `source_check.json`.

The exact-check reports confirm **108 new R4 checks**:
$21+47+28+12$. The terminal JSON uses the keys `count` and `passed`,
whereas the other current reports use `check_count` and `all_passed`;
this schema difference does not change the count or result. The inherited
totals 30, 22, 7, and 38 are separately identified correctly. The R3
terminal checker exists in `previous_r3/` and is no longer a top-level
current checker.

## Scope, abstract, and claims about analyticity

The README, index, renderer abstract, protected Chinese theorem, and its
English rendering all describe the same fixed-area nonconvex-exclusion
result. The exactly-five-active-side competitor clause is preserved.
The separate convex extremal theorem remains an explicit hypothesis of
the appendix corollary and is outside the main goal's dependency closure.

The renderer's output stem is the intended R4 stem. Its abstract describes
the new proofs without claiming an unconditional regular-pentagon theorem,
removal of every series, or elimination of all finite algebra. The main
documentation explicitly retains polynomial identities, rational partial
fractions, positive squares, scalar endpoint/tangent comparisons, and
classical series in the geometric foundations. It also correctly states
that supplementary execution is not a proof premise.

The source and statement reports explicitly identify themselves as custom
checks. The strict configuration and the unavailability of official
qmd-prover/Quarto are stated accurately. Apart from the resolved word
“verified,” no official local/global verdict or proof-assistant
certification is implied.

## Follow-up after the R4 build

The rewritten `review/README.md` and `review/integration_review.md` now
describe R4, distinguish the archived R3 terminal calculation, give the
correct 108 new checks and 18/58/55 source counts, and accurately mark
global visual review as pending at their inspection checkpoint. Their
claims about dependencies and preserved statements agree with the source.
The ambiguous “verified” wording remains corrected. The change notes now
explicitly state the singular residual range as $0<z\le1$.

The actual R4 PDF has 85 pages and 490549 bytes, independently confirmed
from the file. This reviewer completed close visual review of pages
70–74 with no defects; the page-specific record and PDF hash are in
`r4_pdf_noncrossing_qa.md`. The parent editor separately reports that all
85 pages have been inspected through contact sheets and that the other
agents' assigned close reviews have passed. Those broader visual checks
are attributed to their reviewers rather than claimed here.

At this follow-up checkpoint, `review/pdf_check.json` still contained its
historical R3 record. The parent editor is replacing it with the final R4
report and artifact hashes after the close-review results arrive. This
remaining delivery-record update does not affect the completed source,
statement-preservation, mathematical-description, or assigned-page visual
audits. No source or documentation edit is requested beyond completing
that already announced report update.

## Final disposition

**All documentation findings are closed.** The final `pdf_check.json`
now identifies R4, 85 pages, 58 rendered declarations and 55 rendered
proof blocks. Its PDF size of 490549 bytes and SHA256
`882ad81a0e6ce7f351d3f785983515b37878df70423e1369566cccb9bcc81d5a`
match this reviewer's independently confirmed artifact. It records
completed overview coverage of all 85 pages and the three independent
close reviews. The corresponding root, geometry, terminal, and
noncrossing QA reports exist and agree with the stated coverage and
passing results.

The final project README, review index, and integration record now
consistently describe the completed 85-page R4 manuscript and visual
review. The README introduction also correctly distinguishes the two
fourth-degree arguments, one of which was repeated. Together with the
previously confirmed interval and terminology corrections, these changes
resolve every finding recorded above. No source edit, additional test,
or further documentation correction is requested. The stated limits on
official verification and the conditional convex bridge remain explicit.
