from tkinter import *

belepes = Tk()
belepes.title("Felhasználó beleptetes")

felh_nev_cimke = Label(belepes, text="Felhasznalo neve (e-mail):")
felh_jelszo_cimke = Label(belepes, text="Jelszó")

felh_nev = Entry(belepes, width=30)

felh_nev_cimke.grid(row=0, column=0)
felh_jelszo_cimke.grid(row=1, column=0)
felh_nev.grid(row=0, column=1)

belepes.mainloop()