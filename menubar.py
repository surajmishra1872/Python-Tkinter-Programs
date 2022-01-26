from tkinter import*
root=Tk()
def myfunc():
    print("mai ek nathkhat aur shaitan function hoon.")
root.geometry("500x550")
root.title("menubar")
menubar=Menu(root)
menubar.add_command(label="open",command=myfunc)
menubar.add_command(label="close",command=myfunc)
root.config(menu=menubar)
root.mainloop()