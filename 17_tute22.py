from tkinter import *


root =  Tk()

root.geometry("444x234")
root.title("Pari.......")

# For conecting scrallbar to widget
# 1. widget(yscrollcommand = scrollbar.set )
# 2. scrollbar.config(command = widget.yview)


scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y, side=RIGHT)

lbx = Listbox(root, yscrollcommand = scrollbar.set)
for i in range(344):
    lbx.insert(END, f"Item {str(i)}")

lbx.pack(fill=X, padx=44, pady=20)
scrollbar.config(command = lbx.yview)



text = Text(root, yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command = text.yview)






root.mainloop()