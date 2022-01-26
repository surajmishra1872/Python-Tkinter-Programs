from tkinter import*
from PIL import Image,ImageTk
root=Tk()
root.geometry("850x1200")
root.title("Dainik Samachar")
img=[]
news=[]

def textcutter(text):
    text1=""
    for i in range(0, len(text)):
        text1+=text[i]
        if i%100==0 and i!=0:
            text1+="\n"
    return text1

for i in range(0,3):
   image= Image.open(f"{i+1}.jpg")
   image=image.resize((230,265),Image.ANTIALIAS)
   img.append(ImageTk.PhotoImage(image))
   with open(f"{i+1}.txt") as f:
       txt=f.read()
       news.append(textcutter(txt))

f0 = Frame(root, width=800, height=20)
Label(f0,text="Dainik Samachar",font="Verdana 30  bold italic ").pack()
Label(f0,text="Date-20-09-2020",font="Verdana 10  bold italic").pack(side="left",padx=100)
f0.pack()


f1 = Frame(root, width=900, height=200,pady=20,padx=20)
Label(f1,text=news[0],padx=20).pack(side=LEFT)
Label(f1,image=img[0],padx=20,pady=20).pack()
f1.pack(anchor="w")
f2 = Frame(root, width=900, height=200,pady=20,padx=20)
Label(f2,text=news[1],padx=20).pack(side=RIGHT)
Label(f2,image=img[1],padx=20,pady=20).pack()
f2.pack(anchor="w")
f3 = Frame(root, width=900, height=200,pady=20,padx=20)
Label(f3,text=news[2],padx=20).pack(side=LEFT)
Label(f3,image=img[2],padx=20,pady=20).pack()
f3.pack(anchor="w")





root.mainloop()