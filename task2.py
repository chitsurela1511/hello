from distutils.cmd import Command
from select import select
import tkinter as tk
from tkinter import *
from tkinter.tix import Select

root=Tk()
root.geometry("700x700")


def f1():
    cur_Selected=l1.curselection()
    for i in cur_Selected:
        a=l2.get(i)
        numlist2.append(a)
        l2.insert(END,numlist1[i])
        
    

def f2():
    
    cur_Selected=l2.curselection()
    for i in cur_Selected:
        b=l1.get(i)
        numlist1.append(b)
        l1.insert(END,numlist2[i])
     
def f3():
    for i in range(len(numlist1)):
        l2.insert(END,numlist1[i])
     
def f4():
    for i in range(len(numlist2)):
        l1.insert(END,numlist2[i])


numlist1=['1','2','3','4']
l1=Listbox(font=('Arial',16),selectbackground='blue',selectforeground='white',selectmode='multiple')
for i in range (len(numlist1)):
    l1.insert(END,numlist1[i])
    

numlist2=['5','6','7','8']
l2=Listbox(font=('Arial',16),selectmode='multiple')
for j in range (len(numlist2)):
    l2.insert(END,numlist2[j])


btn1=Button(text=">",command=f1)
btn2=Button(text="<",command=f2)
btn3=Button(text=">>",command=f3)
btn4=Button(text="<<",command=f4)


l1.grid(rowspan=4,column=0,row=0)
l2.grid(rowspan=4,column=2,row=0)
btn1.grid(row=0,column=1)  
btn2.grid(row=1,column=1)
btn3.grid(row=2,column=1)
btn4.grid(row=3,column=1)

root.mainloop()