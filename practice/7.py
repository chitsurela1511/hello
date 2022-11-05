
from tkinter import * 
#List Box:
def submit():
    food=[]

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

        print("You have ordered:")
        for index in food:
            print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed (listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window =Tk()

listbox=Listbox(window,bg="#f7ffde",font=("Constantia",20),width=12,selectmode=MULTIPLE)
listbox.pack()


listbox.insert(1,"Pizza")
listbox.insert(2,"Burger")
listbox.insert(3,"Pasta")
listbox.insert(4,"Soup")
listbox.insert(5,"garlic bread")

listbox.config(height=listbox.size())

entryBox =Entry(window)
entryBox.pack()

submitButton =Button(window,text="submit",command=submit)
submitButton.pack()
addButton =Button(window,text="add itmes",command=add)
addButton.pack()
deleteButton =Button(window,text="add itmes",command=delete)
deleteButton.pack()

window.mainloop()