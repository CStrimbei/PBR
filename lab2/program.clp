; Definim culorile posibile
(defrule define-colors
    (not (colors $?))
    =>
    (printout t "Enter the list of colors, separated by spaces: ")
    (bind ?input (readline))
    (assert (colors (explode$ ?input)))
)

; Definim tarile posibile
(defrule define-nodes
    (not (nodes $?))
    =>
    (printout t "Enter the list of nodes, separated by spaces: ")
    (bind ?input (readline))
    (assert (nodes (explode$ ?input)))
)

; Definim perechile de tari vecine
(defrule define-edges
    (not (edges $?))
    =>
    (printout t "Enter the list of edges (pairs of nodes), separated by spaces: ")
    (bind ?input (readline))
    (assert (edges (explode$ ?input)))
)

