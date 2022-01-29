from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymysql, os

class main:
    def __init__(self, root):
        self.window = root
        self.window.title("DBMS PC Part Picker")
        self.window.geometry("1300x800+0+0")
        self.window.config(bg = "white")

        self.bg_img = ImageTk.PhotoImage(file="image/bg_pc.png")
        background = Label(self.window,image=self.bg_img).place(x=0,y=0,relwidth=1,relheight=1)


        # frame = Frame(self.window, bg="black")
        # frame.place(x=350,y=100,width=500,height=550)

        self.frame2 = Frame(self.window, bg = "indianred")
        self.frame2.place(x=700,y=0,relwidth=1, relheight=1)

        self.title = Label(self.frame2,text="Welcome to PC Parts Picker", font=("times new roman",28,"italic"),bg="black", fg="white").place(x=110,y=40)

        self.login_as = Label(self.frame2,text="Login As", font=("times new roman",22,"italic"),bg="indianred", fg="black").place(x=250,y=150)


        self.button1= Button(self.frame2,text="Customer",command=self.redirect_window,font=("times new roman",20, "italic"),bd=0,cursor="hand2",bg="black",fg="bisque").place(x=150,y=260,width=150)
        self.button2= Button(self.frame2,text="Staff",command=self.redirect_window,font=("times new roman",20, "italic"),bd=0,cursor="hand2",bg="black",fg="bisque").place(x=320,y=260,width=150)







    def redirect_window(self):
        self.window.destroy()
        from customer_login import login_page
        root = Tk()
        obj = login_page(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = main(root)
    root.mainloop()