# Beléptetőrendszer
def regisztracio():
    ok_regisztracio = True
    felhasznalo_email = felhasznalonev()
    felhasznalo_jelszo = jelszo_kerese()

    if not jelszo_ellenorzese(felhasznalo_jelszo, 3,"kerem ismet a jelszot"):
        ok_regisztracio = False

        if ok_regisztracio:
            with open("jelszo.txt", "a", encoding="utf-8") as fajl:
                fajl.write(felhasznalo_email + ";" + felhasznalo_jelszo +"\n" )

    return ok_regisztracio

def felhasznalonev():
    felhasznalo_email =input("Kérem az email címét: ")
    while " " in felhasznalo_email or "@" not in felhasznalo_email or "." not in felhasznalo_email :
        felhasznalo_email = input("Nem jó az email!!!\nKérem az email címét: ")
        return felhasznalo_email

def jelszo_kerese():
    felhasznalo_jelszo = input("Kérek egy jeszót (1,a,A, min 8 karakter):")
    ok_jelszo = True
    while ok_jelszo:
        if len(felhasznalo_jelszo) < 8:
            ok_jelszo = False

            van = 0
        for i in range(len(felhasznalo_jelszo)):
            if felhasznalo_jelszo[i].isnumeric():
                van += 1
        if van == 0:
               ok_jelszo = False

        van = 0
        for i in range(len(felhasznalo_jelszo)):
            if felhasznalo_jelszo[i].isupper():
                van += 1
        if van == 0:
            ok_jelszo = False

            van = 0
            for i in range(len(felhasznalo_jelszo)):
                if felhasznalo_jelszo[i].islower():
                    van += 1
            if van == 0:
                ok_jelszo = False

        if not ok_jelszo:
            felhasznalo_jelszo = input("Nem megfelelő a jelszó!!!\nKérek egy jeszót (1,a,A, min 8 karakter):")
            ok_jelszo = True
        else:
            ok_jelszo = False
    return felhasznalo_jelszo
def jelszo_ellenorzese(felhasznalo_jelszo, probalkozas, uzenet):
    i = 1
    jelszo2 = input(uzenet)
    while jelszo2 != felhasznalo_jelszo and i < probalkozas:
        jelszo2 = input(uzenet)
        i += 1
    if jelszo2 == felhasznalo_jelszo:
        ok_jelszo = True
    else:
        ok_jelszo = False
    return ok_jelszo

def beleptetes():
    pass


#Innen indul a program


if regisztracio():
    print("Sikerült a regisztráció, most beléptetjük/")
    beleptetes()
else:
    print("Sajnos nem sikerült a regisztráció! /nPróbálja újra!")
