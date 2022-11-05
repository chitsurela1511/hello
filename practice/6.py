from tkinter import *
#Scale

def submit():
    print("The temprature is:"+ str(scale.get())+"degree c")
window =Tk()

scale =Scale(window,from_=100,to=0,length=600,orient=VERTICAL
,font=('Consolas',20),tickinterval=10,showvalue=0,troughcolor='#69EaFF',fg="red",
bg="black")
scale.pack()

button =Button(text="submit",command=submit)
button.pack()


window.mainloop()