(TeX-add-style-hook
 "Monografia"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("abnt" "a4paper" "12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("babel" "brazil") ("inputenc" "utf8") ("fontenc" "T1") ("abntcite" "alf") ("color" "pdftex") ("graphicx" "pdftex")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "Includes/Capa"
    "Includes/FolhaRosto"
    "Includes/FolhaAprovacao"
    "Includes/Dedicatoria"
    "Includes/Agradecimentos"
    "Includes/Epigrafe"
    "Includes/Resumo"
    "Includes/Abstract"
    "Capitulos/Introducao"
    "Capitulos/Capitulo2"
    "Capitulos/Capitulo3"
    "Capitulos/Capitulo4"
    "Capitulos/Capitulo5"
    "Capitulos/Consideracoes"
    "Capitulos/ApendiceA"
    "Capitulos/AnexoA"
    "abnt"
    "abnt12"
    "babel"
    "inputenc"
    "fontenc"
    "dsfont"
    "amssymb"
    "amsmath"
    "multirow"
    "abntcite"
    "color"
    "graphicx"
    "colortbl"
    "url"
    "abnt-alf"
    "algorithm"
    "algorithmic"
    "tikz"
    "booktabs")
   (TeX-add-symbols
    '("abrv" ["argument"] 1)
    '("simb" ["argument"] 1)
    "listadesimbolos"
    "l"
    "listadeabreviaturas")
   (LaTeX-add-bibliographies
    "Capitulos/Referencias"))
 :latex)

