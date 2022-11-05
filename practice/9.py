from tkinter import *
#menu Bar

def openfile():
    print("File has been open")
def savefile():
    print("File has been save")

root =Tk()
menubar =Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open ",command=openfile)
filemenu.add_command(label="Save ",command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit ",command=quit)

root.mainloop()