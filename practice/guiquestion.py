from ast import Delete
from cgi import test
from tkinter import *
from turtle import bgcolor

window =Tk()
window.title("Form")
window.geometry("700x600")

scrollbar=Scrollbar(window,width=20,troughcolor="red",background="red")
scrollbar.grid(row=0,column=1,rowspan=4,sticky=N+S)

scrollbar1=Scrollbar(window,width=20,orient=VERTICAL)
scrollbar1.grid(row=0,column=1,rowspan=4,sticky=N+S)
test=StringVar()

def b1():
    try:
        a=li.get(li.curselection())
        li2.insert(END,a)
        li.delete(li.curselection())
    except Exception:
        print("select value:")
def b2():
    a=li2.size()
    for i in range(0,li.size()):
        str=li.get(i)
        li2.insert(a+i,str)
        li.delete(0,END)
def b3():
    a=li2.get(li2.curselection())
    li.insert(END,a)
    li2.delete(li2.curselection())

def b4():
    a=li.size()
    for i in range(0,li2.size()):
        str=li2.get(i)
        li.insert(i+a,str)
        li2.delete(0,END)



    

li=Listbox(window,width=20,height=15,bg="#FCD9Ac",font=("Arial",14),yscrollcommand=scrollbar.set)
li.grid(row=0,column=0,rowspan=4)
li.insert(1,"Tea")
li.insert(2,"Coffee")
li.insert(3,"Juice")
li.insert(4,"Alcohol")
li.insert(5,"Water")
li.insert(6,"Cold drink")
li.insert(7,"Smoothie")
li.insert(8,"shake")
li.insert(9,"soup")
li.insert(10,"cold water")
li.insert(11,"red bull")
li.insert(12,"pepsi")
li.insert(13,"coke")
li.insert(14,"pizza")
li.insert(15,"Burger")
li.insert(16,"Dabeli")
li.insert(17,"kiwi")
li.insert(18,"Orange")

scrollbar.config(command=li.yview,troughcolor="red")
scrollbar1.config(command=li.yview)


b=Button(window,text=">",font=("Arial,Bold",12),width=7,height=1,bd=3,command=b1)
b.grid(row=0,column=2,padx=20)

b1=Button(window,text=">>",font=("Arial,Bold",12),width=7,height=1,bd=3,command=b2)
b1.grid(row=1,column=2,padx=40)

b2=Button(window,text="<",font=("Arial,Bold",12),width=7,height=1,bd=3,command=b3)
b2.grid(row=2,column=2,padx=40)

b3=Button(window,text="<<",font=("Arial,Bold",12),width=7,height=1,bd=3,command=b4)
b3.grid(row=3,column=2,padx=40)




li2=Listbox(window,width=20,height=15,bg="#40E0D0",font=("Arial",14),yscrollcommand=scrollbar.set)
li2.grid(row=0,column=3,rowspan=4)
window.mainloop()