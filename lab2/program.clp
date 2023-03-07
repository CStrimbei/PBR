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

; Definim regula de colorare
(defrule color-node
    (adjacent ?node $?adjacent)
    (colors $?colors)
    (not (colored ?node $?))
    =>
    (bind ?color (nth$ (random 0 (length$ $?colors)) $?colors))
    (assert (colored ?node ?color))
    (printout t "Coloring " ?node " with " ?color "..." crlf)
)