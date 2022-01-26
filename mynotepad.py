from tkinter import*
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
root=Tk()

def Newfile():
    global file
    root.title("Untitled-Notepad")
    textarea.delete(1.0,END)
    file=None
def Open():
    global file
    file = asksaveasfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()
def Save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()
def Exit():
    root.destroy()
def Cut():
    textarea.event_generate("<<Cut>>")
def Copy():
    textarea.event_generate("<<Copy>>")
def Paste():
    textarea.event_generate("<<Paste>>")
def Aboutnotepad():
    showinfo("My Notepad","This Is Suraj Mishra Notapad")
def Help():
    showinfo("Help","This Is official Notepad made by Suraj Kumar Mishra .He is a Python Devloper.\n\n Thanks For Using Notepad.\n\n :)")


root.geometry("644x788")
root.title("Untitled-Notepad")
root.wm_iconbitmap("i.ico")

textarea=Text(root,font="Verdana 14")
file = None
textarea.pack(fill="both",expand=True)

menubar=Menu(root)

m1=Menu(menubar,tearoff=0)
m1.add_command(label="New",command=Newfile)
m1.add_command(label="Open",command=Open)
m1.add_command(label="Save",command=Save)
m1.add_separator()
m1.add_command(label="Exit",command=Exit)
menubar.add_cascade(label="File",menu=m1)

m2=Menu(menubar,tearoff=0)
m2.add_command(label="Cut",command=Cut)
m2.add_command(label="Copy",command=Copy)
m2.add_command(label="Paste",command=Paste)
menubar.add_cascade(label="Edit",menu=m2)


m3=Menu(menubar,tearoff=0)
m3.add_command(label="About Notepad",command=Aboutnotepad)
m3.add_command(label="Help",command=Help)
menubar.add_cascade(label="Help",menu=m3)

root.config(menu=menubar)
root.mainloop()