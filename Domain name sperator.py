import os
from tkinter import *
import tkinter as tk

labels = {}
os.system('cls||clear')
r = tk.Tk()
r.minsize(width=400,height=200)
def cal():
    x = e1.get()
    a = 0
    for b in x:
        if b == ".":
            a+=1
        elif b == "c":
            a+=1
        elif b=="o":
            a+=1
        elif b == "m":
            a+=1
    if a >= 4 :
        y = x.split(sep="@")
        g="Your UserName is "+y[0]
        h="Your Domain is "+y[1]
        print(g)
        print(h)
        l1 = Label(r, text=g, font=("arial italic", 18) ).pack()
        l2 = Label(r, text=h, font=("arial italic", 18) ).pack()
    else:
        print("An error occured")
        l1 = Label(r, text="Invalid Email", font=("arial italic", 18) ).pack()
x_var = ""
r.title('User and Domain name splitter')
Label(r, text='Email id').pack()
e1 = Entry(r)
e1.pack()
button = tk.Button(r, text='Enter', width=25,command=cal)
button.pack()
r.mainloop()
