# Nonconvex exclusion for simple pentagons: third English analytic edition

This is the completed R3 continuation of the English proof, dated 12 October 2026. It replaces the regular-tail series construction, the cotangent resolvent argument, two boundary polynomial calculations, and the two-chart first-terminal comparison with direct integral, differential, and convexity arguments. The second terminal estimate and the large-height spectral constants are retained.

**Main conclusion.** Every nonconvex simple polygon with at most five active sides has a same-area simple polygonal competitor with at most five active sides and a strictly smaller first Dirichlet eigenvalue. The competitor may also be required to have exactly five active sides. The regular-pentagon conclusion in the appendix remains conditional on a separate convex extremal theorem.

## Complete deliverables

- `manuscript/Nonconvex-Pentagon-Analytic-Proof-English-R3-20261012.pdf`: the complete 83-page English manuscript, including the statements, proofs, and references.
- `manuscript/Nonconvex-Pentagon-Analytic-Proof-English-R3-20261012.tex`: the standalone LaTeX manuscript, with the bibliography embedded.
- `workspace/`: the editable semantic QMD chapters.
- `ANALYTIC_CHANGES.md`: the integrated R3 replacements, exact ranges, and inherited results.
- `external-inputs.md`: the classical inputs and their precise uses.
- `review/`: the current mathematical audits, integrated derivation records, portable exact checks, and source/render reports. See `review/README.md` for the distinction between current and historical records.

## What changes in R3

| Part | Integrated replacement | Preserved or strengthened result |
|---|---|---|
| R.6.1, new exported `lem-regular-tail` | A Volterra equation and a global contraction construct regular inverse-square solutions, with endpoint asymptotics and the variational minimizing property | Construction for every real $a>1$ and every $T>0$; positivity and the minimizing property when $T<\lambda_D(a)$ |
| R.6.2, adjacent orders and tail response | First-order differential factorization proves the exact recurrence; one positive comparison function supplies the original tail bound directly | $D_s=s-T/(s+D_{s+1})$ for $s>1$ and $0<T<\lambda_D(s)$, with positive denominator; the proof gives $D_\sigma>\mathsf T(\sigma,T)$ under the original radical and denominator hypotheses |
| R.7, cotangent response | An explicit comparison function, a monotone cubic residual, and a Sturm argument using both zero endpoints replace the finite projection and resolvent proof | The same strict inequality $\sqrt K\cot\sqrt K>\mathsf H(K)$ for all $0<K<\pi^2$ |
| M.5, vanishing short-tail boundary | A pointwise gain bound at fixed $A$ and one convex tangent replace the quartic comparison and the obsolete gain split | The same strict boundary monotonicity on the admissible domain with $3/8<h\le4$ |
| M.6, container equality boundary | A reciprocal-coordinate concavity proof replaces the degree-five numerator | The sufficient expression in (M.6.7) is greater than $1/8$ for every $h\ge1/2$; the remaining small-height branch is retained |
| T.3, first terminal curve | One reciprocal majorant on the full interval, a global curvature correction, and one tangent replace the two response charts | The proof gives $Z_\Psi>289/136800>27/16000$ for $3/8\le h\le4$; the declared margin remains $27/16000$ |
| T.2, initial tail ratio | A positive logarithmic derivative replaces the opening polynomial comparison | The same bound $T_0/B^2<2961/16900<30/169$, with the subsequent common-tail curvature proof retained |

The new regular-tail lemma exports the solution construction and its functional properties so that the crossing and coupled arguments can cite them directly. Its order range is $a>1$, including the higher adjacent orders needed by the noncrossing proof. The tail comparison and both terminal payments continue to use the same physical energy in the head and tail.

## Retained conclusions and remaining algebra

T.4 retains $Z_\Phi>3/500$ for $\sqrt3-1<h\le4$. The crossing estimate retains

$$
\lambda_1(K_{s;1,t})>\frac{25s-11}{2F_0(t)}
\qquad(2\le s\le3,\ 0\le t\le3/2),
$$

and therefore the geometric constants $39/(2D)$ and $32/D$. The noncrossing estimate retains $\Lambda_2(\delta)>625/32>39/2$ and $\Lambda_3(\delta)>1525/48>1587/50$ for $0\le\delta\le1/4$. The operators, scaling, and area function in these statements are defined in `workspace/high.qmd`.

The earlier trace-surrogate assertions and the continuous 945 trace envelope remain retired. They are not asserted by the direct Sturm proof. R3 also removes the finite-projection/resolvent argument from R.7, while preserving its rational response function and complete range.

Explicit finite polynomial identities, rational partial fractions, positive squares, and finitely many endpoint or tangent comparisons remain in the written proof. In particular, the new T.3 majorant has a short polynomial squared-remainder identity with an explicit nonnegative endpoint factor. Each interval conclusion follows from the displayed analytic argument. Grids, numerical spectral calculations, and execution of supplementary scripts are not proof premises.

## Protected theorem and English presentation

The original `goals.qmd`, statement locks, `AGENTS.md`, and strict verification configuration are unchanged. The protected goal retains its canonical Chinese bytes and identity. `render/goal-en.json` and `render/english-goal.lua` provide an English presentation of that same goal; they do not create a second semantic target. The manuscript and proof chapters are in English.

The central theorem excludes nonconvex minimizers. The project does not prove the separate convex-pentagon extremal theorem assumed by the final conditional appendix corollary, and that assumption is not in the main goal's dependency closure.

## Build and reproduce the checks

The manuscript is rendered through the supplied Pandoc/XeLaTeX build, independently of Quarto. The portable renderer requires Python 3, Pandoc, and XeLaTeX. From the project root:

```sh
python3 render/build_manuscript.py
```

Then run this command twice from `manuscript/`:

```sh
xelatex -interaction=nonstopmode -halt-on-error Nonconvex-Pentagon-Analytic-Proof-English-R3-20261012.tex
```

The accompanying `.bbl` allows the renderer to embed the current bibliography. The generated TeX also compiles independently.

The supplementary checks use Python 3; the structural checker additionally requires PyYAML:

```sh
python3 review/check_project.py
python3 review/check_r3_boundaries.py
python3 review/check_r3_cot.py
python3 review/check_r3_tail.py
python3 review/check_r3_terminal.py
python3 review/check_r2_crossing.py
```

The four new R3 exact checkers contain **99 passing checks**: 30 boundary/T.2, 22 cotangent, 7 tail, and 40 terminal checks. The retained crossing checker contains **38 passing checks**. These are exact identity and scalar-arithmetic checks; they do not establish interval signs by sampling or replace mathematical review.

## Review and verification status

The current custom source report records **18 QMD files, 58 declarations, and 55 linked proof blocks**, with no reported source findings, unresolved semantic references, import/export defects, dependency cycles, duplicate equation tags, or changed protected files. All 57 pre-existing declaration bodies are preserved; the only additional declaration is the exported regular-tail lemma. The parameter-definition files also remain byte-identical to R2. Read the JSON reports for the exact scope of each check.

The 83-page PDF has compiled without XeLaTeX warnings or overfull/underfull boxes. An automated scan found no off-page text spans. All 83 pages were reviewed in contact sheets, with close and independent checks of the revised proof pages. A stale sentence about two majorants was corrected and the rebuilt page rechecked. No clipping, overlapping equations, missing glyphs, or unresolved layout defects remain.

The retained qmd-prover configuration is `codex`, model `gpt-6.1-sol`, effort `xhigh`, with strict citations, strict proof and refutation rigor, and assumptions forbidden. The external basis is unrestricted; no restriction file or assumption node was introduced.

**The official qmd-prover and Quarto executables were unavailable during this revision.** The current records document independent mathematical cross-review, exact rational checks, custom source checks, and manuscript inspection. They do not constitute official local verdicts, global qmd-prover composition, or proof-assistant certification. Standard PDF rendering through Pandoc and XeLaTeX is a separate publishing step.

All four current R3 files named `*_proposal.md` are integrated and reviewed derivation records, not pending replacements. Superseded R2 terminal calculations and reports are archived under `review/previous_r2/`; earlier English records remain under `review/previous_english/`. The `r2_crossing_*` records remain current for the retained crossing calculation.
