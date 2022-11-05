from cProfile import label
from tkinter import*


c_root =Tk()

#gui logic
#width x Height
c_root.geometry("644x234")

#width , height
c_root.minsize(300,100)

#width , Height
c_root.maxsize(1200,988)

#lable
ab = Label(text="chit is a good boy and this is his Gui")
# To use Lable
ab.pack()


c_root.mainloop()      

