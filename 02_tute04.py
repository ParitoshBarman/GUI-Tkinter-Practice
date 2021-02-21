from tkinter import *

root =  Tk()

# Width x Hight
root.geometry("444x234")

# Width, Hight
root.minsize(300, 100)

# Width, Hight
root.maxsize(1200, 500)

lavel1 = Label(text = 'Paritosh is a good boy and this is his GUI') 
lavel1.pack()


root.mainloop()
