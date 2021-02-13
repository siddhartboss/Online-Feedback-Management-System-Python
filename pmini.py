from tkinter import *
import sqlite3

root = Tk()
root.geometry('530x550')
root.title("Feedback Form")
root.configure(background = "pink")

fullname=StringVar()
email=StringVar()
var = IntVar()
c=StringVar()
product=StringVar()
var1= IntVar()
suggestion=StringVar()



def database():
   name1=fullname.get()

   email1=email.get()

   if(var == 1):
      gender = 'Male'
   else:
      gender = 'Female'
   
   category=c.get()
   
   pro=product.get()

   if(var1 == 1):
      r1 = 'Good'
   else:
      r1 = 'Bad'

   s=suggestion.get()

   con=sqlite3.connect('data.db')
   con.execute('CREATE TABLE IF NOT EXISTS fform(Fullname TEXT,Email TEXT,Gender TEXT,category TEXT, product TEXT, comment TEXT, suggestion TEXT)')

   con.execute('INSERT INTO fform(FullName,Email,Gender,category,product,comment,suggestion)VALUES(?,?,?,?,?,?,?)',(name1,email1,gender,category,pro,r1,s))
   con.commit()
   

             
label_0 = Label(root, text="Feedback form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=70,y=130)

entry_1 = Entry(root,textvar=fullname)
entry_1.place(x=250,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=70,y=180)

entry_2 = Entry(root,textvar=email)
entry_2.place(x=250,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=250,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=305,y=230)

label_4 = Label(root, text="Category",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['Food','Cloths','Electical','Beauty','Book','Hardware'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select category') 
droplist.place(x=250,y=280)


label_5 = Label(root, text="Product",width=20,font=("bold", 10))
label_5.place(x=70,y=330)

entry_1 = Entry(root,textvar=product)
entry_1.place(x=250,y=330)

label_4 = Label(root, text="Review",width=20,font=("bold", 10))
label_4.place(x=70,y=380)

Radiobutton(root, text="Good",padx = 5, variable=var1, value=1).place(x=250,y=380)
Radiobutton(root, text="Bad",padx = 20, variable=var1, value=2).place(x=305,y=380)

label_5 = Label(root, text="Suggestion",width=20,font=("bold", 10))
label_5.place(x=70,y=430)

entry_3 = Entry(root,textvar=suggestion)
entry_3.place(x=250,y=430)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=480)

root.mainloop()

