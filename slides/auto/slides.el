(TeX-add-style-hook
 "slides"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("babel" "brazilian")))
   (add-to-list 'LaTeX-verbatim-environments-local "semiverbatim")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "beamer"
    "beamer10"
    "inputenc"
    "babel"
    "algorithm"
    "algorithmic"
    "amsmath"
    "amsfonts"
    "amssymb"
    "tikz"
    "times")
   (TeX-add-symbols
    "signed")
   (LaTeX-add-labels
    "fig:tts-arch"
    "fig:arch"
    "tab:intsint")
   (LaTeX-add-environments
    '("aquote" 1))
   (LaTeX-add-saveboxes
    "mybox"))
 :latex)

