class Felhasznalo:
    pass

class Jelszo:
    jelszo = "valami"
    def __int__(self):
        #self.jelszo_generalasa()
        pass
    def jelszo_kerese(self):
        pass

    def jelszo_ellenorzese(self):
        pass

    def jelszo_generalasa(self):
        self.jelszo = "semmi"

pw = Jelszo()
print(pw.jelszo)
pw.jelszo_generalasa()
print(pw.jelszo)

