from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymysql, os



# we need to add costumer details : first_name, email, contact_number, address, city, state, last_name=None, zip_code=None
class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("DBMS PC Part Picker Signup")
        self.window.geometry("1300x800+0+0")
        self.window.config(bg = "white")

        self.bg_img = ImageTk.PhotoImage(file="image/bg_pc.png")
        background = Label(self.window,image=self.bg_img).place(x=0,y=0,relwidth=1,relheight=1)


        frame = Frame(self.window, bg="white")
        frame.place(x=350,y=100,width=500,height=550)

        title1 = Label(frame, text="PC Parts Picker", font=("Times New Roman",25,"italic"),bg="white").place(x=20, y=10)
        title2 = Label(frame, text="Join with us in the journey", font=("Times New Roman",13),bg="white", fg="gray").place(x=20, y=50)

        first_name = Label(frame, text="First name", font=("Times New Roman",15,"italic"),bg="white").place(x=20, y=100)
        l_name = Label(frame, text="Last name", font=("Times New Roman",15,"italic"),bg="white").place(x=240, y=100)

        self.fname_txt = Entry(frame,font=("arial"))
        self.fname_txt.place(x=20, y=130, width=200)

        self.lname_txt = Entry(frame,font=("arial"))
        self.lname_txt.place(x=240, y=130, width=200)

        email = Label(frame, text="Email", font=("Times New Roman",15,"italic"),bg="white").place(x=20, y=180)

        self.email_txt = Entry(frame,font=("arial"))
        self.email_txt.place(x=20, y=210, width=420)

        sec_question = Label(frame, text="Security questions", font=("Times New",15,"italic"),bg="white").place(x=20, y=260)
        answer = Label(frame, text="Answer", font=("Times New Roman",15,"italic"),bg="white").place(x=240, y=260)

        self.questions = ttk.Combobox(frame,font=("Times New Roman",13),state='readonly',justify=CENTER)
        self.questions['values'] = ("Select","What's your favorite city?","What's your favourite Anime?"," Your pet's name", "Birthplace")
        self.questions.place(x=20,y=290,width=200)
        self.questions.current(0)

        self.answer_txt = Entry(frame,font=("arial"))
        self.answer_txt.place(x=240, y=290, width=200)

        password =  Label(frame, text="New password", font=("Times New Roman",15,"italic"),bg="white").place(x=20, y=340)

        self.password_txt = Entry(frame,font=("arial"))
        self.password_txt.place(x=20, y=370, width=420)

        self.terms = IntVar()
        terms_and_con = Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.terms,onvalue=1,offvalue=0,bg="white",font=("times new roman",12, "italic")).place(x=20,y=420)
        self.signup = Button(frame,text="Sign Up",command=self.signup_func,font=("times new roman",15, "italic"),bd=0,cursor="hand2",bg="maroon",fg="white").place(x=120,y=470,width=250)




    def signup_func(self):
        if self.fname_txt.get()=="" or self.lname_txt.get()=="" or self.email_txt.get()=="" or self.questions.get()=="Select" or self.answer_txt.get()=="" or self.password_txt.get() == "":
            messagebox.showerror("Error!","All fields are required",parent=self.window)

        elif self.terms.get() == 0:
            messagebox.showerror("Error!","Please Agree with our Terms & Conditions",parent=self.window)

        else:
            try:
                connection = pymysql.connect(host="sigma.jasoncoding.com", user="ardeliaraminta", password="lunathemoonchild", database="pcparts_db", port=5555)
                cur = connection.cursor()
                cur.execute("SELECT * from user_register where email=%s",self.email_txt.get())
                row=cur.fetchone()

                #check in the db if the email exists or not 
                if row!=None:
                    messagebox.showerror("Error!","The email is already existed, please try again with another email",parent=self.window)
                else:
                    cur.execute("INSERT into user_register (first_name,last_name,email,question,answer,password) values(%s,%s,%s,%s,%s,%s)",
                                    (
                                        self.fname_txt.get(),
                                        self.lname_txt.get(),
                                        self.email_txt.get(),
                                        self.questions.get(),
                                        self.answer_txt.get(),
                                    
                                        self.password_txt.get()
                                    ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)


    def reset_fields(self):
        self.fname_txt.delete(0, END)
        self.lname_txt.delete(0, END)
        self.email_txt.delete(0, END)
        self.questions.current(0)
        self.answer_txt.delete(0, END)
        self.password_txt.delete(0, END)


    def redirect_window(self):
        self.window.destroy()
        from login import login_page
        root = Tk()
        obj = login_page(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()