from tkinter import*
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("550x500")
    def button(self):
        self.var=StringVar()
        self.var.set("hello")
        self.bar=Label(self,text="hello",textvar=self.var,relief=SUNKEN,anchor="w")
        self.bar.pack(side=BOTTOM,fill="x")
    def buttom(self):
        self.but=Button(self,text="click",relief=SUNKEN).pack()
if __name__== '__main__':
    window=GUI()
    window.button()
    window.buttom()
    window.mainloop()

