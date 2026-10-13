# Nonconvex exclusion for simple pentagons: fourth English analytic edition

This R4 continuation, dated 12 October 2026, makes three substantial parts of the proof more direct: the full short-tail-dominant branch, the noncrossing spectral comparison, and the first terminal head-majorant inequality. It also gives a uniform denominator bound and removes two fourth-degree sign arguments from the head comparison, one of which was repeated. The complete mathematical proofs are integrated into the English manuscript.

**Main conclusion.** Every nonconvex simple polygon with at most five active sides has a same-area simple polygonal competitor with at most five active sides and a strictly smaller first Dirichlet eigenvalue. The competitor may also be required to have exactly five active sides. The appendix's regular-pentagon conclusion remains conditional on a separate convex extremal theorem.

## Complete deliverables

- `manuscript/Nonconvex-Pentagon-Analytic-Proof-English-R4-20261012.pdf`: the complete 85-page English manuscript, including all statements, proofs, and references.
- `manuscript/Nonconvex-Pentagon-Analytic-Proof-English-R4-20261012.tex`: the standalone LaTeX manuscript, with the bibliography embedded.
- `workspace/`: the editable semantic QMD chapters.
- `ANALYTIC_CHANGES.md`: the R4 derivations, exact ranges, and distinction from inherited results.
- `external-inputs.md`: the classical inputs and their precise uses.
- `review/`: independent mathematical audits, integrated derivation records, exact checks, and source and manuscript reports. `review/README.md` distinguishes current and historical records.

## What changes in R4

| Part | New analytic argument | Result and exact scope |
|---|---|---|
| M.4, the branch where the short tail is wider | Geometry gives $2<h\le4$; positive-denominator response estimates reduce the whole branch to one convex rational function and one tangent | The proof gives $\mathcal G-\mathcal B(A,w)>419/2400>1/6$ on all of $\mathcal D_*\cap\{q>p\}$. The declaration keeps the original margin $1/150$. |
| H.6, noncrossing spectral bounds | One positive singular comparison family is glued to a positive free polynomial; the complete quadratic-form identity includes a positive interface jump | The same strict bounds $\Lambda_2>625/32>39/2$ and $\Lambda_3>1525/48>1587/50$ hold for every $0\le\delta\le1/4$. Scaling monotonicity remains valid for all real $2\le a\le3$ and all $\delta\ge0$. |
| T.3, the actual head loss versus the reciprocal majorant | A positive linear rescaling $\mathcal W$ of $M-S$ has negative third derivative; strong convexity handles the lower interval, and concavity of $\mathcal W'$ handles the upper interval | The same $S<M$ holds on $[3/8,4]$. The unchanged subsequent proof still gives $Z_\Psi>289/136800>27/16000$ on the full interval. |
| R.4, positivity of the tail denominator | A square-root bound and one completed square replace the two order cases | Throughout the original domain, including $b=0$, $CD>2(\sigma-29/20)^2+639/200>0$. |
| M.3 and M.3.4, head range and large-height comparison | Direct reciprocal estimates replace two fourth-degree numerator arguments, one of which was repeated | $0<v_h<96/121<1$ for $h>3/8$, and $6R_1/(h+2)<7203/8000<1$ for $h\ge\sqrt2$. All original derivative and boundary assertions remain unchanged. |

The H.6 proof now depends directly only on the comparison operator and its common form domain. It does not use exact regular solutions, adjacent-order recurrence chains, separated spectral bounds, or the trigonometric interface response. The recurrence and regular-solution lemma remain available for the rest of the project; H.5 retains its own required inputs.

The T.3 replacement is a calculus proof of the sign of the original gap. Its rescaling is positive and linear, so it introduces no sign ambiguity. It keeps the same majorant $M$, the same original payment, both gain terms, and the shared head and tail energy. It removes the former degree-seven squared-remainder argument, although the new calculus passage is longer than that identity.

## Inherited results and remaining algebra

R3's Volterra construction, differential factorization, direct tail barrier, two-endpoint cotangent comparison, M.5 gain/tangent argument, M.6 concavity argument, and initial T.2 logarithmic-derivative estimate are retained. T.4 still gives $Z_\Phi>3/500$ for $\sqrt3-1<h\le4$.

The crossing estimate remains

$$
\lambda_1(K_{s;1,t})>\frac{25s-11}{2F_0(t)}
\qquad(2\le s\le3,\ 0\le t\le3/2),
$$

with the geometric constants $39/(2D)$ and $32/D$. Operators and scaling are defined in `workspace/high.qmd`. The retired trace-surrogate assertions and the continuous 945 trace envelope remain retired.

Explicit polynomial identities, rational partial fractions, positive squares, and finite endpoint or tangent calculations remain. The new spectral proof itself uses a positive free polynomial, and the terminal proof uses an elementary cubic maximum. Every interval sign is justified by the written differential, convexity, or variational argument. Grids, numerical eigenvalue approximations, and execution of supplementary scripts are not proof premises. This revision does not claim that every finite algebraic identity or every classical series in the geometric foundations has disappeared.

## Protected theorem and English presentation

All 58 R3 declaration bodies and their metadata are preserved. The parameter-definition files, original `goals.qmd`, statement locks, `AGENTS.md`, and strict verification configuration remain unchanged. The goal retains its canonical Chinese bytes and identity; `render/goal-en.json` and `render/english-goal.lua` supply an English presentation of that same goal. They do not create a second semantic target.

The central theorem excludes nonconvex minimizers. The separate convex-pentagon extremal theorem is an explicit hypothesis only of the final conditional appendix corollary and is absent from the main goal's dependency closure.

## Build and reproduce the checks

The supplied renderer requires Python 3, Pandoc, and XeLaTeX. From the project root:

```sh
python3 render/build_manuscript.py
```

Then run this command twice from `manuscript/`:

```sh
xelatex -interaction=nonstopmode -halt-on-error Nonconvex-Pentagon-Analytic-Proof-English-R4-20261012.tex
```

The accompanying `.bbl` lets the renderer embed the current bibliography. The generated TeX also compiles independently.

The new supplementary exact checks use Python's standard library. The structural checker additionally requires PyYAML:

```sh
python3 review/check_project.py
python3 review/check_r4_boundary.py
python3 review/check_r4_noncrossing.py
python3 review/check_r4_terminal.py
python3 review/check_r4_pole_and_head.py
```

The four R4 scripts contain **108 passing exact checks**: 21 for M.4, 47 for H.6, 28 for T.3, and 12 for the denominator and head reductions. Independent mathematical review checks the full ranges, endpoint behavior, positive multipliers, interface signs, form domains, strictness, and unchanged downstream uses. Exact checks corroborate selected formulas and scalar arithmetic; they are not interval sampling or mathematical verification by execution.

Retained exact scripts are `check_r3_boundaries.py` (30 checks), `check_r3_cot.py` (22), `check_r3_tail.py` (7), and `check_r2_crossing.py` (38). Their inherited outputs are distinguished from the new R4 results. The superseded R3 terminal script and its report are archived under `review/previous_r3/`.

## Review and verification status

The custom source report records **18 QMD files, 58 declarations, and 55 linked proof blocks**. Statement preservation and dependency details appear in `review/r4_statement_preservation.json` and `review/source_check.json`. The 85-page PDF compiled without warnings or overfull/underfull boxes. An automated scan found no off-page text spans. All pages were reviewed in contact sheets, with close and independent checks of the revised proof pages; no unresolved layout defect remains. The final rendering and visual inspection are recorded in `review/pdf_check.json` and the current page-specific QA reports.

The retained configuration is `codex` / `gpt-6.1-sol` / `xhigh`, with strict citations, strict proof and refutation rigor, fresh context, and assumptions forbidden. No setting, lock, or assumption was changed. The official qmd-prover and Quarto executables were unavailable. These custom source checks and independent mathematical reviews are not official local or global verifier verdicts, and no proof-assistant certification is claimed.

The source proofs and the standalone manuscript contain the complete deliverable. Historical records remain under `review/previous_r3/`, `review/previous_r2/`, and `review/previous_english/` with their original scope and edition identified.
