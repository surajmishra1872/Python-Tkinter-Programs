from tkinter import*
root=Tk()
root.geometry("500x500")
root.title("scrolbar")
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
lsb=Listbox(root,yscrollcommand=scrollbar.set)
for i in range(400):
    lsb.insert(END,f"item is:{i}")
lsb.pack(fill="both")
scrollbar.config(command=lsb.yview)


root.mainloop()
