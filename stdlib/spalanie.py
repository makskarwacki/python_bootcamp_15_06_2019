import tkinter
from tkinter import messagebox
def policz():
    try:
        dystans = int(dystans_entry.get())
        spalanie = int(spalanie_entry.get())
        cena = float(cena_entry.get())

        koszt = (dystans / 100) * spalanie * cena
        wynik_label.configure(text=koszt)
    except ValueError:
        messagebox.showerror("Błędne dane!", "Musisz wprowadzić dane liczbowe")

root = tkinter.Tk()

root.columnconfigure(0, weight=4)
root.columnconfigure(1, weight=2)

dystans_label = tkinter.Label(master=root, text="Dystans")
spalanie_label = tkinter.Label(master=root, text="Spalanie")
cena_label = tkinter.Label(master=root, text="Cena")
wynik_label = tkinter.Label(master=root, text="-")

dystans_entry = tkinter.Entry(master=root)
spalanie_entry = tkinter.Entry(master=root)
cena_entry = tkinter.Entry(master=root)

policz_button = tkinter.Button(master=root, text="Przelicz", command=policz)

dystans_label.grid(row=0, column=0)
dystans_entry.grid(row=0, column=1)
spalanie_label.grid(row=1, column=0)
spalanie_entry.grid(row=1, column=1)
cena_label.grid(row=2, column=0)
cena_entry.grid(row=2, column=1)
policz_button.grid(row=4, column=2)
wynik_label.grid(row=5, column=3)

root.mainloop()