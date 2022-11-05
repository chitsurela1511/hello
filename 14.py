from tkinter import *
root =Tk()
root.geometry("400x400")
def openwindow():
    second=Toplevel(root)
    second.geometry("300x300")
    l=Label(second,text="hello")
    l.pack()
    root.withdraw()
    root.iconify()
    root.destroy()
    second.mainloop()
    
btn=Button(root,text="Open new window",command=openwindow)
btn.place(x=100,y=100)
exit()


root.mainloop()  