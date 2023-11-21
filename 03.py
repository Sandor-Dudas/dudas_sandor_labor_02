import tkinter as tk

class UnitConverter:
    def __init__(self, master):
        # Inicializálja az osztályt
        self.master = master
        master.title("Mértékegység Átváltó")

        # Felhasználói felület elemei
        self.input_label = tk.Label(master, text="Mennyiség:")
        self.input_label.grid(row=0, column=0, padx=10, pady=10)

        self.input_entry = tk.Entry(master)
        self.input_entry.grid(row=0, column=1, padx=10, pady=10)

        self.from_unit_label = tk.Label(master, text="Kiinduló mértékegység:")
        self.from_unit_label.grid(row=1, column=0, padx=10, pady=10)

        # Kiinduló mértékegység kiválasztó menü
        self.from_unit_var = tk.StringVar()
        self.from_unit_var.set("mm")
        self.from_unit_menu = tk.OptionMenu(master, self.from_unit_var, "mm", "cm", "dm", "m", "km")
        self.from_unit_menu.grid(row=1, column=1, padx=10, pady=10)

        self.to_unit_label = tk.Label(master, text="Célmértékegység:")
        self.to_unit_label.grid(row=2, column=0, padx=10, pady=10)

        # Célmértékegység kiválasztó menü
        self.to_unit_var = tk.StringVar()
        self.to_unit_var.set("mm")
        self.to_unit_menu = tk.OptionMenu(master, self.to_unit_var, "mm", "cm", "dm", "m", "km")
        self.to_unit_menu.grid(row=2, column=1, padx=10, pady=10)

        self.result_label = tk.Label(master, text="Eredmény:")
        self.result_label.grid(row=3, column=0, padx=10, pady=10)

        # Az eredményt megjelenítő címke
        self.result_var = tk.StringVar()
        self.result_label_value = tk.Label(master, textvariable=self.result_var)
        self.result_label_value.grid(row=3, column=1, padx=10, pady=10)

        # Átváltás gomb
        self.convert_button = tk.Button(master, text="Átváltás", command=self.convert)
        self.convert_button.grid(row=4, column=0, columnspan=2, pady=10)

    def convert(self):
        # Az átváltás gomb eseménykezelője
        try:
            quantity = float(self.input_entry.get())
            from_unit = self.from_unit_var.get()
            to_unit = self.to_unit_var.get()

            result, to_unit_name = self.convert_units(quantity, from_unit, to_unit)

            # Az eredmény megjelenítése
            self.result_var.set(f"{result} {to_unit_name}")
        except ValueError:
            self.result_var.set("Érvénytelen bemenet")

    def convert_units(self, quantity, from_unit, to_unit):
        # Mértékegység átváltás számítás
        units = {"mm": 0.1, "cm": 1, "dm": 10, "m": 100, "km": 100000}
        result = quantity * units[from_unit] / units[to_unit]
        return result, to_unit

def main():
    # A fő alkalmazás belépési pontja
    root = tk.Tk()
    app = UnitConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
