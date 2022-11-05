from cProfile import label
from cgitb import text
from pickle import FRAME
from tkinter import *
root =Tk()
root.geometry("655x333")

#FRAME
f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y",)

f2=Frame (root,borderwidth=8,bg="grey",relief=SUNKEN)
f2.pack(side=TOP,fill="x")

K =Label(f2,text="Welcome to subline text",font="Helvetica,16,bold",fg="red")
K.pack()

K =Label(f1,text="project Tkinter")
K.pack(pady=142)



root.mainloop()