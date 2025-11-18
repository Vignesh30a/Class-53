from tkinter import *

rt = Tk()
rt.geometry("400x300")
rt.title("main")

def tw():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    l2 = Label(top,text="This da top window!")
    l2.pack()
    top.mainloop()

l = Label(rt,text="Root Window is this")
b = Button(rt,text="Click to open topwindow",command=tw)

l.pack()
b.pack()
rt.mainloop()