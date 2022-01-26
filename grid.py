from tkinter import*
root=Tk()
def getvals():
    print(f"The value of username is :{userentry.get()}")
    print(f"The value of password is :{Passentry.get()}")

root.geometry("500x500")
username=Label(root,text="UserName")
password=Label(root,text="password")
username.grid()
password.grid(row=1)
user=StringVar()
pas=StringVar()
userentry=Entry(root,textvariable=user)
Passentry=Entry(root,textvariable=pas)
userentry.grid(row=0,column=1)
Passentry.grid(row=1,column=1)
submit=Button(root,text="Submit",relief=SUNKEN,command=getvals)
submit.grid()

root.mainloop()