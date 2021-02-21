from tkinter import *

root = Tk()
root.geometry("655x444")
root.title("Paritosh.....")

root.wm_iconbitmap("workspace1_122059.ico")

root.configure(background="orange")


width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")

Button(text="Close", command=root.destroy).pack()



root.mainloop()