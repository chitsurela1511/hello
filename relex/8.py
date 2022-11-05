from logging import root
from tkinter import *
from tkinter.tix import COLUMN

root=Tk()
def getvals():
    print("It works")

root.geometry("644x344")
#Heading

Label(root,text="Traveles Form:",font="comicsanns 13 bold").grid(row=0,column=3)
#Text for our form
name =Label(root,text="Name")
phone =Label(root,text="phone")
Gender =Label(root,text="Gender")
emergency =Label(root,text="Emergency Contact")
paymentmode =Label(root,text="Payment mode")
#Pack text for our form
name.grid(row= 1,column=2)
phone.grid(row= 2,column=2)
Gender.grid(row= 3,column=2)
emergency.grid(row= 4,column=2)
paymentmode.grid(row= 5,column=2)
#Tikinter variable for storing entries
namevalue=StringVar()
phonevalue =StringVar()
Gendervalue=StringVar()
emergencyvalue =StringVar()
paymentmodevalue=StringVar()
foodservicevalue =IntVar()

#Enteries for form

nameentry =Entry(root,textvariable=namevalue)
phoneentry =Entry(root,textvariable=phonevalue)
Genderentry =Entry(root,textvariable=Gendervalue)
emergencyentry =Entry(root,textvariable=emergencyvalue)
paymentmodeentry =Entry(root,textvariable=paymentmode)

#packing Entry
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
Genderentry.grid(row=3,column=3)  
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

#checkButton
foodservice =Checkbutton(text="Want To Prebook Your Males",variable=foodservicevalue)
foodservice.grid(row=6,column=3)

#Button & packing  it and assigning it a command.
Button(text="submit  Travles,",command=getvals).grid(row=7,column=3) 





root.mainloop()