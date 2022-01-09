from tkinter import *
from tkinter import ttk, messagebox
from db import getDb
from PIL import ImageTk

class PC_Picker:
    def __init__(self, root):
        self.window = root
        self.window.title("PCParts")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "white")

        self.bg_img = ImageTk.PhotoImage(file="image/bg_pc.png")
        background = Label(self.window,image=self.bg_img).place(x=0,y=0,relwidth=1,relheight=1)

        self.frame1 = Frame(self.window, bg="black")
        self.frame1.place(x=10, y=10, width=200, relheight = 1)

        def selected():
            print("Selected VGA: {}".format(self.value.get()))
            print("Selected Processor: {}".format(self.value2.get()))
            return None

# this is for the drop down menu of the parts
# *self options list -> show all the list of parts
# it will set the value of the chosen item 

        # choices for the parts

        self.options_list = ["GEFORCE RTX 3090 ", "GEFORCE RTX 3080", "GEOFORCE RTX 3070", "GEFORCE RTX 3060"]
        self.value = StringVar(root)
        self.value.set(" VGA:")
        self.drop = OptionMenu(root,self.value, *self.options_list)
        self.drop.place(x=230,y=100,width=120,height=40)
    
        self.options_list2 = ["AMD Ryzen 9", "AMD Ryzen 7", "AMD Ryzen 5"]
        self.value2 = StringVar(root)
        self.value2.set("CPU:")
        self.drop2 = OptionMenu(root,self.value2, *self.options_list2)
        self.drop2.place(x=230,y=150,width=150,height=40)

        self.options_list3 = [" 8 GB", "16 GB", "32 GB"]
        self.value3 = StringVar(root)
        self.value3.set("Memory:")
        self.drop3 = OptionMenu(root,self.value3, *self.options_list3)
        self.drop3.place(x=230,y=200,width=150,height=40)

        self.options_list3 = [" Windows Home 7", "Windows Home 8", "Windows Home 10"]
        self.value3 = StringVar(root)
        self.value3.set("Operating System:")
        self.drop3 = OptionMenu(root,self.value3, *self.options_list3)
        self.drop3.place(x=230,y=250,width=150,height=40)


        self.options_list4 = [" Windows Home 7", "Windows Home 8", "Windows Home 10"]
        self.value4 = StringVar(root)
        self.value4.set("Operating System:")
        self.drop4 = OptionMenu(textvariable=self.vga, *self.options_list3)
        self.drop4.place(x=230,y=250,width=150,height=40)

    
       
        self.submit_button = Button(root, text='Done', command=selected)
        self.submit_button.place(x=600,y=700,width=150,height=40)


#self.options_list[0], self.options_list[1], self.options_list[2], self.options_list[3] textvariable=self.vga



if __name__ == "__main__":
    root = Tk()
    obj = PC_Picker(root)
    root.mainloop()
