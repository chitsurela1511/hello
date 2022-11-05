from cProfile import label
from tkinter import *

window =Tk()

window.geometry("420x420")
window.title("first programe")

#Label
label =Label(window,text="hello world ",font=('Arial',20,'bold'),fg='green',bg='black'
,relief=SUNKEN,bd=10,padx=20,pady=20)
label.pack()
 #label.place(x=0,y=0)



window.mainloop()