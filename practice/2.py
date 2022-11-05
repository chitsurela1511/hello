from tkinter import *
#BUtton
window = Tk()
count =0
def click():
    global count
    count +=1
    print(count)

#Button 
button =Button(window,text="Click me!",command=click,font=("comic sans",30),fg="green"
,bg="black",activeforeground="green",activebackground="black",)
button.pack()



window.mainloop()