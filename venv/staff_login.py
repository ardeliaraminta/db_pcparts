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

        self.frame1 = Frame(self.window, bg="indianred")
        self.frame1.place(x=0, y=0, width=450, relheight = 1)

        label1 = Label(self.frame1, text= "pc ", font=("times new roman", 40, "italic"), bg="indianred", fg="white").place(x=100,y=300)
        label2 = Label(self.frame1, text= "picker ^^", font=("times new roman", 40, "italic"), bg="indianred", fg="white").place(x=162,y=300)
        label3 = Label(self.frame1, text= "Staff Login", font=("times new roman", 13, "italic"), bg="black", fg="white").place(x=100,y=380)

        self.frame2 = Frame(self.window, bg = "black")
        self.frame2.place(x=450,y=0,relwidth=1, relheight=1)

        self.frame3 = Frame(self.frame2, bg="white")        
        self.frame3.place(x=140,y=150,width=400,height=300)

        self.email_label = Label(self.frame3,text="Email Address", font=("times new roman",20,"italic"),bg="white", fg="black").place(x=50,y=40)
        self.email_entry = Entry(self.frame3,font=("times new roman",15,"italic"),bg="white",fg="black")
        self.email_entry.place(x=50, y=80, width=300)

        self.password_label = Label(self.frame3,text="Password", font=("times new roman",20,"italic"),bg="white", fg="black").place(x=50,y=120)
        self.password_entry = Entry(self.frame3,font=("times new roman",15,"italic"),bg="white",fg="black",show="*")
        self.password_entry.place(x=50, y=160, width=300)

        
        self.login_button = Button(self.frame3,text="Log In",command=self.login,font=("times new roman",15, "bold"),bd=0,cursor="hand2",bg="indianred",fg="white").place(x=50,y=200,width=300)

    def login(self):
        if self.email_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("Error!","All fields are required",parent=self.window)
        else:
            try:
                connection=pymysql.connect(host="sigma.jasoncoding.com",user="ardeliaraminta",password="lunathemoonchild",database="pcparts_db", port = 5555)
                cur = connection.cursor()
                cur.execute("SELECT * from staff_login where email=%s and password=%s",(self.email_entry.get(),self.password_entry.get()))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!","Invalid Data Entry" ,parent=self.window)
                else:
                    messagebox.showinfo("Success","Welcome to PC Parts Picker Inventory",parent=self.window)
                    self.redirect_window()
                    self.reset_fields()
                    connection.close()

            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

      
    def redirect_window(self):
        self.window.destroy()
        from inventory import Inventory
        root = Tk()
        obj = Inventory(root)
        root.mainloop()


        
    def reset_fields(self):
        self.email_entry.delete(0,END)
        self.password_entry.delete(0,END)

if __name__ == "__main__":
    root = Tk()
    obj = login_page(root)
    root.mainloop()