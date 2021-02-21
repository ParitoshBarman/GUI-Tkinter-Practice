from tkinter import *
from PIL import Image, ImageTk

root =  Tk()

root.geometry('445x244')

# photo = PhotoImage(file="1.png")


# For jpg Images
image = Image.open('pari01.jpg')
photo = ImageTk.PhotoImage(image)

lavel1 = Label(image = photo)
lavel1.pack()


root.mainloop()
