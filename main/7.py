from tkinter import *
from math import *
root = Tk()

root.geometry("500x100")
root.title('CALCULATOR')
def add():
    blank.delete(0, END)
    Ans = int(num1.get()) + int(num2.get())
    blank.insert(0, Ans)
def sub():
    blank.delete(0, END)
    Ans = int(num1.get()) - int(num2.get())
    blank.insert(0, Ans)
def mult():
    blank.delete(0, END)
    Ans = int(num1.get()) * int(num2.get())
    blank.insert(0, Ans)
def div():
    blank.delete(0, END)
    Ans = int(num1.get()) / int(num2.get())
    blank.insert(0, Ans)
def clear():
    blank.delete(0, END)
    num2.delete(0, END)
    num1.delete(0, END)
def sq():
    blank.delete(0, END)
    Ans = int(num1.get()) * int(num1.get())
    blank.insert(0, Ans)

def sqrtt():
    blank.delete(0, END)
    h = int(num1.get())
    a = sqrt(h)
    Ans = (int(a))
    blank.insert(0, Ans)


Label(root, text = "Enter Num 1:").grid(row=0)
Label(root, text = "Enter Num 2:").grid(row=1)
Label(root, text = "The Answer is:").grid(row=2)


num1 = Entry(root)
num2 = Entry(root)
blank = Entry(root)


num1.grid(row=0, column=1)
num2.grid(row=1, column=1)
blank.grid(row=2, column=1)


Button(root, text='Quit', command=root.destroy).grid(row=4, column=0, sticky=W)
Button(root, text='Add', command=add).grid(row=0, column=3, sticky=W,)
Button(root, text='Subtract', command=sub).grid(row=0, column=4, sticky=W)
Button(root, text='Multiply', command=mult).grid(row=0, column=5, sticky=W)
Button(root, text='Divide', command=div).grid(row=0, column=6, sticky=W)
Button(root, text='^2', command=sq).grid(row=0, column=7, sticky=W)
Button(root, text='Sqrt', command=sqrtt).grid(row=0, column=8, sticky=W)
Button(root, text='Clear', command=clear).grid(row=0, column=9, sticky=W)

root.mainloop()