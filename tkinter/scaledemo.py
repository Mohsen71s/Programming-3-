from tkinter import * 
top = Tk()
top.geometry("200x200") 
lbl=Label(top,text="Price :",bg="yellow",fg="red") 
lbl.pack()
scale = Scale( top, from_ = 100, to = 1000, orient = HORIZONTAL)
scale.pack(anchor=CENTER)
top.mainloop()