from logging import root
from tkinter import *
import tkinter

def getvals():
    print(f"The value of username is :{uservalue.get()}")
    print(f"The value of password is :{passvalue.get()}")
root=Tk()

root.geometry("655x333")

user =Label(root,text="username")
password=Label(root,text="password")

user.grid()
password.grid(row=1)

#variable classes in tkinter
# Boleanvar,Doublevar,Intvar,stringvar

#1 string variable :
uservalue =StringVar()
passvalue =StringVar()
#Entry widget :
userentry =Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=getvals).grid()


root.mainloop()