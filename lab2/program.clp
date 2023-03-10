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

(defrule define-adj
   =>
   (printout t "Enter a pair of adjacent nodes or type 'done' to continue: ")
   (bind ?input (readline))
   (while (not (eq ?input "done"))
      (assert (adjacent (explode$ ?input)))
      (printout t "Enter a pair of adjacent nodes or type 'done' to continue: ")
      (bind ?input (readline)))
)


; Definim regula de colorare
(defrule colornodes
    (colors $?colors)
    (nodes $?nodes)
    (adjacent $?adjacent)
    =>
    (bind ?node (nth$ ?nodes (random (length$ ?nodes))))
    (bind ?color (nth$ ?colors (random (length$ ?colors))))
    (assert (colored ?node ?color))
    (retract (nodes ?node))
    (retract (adjacent ?adjacent))
    (retract (colors ?color))
)
)