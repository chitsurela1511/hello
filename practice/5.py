from tkinter import *
#Radio Button:
food =["Pizza","Burger","Pepsi"]

def order():
    if(x.get()==0):
        print("You order pizza")
    elif(x.get()==1):
        print("You order Burger")
    elif(x.get()==2):
        print("You order pepsi")
    else:
        print("huh?")
window =Tk()

x=IntVar()

for index in range(len(food)):
    radiobutton =Radiobutton(window,text=food[index],variable=x,value=index
    ,padx=25,font=("Impact",20),command=order)
   
    radiobutton.pack(anchor=W)


window.mainloop()