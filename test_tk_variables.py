import tkinter as tk
from tkinter.constants import ALL

w = tk.Tk()

input = tk.StringVar()
l = tk.Entry(w, textvariable=input)
l.pack()


def update(event):
    getter = l.get()
    if getter != '':
        print(getter)
    l.delete(0, len(getter))


l.bind('<Return>', update)

l.focus_set()
w.mainloop()
