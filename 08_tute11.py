from tkinter import *

root = Tk()
root.geometry("655x355")


def getvals():
    print("It's works!...")

Label(root, text="Welcome to Paritosh Travels", font="comicsansms 16 bold", pady=19).grid(row=0, column=3)

name = Label(root, text="Name--> ")
phone = Label(root, text="Phone--> ")
gender = Label(root, text="Gender--> ")
emergency = Label(root, text="Emergency contact--> ")
paymentmode = Label(root, text="Payment Mode--> ")

name.grid(row=1 , column=2)
phone.grid(row=2 , column=2)
gender.grid(row=3 , column=2)
emergency.grid(row=4 , column=2)
paymentmode.grid(row=5 , column=2)


nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
emergencyContectValue = StringVar()
paymentModeValue = StringVar()
foodServiceValue = IntVar()



nameentry = Entry(root, textvariable=nameValue)
phoneentry = Entry(root, textvariable=phoneValue)
genderentry = Entry(root, textvariable=genderValue)
emergencyentry = Entry(root, textvariable=emergencyContectValue)
paymententry = Entry(root, textvariable=paymentModeValue)





nameentry.grid(row=1 , column=3)
phoneentry.grid(row=2 , column=3)
genderentry.grid(row=3 , column=3)
emergencyentry.grid(row=4 , column=3)
paymententry.grid(row=5 , column=3)
# entry.grid(row= , column=3)
# entry.grid(row= , column=3)


# Checkbox and packing it
foodService = Checkbutton(text= "Want to prebook your meals?", variable = foodServiceValue)
foodService.grid(row=6, column=3)


Button(text="Submit to Paritosh Travels", command= getvals).grid(row=7, column=3)




root.mainloop()