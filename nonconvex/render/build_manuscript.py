#!/usr/bin/env python3
"""Render the semantic QMD proof as a standalone English LaTeX manuscript.

Requirements: Python 3 and Pandoc on PATH. Compile the generated TeX with
XeLaTeX. If a .bbl exists beside the output, its bibliography is embedded.
This renderer does not run or imitate qmd-prover.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir', type=Path, default=ROOT / 'manuscript')
args = parser.parse_args()
OUT = args.output_dir.resolve()
OUT.mkdir(parents=True, exist_ok=True)
STEM = 'Nonconvex-Pentagon-Analytic-Proof-English-R4-20261012'
translation = json.loads((ROOT / 'render/goal-en.json').read_text())
actual_hash = hashlib.sha256((ROOT / 'goals.qmd').read_bytes()).hexdigest()
if actual_hash != translation['canonical_sha256']:
    raise SystemExit('Protected goal changed: review the English presentation before rendering.')

blockpat = re.compile(r'^::: \{([^\n]+)\}\n(.*?)^:::\s*$', re.M | re.S)
refpat = re.compile(r'@((?:def|lem|prp|thm|cor)-[A-Za-z0-9-]+)')
chapters = [
    ('goals.qmd', 'The main theorem and its scope'),
    ('workspace/foundations.qmd', 'Admissible domains and critical variations'),
    ('workspace/geometry.qmd', 'Geometric reduction to one reflex angle'),
    ('workspace/candidate.qmd', 'Actual sections and candidate parameters'),
    ('workspace/interface.qmd', 'The common-interface response principle'),
    ('workspace/constants.qmd', 'Elementary rational bounds'),
    ('workspace/analytic.qmd', 'Middle-height parameters and explicit responses'),
    ('workspace/algebra-definitions.qmd', 'Rational terminal constructions'),
    ('workspace/small.qmd', 'Exclusion of small-height candidates'),
    ('workspace/robin.qmd', 'Head and tail responses and pole-free comparison'),
    ('workspace/monotonicity.qmd', 'Parameter monotonicity and boundary reduction'),
    ('workspace/terminal.qmd', 'Analytic positivity on the terminal curves'),
    ('workspace/high.qmd', 'Large heights: direct Sturm comparison'),
    ('workspace/coupled.qmd', 'Coupled responses and middle-height exclusion'),
    ('workspace/assembly.qmd', 'Emptiness of the candidate set'),
    ('workspace/main-proof.qmd', 'Complete proof of the main theorem'),
    ('workspace/appendix.qmd', 'Degeneration, existence, and the conditional convex bridge'),
]

def convert(md):
    md = re.sub(r'~(@(?:def|lem|prp|thm|cor)-[A-Za-z0-9-]+)~', r' \1 ', md)
    md = refpat.sub(lambda m: r'\ref{' + m[1] + '}', md)
    def citation(match):
        keys = re.findall(r'@([A-Za-z0-9:_-]+)', match[0])
        return r'\cite{' + ','.join(keys) + '}'
    md = re.sub(r'\[(?:[^\]\n]*@[A-Za-z0-9:_-]+[^\]\n]*)\]', citation, md)
    md = re.sub(r'\$\$(.*?)\$\$', lambda m: '$$' + re.sub(r'\n\s*\n', '\n', m[1]) + '$$', md, flags=re.S)
    result = subprocess.run(
        ['pandoc', '--from=markdown+tex_math_dollars+raw_tex+smart', '--to=latex', '--wrap=none'],
        input=md, text=True, capture_output=True, check=True,
    )
    return result.stdout

header = r'''\documentclass[11pt,a4paper]{article}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\usepackage{amsmath,amssymb,amsthm,mathrsfs,bm,mathtools}
\usepackage[a4paper,top=23mm,bottom=23mm,left=23mm,right=23mm]{geometry}
\usepackage{graphicx,booktabs,longtable,array,multirow,xcolor,xurl}
\usepackage[unicode,colorlinks=true,linkcolor=black,citecolor=black,urlcolor=blue!50!black]{hyperref}
\usepackage{bookmark,fancyhdr,enumitem}
\setlength{\headheight}{16pt}
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\small Nonconvex exclusion for simple pentagons}
\fancyhead[R]{\small Analytic proof}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.2pt}
\setlength{\parindent}{1.5em}
\setlength{\parskip}{3pt}
\linespread{1.08}
\setlength{\emergencystretch}{3em}
\setcounter{tocdepth}{1}
\allowdisplaybreaks[1]
\newtheoremstyle{proofmanuscript}{7pt}{5pt}{\normalfont}{}{\bfseries}{.}{\newline}{\thmname{#1}\thmnumber{ #2}\thmnote{ (#3)}}
\theoremstyle{proofmanuscript}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\title{\textbf{Nonconvex Exclusion for Simple Pentagons of Fixed Area}\\[6pt]\large Fourth English analytic edition}
\author{}
\date{12 October 2026}
\begin{document}
\maketitle
\begin{abstract}
Every nonconvex simple polygon of fixed area with at most five active sides admits a strictly better same-area competitor for the first Dirichlet eigenvalue. Continuous Steiner deformation and ear reflection reduce the problem to candidates with their actual Euclidean section geometry. Small heights are excluded by a triangular container. Middle heights are treated by head and tail responses at the same physical interface and energy. A Volterra equation constructs the regular singular-tail solutions, while direct differential comparisons prove the tail and cotangent response bounds. In this edition, one convex lower bound handles the complete short-tail-dominant branch, and one completed square proves positivity of the tail denominator without an order split. A differential argument for a positive rescaling of the head gap replaces the first terminal curve's degree-seven squared-remainder argument; its original payment and subsequent curvature estimate are preserved. At large heights, a positive comparison function glued across the physical interface proves both noncrossing spectral bounds directly on the full form domain. The crossing bound remains uniform for every real order between two and three. The appendix connects the result to existence of minimizers. Its final regular-pentagon corollary explicitly assumes a separate convex-pentagon extremal theorem.
\end{abstract}
\clearpage
\tableofcontents
\clearpage
'''
parts = [header]
counts = {'declarations': 0, 'proofs': 0}
for filename, title in chapters:
    source = (ROOT / filename).read_text()
    if source.startswith('---\n'):
        source = source.split('---', 2)[2]
    parts.append('\n\\section{' + title + '}\n')
    last = 0
    for match in blockpat.finditer(source):
        outside = source[last:match.start()].strip()
        if outside:
            parts.append(convert(outside))
        attrs, body = match[1], match[2]
        attr = dict(re.findall(r'([\w-]+)="([^"]*)"', attrs))
        kind = re.search(r'\.(definition|lemma|proposition|theorem|corollary|proof)\b', attrs)[1]
        ident = re.search(r'#([\w-]+)', attrs)
        if kind == 'proof':
            counts['proofs'] += 1
            parts.append(r'\begin{proof}[Proof of ' + r'\ref{' + attr['of'] + '}]\n')
            parts.append(convert(body))
            parts.append('\\end{proof}\n')
        else:
            counts['declarations'] += 1
            name = attr['name']
            if ident[1] == translation['id']:
                name = translation['name']
                body = translation['statement_markdown']
            name = name.replace('&', r'\&').replace('_', r'\_')
            parts.append('\\begin{' + kind + '}[' + name + ']\\label{' + ident[1] + '}\n')
            parts.append(convert(body))
            parts.append('\\end{' + kind + '}\n')
        last = match.end()
    if source[last:].strip():
        parts.append(convert(source[last:]))

bbl = OUT / (STEM + '.bbl')
if bbl.exists():
    parts.append('\n\\clearpage\n' + bbl.read_text() + '\n\\end{document}\n')
else:
    parts.append('\n\\clearpage\n\\nocite{*}\n\\bibliographystyle{plain}\n\\bibliography{references}\n\\end{document}\n')
tex = '\n'.join(parts)
if re.search(r'[\u3000-\u303f\u3400-\u9fff\uff00-\uffef]', tex):
    raise SystemExit('Unexpected untranslated text in the rendered manuscript.')
(OUT / (STEM + '.tex')).write_text(tex)
shutil.copy2(ROOT / 'references.bib', OUT / 'references.bib')
print(json.dumps({'tex': str(OUT / (STEM + '.tex')), 'bytes': len(tex.encode()), **counts, 'protected_goal_sha256': actual_hash}))
