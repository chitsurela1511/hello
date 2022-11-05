from cProfile import label
import tkinter as tk
from tkinter import*

root =tk.Tk()
root.geometry("600x400")
name_var=tk.StringVar()
passw_var=tk.StringVar()
def submit():
    name=name_var.get()
    password=passw_var.get()
    label_name=tk.Label(text=name)
    label_name.grid(row=3,column=1)

    label_password=tk.Label(text=password)
    label_password.grid(row=4,column=1)
    #print("The name is :"+ name)
    #print("The password is :"+password)

    name_var.set("")
    passw_var.set("")


name_label=tk.Label(root,text='Username',font=('Arial',10,'bold') )
name_entry=tk.Entry(root,textvariable=name_var,font=('Arial',10,'bold'))


passw_label=tk.Label(root,text='password',font=('Arial',10,'bold') )
passw_entry=tk.Entry(root,textvariable=passw_var,font=('Arial',10,'bold'))

sub_btn=tk.Button(root,text='Submit',command=submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=0)


root.mainloop()