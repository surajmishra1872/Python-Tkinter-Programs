from tkinter import*
root=Tk()
root.geometry("650x400")
root.title("Frame")
f1=Frame(root,bg="green",borderwidth=5,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
f2=Frame(root,bg="green",borderwidth=5, relief=SUNKEN)
f2.pack(side=TOP,fill=X)
text1=Label(f1,text="Hello Program",fg="blue",pady=15)
text1.pack(pady=142)
text2=Label(f2,text="Suraj Mishra Software",fg="blue" , pady=15)
text2.pack()
root.mainloop()