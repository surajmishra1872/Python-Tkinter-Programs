from  tkinter import*
root=Tk()
root.geometry("400x400")
def suraj():
    print("hello suraj bhai")
def shivay():
    print("shivay singh oberoi")
def mishra():
    print("hello mishra G")
frame=Frame(root,borderwidth=5,relief=SUNKEN,bg="Teal")
frame.pack(fill="x")
b1=Button(frame,text="click me",fg="red",bd="5",command=hello)
b1.pack(side=LEFT,padx=20,fill="x")
b2=Button(frame,text="click me",fg="red",bd="5",command=suraj)
b2.pack(side=LEFT,padx=20,fill="x")
b3=Button(frame,text="click me",fg="red",bd="5",command=shivay)
b3.pack(side=LEFT,padx=20,fill="x")
b4=Button(frame,text="click me",fg="red",bd="5",command=mishra)
b4.pack(side=LEFT,padx=20,fill="x")
root.mainloop()
