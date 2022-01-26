from tkinter import*
import tkinter.messagebox as msg
root=Tk()
root.geometry("550x520")
root.title("MessageBox")
def myfunc():
    print("hello guys!")
    #a=msg.showinfo("help","you need to help")
    #msg.showinfo("help","hello")
    #a=msg.askokcancel("Question","what is this?")
    #a=msg.askretrycancel("gui","bye bye!!!")
    a=msg.askquestion("rate us","Was Your Experience in good?")
    if a=="yes":
        a="Please rate us on playstore"
    else:
        a="Please email your problem"
    msg.showinfo("coustmer",a)
menubar=Menu(root)
m1=Menu(menubar,tearoff=0)
m1.add_command(label="open",command=myfunc)
m1.add_command(label="close",command=myfunc)
root.config(menu=menubar)
menubar.add_cascade(label="file" ,menu=m1)


m2=Menu(menubar,tearoff=0)
m2.add_command(label="open",command=myfunc)
m2.add_command(label="close",command=myfunc)
root.config(menu=menubar)
menubar.add_cascade(label="file" ,menu=m2)





root.mainloop()