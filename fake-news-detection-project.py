from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

class multiple:
    def __init__(self,root):
        self.root=root
        self.root.title('Home page')
        self.root.geometry('400x400')
        self.root.config(bg='#DBAE58')

        title = Label(self.root,text='HOME PAGE',bg='#DBAE58',font=('bold','20'))
        title.pack()
        admin_button = Button(self.root,text='Admin',bg='lightgrey',command=self.admin_page)
        admin_button.place(x=150,y=100)
        user_button = Button(self.root, text='User', bg='lightgrey',command=self.user_page)
        user_button.place(x=150, y=200)

    def admin_page(self):
        window = Tk()
        window.title('Admin page')
        window.geometry('300x300')
        window.config(bg='cadetblue')

        title = Label(window, text='ADMIN PAGE', bg='cadetblue', font=('bold', '15'))
        title.pack()
        register_button = Button(window, text='Register', bg='lightgrey',command=self.admin_register_page)
        register_button.place(x=120, y=80)
        login_button = Button(window, text='Login', bg='lightgrey',command=self.admin_login_page)
        login_button.place(x=120, y=140)


    def admin_register_page(self):
        window1 = Tk()
        window1.title('Admin Register Page')
        window1.geometry("300x300")
        window1.config(bg="cadetblue")

        title = Label(window1, text='ADMIN REGISTRATION PAGE', bg='cadetblue', font=('bold', '10'))
        title.pack()
        username_label = Label(window1,text='Username:',bg='cadetblue')
        username_label.place(x=40,y=60)
        password_label = Label(window1, text='Password:', bg='cadetblue')
        password_label.place(x=40, y=100)
        email_label = Label(window1, text='Email Id:', bg='cadetblue')
        email_label.place(x=40, y=140)

        self.username_entry = Entry(window1)
        self.username_entry.place(x=130,y=60)
        self.password_entry = Entry(window1)
        self.password_entry.place(x=130,y=100)
        self.email_entry = Entry(window1)
        self.email_entry.place(x=130,y=140)

        register_button1 = Button(window1,text='Register',bg='lightgrey',command=self.admin_register_data)
        register_button1.place(x=120,y=200)

    def admin_login_page(self):
        window2 = Tk()
        window2.title('Admin Login Page')
        window2.geometry('300x300')
        window2.config(bg='cadetblue')

        title = Label(window2, text='ADMIN LOGIN PAGE', bg='cadetblue', font=('bold', '15'))
        title.pack()
        username_label = Label(window2,text='Username',bg='cadetblue')
        username_label.place(x=40,y=60)
        password_label = Label(window2, text='Password', bg='cadetblue')
        password_label.place(x=40, y=100)

        self.username_entry1 = Entry(window2)
        self.username_entry1.place(x=130, y=60)
        self.password_entry1 = Entry(window2)
        self.password_entry1.place(x=130, y=100)

        login_button1 = Button(window2,text='Login',bg='lightgrey',command=lambda:[self.admin_news_page(),self.admin_login_data()])
        login_button1.place(x=120,y=170)

    def admin_news_page(self):
        window3 = Tk()
        window3.title('Admin News Page')
        window3.geometry('300x300')
        window3.config(bg='cadetblue')

        title = Label(window3, text='ADMIN NEWS PAGE', bg='cadetblue', font=('bold', '15'))
        title.pack()
        title_label = Label(window3, text='Title:', bg='cadetblue')
        title_label.place(x=40, y=100)


        self.title_entry = Entry(window3)
        self.title_entry.place(x=100,y=100)

        submit_button = Button(window3,text='Submit',bg='lightgrey',command=self.admin_news)
        submit_button.place(x=120,y=140)







    def user_page(self):
        window4 = Tk()
        window4.title('User page')
        window4.geometry('300x300')
        window4.config(bg='#EE7879')

        title = Label(window4, text='USER PAGE', bg='#EE7879', font=('bold', '15'))
        title.pack()
        register_button = Button(window4, text='Register', bg='lightgrey',command=self.user_register_page)
        register_button.place(x=120, y=80)
        login_button = Button(window4, text='Login', bg='lightgrey',command=self.user_login_page)
        login_button.place(x=120, y=140)


    def user_register_page(self):
        window5 = Tk()
        window5.title('User register page')
        window5.geometry('300x300')
        window5.config(bg='#EE7879')

        title = Label(window5, text='USER REGISTRATION PAGE', bg='#EE7879', font=('bold', '10'))
        title.pack()
        username_label = Label(window5, text='Username:', bg='#EE7879')
        username_label.place(x=40, y=60)
        password_label = Label(window5, text='Password:', bg='#EE7879')
        password_label.place(x=40, y=100)
        email_label = Label(window5, text='Email Id:', bg='#EE7879')
        email_label.place(x=40, y=140)

        self.username_entry2 = Entry(window5)
        self.username_entry2.place(x=130, y=60)
        self.password_entry2 = Entry(window5)
        self.password_entry2.place(x=130, y=100)
        self.email_entry2 = Entry(window5)
        self.email_entry2.place(x=130, y=140)

        register_button2 = Button(window5, text='Register', bg='lightgrey',command=self.user_register_data)
        register_button2.place(x=120, y=200)


    def user_login_page(self):
        window6 = Tk()
        window6.title('User Login Page')
        window6.geometry('300x300')
        window6.config(bg='#EE7879')

        title = Label(window6, text='USER LOGIN PAGE', bg='#EE7879', font=('bold', '15'))
        title.pack()
        username_label = Label(window6, text='Username', bg='#EE7879')
        username_label.place(x=40, y=60)
        password_label = Label(window6, text='Password', bg='#EE7879')
        password_label.place(x=40, y=100)

        self.username1_entry3 = Entry(window6)
        self.username1_entry3.place(x=130, y=60)
        self.password1_entry3 = Entry(window6)
        self.password1_entry3.place(x=130, y=100)

        login_button2 = Button(window6, text='Login', bg='lightgrey',command=self.user_news_page,)
        login_button2.place(x=120, y=170)

    def user_news_page(self):
        window7 = Tk()
        window7.title('User Login Page')
        window7.geometry('300x300')
        window7.config(bg='#EE7879')

        title = Label(window7, text='USER NEWS PAGE', bg='#EE7879', font=('bold', '15'))
        title.pack()
        title_label1 = Label(window7,text='Title',bg='#EE7879')
        title_label1.place(x=40,y=80)
        description_label = Label(window7,text='Description',bg='#EE7879')
        description_label.place(x=40,y=120)

        self.title_entry1 = Entry(window7)
        self.title_entry1.place(x=120, y=80)
        self.description_entry = Entry(window7)
        self.description_entry.place(x=120,y=120)


        submit_button = Button(window7, text='Submit', bg='lightgrey',command=self.login_news)
        submit_button.place(x=120, y=160)


    def admin_register_data(self):
        mydb = mysql.connector.connect(host='localhost',port='3306',user='root',password='soudhi',database='fake_detection')
        mycursor = mydb.cursor()

        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.password_entry.get()


        mycursor.execute("insert into admin_register values(%s,%s,%s)",(username,password,email))
        mydb.commit()
        msg.showinfo("registration details","registered succesfully")

    def admin_login_data(self):
        mydb = mysql.connector.connect(host='localhost', port='3306', user='root', password='soudhi',database='fake_detection')
        mycursor = mydb.cursor()

        username1 = self.username_entry1.get()
        password1 = self.password_entry1.get()

        mycursor.execute("select * from admin_register where username=%s and password=%s",(username1,password1))


        c=0
        for i in mycursor:
            c= c+1

        if c>0:
            mycursor.execute("insert into admin_login values(%s,%s)",(username1,password1,))
            mydb.commit()
            msg.showinfo("login details","valid user")
        else:
            msg.showerror("login details","invalid user")

    def admin_news(self):
        mydb = mysql.connector.connect(host='localhost', port='3306', user='root', password='soudhi',database='fake_detection')
        mycursor = mydb.cursor()


        title =  self.title_entry.get()

        mycursor.execute("insert into admin_title values(%s)",(title,))
        mydb.commit()
        msg.showinfo("title details","title added")



    def user_register_data(self):
        mydb = mysql.connector.connect(host='localhost', port='3306', user='root', password='soudhi',database='fake_detection')
        mycursor = mydb.cursor()


        username2 = self.username_entry2.get()
        password2 = self.password_entry2.get()
        email2 = self.email_entry2.get()

        mycursor.execute("insert into user_register values(%s,%s,%s)", (username2, password2, email2,))
        mydb.commit()
        msg.showinfo("registration details", "registered succesfully")


    def user_login_data(self):
        mydb = mysql.connector.connect(host='localhost', port='3306', user='root', password='soudhi',database='fake_detection')
        mycursor = mydb.cursor()

        username3 = self.username1_entry3.get()
        password3 = self.password1_entry3.get()

        mycursor.execute("select * from user_register where username=%s and password=%s",(username3,password3))

        d = 0
        for i in mycursor:
            d = d+1
        if d>0:
            mycursor.execute("insert into user_login values(%s,%s)",(username3,password3,))
            mydb.commit()
            msg.showinfo("login details","valid user")
        else:
            msg.showerror("login details","invalid user")

    def login_news(self):
        mydb = mysql.connector.connect(host='localhost', port='3306', user='root', password='soudhi', database='fake_detection')
        mycursor = mydb.cursor()

        title1 = self.title_entry1.get()
        description1 = self.description_entry.get()


        mycursor.execute("select * from admin_title where title=%s",(title1,))
        z=0
        for i in mycursor:
            z= z+1
        if z>0:
            mycursor.execute("insert into user_title values(%s,%s)",(title1,description1))
            mydb.commit()
            msg.showinfo("login details",'valid')
        else:
            msg.showerror("login details","invalid")

root = Tk()
obj = multiple(root)
root.mainloop()