from tkinter import *
import tkinter.messagebox as tmsg


root =  Tk()

root.geometry("444x234")
root.title("Pari.......")

def order():
    tmsg.showinfo("Order received!",f"We have received your order for {var.get()}...   Thanks for ordering...")




# var = IntVar()
var = StringVar()
# var.set(1)
var.set("Radio")
Label(root, text="What you like to have sir?", justify=LEFT, padx=14, font="lucida 19 bold").pack()

radio = Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa" ).pack(anchor="w")
radio = Radiobutton(root, text="Idly", padx=14, variable=var, value="Idly" ).pack(anchor="w")
radio = Radiobutton(root, text="Parotha", padx=14, variable=var, value="Parotha").pack(anchor="w")
radio = Radiobutton(root, text="Samosa", padx=14, variable=var, value="Samosa").pack(anchor="w")

Button(text="Order Now", command=order).pack()




root.mainloop()