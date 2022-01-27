from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymysql, os
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import tkinter as tk
from data import *
 
class payment_window:
    def __init__(self, root):
        """Define window for the app"""
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root["bg"] = "maroon"

        self.pay_type = StringVar()
        # self.button_rename = tk.Button(self.root, text = "New window",
        #     command= lambda: self.new_window(Win2)).pack()

        F2 = LabelFrame(self.root,bd=10, relief=GROOVE, text = "RECEIPT", font=("times new roman", 20, "bold"),bg="white", fg= "black")
        F2.place(x=5, y=180,width=360, height=380)

        card2= Label(F2, text="Payment Type:", font=("times new roman", 16, "bold"),bg="maroon",fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        # osqt = Entry(F2, width=7,textvariable=self.pay_type, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10,pady=10)
        # # self.ssdb = db.get_products_by_category("SSD")

        self.options_list4 = ["Credit Card", "Paypal", "COD"]
        self.pay_type.set("")

        payment = OptionMenu(F2,self.pay_type, *self.options_list4)
        payment.place(x=170,y=10,width=100,height=30)


        butt = Button(F2, command = self.payment, text= "Proceed",bg="maroon", fg="white",pady=15, width = 10, height = 2, font="arial 10 bold")
        butt.place(x =25, y = 100)

        print("Orders")
        for transaction in Data.transactions:
            print("Product ID:", transaction.product_id)
            print("Quantity:", transaction.quantity)
            print("Total amount:", transaction.total_amount)
            print("-"*10)
    
        
        
        F5 = Frame(self.root,bd=10, relief=GROOVE)
        F5.place(x=1010, y=200,width=325, height=360)

        bill_title = Label(F5, text="Bill Area", font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.textarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1) 


        F6 = LabelFrame(self.root,bd=10, relief=GROOVE, text = "Bill Menu", font=("times new roman", 15, "bold"),bg="#074463", fg= "gold")
        F6.place(x=0, y=560,relwidth=1, height=140)


        btn_F = Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750, width=580, height=105)


        Gbill = Button(btn_F, command=self.bill_area, text="Generate Bill", bg="maroon", fg="white",pady=15, width = 20, font="arial 12 bold").grid(row=0, column=1,padx=5,pady=5)
        Exit = Button(btn_F, text="Exit", bg="maroon", fg="white",pady=15, width=11, font="arial 12 bold").grid(row=0, column=3,padx=5,pady=5)
        self.welcome_bill()

    def payment(self):
       self.textarea.insert(END, f"\t Payment Type : {self.pay_type.get()} \n")


        
        

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END, "\t PC Parts Picker <3\n")
        self.textarea.insert(END, f"\n===================================")
        self.textarea.insert(END, f"Products ID \t\tQty\t Total Amount")
        self.textarea.insert(END, f"\n===================================")



    def bill_area(self):
        self.welcome_bill()
        for transaction in Data.transactions:
            self.textarea.insert(END, f"{transaction.product_id} \t\t{transaction.quantity}\t {transaction.total_amount}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = payment_window(root)
    app.root.title("Payment")
    root.mainloop()