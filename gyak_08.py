from tkinter import *

def ok_gomb_kezelese():
    belepes.destroy()

def reg_gomb_kezelese():
    belepes.destroy()

belepes = Tk()
belepes.title("Felhasználó beleptetes")

felh_nev_cimke = Label(belepes, text="Felhasznalo neve (e-mail):")
felh_jelszo_cimke = Label(belepes, text="Jelszó:")

felh_nev = Entry(belepes, width=30)
felh_jelszo = Entry(belepes, width=20)

gomb_ok = Button(belepes, text="OK", command=ok_gomb_kezelese, width=10)
gomb_reg = Button(belepes, text="Regisztrció", command=reg_gomb_kezelese)

felh_nev_cimke.grid(row=0, column=0, padx=10, pady=20, sticky=E)
felh_jelszo_cimke.grid(row=1, column=0, sticky=E, padx=10)
felh_nev.grid(row=0, column=1, padx=10, sticky=W)
felh_jelszo.grid(row=1, column=1, sticky=W, padx=10)
gomb_ok.grid(row=2, column=0, pady=20)
gomb_reg.grid(row=2, column=1)

belepes.mainloop()