from  tkinter import *
#SCroll Bar:
main=Tk()

Scroll=Scrollbar(main)
Scroll.pack(fill=Y,side=RIGHT)

#ListBox
lb=Listbox(main,yscrollcommand=Scroll.set)
for i in range(30):
    lb.insert(END,"Number "+str(i))
lb.pack()

Scroll.config(command=lb.yview)

main.mainloop()