from tkinter import *
import tkinter.messagebox as tmsg

root =  Tk()

root.geometry("744x534")
root.title("Pari.......")

def myfunc():
    print("Main a bahuti saytan and natkhat fanction hoon")

def help():
    print("I will help you")
    a=tmsg.showinfo("Help", "Pari will help you with This GUI")
    print(a)

def rate():
    print("Rate us")
    value=tmsg.askquestion("How was your expirence?", "How was your expirence")
    print(value)
    if value=="yes":
        msg = "Great..  Rete us on app store please"
    else:
        msg = "Tell us what went wrong . we will call soon"
    tmsg.showinfo("Experience", msg)

def friend():
    ans = tmsg.askretrycancel("Friend ban jao", "Sorry nehi banunga")
    if ans:
        print("Retry karne pe vi nehi hoga")
    else:
        print("Bahut badiya bhai cancel kar diya")

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







m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Helpiii", command=help)
m3.add_command(label="Rate us", command=rate)
m3.add_command(label="Friend", command=friend)
mainmenu.add_cascade(label="Help", menu=m3)

root.config(menu=mainmenu)




# m4 = Menu(m3, tearoff=0)
# m3.add_cascade(label="Hi", menu=m4)





root.mainloop()
