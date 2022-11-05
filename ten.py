import tkinter as tk
from tkinter import *

root=Tk()

root.geometry("500x500")

def getCourceList():
    SelectedCourses=[]
    curSelected=lb.curselection()

    for i in curSelected:
        c=lb.get(i)
        SelectedCourses.append(c)
        print(SelectedCourses)
#Declaring Lable
Course =Label(text="Select Courses")
Course.pack()

CourseLIST=['Software Development','Animation','ITIMS','Digital Design']
lb =Listbox(font=("Arial",16),selectmode="multiple")
for i in range(len(CourseLIST)):
    lb.insert(END,CourseLIST[i])
btn=Button(text="Get Courses",command=getCourceList)
btn.pack()

lb.pack()
root.mainloop()