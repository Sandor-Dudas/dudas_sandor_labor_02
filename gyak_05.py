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
    while " " in felhasznalo_email:
        felhasznalo_email = input("Nem jó az email!!!\nKérem az email címét: ")

def jelszo_kerese():
    pass

def jelszo_ellenorzese():
    ok_jelszo = True
    return ok_jelszo

def beleptetes():
    pass


#Innen indul a program
felhasznalo_email = ""
felhasznalo_jelszo = ""
if regisztracio():
beleptetes()
