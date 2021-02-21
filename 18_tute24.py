from tkinter import *


def upload():
    statusbar.set("Busy...")
    sbar.update()
    import time
    time.sleep(2)
    statusbar.set("Ready Now")

root =  Tk()

root.geometry("444x234")
root.title("Pari.......")


statusbar = StringVar()
statusbar.set("Ready")

sbar = Label(root, textvariable=statusbar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)

Button(root, text = "Uplode", command= upload).pack()




root.mainloop()