import tkinter

def sumuj():
    print("Sumuję")
    a = int(a_entry.get())
    b = int(b_entry.get())
    wynik = a + b
    wynik_label.configure(text=wynik)

root = tkinter.Tk()

a_label = tkinter.Label(master=root, text="a")
a_label.grid(row=0, column=0)
a_entry = tkinter.Entry(master=root)
a_entry.grid(row=0, column=1)

b_label = tkinter.Label(master=root, text="b")
b_label.grid(row=1, column=0)
b_entry = tkinter.Entry(master=root)
b_entry.grid(row=1, column=1)

sum_button = tkinter.Button(master=root, text="+", command=sumuj)
sum_button.grid(row=2, column=0)

wynik_label = tkinter.Label(master=root, text="Wynik: - ")
wynik_label.grid(row=2, column=1)
root.mainloop()