from tkinter import*
root=Tk()
root.title("listbox with suraj")
def func():
    global i
    lst.insert(ACTIVE,f"{i}")
    i+=1
i=0

root.geometry("800x800")
lst=Listbox(root,height=40,width=100,bg="Teal")
lst.insert(END,"hello suraj bhai ka hal ba")
lst.pack()
Button(root,text="Submit",command=func).pack()
root.mainloop()