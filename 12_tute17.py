from tkinter import *

root =  Tk()

root.geometry("744x534")
root.title("Pari.......")

def myfunc():
    print("Main a bahuti saytan and natkhat fanction hoon")


# #  Use these to create a non dropdown menu
# mymanu = Menu(root)
# mymanu.add_command(label="File", command=myfunc)
# mymanu.add_command(label="Exit", command=quit)
# root.config(menu=mymanu)



mainmenu = Menu(root)


m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="My Project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save as", command=myfunc)
m1.add_command(label="Print", command=myfunc)

root.config(menu=mainmenu)

mainmenu.add_cascade(label="File", menu=m1)




m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Past", command=myfunc)
m2.add_command(label="Find", command=myfunc)


root.config(menu=mainmenu)

mainmenu.add_cascade(label="Edit", menu=m2)




root.mainloop()
