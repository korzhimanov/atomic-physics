.RECIPEPREFIX = >

pdf: content/chapter$(N).md
> pandoc -V papersize=A4 -V fontenc=T2A -V linkcolor=cyan -V babel-lang=russian -V mainfont="Liberation Serif" --pdf-engine=xelatex content/chapter$(N).md -o pdf/chapter$(N).pdf

pdf-sem: content/seminar$(N).md
> pandoc -V papersize=A4 -V fontenc=T2A -V linkcolor=cyan -V babel-lang=russian -V mainfont="Liberation Serif" --pdf-engine=xelatex content/seminar$(N).md -o pdf/seminar$(N).pdf

pdf-all: content/chapter*.md
> pandoc -V documentclass=book -V papersize=A4 -V fontenc=T2A -V linkcolor=cyan -V babel-lang=russian -V mainfont="Liberation Serif" --pdf-engine=xelatex -f markdown+smart --toc --top-level-division=chapter --number-sections content/chapter*.md content/literature.md content/title.yaml -s -o pdf/atomic-physics.pdf
