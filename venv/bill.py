from tkinter import *
import math
import random
from tkinter import messagebox
import os
from tokenize import String
from matplotlib.pyplot import get
import db



class Bill_App:

    ssdb = []
    vgab = []
    mondb = []
    ramdb = []
    total = 0 


    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")

        # bg_color = "#074463"
        title = Label(self.root, text="Database Parts Picker",bd=12, relief=GROOVE, bg="#074463", fg= "white", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        # ===============================================variable=================================


        self.vgaqt = IntVar()
        self.vga = StringVar()

        self.osqt = IntVar()
        self.os = StringVar()

        self.cpuqt = IntVar()
        self.cpu = StringVar()

        self.ramqt = IntVar()
        self.ram = StringVar()

        self.monitorqt = IntVar()
        self.monitor = StringVar()

        self.gel = IntVar()
        self.loshan = IntVar()

        # ========================total price============

        self.product_price = StringVar()
        self.g_price = StringVar()
        self.cold_drink_price = StringVar()

        self.product_tax = StringVar()
        self.g_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # ================================customer============================

        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.customer_email=StringVar()
        x = random.randint(1000,9999)
        self.customer_email.set(str(x))
        self.search_bill=StringVar()



#customer details 
        F1 = LabelFrame(self.root,bd=10, relief=GROOVE, text = "Customer Details", font=("times new roman", 30, "bold"),bg="black", fg= "white")
        F1.place(x=0, y=80, relwidth=1)

        customername = Label(F1, text="Customer's Name",bg="black",fg="white" , font=("times new roman",18,"bold")).grid(row=0, column=0, padx=20, pady=5)
        c_txt = Entry(F1,width=15, textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0, column=1, padx=10, pady=5)

        phonenum = Label(F1, text=" Phone Number",bg="black",fg="white" , font=("times new roman",18,"bold")).grid(row=0, column=2, padx=20, pady=5)
        p_txt = Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0, column=3, padx=10, pady=5)

        bill = Label(F1, text=" Customer's Email",bg="black",fg="white" , font=("times new roman",18,"bold")).grid(row=0, column=4, padx=20, pady=5)
        bill_tct = Entry(F1,width=15,textvariable=self.customer_email,font="arial 15",bd=7,relief=SUNKEN).grid(row=0, column=5, padx=10, pady=5)

        # bill_btn = Button(F1, text="Search",command=self.find_bill,textvariable=self.search_bill, width=10, font="arial 12 bold").grid(row=0, column=6, pady=10,padx=10)

        # ============================ PRODUCT =============================================================


        F2 = LabelFrame(self.root,bd=10, relief=GROOVE, text = "Products", font=("times new roman", 20, "bold"),bg="maroon", fg= "white")
        F2.place(x=5, y=180,width=360, height=380)

        card = Label(F2, text="VGA :", font=("Times New Roman", 16, "bold"),bg="maroon",fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        vga_qt = Entry(F2, width=7,textvariable=self.vgaqt, font=("times new roman", 16, "bold"),bd=2, relief=SUNKEN).grid(row=0, column=1,padx=10,pady=10)

        self.vgab = db.get_products_by_category("Graphics Card")
        
        self.options_list3 = [self.vgab[i][1] for i in range(len(self.vgab))]
        self.vga.set("VGA:")
        vga = OptionMenu(F2,self.vga, *self.options_list3)
        vga.place(x=98,y=15,width=80,height=30)

        '''
        [(0, 'Nvidia GTX 2070', 15),
        (1, 'Nvidia RTX 3080', 11)
        ]

        vga_dict = {
            'Nvidia GTX 2070': {
                'id' : 0,
                'name' : 'Nvidia GTX 2070',
                'stock' : 15
            }
        }

        vga_dict['Nvidia GTX 2070']['name']
        '''

    


        card2= Label(F2, text="SSD :", font=("times new roman", 16, "bold"),bg="maroon",fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        osqt = Entry(F2, width=7,textvariable=self.osqt, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10,pady=10)
        self.ssdb = db.get_products_by_category("SSD")

        self.options_list4 = [self.ssdb[i][1] for i in range(len(self.ssdb))]
        self.os.set("SSD")

        os = OptionMenu(F2,self.os, *self.options_list4)
        os.place(x=100,y=65,width=80,height=30)

        print(self.options_list4)


        ram_lb = Label(F2, text="RAM : ", font=("times new roman", 16, "bold"),bg="maroon",fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        ram_txt = Entry(F2, width=7, textvariable=self.ramqt , font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10,pady=10)

        self.ramdb= db.get_products_by_category("RAM")

        self.options_list5 = [self.ramdb[i][1] for i in range(len(self.ramdb))]
        self.ram.set("RAM:")

        ram = OptionMenu(F2,self.ram, *self.options_list5)
        ram.place(x=100,y=110,width=80,height=30)


        monitor_lb = Label(F2, text="Monitor : ", font=("times new roman", 16, "bold"),bg="maroon",fg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        monitor_txt = Entry(F2, width=7, textvariable=self.monitorqt , font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10,pady=10)

        self.mondb= db.get_products_by_category("MONITORS")
        self.options_list5 = [self.mondb[i][1] for i in range(len(self.mondb))]
        self.monitor.set("Monitor:")

        mon = OptionMenu(F2,self.monitor, *self.options_list5)
        mon.place(x=100,y=170,width=80,height=30)

        hair_g_lb = Label(F2, text="Power Supply :", font=("times new roman", 16, "bold"),bg="maroon",fg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        hair_g_txt = Entry(F2, width=10, textvariable=self.gel , font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10,pady=10)

        body_lb = Label(F2, text="Motherboard :", font=("times new roman", 16, "bold"),bg="maroon",fg="white").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        body_txt = Entry(F2, width=10, textvariable=self.loshan , font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10,pady=10)


    


        # ====================================Bill Area==========================
        
        F5 = Frame(self.root,bd=10, relief=GROOVE)
        F5.place(x=1010, y=200,width=325, height=360)

        bill_title = Label(F5, text="Bill Area", font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.textarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1) 


        # ==========================================Button Frame==========================


        F6 = LabelFrame(self.root,bd=10, relief=GROOVE, text = "Bill Menu", font=("times new roman", 15, "bold"),bg="#074463", fg= "gold")
        F6.place(x=0, y=560,relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total price of product" ,font=("times new roman",14,"bold")).grid(row=0, column=0,padx=20,pady=1,sticky="w")
        m1_txt = Entry(F6,width=18, textvariable=self.product_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0, column=1,padx=10,pady=1)


        # =================================================


        c1_lbl = Label(F6, text="product tax" ,font=("times new roman",14,"bold")).grid(row=0, column=2,padx=20,pady=1,sticky="w")
        c1_txt = Entry(F6,width=18, textvariable=self.product_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0, column=3,padx=10,pady=1)

        c2_lbl = Label(F6, text="Product Tax" ,font=("times new roman",14,"bold")).grid(row=1, column=2,padx=20,pady=1,sticky="w")
        c2_txt = Entry(F6,width=18, textvariable=self.g_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1, column=3,padx=10,pady=1)


        btn_F = Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750, width=580, height=105)

        total_btn = Button(btn_F, command=self.total, text="Total", bg="maroon", fg="white",pady=15, width=11, font="arial 12 bold").grid(row=0, column=0,padx=5,pady=5)
        Gbill = Button(btn_F, command=self.bill_area, text="Generate Bill", bg="maroon", fg="white",pady=15, width=11, font="arial 12 bold").grid(row=0, column=1,padx=5,pady=5)
        Clear = Button(btn_F, text="Clear", bg="maroon", fg="white",pady=15, width=11, font="arial 12 bold").grid(row=0, column=2,padx=5,pady=5)
        Exit = Button(btn_F, text="Exit", bg="maroon", fg="white",pady=15, width=11, font="arial 12 bold").grid(row=0, column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        
        self.total_product_price =(self.vgaqt.get()*999 + self.osqt.get()*199 + self.cpuqt.get()*1199)
        self.product_price.set(str(self.total_product_price))
        self.billing_price = float(self.product_price.get())
        

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END, "\t PC Parts Picker <3\n")
        self.textarea.insert(END, f"\n Customer's Email : {self.customer_email.get()}")
        self.textarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number : {self.c_phone.get()}")
        self.textarea.insert(END, f"\n===================================")
        self.textarea.insert(END, f"Products\t\tQty\t  Price")
        self.textarea.insert(END, f"\n===================================")


    def bill_area(self):
        self.welcome_bill()
        # products
        self.total = 0
        if self.vgaqt.get()!=0 :
            index = -1
            for x in range(len(self.vgab)):
                if self.vgab[x][1] == self.vga.get():
                    index = x
                    self.total += self.vgab[x][2]

            self.textarea.insert(END, f"{self.vga.get()}\t\t{self.vgaqt.get()}\t  {(self.vgab[index][2])}\t\t")
        
        self.total = 0
        if self.osqt.get()!=0 :
            index = -1
            for x in range(len(self.ssdb)):
                if self.ssdb[x][1] == self.os.get():
                    index = x
                    self.total += self.ssdb[x][2] 
            self.textarea.insert(END, f"{self.os.get()}\t\t{self.osqt.get()}\t  {(self.ssdb[index][2])}")

        self.total = 0 
        if self.ramqt.get()!=0 :
            index = -1
            for x in range(len(self.ramdb)):
                if self.ramdb[x][1] == self.ram.get():
                    index = x
                    self.total += self.ramdb[x][2]
            self.textarea.insert(END, f"{self.ram.get()}\t\t{self.ram.get()}\t  {(self.ram[index][2])}")
        
        self.total = 0
        if self.monitorqt.get()!=0 :
            index = -1
            for x in range(len(self.mondb)):
                if self.mondb[x][1] == self.monitor.get():
                    index = x
                    self.total += self.mondb[x][2] 
            self.textarea.insert(END, f"{self.monitor.get()}\t\t{self.monitorqt.get()}\t  {(self.mondb[index][2])}")

        self.textarea.insert(END,"\n-----------------------------------")
        self.textarea.insert(END, f"\nTotal price\t\t\t{self.billing_price}")
        self.save_bill()
        

        # ****************************saving of bill*******************************************************
    def save_bill(self):
        op = messagebox.askyesno("save Bill","Do you want to save the bil?")
        if op>0:
            self.bill_data = self.textarea.get('1.0',END)
            f1 = open("Bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close
            messagebox.showinfo("saved", f"Bill no. : {self.bill_no.get()} saved successfully")
        else:
            return
    
    # def find_bill(self):
    #     present = "no"
    #     for i in os.listdir("Bills/"):
    #         if i.split('.')[0]==self.search_bill.get():
    #             f1 = open(f"Bills/{i}","r")
    #             self.textarea.delete('1.0',END)
    #             for d in f1:
    #                 self.textarea.insert(END,d)
    #             f1.close()
    #             present="yes"
    #     if present=="no":
    #         messagebox.showerror("Error","Invalid Bill No.")
       

root = Tk()
obj = Bill_App(root)
root.mainloop()