from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()



# The line gose from the point x1, y1 and x2, y2
can_widget.create_line(0, 0, 800, 400, fill="red")
can_widget.create_line(0, 400, 800, 0, fill="green")



# To create a rectangle sepecify parameters in this order --->>
# can_widget.create_rectangle(3, 5, 700, 300, fill='blue')
can_widget.create_rectangle(50, 50, 750, 350)


can_widget.create_text(200, 200, text="Python")



can_widget.create_oval(344, 233, 244, 355)





root.mainloop()