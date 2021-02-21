from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("666x555")


def getdoller():
    print(f"We have credited {myslider2.get()} dollers to your bank accound")
    tmsg.showinfo("Amount credited!",f"We have credited {myslider2.get()} dollers to your bank accound")

# myslider = Scale(root, from_=0, to=100)
# myslider.pack()


Label(root, text="How many dollers you want").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
# myslider2.set(34)
myslider2.pack()

Button(text="Get dollers!", pady=10, command=getdoller).pack()

root.mainloop()