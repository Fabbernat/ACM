# John

## Fő téma:  játékok visszavezetése Nim-re

A Nim ha jól értem egy olyan játék, hogy van egy tárolóban `x` darab valami, pl. van egy tálban `x` darab babszem.
A játékot 2 játékos játssza.
A játékosok megegyeznek róla, hogy minden lépésben `y` és `z` közötti babszemet ki kell venni a tálból.
Így, ha mind a kettő fél optimálisan játszik, biztosan mindig ugyanaz lesz a győztes
azonos értékű `x` `y` és `z` esetén.

# Feladat megoldásának a leírása
- Igazából hasonlóan kell megoldani, mint a 10. héten vett feladatokat.
- A játék kimenetelét a kezdő játékos (John) számára akarjuk meghatározni, optimális játékstratégiát feltételezve mindkét fél részéről.
- Minden tesztesethez kiszámoljuk a cukorkák számának XOR összegét
- Ha páratlan, akkor az eredmény 1 lesz az adott bitpozíción, ha páros, akkor 0
N 1 és 47 között van - 