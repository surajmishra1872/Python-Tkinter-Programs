from tkinter import*
import tkinter.messagebox as msg
root=Tk()
def food():
    print(f"We are getting Your order for:{var.get()}: Thanks for ordering from SKF Food ")
    msg.showinfo("SKF",f"We are getting Your order for:{var.get()}: Thanks for ordering from SKF Food ")
root.title("SKF FOODS :)")
root.geometry("800x8000")
Label(root,text="What You Like To Eat ,Plese Select options",padx=30,pady=30,justify=LEFT,font="Verdana 20 bold italic").pack()
var=StringVar()
var.set("radio")
Radiobutton(root,text="Dosa",variable =var,value="Dosa",padx=10,font="Verdana 15 bold italic").pack(anchor="w")
Radiobutton(root,text="Italiy",variable =var,value="Italiy",padx=10,font="Verdana 15 bold italic").pack(anchor="w")
Radiobutton(root,text="Fast Food",variable =var,value="Fast Food",padx=10,font="Verdana 15 bold italic").pack(anchor="w")
Radiobutton(root,text="Pizza",variable =var,value="Pizza",padx=10,font="Verdana 15 bold italic").pack(anchor="w")
Button(root,text="Submit",command=food,padx=50,pady=15).pack()
root.mainloop()