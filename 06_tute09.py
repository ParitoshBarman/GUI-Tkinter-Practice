from tkinter import *

root = Tk()
root.title('Paritosh......')
root.geometry("655x333")


def hello():
    print("Hello tkinter buttons")

def name():
    print("Name is PariTosh")





f1 = Frame(root, borderwidth=6, bg='grey', relief=SUNKEN)
f1.pack(side=LEFT, anchor="nw")

b1 = Button(f1, fg='red', text="Print now", command = hello)
b1.pack(side=LEFT)


b2 = Button(f1, fg='red', text="Tell me name now", command=name)
b2.pack(side=LEFT, padx=23)

b3 = Button(f1, fg='red', text="Print now")
b3.pack(side=LEFT, padx=23)

b4 = Button(f1, fg='red', text="Print now")
b4.pack(side=LEFT, padx=23)




root.mainloop()