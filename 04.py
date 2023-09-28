#számologép
print("Számológép")
def adatkeres(tipus):
    szam = input("Kérek egy számot: ")
    while not szam.isnumeric():
        print("Rossz érték!!!")
        szam = input("Kérek egy számot: ")
    szam = int(szam)
    return szam


# A program eleje
print("Számológép")
szam1 = adatkeres("sz")
muvelet =input("Kérem a műveleti jelet (+,-,/,*)")
while muvelet not in ["+", "-", "*", "/"]:
    print("Nem érvényes műveleti jel!!!")
    muvelet =input("Kérem a műveleti jelet (+,-,/,*)")
szam2 = adatkeres("sz")

eredmeny = 0
if muvelet == "+":
    eredmeny = szam1 + szam2
elif muvelet == "-":
    eredmeny = szam1 - szam2
elif muvelet == "*":
    eredmeny = szam1 * szam2
elif muvelet == "/":
    eredmeny = szam1 / szam2

print(str(szam1).rjust(50))
print(muvelet, end="")
print(str(szam2).rjust(49))
print("".rjust(50, "_"))
print(str(eredmeny).rjust(50))
