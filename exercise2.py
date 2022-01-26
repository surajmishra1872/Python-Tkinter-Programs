from tkinter import*
root=Tk()
root.geometry("300x260")
def winsize():
    root.geometry(f"{wdt.get()}x{hgt.get()}")
width=Label(root,text="Width:")
width.grid(row=1)
hight=Label(root,text="Height:")
hight.grid(row=2)
wdt=StringVar
hgt=StringVar
Entry(root,textvariable=wdt).grid(row=1,column=3)
Entry(root,textvariable=hgt).grid(row=2,column=3)
Button(root,text="Submit",relief=SUNKEN,command=winsize).grid()

root.mainloop()