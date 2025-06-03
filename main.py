import tkinter as tk
from tkinter.ttk import Combobox

# appsettling
app = tk.Tk()
app.title("Formulasier - Automatic Formula Calculator")
app.geometry("750x500")
app.resizable(False, False)


# header
header = tk.LabelFrame(app, width=740, height=75, background="#ccc")
header.place(x=5, y=5)

h1 = tk.Label(header, text="Formulasier - Automatic Formula Calculator", font="times 15 bold", background="#ccc")
h1.place(x=5, y=20)


# menu
menuItemText = Combobox(app, text="Lessons...")
menuItemText.place(x=5, y=80)


app.mainloop()