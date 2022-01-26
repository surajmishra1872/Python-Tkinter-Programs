from tkinter import*
root=Tk()
def myfunc():
    print("mai ek nathkhat aur shaitan function hoon.")
root.geometry("500x550")
root.title("drop down menubar")
menubar=Menu(root)
m1=Menu(menubar,tearoff=0)
m1.add_command(label="open",command=myfunc)
m1.add_command(label="save",command=myfunc)
m1.add_command(label="print",command=myfunc)
root.config(menu=menubar)
menubar.add_cascade(label="Files",menu=m1)

m2=Menu(menubar,tearoff=0)
m2.add_command(label="open",command=myfunc)
m2.add_command(label="save",command=myfunc)
m2.add_command(label="print",command=myfunc)
root.config(menu=menubar)
menubar.add_cascade(label="Files",menu=m2)

root.mainloop()