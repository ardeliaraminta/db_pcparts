from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymysql, os



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

        title1 = Label(frame, text="PC Parts Picker", font=("Times New Roman",20,"italic"),bg="white").place(x=20, y=10)
        title2 = Label(frame, text="Join with us in the journey", font=("Times New Roman",10,"italic"),bg="white", fg="gray").place(x=20, y=50)

        first_name = Label(frame, text="First name", font=("Times New Roman",11,"italic"),bg="white").place(x=15, y=80)
        l_name = Label(frame, text="Last name", font=("Times New Roman",11,"italic"),bg="white").place(x=240, y=80)

        self.fname_txt = Entry(frame,font=("arial"))
        self.fname_txt.place(x=18, y=100, width=200)

        self.lname_txt = Entry(frame,font=("arial"))
        self.lname_txt.place(x=236, y=100, width=200)

        email = Label(frame, text="Email", font=("Times New Roman",11,"italic"),bg="white").place(x=20, y=130)
        self.email_txt = Entry(frame,font=("arial"))
        self.email_txt.place(x=20, y=160, width=420)

        sec_question = Label(frame, text="Security questions", font=("Times New Roman",11,"italic"),bg="white").place(x=20, y=196)
        answer = Label(frame, text="Answer", font=("Times New Roman",11,"italic"),bg="white").place(x=240, y=190)
        self.questions = ttk.Combobox(frame,font=("Times New Roman",11),state='readonly',justify=CENTER)
        self.questions['values'] = ("Select","What's your favorite city?","What's your favourite Anime?"," Your pet's name", "Birthplace")
        self.questions.place(x=20,y=220,width=200)
        self.questions.current(0)

        self.answer_txt = Entry(frame,font=("arial"))
        self.answer_txt.place(x=240, y=220, width=200)

        password =  Label(frame, text="Password", font=("Times New Roman",11,"italic"),bg="white").place(x=20, y=250)
        self.password_txt = Entry(frame,font=("arial"))
        self.password_txt.place(x=20, y=270, width=200)

        city =  Label(frame, text="City", font=("Times New Roman",11,"italic"),bg="white").place(x=240, y=250)
        self.city = Entry(frame,font=("arial"))
        self.city.place(x=240, y=270, width=200)

        contact_number = Label(frame, text="Contact Number", font=("Times New Roman",10,"italic"),bg="white").place(x=20, y=295)
        self.contact = Entry(frame,font=("arial"))
        self.contact.place(x=20, y=315, width=200)

        address = Label(frame, text="Address", font=("Times New Roman",10,"italic"),bg="white").place(x=240, y=295)
        self.address = Entry(frame,font=("arial"))
        self.address.place(x=240, y=315, width=200)

        state = Label(frame, text="State", font=("Times New Roman",10,"italic"),bg="white").place(x=20, y=340)
        self.state = Entry(frame,font=("arial"))
        self.state.place(x=20, y=370, width=200)

        zip = Label(frame, text="Zip Code", font=("Times New Roman",10,"italic"),bg="white").place(x=240, y=340)
        self.zip = Entry(frame,font=("arial"))
        self.zip.place(x=240, y=370, width=200)

        self.terms = IntVar()
        terms_and_con = Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.terms,onvalue=1,offvalue=0,bg="white",font=("times new roman",12, "italic")).place(x=20,y=420)
        self.signup = Button(frame,text="Sign Up",command=self.signup_func,font=("times new roman",15, "italic"),bd=0,cursor="hand2",bg="indianred",fg="white").place(x=120,y=470,width=250)

        self.sign_in = Button(frame,text="Already have an account?",command=self.redirect_window,font=("times new roman",12, "italic"),bd=0,cursor="hand2",bg="maroon",fg="white").place(x=120,y=520,width=250)





    def signup_func(self):
        if self.fname_txt.get()=="" or self.lname_txt.get()=="" or self.email_txt.get()=="" or self.questions.get()=="Select" or self.answer_txt.get()=="" or self.password_txt.get() == "" or self.contact.get() == "" or self.address.get() == "" or self.state.get() == "" or self.zip.get() == "" or self.city.get() == "":
            messagebox.showerror("Error!","All fields are required",parent=self.window)

        elif self.terms.get() == 0:
            messagebox.showerror("Error!","Please Agree with our Terms & Conditions",parent=self.window)

        else:
            try:
                connection = pymysql.connect(host="sigma.jasoncoding.com", user="ardeliaraminta", password="lunathemoonchild", database="pcparts_db", port=5555)
                cur = connection.cursor()
                cur.execute("SELECT * from Customers where email=%s",self.email_txt.get())
                row=cur.fetchone()

                #check in the db if the email exists or not 
                if row!=None:
                    messagebox.showerror("Error!","The email is already existed, please try again with another email",parent=self.window)
                else:
                    cur.execute("INSERT into Customers (first_name,last_name,email, contact_number, address, city, State, zip, password, security_answers, security_questions) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                    (
                                        self.fname_txt.get(),
                                        self.lname_txt.get(),
                                        self.email_txt.get(),
                                        self.contact.get(),
                                        self.address.get(), 
                                        self.city.get(),
                                        self.state.get(), 
                                        self.zip.get(),
                                        self.password_txt.get(),
                                        self.answer_txt.get(),
                                        self.questions.get()
                                    ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
                    self.redirect_window()
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
        from customer_login import login_page
        root = Tk()
        obj = login_page(root)
        root.mainloop()


    def redirect_window2(self):
        self.window.destroy()
        from bill import Bill_App
        root = Tk()
        obj = Bill_App(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()