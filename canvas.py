from tkinter import*
root=Tk()
root.geometry("800x400")
root.title("Hello CANVAS")
c1=Canvas(root,width=800,height=400)
c1.pack()
c1.create_line(0,400,800,0)
c1.create_line(0,0,800,400)
c1.create_rectangle(10,10,700,300,fill="Teal")

root.mainloop()