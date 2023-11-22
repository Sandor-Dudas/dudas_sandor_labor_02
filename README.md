# labor_02 beadandó
Dudás Sándor Bence - CET7CJ

Modul: Tkinter, a program grafikus eleminek létrehozásához, és kezelésükhöz szükséges. (a felhasználó ezt látja)

Függvények: - __init__(self, master) az osztály függvénye, ahol létrejön a grafikus felhasználói felület az elemekkel.
            - convert(self) Az átváltás gomb eseménykezelője, ami meghívódik, ha a felhasználó rákattint az Aáváltás gombra, és megjeleníti a felhasználói feluleten (GUI).
            - convert_units(self, quantity, from_unit, to_unit) ez a függvény végzi a mértékegység átváltását.
            - main() az alkalmazás belépési pontja, a program futtatásakor létrehozza a Tkinter-t, és elindítja az "UnitConverter" osztályt a programba.


Osztály:    - __init__ létrehozza az attribútumokat, pl.: master, ami létrehozza a cimkéket az adatbekérő mezőket, és a gombokat.
            - convert, itt van az átváltási logika, felhasználó adatait begyüjti, miután megkapta az adatokat, utánna meghíja a convert_units függvényt, és megjeleníti az eredményt a GUI-n.
            - convert_units, a felhasználó megadta az átváltási adatait, és itt történik meg maga az átváltás a kiinduló és célmértékegység között.

self, az osztályokon bellül használhatóak hivatkozásokra
