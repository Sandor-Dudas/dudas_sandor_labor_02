#szamologep

print("Számológép")

szam1 = input("Kérek egy számot: ")
while not szam1.isnumberic():
    print("Rossz érték!!!")
    szam1 = input("Kérek egy számot: ")
szam1 = int(szam1)