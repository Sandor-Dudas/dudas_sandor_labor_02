# Beléptetőrendszer
def regisztracio():
    ok_regisztracio = True
    felhasznalonev()
    jelszo_kerese()
    ciklus = 1
    while not jelszo_ellenorzese():
        ciklus += 1
        if ciklus > 3:
            ok_regisztracio = False
            break
    return ok_regisztracio

def felhasznalonev():
    felhasznalo_email =input("Kérem az email címét: ")
    while " " in felhasznalo_email or "@" not in felhasznalo_email or "." not in felhasznalo_email :
        felhasznalo_email = input("Nem jó az email!!!\nKérem az email címét: ")

def jelszo_kerese():
    felhasznalo_jelszo = input("Kérek egy jeszót (1,a,A, min 8 karakter):")
    ok_jelszo = True
    while ok_jelszo:
        if len(felhasznalo_jelszo) < 8:
            ok_jelszo = False

        van = False
        for i in range(len(felhasznalo_jelszo)):
            if felhasznalo_jelszo[i].isnumeric():
                van = True
    felhasznalo_jelszo = input("Nem megfelelő a jelszó!!!\nKérek egy jeszót (1,a,A, min 8 karakter):")
def jelszo_ellenorzese():
    ok_jelszo = True
    return ok_jelszo

def beleptetes():
    pass


#Innen indul a program
felhasznalo_email = ""
felhasznalo_jelszo = ""
jelszo_kerese()
if regisztracio():
    beleptetes()
