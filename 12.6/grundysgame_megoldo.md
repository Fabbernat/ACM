# Grundy's Game
## Fő téma: Sprague-Grundy tétel, játékok visszavezetése Nim-re



# Feladat megoldásának a leírása


Előre kiszámoltam és egy tömbben eltároltam azokat az n értékeket (1 és 10^6 között), 
amelyekre a második játékos nyer, ha mindkét játékos optimálisan játszik.
Ezután a bemenetben kapott n értékekre kikerestem a tömbből, hogy a második játékos nyer-e, és ennek megfelelően outputotja a helyes válasz.
Az algoritmus lényegében egy lookup table mappelése input alapján