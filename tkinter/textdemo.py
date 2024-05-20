from tkinter import * 
top = Tk() 
top.title("Address")
top.geometry("300x200") 
lbl=Label(top,text="Address :",fg="red",bg="yellow") 
lbl.place(x=10,y=10) 
txt=Text(top,width=15,height=5) 
txt.place(x=10,y=40)
top.mainloop()