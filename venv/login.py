from tkinter import *
from tkinter import ttk, messagebox
from db import getDb
from signup import SignUp

class Login:
    def __init__(self, root):
        self.window = root
        self.window.title("Login PCParts")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "white")


        self.frame1 = Frame(self.window, bg="maroon")
        self.frame1.place(x=0, y=0, width=450, relheight = 1)

        label1 = Label(self.frame1, text= " PCParts Picks", font=("Courier", 30, "bold"), bg="black", fg="white").place(x=100,y=300)
        label3 = Label(self.frame1, text= "It's all about power and choices.", font=("Courier", 13, "bold"), bg="black", fg="white").place(x=100,y=360)


        self.frame2 = Frame(self.window, bg = "gray95")
        self.frame2.place(x=450,y=0,relwidth=1, relheight=1)
        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=140,y=150,width=500,height=450)

        self.email_label = Label(self.frame3,text="Email Address", font=("courier",15,"italic"),bg="white", fg="grey").place(x=50,y=40)
        self.email_entry = Entry(self.frame3,font=("courier",15,"bold"),bg="white",fg="gray")
        self.email_entry.place(x=50, y=80, width=300)

        self.password_label = Label(self.frame3,text="Password", font=("courier",15,"italic"),bg="white", fg="grey").place(x=50,y=120)
        self.password_entry = Entry(self.frame3,font=("times new roman",15,"bold"),bg="white",fg="gray",show="*")
        self.password_entry.place(x=50, y=160, width=300)


        self.login_button = Button(self.frame3,text="Log In",command=self.login,font=("times new roman",15, "bold"),bd=0,cursor="hand2",bg="black",fg="white").place(x=50,y=200,width=300)
        self.create_button = Button(self.frame3,text="Create New Account",command=self.redirect_window,font=("times new roman",13, "bold"),bd=0,cursor="hand2",bg="black",fg="white").place(x=80,y=300,width=250)

# create connection to database but havent created the actual database :(

    def login(self):
        if self.email_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("Error!","All fields are required",parent=self.window)
        else:
            try:
                db = getDb()
                cursor = db.cursor()
                cursor.execute("SELECT * from login_pc WHERE email=%s and password=%s",(self.email_entry.get(),self.password_entry.get()))
                row=cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error!","Invalid username & password",parent=self.window)
                else:
                    messagebox.showinfo("Success","Welcome to the PC Part Picker",parent=self.window)
                    self.reset_fields()
                    cursor.close()

            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)


            except Exception as e:
                messagebox.showerror("Error", f"{e}")
                

    def redirect_window(self):
        self.window.destroy()
        root = Tk()
        obj = SignUp(root)
        root.mainloop()

     
        
    def reset_fields(self):
        self.email_entry.delete(0,END)
        self.password_entry.delete(0,END)


if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()
