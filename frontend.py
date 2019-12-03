from tkinter import *
from tkinter import messagebox
from  sqlconnectivity import *
from weather import *
from msg_built import *

def view_database():
    top3 = Toplevel()
    top3.title("Database")

    l1 = Label(top3, text="Farmer's Weather System", bg="dark grey", font=("Times", 19, "bold"))
    l1.grid(row=0, column=0, columnspan=6)

    top3.geometry("290x140+120+120")

    list1 = Listbox(top3, height = 4, width = 45)
    list1.grid(row = 2, column =0, rowspan = 6, columnspan = 2)

    #now we need to attach a scrollbar to the listbox, and the other direction,too
    sb1 = Scrollbar(top3)
    sb1.grid(row = 2, column = 3, rowspan = 9)
    list1.config(yscrollcommand = sb1.set)
    sb1.config(command = list1.yview)

    sb2 = Scrollbar(top3,orient=HORIZONTAL)
    sb2.grid(row=9, column=1)
    list1.config(xscrollcommand=sb2.set)
    sb2.config(command=list1.xview)

    list1.delete(0, END)
    result = view_all()
    num=1
    for row in result:
        list1.insert(END, row)

    button1 = Button(top3,text="Close",width=15,command = top3.destroy)
    button1.grid(row=9,column = 0)

def open_window():
   #top1 = Toplevel()
    #top1.title("hello")
    #top1.geometry("290x140+120+120")
    message_built()
    messagebox.showinfo("Send Status", "Send Successfully")

def submit():
    name = enter_name.get()
    city = enter_city.get()
    mobile = enter_mobile.get()
    weather_report = weather_finder(enter_city.get())
    for details in weather_report:
        print(details[0], details[1], details[2], details[3])
        time = details[0]
        Date = details[1]
        desc = details[2]
        temp = details[3]
        #print(temp)
        insert(mobile,city,name,Date,time,desc,temp)
    messagebox.showinfo("registration", "Registration Successfully")

def registration():
    global enter_name , enter_city ,enter_mobile
    top2 = Toplevel()
    top2.geometry("290x140+120+120")
    top2.title("Registration")

    l1 = Label(top2, text="Farmer's Weather System", bg="dark grey", font=("Times", 19, "bold"))
    l1.grid(row=0, column=0, columnspan=6)

    l2 = Label(top2, text="Name", font=("Times", 14))
    l2.grid(row = 1, column = 0)
    enter_name = StringVar()
    e2 = Entry(top2, textvariable = enter_name)
    e2.grid(row = 1, column = 1)

    l3 = Label(top2, text="Mobile No. ", font=("Times", 14))
    l3.grid(row = 2, column = 0)
    enter_mobile = StringVar()
    e2 = Entry(top2, textvariable = enter_mobile)
    e2.grid(row = 2, column = 1)

    l4 = Label(top2, text="City", font=("Times", 14))
    l4.grid(row = 3, column = 0)
    enter_city = StringVar()
    e3 = Entry(top2,textvariable= enter_city)
    e3.grid(row = 3, column = 1)

    button1 = Button(top2,text="Submit" ,width = 20, command=submit)
    button1.grid(row = 4 , column =0)

    button2 = Button(top2, text="Close", width=20, command=top2.destroy)
    button2.grid(row=4, column=1)

   # registration_data()

   # print(enter_word1.get(),enter_word2.get(),enter_word3.get())
    #insert("8542049002", "allahabad", "toshu1", "209-11-25",'6PM' ,"few clouds", "30.98")

top = Tk()
top.geometry("290x140+120+120")
top.title("Farmer's Weather System")
l1 = Label(top, text="Farmer's Weather System", bg="dark grey", font=("Times", 19, "bold"))
l1.grid(row=0, column=0, columnspan=6)

l1 = Label(top, text="", font=("Times", 19, "bold"))
l1.grid(row=1, column=0, columnspan=6)

button = Button(top,text="Send",width = 20, command = open_window)
button.grid(row=2,column = 1)

button = Button(top , text="close" , width = 20, command = top.destroy)
button.grid(row =3,column = 1)

button = Button(top , text="Registration" , width = 20, command = registration)
button.grid(row =2,column = 0)

button = Button(top , text="View All Details" , width = 20,command = view_database)
button.grid(row =3,column = 0)

top.mainloop()