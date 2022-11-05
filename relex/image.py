from email.mime import image
from tkinter import *
# from PIL import Image, 

ab_root =Tk()

ab_root.geometry("455x244")

#photo image class
photo =PhotoImage(file="1.png")

#For jpg Images
image =Image.open("1.jpg")
photo = ImageTk.photoImage(image)



#to add in lable
abc_lable =Label(image=photo)

# pack the lable
abc_lable.pack()

  
ab_root.mainloop()