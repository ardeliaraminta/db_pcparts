#inventory of the products 
# add,delete

from tkinter import *
from tkinter import ttk, messagebox
import pymysql

class inventory:
    def __init__(self, root):
        self.window = root
        self.window.title("Inventory")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "white")

        self.frame1 = Frame(self.window, bg="maroon")
        self.frame1.place(x=0, y=0, width=450, relheight = 1)

        self.frame2 = Frame(self.window, bg = "black")
        self.frame2.place(x=450,y=0,relwidth=1, relheight=1)

        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=140,y=150,width=500,height=450)

        self.product_name = Label(self.frame3,text="Product Name", font=("times new roman",20,"italic"),bg="white", fg="black").place(x=50,y=40)
        self.product_name = Entry(self.frame3,font=("times new roman",15,"italic"),bg="white",fg="black")
        self.product_name.place(x=50, y=80, width=300)

        self.price = Label(self.frame3,text="Price", font=("times new roman",20,"italic"),bg="white", fg="black").place(x=50,y=120)
        self.price = Entry(self.frame3,font=("times new roman",15,"italic"),bg="white",fg="black")
        self.price.place(x=50, y=160, width=300)

        self.category = Label(self.frame3,text="Catagory", font=("times new roman",20,"italic"),bg="white", fg="black").place(x=50,y=200)
        self.category = Entry(self.frame3,font=("times new roman",15,"italic"),bg="white",fg="black")
        self.category.place(x=50, y=240, width=300)

        self.stock = Label(self.frame3,text="Stock", font=("times new roman",20,"italic"),bg="white", fg="black").place(x=50,y=280)
        self.stock = Entry(self.frame3,font=("times new roman",15,"italic"),bg="white",fg="black")
        self.stock.place(x=50, y=320, width=300)

        self.addProduct = Button(self.frame3,text="Add Product",command=self.add_product,font=("times new roman",15, "italic"),bd=0,cursor="hand2",bg="maroon",fg="white").place(x=50,y=360,width=250)

# product_name, price, category_id, Stock

    def add_product(self):
        if self.product_name.get()=="" or self.price.get()=="" or self.category.get()=="" or self.stock.get()=="":
            messagebox.showerror("Error!","All fields are required",parent=self.window)

        else:
            try:
                connection = pymysql.connect(host="sigma.jasoncoding.com", user="ardeliaraminta", password="lunathemoonchild", database="pcparts_db", port=5555)
                cur = connection.cursor()
                cur.execute("SELECT * from Products where product_name=%s",self.product_name.get())
                row=cur.fetchone()

                #check in the db if the email exists or not 
                if row!=None:
                    messagebox.showerror("Error!","The product is already listed, please add another product",parent=self.window)
                else:
                    cur.execute("INSERT into Products (product_name,price,category_id,Stock) values(%s,%s,%s,%s)",
                                    (
                                        self.product_name.get(),
                                        self.price.get(),
                                        self.category.get(),
                                        self.stock.get(),
                                    ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Congratulations!","Product Registered",parent=self.window)
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)        

if __name__ == "__main__":
    root = Tk()
    obj = inventory(root)
    root.mainloop()