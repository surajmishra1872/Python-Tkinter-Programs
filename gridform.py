from tkinter import*
root=Tk()
def call():
    print("ae hallo!")
root.geometry("700x700")
Label(root,text="shivay Tours and Travels",font="Verdana 25 bold",bg="Yellow",fg="red").grid(row=0,column=3)
Label(root,text="Name:").grid(row=1,column=2)
Label(root,text="Address:").grid(row=2,column=2)
Label(root,text="Contact no:").grid(row=3,column=2)
Label(root,text="other No.").grid(row=4,column=2)

name=StringVar()
address=StringVar()
Contact=IntVar()
otherno=IntVar()
foodconfirm=IntVar()
Entry(root,textvariable=name).grid(row=1,column=3)
Entry(root,textvariable=address).grid(row=2,column=3)
Entry(root,textvariable=Contact).grid(row=3,column=3)
Entry(root,textvariable=otherno).grid(row=4,column=3)
Checkbutton(root,text="Food is mentained?").grid(row=5,column=3)
Button(root,text="click to book shivay Tours and travels",command=call).grid(row=6,column=3)

root.mainloop()