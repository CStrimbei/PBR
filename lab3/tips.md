- fapt de control pt meniu
- daca nu exista, nu se afiseaza meniul, si ulterior nu mai ruleaza programul
- dupa ce tratam o optiune, facem un alt fapt meniu
- nu il facem decat dupa ce am terminat tratarea optiunii
- in optiune facem fapt optiune si dupa ce a fost completat, il stergem, si refacem faptul meniu
- variabila globala pt calculatul pct. studentului, dupa ce terminam resetam etc

- ultimu lab cu CLIPS

Code example:
(deffacts fapte_initiale
 (meniu)
)

(defrule afiseaza_meniu
?a<-(meniu)
=>
(retract ?a)
(printout t “1. Adaugă…” crlf)
….
(printout t “Dati optiunea:”)
(assert (optiune (read))
)

(defrule citire_laborator
?a<-(optiune 2)
?b<-(student ?x)
?c<-(student (nume ?x))
=>
(retract ?a ?b)
(printout t “Dati punctaje:”)
(modify ?c (laborator (explode$ (readline))))
(assert (meniu))
)
