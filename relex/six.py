from tkinter import *

root =Tk()
root.geometry("655x333")

def hello():
    print("hello tkinter Button")

def hey():
    print("This is meee")

def me():
    print("chit")

def hi():
    print("Good Afternoon")

frame =Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1=Button(frame ,fg="red",text="print now",command=hello)
b1.pack(side=LEFT,padx=23)

b2=Button(frame,fg="red",text="print now",command=hey)
b2.pack(side=LEFT,padx=23)

b3=Button(frame,fg="red",text="print now",command=me)
b3.pack(side=LEFT,padx=23)

b4=Button(frame,fg="red",text="print now",command=hi)
b4.pack(side=LEFT,padx=23)

root.mainloop()