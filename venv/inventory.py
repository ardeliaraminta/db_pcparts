#inventory of the products 
# add,delete

from tkinter import *
from tkinter import ttk, messagebox
import pymysql

class Inventory:
    def __init__(self, root):
        self.window = root
        self.window.title(" Parts Inventory")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "white")

        self.frame1 = Frame(self.window, bg="maroon")
        self.frame1.place(x=0, y=0, width=450, relheight = 1)

        self.frame2 = Frame(self.window, bg = "black")
        self.frame2.place(x=450,y=0,relwidth=1, relheight=1)

        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=140,y=150,width=1000,height=800)

        self.box = Listbox(self.frame3)
        self.box.place(x=500,y=80,width=300,height=280)
        self.box.bind('<<ListboxSelect>>',self.get_selected_row)

        self.sc = Scrollbar(self.frame3)
        self.sc.place(x=840,y=80)
        self.box.configure(yscrollcommand=self.sc.set)
        self.sc.configure(command=self.box.yview)

        self.product = Label(self.frame3,text="Product Name", font=("times new roman",16,"italic"),bg="white", fg="black").place(x=50,y=40)
        self.product = Entry(self.frame3,font=("times new roman",15,"italic"),bg="white",fg="black")
        self.product.place(x=50, y=80, width=300)

        self.price = Label(self.frame3,text="Price in Dollars", font=("times new roman",16,"italic"),bg="white", fg="black").place(x=50,y=120)
        self.price = Entry(self.frame3,font=("times new roman",15,"italic"),bg="white",fg="black")
        self.price.place(x=50, y=160, width=300)

        self.category = Label(self.frame3,text="Category", font=("times new roman",16,"italic"),bg="white", fg="black").place(x=50,y=200)
        self.category = Entry(self.frame3,font=("times new roman",15,"italic"),bg="white",fg="black")
        self.category.place(x=50, y=240, width=300)

        self.stock = Label(self.frame3,text="Stock", font=("times new roman",16,"italic"),bg="white", fg="black").place(x=50,y=280)
        self.stock = Entry(self.frame3,font=("times new roman",15,"italic"),bg="white",fg="black")
        self.stock.place(x=50, y=320, width=300)

        self.addProduct = Button(self.frame3,text="Add Product",command=self.add_product,font=("times new roman",15, "italic"),bd=0,cursor="hand2",bg="maroon",fg="white").place(x=50,y=360,width=250)

        self.viewProduct = Button(self.frame3,text="View Products",command=self.view_command,font=("times new roman",15, "italic"),bd=0,cursor="hand2",bg="maroon",fg="white").place(x=50,y=400,width=250)

        self.deleteProduct = Button(self.frame3,text="Delete Product",command=self.delete_command,font=("times new roman",15, "italic"),bd=0,cursor="hand2",bg="maroon",fg="white").place(x=50,y=440,width=250)
        
        self.searchProduct = Button(self.frame3,text="Search Product",command=self.search_command,font=("times new roman",15, "italic"),bd=0,cursor="hand2",bg="maroon",fg="white").place(x=50,y=480,width=250)
        

    def add_product(self):
        if self.product.get()=="" or self.price.get()=="" or self.category.get()=="" or self.stock.get()=="":
            messagebox.showerror("Error!","All fields are required",parent=self.window)

        else:
            try:
                connection = pymysql.connect(host="sigma.jasoncoding.com", user="ardeliaraminta", password="lunathemoonchild", database="pcparts_db", port=5555)
                cur = connection.cursor()
                cur.execute("SELECT * from Products where product_name=%s",self.product.get())
                row=cur.fetchone()

                #check in the db if the email exists or not 
                if row!=None:
                    messagebox.showerror("Error!","The product is already listed, please add another product",parent=self.window)
                else:
                    cur.execute("INSERT into Products (product_name,price,category_id,Stock) values(%s,%s,%s,%s)",
                                    (
                                        self.product.get(),
                                        self.price.get(),
                                        self.category.get(),
                                        self.stock.get(),
                                    ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Congratulations!","Product Registered",parent=self.window)
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    def view_command(self):
        ''' view_command function to show the output database.
    
        '''
        self.box.delete(0,END)  
        for rows in self.view():
            self.box.insert(END,rows)        

    def view(self):
        connection = pymysql.connect(host="sigma.jasoncoding.com", user="ardeliaraminta", password="lunathemoonchild", database="pcparts_db", port=5555)
        cur = connection.cursor()
        cur.execute("SELECT * from Products")
        rows=cur.fetchall()
        connection.close()
        return rows

    def clear_entries(self):
        ''' clear_entries function to clear content of entries.
    
        '''
        self.product.delete(0,END)
        self.price.delete(0,END)
        self.category.delete(0,END)
        self.stock.delete(0,END)

    def get_selected_row(self, event):
        global selected_tuple
        if self.box.curselection() != ():
 
            index = self.box.curselection()[0]
            selected_tuple = self.box.get(index)
            self.clear_entries()
            self.product.insert(END,selected_tuple[1])
            self.price.insert(END,selected_tuple[2])
            self.category.insert(END,selected_tuple[3])
            self.stock.insert(END,selected_tuple[4])

    def delete_command(self):
        ''' delete_command function to delete the data of a specific student.
    
        '''
        index = self.box.curselection()[0]
        selected_tuple = self.box.get(index)
        self.delete(selected_tuple[0])
        self.clear_entries()
        self.view_command()

    def delete(self,product):
        connection = pymysql.connect(host="sigma.jasoncoding.com", user="ardeliaraminta", password="lunathemoonchild", database="pcparts_db", port=5555)
        cur = connection.cursor()
        cur.execute("DELETE FROM Products WHERE product_name=%s",self.product.get())
        connection.commit()
        connection.close()

    def search(self,product="",price="",category="",stock=""):
        connection = pymysql.connect(host="sigma.jasoncoding.com", user="ardeliaraminta", password="lunathemoonchild", database="pcparts_db", port=5555)
        cur = connection.cursor()
        cur.execute("SELECT * from Products where product_name=%s or price=%s or category_id=%s or Stock =%s", (self.product.get(),self.price.get(),self.category.get(),self.stock.get()))
        rows=cur.fetchall()
        connection.close()
        return(rows)

    def search_command(self):
        self.box.delete(0,END)
        for rows in self.search(self.product.get(),self.price.get(),self.category.get(),self.stock.get()):
            self.box.insert(END,rows)

if __name__ == "__main__":
    root = Tk()
    obj = Inventory(root)
    root.mainloop()