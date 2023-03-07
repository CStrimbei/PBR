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

(defrule define-adjacent
    (nodes $?nodes)
    =>
    (foreach ?node ?nodes
        (printout t "Enter the list of adjacent nodes for " ?node ": ")
        (bind ?input (readline))
        (bind ?adjacent (explode$ ?input))
        (assert (adjacent ?node ?adjacent))
    )
)