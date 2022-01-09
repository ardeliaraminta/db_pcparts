from tkinter import *
import math
import random
from tkinter import messagebox
import os

class Bill_App:
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

        self.face_wash = IntVar()
        self.spray = IntVar()
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
        self.bill_no=StringVar()
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()



#customer details 
        F1 = LabelFrame(self.root,bd=10, relief=GROOVE, text = "Customer Details", font=("times new roman", 30, "bold"),bg="black", fg= "white")
        F1.place(x=0, y=80, relwidth=1)

        customername = Label(F1, text="Customer's Name",bg="black",fg="white" , font=("times new roman",18,"bold")).grid(row=0, column=0, padx=20, pady=5)
        c_txt = Entry(F1,width=15, textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0, column=1, padx=10, pady=5)

        phonenum = Label(F1, text=" Phone Number",bg="black",fg="white" , font=("times new roman",18,"bold")).grid(row=0, column=2, padx=20, pady=5)
        p_txt = Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0, column=3, padx=10, pady=5)

        bill = Label(F1, text=" Bill",bg="black",fg="white" , font=("times new roman",18,"bold")).grid(row=0, column=4, padx=20, pady=5)
        bill_tct = Entry(F1,width=15,textvariable=self.bill_no,font="arial 15",bd=7,relief=SUNKEN).grid(row=0, column=5, padx=10, pady=5)

        bill_btn = Button(F1, text="Search",command=self.find_bill,textvariable=self.search_bill, width=10, font="arial 12 bold").grid(row=0, column=6, pady=10,padx=10)

        # ============================ PRODUCT =============================================================


        F2 = LabelFrame(self.root,bd=10, relief=GROOVE, text = "Products", font=("times new roman", 20, "bold"),bg="maroon", fg= "white")
        F2.place(x=5, y=180,width=360, height=380)

        card = Label(F2, text="VGA :", font=("Times New Roman", 16, "bold"),bg="maroon",fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        vga_qt = Entry(F2, width=10,textvariable=self.vgaqt, font=("times new roman", 16, "bold"),bd=2, relief=SUNKEN).grid(row=0, column=1,padx=10,pady=10)
        self.options_list3 = ["GEFORCE RTX 3090 ", "GEFORCE RTX 3080", "GEOFORCE RTX 3070", "GEFORCE RTX 3060"]
        self.vga.set("VGA:")
        

        vga = OptionMenu(F2,self.vga, *self.options_list3)
        vga.place(x=98,y=15,width=50,height=30)


        card2= Label(F2, text="OS :", font=("times new roman", 16, "bold"),bg="maroon",fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        osqt = Entry(F2, width=10,textvariable=self.osqt, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10,pady=10)
        self.options_list4 = [" Windows Home 7", "Windows Home 8", "Windows Home 10"]
        self.os.set("OS")

        os = OptionMenu(F2,self.os, *self.options_list4)
        os.place(x=100,y=65,width=50,height=30)


        card3 = Label(F2, text="VGA :", font=("Times New Roman", 16, "bold"),bg="maroon",fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        cpu_qt = Entry(F2, width=10,textvariable=self.cpuqt, font=("times new roman", 16, "bold"),bd=2, relief=SUNKEN).grid(row=0, column=1,padx=10,pady=10)
        self.options_list5 = ["AMD Ryzen 9", "AMD Ryzen 7", "AMD Ryzen 5"]
        self.cpu.set("CPU:")

        cpu = OptionMenu(F2,self.cpu, *self.options_list5)
        cpu.place(x=100,y=110,width=50,height=30)






        face_w_lb = Label(F2, text="CPU : ", font=("times new roman", 16, "bold"),bg="maroon",fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        face_w_txt = Entry(F2, width=10, textvariable=self.face_wash , font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=2, column=1,padx=10,pady=10)

        hair_s_lb = Label(F2, text="Monitor : ", font=("times new roman", 16, "bold"),bg="maroon",fg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        hair_s_txt = Entry(F2, width=10, textvariable=self.spray , font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=3, column=1,padx=10,pady=10)

        hair_g_lb = Label(F2, text="Power Supply :", font=("times new roman", 16, "bold"),bg="maroon",fg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        hair_g_txt = Entry(F2, width=10, textvariable=self.gel , font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=4, column=1,padx=10,pady=10)

        body_lb = Label(F2, text="Motherboard :", font=("times new roman", 16, "bold"),bg="maroon",fg="white").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        body_txt = Entry(F2, width=10, textvariable=self.loshan , font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10,pady=10)


    


        # ====================================Bill Aread==========================
        
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

        c3_lbl = Label(F6, text="" ,font=("times new roman",14,"bold")).grid(row=2, column=2,padx=20,pady=1,sticky="w")
        c3_txt = Entry(F6,width=18, textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2, column=3,padx=10,pady=1)


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

        # self.total_g_price =float(((self.dal.get()*120)+(self.rice.get()*40)+(self.oil.get()*100)+(self.sugar.get()*180)+(self.tea.get()*40)+(self.wheat.get()*80)))
        # self.g_price.set("Rp. " + str(self.total_g_price))

        # self.total_cold_drink_price =float(((self.maza.get()*90)+(self.cock.get()*85)+(self.sprite.get()*96)+(self.thumbsup.get()*100)+(self.limca.get()*65)+(self.frooti.get()*75)))
        # self.cold_drink_price.set("Rp. " + str(self.total_cold_drink_price))

        # # self.total_product_tax = float((self.total_product_price.get()*0.18))
        # self.product_tax.set("Rp. " + str(self.total_product_price*0.18))
        # self.g_tax.set("Rp. " + str(self.total_g_price*0.18))
        # self.cold_drink_tax.set("Rp. " + str(self.total_cold_drink_price*0.18))

        self.billing_price = float(self.product_price.get())
        

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END, "\t PC Parts Picker <3\n")
        self.textarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number : {self.c_phone.get()}")
        self.textarea.insert(END, f"\n===================================")
        self.textarea.insert(END, f"Products\t\tQty\t  Price")
        self.textarea.insert(END, f"\n===================================")


    def bill_area(self):
        self.welcome_bill()
        # products
        if self.vgaqt.get()!=0 :
            self.textarea.insert(END, f"VGA\t\t{self.vgaqt.get()}\t  {(self.vgaqt.get()*999)}")
        if self.osqt.get()!=0 :
            self.textarea.insert(END, f"\Operating System\t\t{self.osqt.get()}\t  {(self.osqt.get()*199)}")
        if self.cpuqt.get()!=0 :
            self.textarea.insert(END, f"\CPU\t\t{self.cpuqt.get()}\t  {(self.cpuqt.get()*1199)}")

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
    
    def find_bill(self):
        present = "no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1 = open(f"Bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")


        

root = Tk()
obj = Bill_App(root)
root.mainloop()