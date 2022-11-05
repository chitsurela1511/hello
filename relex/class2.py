from tkinter import *

root =Tk()

root.geometry("200x200")  
l1=Label(text="First")
l2=Label(text="second")
l3=Label(text="third")
l4=Label(text="Four")


l1.grid(row=0,column=0,sticky=W,padx=50)
l2.grid(row=0,column=1)
l3.grid(row=1,column=0)
l4.grid(row=1,column=1)
root.mainloop()