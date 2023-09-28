#szamologep

print("Számológép")

szam1 = input("Kérek egy számot: ")
while not szam1.isnumberic():
    print("Rossz érték!!!")
    szam1 = input("Kérek egy számot: ")
szam1 = int(szam1)

muvelet =input("Kérem a műveleti jelet (+,-,/,*)")
while muvelet not in ["+", "-", "*", "/"]:
    print("Nem érvényes műveleti jel!!!")
    muvelet =input("Kérem a műveleti jelet (+,-,/,*)")

szam2 = input("Kérek egy számot: ")
while not szam2.isnumberic():
    print("Rossz érték!!!")
    szam1 = input("Kérek egy számot: ")
szam2 = int(szam2)

eredmeny = 0
if muvelet == "+":
    eredmeny = szam1 + szam2
elif muvelet == "-":
    eredmeny = szam1 - szam2
elif muvelet == "*":
    eredmeny = szam1 * szam2
elif muvelet == "/":
    eredmeny = szam1 / szam2

