from re import T
from tkinter import *
from tkinter import messagebox
#Message Box:

def click():
    
    #messagebox.showinfo(title="This is an info message box",message="You are a person")

    # messagebox.showwarning(title="Warning!",message="You have a Virus!")
    messagebox.showerror(title="This is an info message box",message="You are a person")
   
window =Tk()

button =Button(window,command=click,text="click me")
button.pack()

window.mainloop()