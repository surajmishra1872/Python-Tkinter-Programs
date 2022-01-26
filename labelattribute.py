from tkinter import*
root=Tk()
root.geometry("800x800")
root.title("First GUI APP")
text=Label(text=""""Abdul Rashid Salim Salman Khan  
\n About this soundpronunciation 27 December 1965)[5] is an Indian film actor, 
\nproducer, occasional singer and television personality. 
\nIn a film career spanning over thirty years, Khan has received numerous awards, 
\nincluding two National Film Awards as a film producer, and two Filmfare Awards for acting.""",
 bg="green" ,fg="white" ,pady=5,padx=5,font="Vivaldi 20 italic" , borderwidth=5,relief=SUNKEN)
text.pack(fill=Y,pady=100,padx=10)


root.mainloop()
