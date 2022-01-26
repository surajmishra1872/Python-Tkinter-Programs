from tkinter import *
from PIL import Image, ImageTk
mahmudul_root = Tk()

image = Image.open("suraj.png")
photo = ImageTk.PhotoImage(image)
varun_label = Label(image=photo)
image = Image.open("suraj.png")
photo = ImageTk.PhotoImage(image)
varun_label = Label(image=photo)
varun_label.pack()
mahmudul_root.mainloop()