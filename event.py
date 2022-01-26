from tkinter import*
root=Tk()
def focus(event):
    print(f"You clicked on the button at {event.x}, {event.y}")
root.geometry("800x400")
root.title("GUI event")
widget=Button(root,text="please click me")
widget.pack()
widget.bind("<Enter>",focus)
root.mainloop()
