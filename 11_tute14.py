from tkinter import *

root =  Tk()

root.geometry('645x344')


def pari(event):
    print(f"You click the button at {event.x}, {event.y}")


widget = Button(root, text = 'Click me please')
widget.pack()

widget.bind('<Button-1>', pari)
widget.bind('<Double-1>', quit)



root.mainloop()