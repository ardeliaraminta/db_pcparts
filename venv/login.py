from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import os



class login_page:
    def __init__(self, root):
        self.window = root
        self.window.title("DBMS PC Part Picker Login")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "white")

        self.frame1 = Frame(self.window, bg="maroon")
        self.frame1.place(x=0, y=0, width=450, relheight = 1)

        label1 = Label(self.frame1, text= "pc ", font=("times new roman", 40, "italic"), bg="black", fg="white").place(x=100,y=300)
        label2 = Label(self.frame1, text= "picker ^^", font=("times new roman", 40, "italic"), bg="black", fg="white").place(x=162,y=300)
        label3 = Label(self.frame1, text= "It's all about your choices", font=("times new roman", 13, "italic"), bg="black", fg="white").place(x=100,y=360)

        self.frame2 = Frame(self.window, bg = "black")
        self.frame2.place(x=450,y=0,relwidth=1, relheight=1)

        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=140,y=150,width=500,height=450)

        self.email_label = Label(self.frame3,text="Email Address", font=("times new roman",20,"italic"),bg="white", fg="black").place(x=50,y=40)
        self.email_entry = Entry(self.frame3,font=("times new roman",15,"italic"),bg="white",fg="black")
        self.email_entry.place(x=50, y=80, width=300)

        self.password_label = Label(self.frame3,text="Password", font=("times new roman",20,"italic"),bg="white", fg="black").place(x=50,y=120)
        self.password_entry = Entry(self.frame3,font=("times new roman",15,"italic"),bg="white",fg="black",show="*")
        self.password_entry.place(x=50, y=160, width=300)

        
        self.login_button = Button(self.frame3,text="Log In",command=self.login,font=("times new roman",15, "bold"),bd=0,cursor="hand2",bg="maroon",fg="white").place(x=50,y=200,width=300)
        self.forgotten_pass = Button(self.frame3,text="Forgotten password?",command=self.forgot_func,font=("times new roman",10, "bold"),bd=0,cursor="hand2",bg="white",fg="maroon").place(x=125,y=260,width=150)
        self.create_button = Button(self.frame3,text="Create New Account",command=self.redirect_window,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="maroon",fg="white").place(x=80,y=320,width=250)


    def login(self):
        if self.email_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("Error!","All fields are required",parent=self.window)
        else:
            try:
                connection=pymysql.connect(host="sigma.jasoncoding.com",user="ardeliaraminta",password="lunathemoonchild",database="pcparts_db", port = 5555)
                cur = connection.cursor()
                cur.execute("select * from Customers where email=%s and password=%s",(self.email_entry.get(),self.password_entry.get()))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!","Invalid Data Entry" ,parent=self.window)
                else:
                    messagebox.showinfo("Success","Welcome to PC Parts picker",parent=self.window)
                    self.reset_fields()
                    connection.close()

            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    def forgot_func(self):
        if self.email_entry.get()=="":
            messagebox.showerror("Error!", "Please enter your Email Id",parent=self.window)
        else:
            try:
                connection=pymysql.connect(host="sigma.jasoncoding.com",user="ardeliaraminta",password="lunathemoonchild",database="pcparts_db", port = 5555)
                cur = connection.cursor()
                cur.execute("select * from Customers where email=%s", self.email_entry.get())
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!", "Email Id doesn't exists")
                else:
                    connection.close()
                    
                    self.root=Toplevel()
                    self.root.title("Forget Password?")
                    self.root.geometry("400x440+450+200")
                    self.root.config(bg="white")
                    self.root.focus_force()
                    self.root.grab_set()

                    title3 = Label(self.root,text="Change your password",font=("times new roman",20,"italic"),bg="white").place(x=10,y=10)
                    title4 = Label(self.root,text="Data Validation",font=("times new roman",12),bg="white").place(x=10,y=45)
                    title5 = Label(self.root, text="Select your question", font=("times new roman", 15, "bold"), bg="white").place(x=10,y=85)

                    self.sec_ques = ttk.Combobox(self.root,font=("times new roman",13),state='readonly',justify=CENTER)
                    self.sec_ques['values'] = ("Select","What's your favorite city?","What's your favourite Anime?"," Your pet's name", "Birthplace")
                    self.sec_ques.place(x=10,y=120, width=270)
                    self.sec_ques.current(0)
                    
                    title6 = Label(self.root, text="Answer", font=("times new roman", 15, "bold"), bg="white").place(x=10,y=160)

                    self.ans = Entry(self.root,font=("arial"))
                    self.ans.place(x=10,y=195,width=270)

                    title7 = Label(self.root, text="New Password", font=("times new roman", 15, "bold"), bg="white").place(x=10,y=235)
                    self.new_pass = Entry(self.root,font=("arial"))
                    self.new_pass.place(x=10,y=270,width=270)

                    self.create_button = Button(self.root,text="Submit",command=self.change_pass,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="maroon",fg="white").place(x=95,y=340,width=200)


            except Exception as e:
                messagebox.showerror("Error", f"{e}")
                
      
    def change_pass(self):
        if self.email_entry.get() == "" or self.sec_ques.get() == "Select" or self.new_pass.get() == "":
            messagebox.showerror("Error!", "Please fill the all entry field correctly")
        else:
            try:
                connection=pymysql.connect(host="sigma.jasoncoding.com",user="ardeliaraminta",password="lunathemoonchild",database="pcparts_db", port = 5555)
                cur = connection.cursor()
                cur.execute("SELECT * from user_register where email=%s and question=%s and answer=%s", (self.email_entry.get(),self.sec_ques.get(),self.ans.get()))
                row=cur.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "Please fill the all entry field correctly")
                else:
                    try:
                        cur.execute("UPDATE Customers set password=%s where email=%s", (self.new_pass.get(),self.email_entry.get()))
                        connection.commit()

                        messagebox.showinfo("Successful", "Password has changed successfully")
                        connection.close()
                        self.reset_fields()
                        self.root.destroy()

                    except Exception as er:
                        messagebox.showerror("Error!", f"{er}")
                        
            except Exception as er:
                        messagebox.showerror("Error!", f"{er}")
            

    def redirect_window(self):
        self.window.destroy()
        from signup import SignUp
        root = Tk()
        obj = SignUp(root)
        root.mainloop()


        
    def reset_fields(self):
        self.email_entry.delete(0,END)
        self.password_entry.delete(0,END)

if __name__ == "__main__":
    root = Tk()
    obj = login_page(root)
    root.mainloop()