from tkinter import*
import time
root=Tk()
def update():
    statusvariable.set("busy...")
    sbr.update()
    time.sleep(2)
    statusvariable.set("Ready")
root.geometry("500x400")
root.title("status bar")
statusvariable=StringVar()
statusvariable.set("Ready")
sbr =Label(root,textvariable=statusvariable,borderwidth=2,relief=SUNKEN,anchor="w")
sbr.pack(side=BOTTOM,fill=X)
Button(root,text="Update",command=update).pack()
Label(root,text="Mza aa gya guru !!",font="Verdana 25 bold italic",fg="red").pack()

root.mainloop()