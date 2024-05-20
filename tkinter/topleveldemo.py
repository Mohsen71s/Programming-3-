from tkinter import *
top = Tk() 
top.geometry("300x200") 
def fun():
    chld = Toplevel(top) 
    chld.mainloop()
btn1 = Button(top, text = "Open",width=10,command=fun)
btn1.place(x=50,y=50) 
top.mainloop() 
