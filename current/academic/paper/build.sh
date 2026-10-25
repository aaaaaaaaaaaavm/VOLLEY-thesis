#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
pdflatex -interaction=nonstopmode -halt-on-error paper.tex > build-pass1.log
pdflatex -interaction=nonstopmode -halt-on-error paper.tex > build-pass2.log
