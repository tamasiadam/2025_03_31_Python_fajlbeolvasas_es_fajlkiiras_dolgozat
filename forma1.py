"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""


versenyzok = []
with open('beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nev = adatok[0]
        csapat = adatok[1]
        gyozelmek_szama = int(adatok[2])
        futamok_szama = int(adatok[3])
        versenyzok.append([nev, csapat, gyozelmek_szama, futamok_szama])

futamos = 0
futamos_neve = ""
for versenyzo in versenyzok:
    if versenyzo[3] > futamos:
        futamos = versenyzo[3]
        futamos_neve = versenyzo[0]

nyertes_neve = ""
nyertes_szam = 0
for versenyzo in versenyzok:
    if versenyzo[2] > nyertes_szam:
        nyertes_szam = versenyzo[2]
        nyertes_neve = versenyzo[0]

for futam in versenyzok:
    futamok_szama = []
    futamok_szama.append(futam[3])
    atlag_futam = sum(futamok_szama) / len(futamok_szama)


print(f"A beolvasott fájlban összesen {len(versenyzok)} versenyző szerepel.")
print(f"A legtöbb futamot nyert versenyző: {nyertes_neve}")
print(f"A legtöbb futamot teljesített versenyző: {futamos_neve} ")
print(f"Az átlagos futamszám: {atlag_futam}")

