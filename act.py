from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Image')
root.geometry('400x400')

im = ImageTk.PhotoImage(Image.open('mc background.jpeg'))
l = Label(root, image=im, height=350, width=300)
l.place(x=50,y=0)
l2 = Label(root, text="This is how you image in Tk.")
l2.place(x=40, y=360)

root.mainloop()
