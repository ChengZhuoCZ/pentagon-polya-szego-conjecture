# Nonconvex exclusion for simple pentagons: second English analytic edition

This is the complete R2 continuation of the English proof. It replaces all three long algebraic arguments targeted in this round: the first terminal payment, the second terminal payment, and the crossing large-height trace argument.

**Main conclusion.** Every nonconvex simple polygon with at most five active sides has a same-area simple polygonal competitor with at most five active sides and a strictly smaller first Dirichlet eigenvalue. The competitor may also be required to have exactly five active sides. The appendix's regular-pentagon conclusion remains explicitly conditional on a separate convex extremal theorem.

## Complete deliverables

- `manuscript/Nonconvex-Pentagon-Analytic-Proof-English-R2-20261012.pdf`: the complete English manuscript, including all statements, proofs, and references.
- `manuscript/Nonconvex-Pentagon-Analytic-Proof-English-R2-20261012.tex`: the standalone LaTeX manuscript, with the bibliography embedded.
- `workspace/`: the editable semantic QMD chapters.
- `ANALYTIC_CHANGES.md`: the mathematical replacements, exact ranges, and inherited results.
- `external-inputs.md`: the classical inputs and their hypotheses.
- `review/`: the current mathematical audits, portable exact-identity checks, and source/render reports. The preceding edition's records are retained under `review/previous_english/` and describe that earlier checkpoint.

## What changes in R2

| Part | Previous argument removed | New argument | Explicit conclusion |
|---|---|---|---|
| T.3, first terminal curve | Degree-twelve payment and its four-part factorization | Two reciprocal majorants, uniform curvature, and tangent comparisons | \(Z_\Psi>27/16000\) for \(3/8\le h\le4\) |
| T.4, second terminal curve | Degree-six payment factorization | A positive quadratic remainder, a convex reciprocal sum, and one tangent | \(Z_\Phi>3/500\) for \(\sqrt3-1<h\le4\) |
| H.5, crossing large heights | Green trace, trace polynomials, coefficient-sign single-minimum proof, and characteristic trace identity | A positive Sturm comparison function and concavity of the interface response | \(\lambda_1(K_{s;1,t})>(25s-11)/(2F_0(t))\) for \(2\le s\le3\), \(0\le t\le3/2\) |

The two terminal results strengthen the same original payments, with the same coupled head and tail energy. The crossing result directly proves the eigenvalue constants required by the large-height contradiction. The discarded stronger trace-surrogate assertions are no longer part of the current argument; they are not claimed as consequences of the new proof. Mercer's trace theorem is no longer needed.

The preceding edition's common-tail curvature estimate, variational Hadamard argument, finite-projection cotangent response, noncrossing Sturm comparison, and earlier geometric reductions are retained. Ordinary differentiation, rational arithmetic, elementary square identities, and finitely many endpoint or tangent evaluations still occur. Each remaining interval sign is justified analytically in the text; supplementary code is not a premise of the proof.

## Protected theorem and English presentation

The original `goals.qmd`, statement locks, `AGENTS.md`, and verification configuration are unchanged. The protected goal retains its canonical Chinese bytes and identity. `render/goal-en.json` and `render/english-goal.lua` provide an English presentation of that same goal; they do not create a second semantic target. The manuscript and proof chapters are in English.

## Build and reproduce the checks

The delivered PDF is already compiled. The portable renderer requires Python 3, Pandoc, and XeLaTeX. From the project root:

```sh
python3 render/build_manuscript.py
```

Then run this command twice from `manuscript/`:

```sh
xelatex -interaction=nonstopmode -halt-on-error Nonconvex-Pentagon-Analytic-Proof-English-R2-20261012.tex
```

The accompanying `.bbl` allows the renderer to embed the current bibliography. The generated TeX also compiles independently.

The supplemental checks use Python 3; the structural checker additionally requires PyYAML:

```sh
python3 review/check_project.py
python3 review/check_r2_terminal.py
python3 review/check_r2_crossing.py
```

These scripts reproduce selected exact identities, scalar rational comparisons, and source relationships. They do not numerically sample the intervals, prove theorems by parameter boxes, or replace mathematical review.

## Review and verification status

The R2 source check reports 18 QMD files, 57 declarations, and 54 linked proof blocks, with no unresolved references, import/export defects, dependency cycles, duplicate equation tags, or changed protected files. Read the current JSON reports for their exact scope and results.

The retained qmd-prover configuration is `codex`, model `gpt-6.1-sol`, effort `xhigh`, strict citations, strict proof and refutation rigor, and assumptions forbidden. The external basis is unrestricted; no restriction file or assumption node was introduced.

**The official qmd-prover and Quarto executables were unavailable during this revision.** The current records document independent mathematical cross-review, exact rational checks, source checks, and manuscript inspection. They do not constitute official local verdicts, global qmd-prover composition, or proof-assistant certification. The absence of such a run is not presented as a mathematical refutation of the supplied proof.

The central theorem continues to exclude nonconvex minimizers. A separate convex-pentagon extremal theorem is a hypothesis only of the final conditional appendix corollary.
