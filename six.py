from tkinter import CENTER ,Button ,Tk
from tkinter import*

master=Tk()

master.geometry("200x200")
b1=Button(master,text="Click me !")
b1.place(relx=1,x=-2,y=2,anchor=NE)

b2=Button(master ,text="New")
b2.place(relx=0.5,rely=0.5,anchor=CENTER)


master.mainloop();
