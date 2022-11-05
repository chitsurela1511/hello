from tkinter import*
import tkinter as tk
root =tk.Tk()
root.geometry("300x200")

w=Label(root,text='TAJ HOTEL:',font="50").pack()

Checkbutton1= tk.IntVar()
Checkbutton2= tk.IntVar()
Checkbutton3= tk.IntVar()
Checkbutton4=tk.IntVar()

Button1=Checkbutton(root,text="Pizza =500",variable=Checkbutton1,
height=2,width=10)

Button2=Checkbutton(root,text="Burger=80",variable=Checkbutton2
,height=2,width=10)

Button3=Checkbutton(root,text="Dosa=200",variable=Checkbutton3,height=2,width=10)
Button4=Checkbutton(root,text="cold Drink =70",variable=Checkbutton4,height=2,width=10)

Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()

btn1=Button(text="Calculator")
btn1.pack()


root.mainloop()