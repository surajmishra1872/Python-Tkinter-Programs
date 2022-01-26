from tkinter import*
root=Tk()
def click(event):
    global scrvalue
    text=event.widget.cget("text")
    if text=="=":
        if scrvalue.get().isdigit():
            value=int(scrvalue.get())
        else:
            try:
                value=eval(scrvalue.get())
            except Exception as e:
                value="Error.."

        scrvalue.set(value)
        f.update()
    elif text=="C":
        scrvalue.set("")
        f.update()
    elif text=="OFF":
        exit()
    elif text=="DEL":
        scrvalue.set(scrvalue.get()[:-1])
        f.update()
    else:
        scrvalue.set(scrvalue.get()+text)
        f.update()





root.geometry("500x530")
root.maxsize(500,530)
root.minsize(500,530)
root.title("Calculator By Suraj Mishra")
root.wm_iconbitmap("i.ico")
scrvalue=StringVar()
Entry(root,textvariable=scrvalue,font="Verdana 40 ").pack(padx=10,fill=X,pady=10,ipadx=8)
f=Frame(root,bg="gray")
b = Button(f, text="7", padx=20, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=20, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

b = Button(f, text="9", padx=20, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

b = Button(f, text="DEL", padx=20, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

f.pack(fill="x")

f=Frame(root,bg="gray")
b = Button(f, text="4", padx=20, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=20, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

b = Button(f, text="6", padx=20, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

b = Button(f, text="X", padx=20, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

f.pack(fill="x")

f=Frame(root,bg="gray")
b = Button(f, text="1", padx=20, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=20, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

b = Button(f, text="3", padx=20, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=20, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

f.pack(fill="x")

f=Frame(root,bg="gray")
b = Button(f, text="0", padx=20, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=22, pady=7, font="lucida 24 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=21, pady=12, font="lucida 18 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=28, pady=10, font="lucida 22 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

f.pack(fill="x")

f=Frame(root,bg="gray")
b = Button(f, text="/", padx=23, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=20, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=23, pady=5,fill="x")
b.bind("<Button-1>", click)

b = Button(f, text="OFF", padx=8, pady=14, font="lucida 17 bold")
b.pack(side=LEFT, padx=23, pady=7,fill="x")
b.bind("<Button-1>", click)

b = Button(f, text="=" ,padx=19,pady=9, font="lucida 21  bold")
b.pack(side=LEFT, padx=16, pady=5,fill="x")
b.bind("<Button-1>", click)

f.pack(fill="x")

root.mainloop()
