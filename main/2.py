from tkinter import *
from  tkinter import  ttk
#defining register function
def register():
    #getting form data
    name1=name.get()
    con1=contact.get()
    email1=email.get()
    gen1=gender.get()
    city1=city.get()
    state1=state.get()
    # #applying empty validation
    # if name1=='' or con1==''or email1=='' or gen1==''or city1==''or state1=='':
    #     message.set("fill the empty field!!!")
    # else:
    #     #opening of file to store data 
    #     fileptr = open("PYTHON:/StuReg.txt", "a")#here a means append
    #     if gen1==1:
    #      fileptr.write("\n"+name1+"  "+con1+"  "+email1+"  Male  "+city1+"  "+state1)
    #     else:
    #      fileptr.write("\n" + name1 + "  " + con1 + "  " + email1 + "  Female  " + city1 + "  " + state1)
    #     message.set("Stored successfully")

#defining Registrationform function
def Registrationform():
    global reg_screen
    reg_screen = Tk()
    #Setting title of screen
    reg_screen.title("Registration Form")
    #setting height and width of screen
    reg_screen.geometry("350x400")
    #declaring variable
    global  message;
    global name
    global contact
    global email
    global gender
    global city
    global state
    name = StringVar()
    contact = StringVar()
    email=StringVar()
    gender=IntVar()
    city=StringVar()
    state=StringVar()
    message=StringVar()
    #Creating layout of Registration form
    Label(reg_screen,width="300", text="Please enter details below", bg="orange",fg="white").pack()
    #name Label
    Label(reg_screen, text="Name * ").place(x=20,y=40)
    #name textbox
    Entry(reg_screen, textvariable=name).place(x=90,y=42)
    #contact Label
    Label(reg_screen, text="Contact * ").place(x=20,y=80)
    #contact textbox
    Entry(reg_screen, textvariable=contact).place(x=90,y=82)

    # email Label
    Label(reg_screen, text="Email * ").place(x=20, y=120)
    # email textbox
    Entry(reg_screen, textvariable=email).place(x=90, y=122)

    # gender Label
    Label(reg_screen, text="Gender * ").place(x=20, y=160)
    # gender radiobutton
    Radiobutton(reg_screen,text="Male",variable=gender,value=1).place(x=90,y=162)
    Radiobutton(reg_screen, text="Female", variable=gender, value=2).place(x=150, y=162)

    # city Label
    Label(reg_screen, text="City * ").place(x=20, y=200)
    # city combobox
    monthchoosen = ttk.Combobox(reg_screen, width=27, textvariable=city)
    monthchoosen['values'] = (' Mumbai',
                              ' Bhopal',
                              ' Patna',
                              ' Indore',
                              ' Nagpur',
                              ' Motihari',
                              ' Pune',
                              ' Gwalior',
                              ' Jabalpur',)
    monthchoosen.current()
    monthchoosen.place(x=90,y=202)

    # state Label
    Label(reg_screen, text="State * ").place(x=20, y=240)
    # state combobox
    monthchoosen = ttk.Combobox(reg_screen, width=27, textvariable=state)
    monthchoosen['values'] = (' Madhya Pradesh',
                              ' Maharashtra',
                              ' Bihar',
                              ' Punjab',
                              ' Gujrat',
                              ' Rajsthan',)
    monthchoosen.current()
    monthchoosen.place(x=90, y=242)
    #Label for displaying login status[success/failed]
    Label(reg_screen, text="",textvariable=message).place(x=95,y=264)
    #Login button
    Button(reg_screen, text="Register", width=10, height=1, bg="orange",command=register).place(x=105,y=300)
    reg_screen.mainloop()
#calling function Registrationform
#Registrationform()