from tkinter import *

root = Tk()
root.geometry("655x355")

def getValue():
    print(f"The user name is {userValue.get()}") 
    print(f"The password is {passValue.get()}")

user = Label(root, text="Username")
password = Label(root, text="Password")

user.grid(row=0)
password.grid(row=1)


# Variable classes in Tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

userValue = StringVar()
passValue = StringVar()

userentry = Entry(root, textvariable = userValue)
passentry = Entry(root, textvariable = passValue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getValue).grid()


# f1 = Frame(root, bg='grey', borderwidth=6,  relief=SUNKEN)
# f1.grid()
# Button(f1, text="Submit", command=getValue).grid()



root.mainloop()