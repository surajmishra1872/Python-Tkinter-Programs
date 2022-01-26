from tkinter import*
import tkinter.messagebox as msg
root=Tk()
def rate():
    print(f"Coustmer give us :{a.get()} point out of 100")
    msg.showinfo("Coustmer response",f"Coustmer give us :{a.get()} point out of 100")
    with open("rate.txt","a") as f:
        f.write(f"Coustmer give us :{a.get()} point out of 100\n")

root.title("Slider")
root.geometry("400x450")
Label(root,text="Please Give rate for Food Quality :)").pack()
a=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
a.set(10)
a.pack()
Button(root,text="Submit",pady=10,padx=10,command=rate).pack()
root.mainloop()