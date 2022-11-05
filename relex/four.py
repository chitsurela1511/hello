from tkinter import*


root =Tk()
root.geometry("444x233")
root.title("My GUI with harry")

#imporatant Lable options
# text = adds text
# bd =Background
# fg = foreground
#__________________________________________________________________________________
# font = sets the font
#font =("comicsannsn",19,"bold")  
#2nd way for font
#font ="comicsannsn 19 bold"
#------------------------------------------------------------------------------ 
# padx = x Padding
# pady = y Padding
#-----------------------------------------------------------------
# _Relief = border styling -  RIDGE,GROOVE,RAISED,SUNKEN


# use background color ...
title_lable = Label(text="helllllllloooooooooooooooooooooooooooooo.",bg="white",
fg="blue",padx=23,pady=13,font ="comicsannsn 19 bold",borderwidth=3,relief=SUNKEN)

# Important pack options
# anchor =new anchor="sw"
#side = top,bottom,left,right
# fill=
#padx=
#pady=


title_lable.pack( side =LEFT,fill=Y  )



root.mainloop()