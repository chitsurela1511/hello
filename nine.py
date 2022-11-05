import tkinter as tk
from tkinter import *

root=Tk()

root.geometry("500x500")
listSample=Listbox(root,width=70,height=30,
 fg="green",font=("Arial ",28))

listSample.insert(1,"Pizza")
listSample.insert(1,"Coco")
listSample.insert(1,"Pasta")

listSample.pack()



root.mainloop()