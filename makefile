.RECIPEPREFIX = >
.PHONY: pdf pdf-sem pdf-all

# Дата на титуле: день последнего коммита, затронувшего собираемые файлы;
# при незакоммиченных правках или без git — сегодняшний день.
lastdate = d=$$(git log -1 --format=%ad --date=short -- $(1) 2>/dev/null); if [ -z "$$d" ] || [ -n "$$(git status --porcelain -- $(1) 2>/dev/null)" ]; then d=$$(date +%F); fi; echo "$$d"

pdf: content/chapter$(N).md
> mkdir -p pdf
> pandoc -V papersize=A4 -V fontenc=T2A -V linkcolor=cyan -V babel-lang=russian -V mainfont="Liberation Serif" -M date="$$($(call lastdate,content/chapter$(N).md))" -H tex/preamble.tex --pdf-engine=xelatex content/chapter$(N).md -o pdf/chapter$(N).pdf

pdf-sem: content/seminar$(N).md
> mkdir -p pdf
> pandoc -V papersize=A4 -V fontenc=T2A -V linkcolor=cyan -V babel-lang=russian -V mainfont="Liberation Serif" -M date="$$($(call lastdate,content/seminar$(N).md))" -H tex/preamble.tex --pdf-engine=xelatex content/seminar$(N).md -o pdf/seminar$(N).pdf

pdf-all: content/chapter*.md
> mkdir -p pdf
> pandoc -V documentclass=book -V papersize=A4 -V fontenc=T2A -V linkcolor=cyan -V babel-lang=russian -V mainfont="Liberation Serif" -M date="$$($(call lastdate,content/chapter*.md content/literature.md))" -H tex/preamble.tex --pdf-engine=xelatex -f markdown+smart --toc --top-level-division=chapter --number-sections content/chapter*.md content/literature.md content/title.yaml -s -o pdf/atomic-physics.pdf
