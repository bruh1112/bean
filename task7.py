import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Variable, messagebox

root = tk.Tk()
root.title("CAFE AU BEAN")
root.geometry("500x500")
cap = 3.00
def buy():
    if s1.get().isnumeric() and s2.get().isnumeric() and s3.get().isnumeric() and s4.get().isnumeric():
        print(str(int(s1.get()) * cap))
    else:
        print("gh")drfghhdughdjkghdkfjsdfghjk

defa, defa1, defa2, defa3 = tk.IntVar(0), tk.IntVar(0), tk.IntVar(0), tk.IntVar(0)
check = tk.IntVar()
l1 = tk.Label(root, text="Cappucino")
l2 = tk.Label(root, text="Iced")
l3 = tk.Label(root, text="Espresso")
l4 = tk.Label(root, text="Latte") 
s1 = ttk.Spinbox(root, width=5, textvariable=defa)
s2 = ttk.Spinbox(root, width=5, textvariable=defa1)
s3 = ttk.Spinbox(root, width=5, textvariable=defa2)
s4 = ttk.Spinbox(root, width=5, textvariable=defa3)
r = ttk.Checkbutton(root, text="Takeaway", variable=check)
b = ttk.Button(root, text="buy", command=buy)
check.set(0)
b.pack()
r.pack()
r.place(x=20, y=200)
l1.pack(), l2.pack(), l3.pack(), l4.pack()
l1.place(x=20, y=50), l2.place(x=20, y=70), l3.place(x=20, y=90), l4.place(x=20, y=110)
s1.pack(), s2.pack(), s3.pack(), s4.pack()
s1.place(x=100, y=50), s2.place(x=100, y=70), s3.place(x=100, y=90), s4.place(x=100, y=110)
root.mainloop()