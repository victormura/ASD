
# Arbori binari de cautare echilibrati
DariusB, ambitios din fire, va da o multime vida initial si doreste sa ii raspundeti la Q operatii de tipul:

1. inserati numarul X in multime
2. stergeti numarul X din multime (daca acesta exista)
3. afisati 1 daca numarul X este in multime, alftel afisati 0
4. afisati cel mai mare numar Y, mai mic sau egal cu X
5. afisati cel mai mic numar Y, mai mare sau egal cu X
6. afisati in ordine sortata, toate numerele Z, unde X ≤ Z ≤ Y
Ajutati-l pe DariusB sa rezolve operatiile!

## Date de intrare
În fişierul de intrare abce.in se va afla pe prima linie un numar Q. Urmatoarele Q linii vor contine informatiile: tipul operatiei (de la 1 la 6), X si Y (doar daca este operatie de tip 6).

## Date de ieşire
În fişierul de ieşire abce.out se vor afla in ordine, raspunsurile pentru operatiile de tip 3 (1 sau 0), tip 4 si 5, si tip 6 (toate numerele cerute pe aceeasi linie, separate printr-un spatiu).

## Restricţii
* 1 ≤ Q ≤ 100.000
* Pentru 50% din punctaj, 1 ≤ Q ≤ 1.000
* Pentru 30% din punctaj, DariusB va cere sa rezolvati doar operatii de tipurile 1, 2 si 3
* Pentru alte 40% din punctaj, DariusB va cere sa rezolvati doar operatii de tipurile 1, 2, 3, 4 si 5
-1.000.000.000 <= X, Y <= 1.000.000.000
* Se garanteaza ca operatiile de tip 6 sunt maxim 50
* Se garanteaza ca nu se va efectua o operatie de tip 1 cu un X care se afla deja in multime
* Se garanteaza ca mereu vor fi valori de afisat pentru operatiile 4, 5 si 6

