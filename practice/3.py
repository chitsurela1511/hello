from tkinter import *
#Entry widget:

def submit():
    username =entry.get()
    print("hello"+username)
    #entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

window =Tk()




entry =Entry(window,font=("Arial",50),fg="green",bg="black",show="*")
entry.insert(0,'chit')
entry.pack(side =LEFT)

submit_button =Button(window,text="Submit",command=submit)
submit_button.pack(side=LEFT)

delete_button =Button(window,text="delete",command=delete)
delete_button.pack(side=LEFT)

backspace_button =Button(window,text="Backspace",command=backspace)
backspace_button.pack(side=LEFT)

window.mainloop()