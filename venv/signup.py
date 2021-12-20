from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from db import getDb
from picker import PC_Picker
class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Sign Up")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "white")

        self.bg_img = ImageTk.PhotoImage(file="image/bg_pc.png")
        background = Label(self.window,image=self.bg_img).place(x=0,y=0,relwidth=1,relheight=1)


        frame = Frame(self.window, bg="white")
        frame.place(x=350,y=100,width=500,height=550)

        title1 = Label(frame, text="Sign Up", font=("times new roman",25,"bold"),bg="white").place(x=20, y=10)
        title2 = Label(frame, text="Join with us in this adventure!", font=("times new roman",13),bg="white", fg="gray").place(x=20, y=50)

        f_name = Label(frame, text="First name", font=("times new roman",15,"bold"),bg="white").place(x=20, y=100)
        l_name = Label(frame, text="Last name", font=("times new roman",15,"bold"),bg="white").place(x=240, y=100)

        self.fname_txt = Entry(frame,font=("arial"))
        self.fname_txt.place(x=20, y=130, width=200)

        self.lname_txt = Entry(frame,font=("arial"))
        self.lname_txt.place(x=240, y=130, width=200)

        email = Label(frame, text="Email", font=("times new roman",15,"bold"),bg="white").place(x=20, y=180)

        self.email_txt = Entry(frame,font=("arial"))
        self.email_txt.place(x=20, y=210, width=420)

        sec_question = Label(frame, text="Security questions", font=("times new roman",15,"bold"),bg="white").place(x=20, y=260)
        answer = Label(frame, text="Answer", font=("times new roman",15,"bold"),bg="white").place(x=240, y=260)

        self.questions = ttk.Combobox(frame,font=("times new roman",13),state='readonly',justify=CENTER)
        self.questions['values'] = ("Select","Where were you born?","Your Favorite City","Your cat's name")
    
        self.questions.place(x=20,y=290,width=200)
        self.questions.current(0)

        self.answer_txt = Entry(frame,font=("arial"))
        self.answer_txt.place(x=240, y=290, width=200)

        password =  Label(frame, text="New password", font=("times new roman",15,"bold"),bg="white").place(x=20, y=340)

        self.password_txt = Entry(frame,font=("arial"))
        self.password_txt.place(x=20, y=370, width=420)

        self.terms = IntVar()
        terms = Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.terms,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=20,y=420)

        self.signup = Button(frame,text="Sign Up",command=self.signup_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="deepskyblue",fg="white").place(x=120,y=470,width=250)




    def signup_func(self):
        #temporary window redirection 
        self.window.destroy()
        root = Tk()
        obj = PC_Picker(root)
        root.mainloop()


        """USE THIS FUNCTION TO CHECK THE EMAILS AND ALSO WRITE TO DATABASE THANK YEW"""

    #     if self.fname_txt.get()=="" or self.lname_txt.get()=="" or self.email_txt.get()=="" or self.questions.get()=="Select" or self.answer_txt.get()=="" or self.password_txt.get() == "":
    #         messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)

    #     elif self.terms.get() == 0:
    #         messagebox.showerror("Error!","Please Agree with our Terms & Conditions",parent=self.window)

        # else:
        #     try:
        #         db = getDb()
        #         cursor = db.cursor()
        #         cursor.execute("select * from ___ where email=%s",self.email_txt.get())
        #         row=cursor.fetchone()

            #check whether existing email is used 
        #         if row!=None:
        #             messagebox.showerror("Error!","The email id is already exists, please try again with another email id",parent=self.window)
        #         else:
        #             cursor.execute("SELECT ----) values(%s,%s,%s,%s,%s,%s)",
        #                             ('''get function''))
                                       
                                    
        #             cursor.commit()
        #             cursor.close()
        #             messagebox.showinfo("Register success",parent=self.window)
        #             self.reset_fields()
        #     except Exception as ex:
        #         messagebox.showerror("Error!",f"Error due to {str(ex)}",parent=self.window)


    def reset_fields(self):
        pass
    
if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()
