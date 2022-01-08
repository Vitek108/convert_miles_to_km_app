from tkinter import Tk, Button, Label, DoubleVar, Entry

window = Tk()
window.title("Převod jednotek")
window.configure(background="#1ba49c")
window.geometry("320x220")
window.resizable(width=False, height=False)

ml_lbl = Label(window, text="Míle:", bg="white", fg="black", width=14)
ml_lbl.grid(column=0, row=0, padx=35, pady=30)

ml_value = DoubleVar() # hodnota může být tedy int či float
ml_entry = Entry(window, textvariable=ml_value, width=14)
ml_entry.grid(column=1, row=0)
ml_entry.delete(0, "end") #hodnoty od nuly výše jsou při spuštění smazané

km_lbl = Label(window, text="Kilometr:", bg="#D3D3D3", fg="black", width=14)
km_lbl.grid(column=0, row=1)

km_value = DoubleVar()
km_entry = Entry(window, textvariable=km_value, width=14)
km_entry.grid(column=1, row=1, pady=15)
km_entry.delete(0, "end")


def convert():
    value = float(ml_entry.get())
    kilometr = value * 1.6093
    km_value.set("%.4f" % kilometr)


convert_btn = Button(window, text="Převést!", bg="#ffff99", fg="black", width=14, command=convert)
convert_btn.grid(column=0, row=3, padx=15, pady=20)


def clear():
    ml_value.set("")
    km_value.set("")


clear_btn = Button(window, text="Smazat", bg="#A9A9A9", fg="black", width=14, command=clear)
clear_btn.grid(column=1, row=3, padx=15, pady=20)





window.mainloop()