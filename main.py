from tkinter import *
root = Tk()
root.geometry("400x300")

def getvals():
    print("Acceptes")

Label(root, text = "Python Registration Form", font = "arial 15 bold").grid(row = 0, column = 3)

name = Label(root, text = "Name")
phone = Label(root, text = "Phone")
gender = Label(root, text = "Gender")
emergency = Label(root, text = "Emergency")
paymentmood = Label(root, text = "Paymentmood")

name.grid(row = 1, column = 2)
phone.grid(row = 2, column = 2)
gender.grid(row = 3, column = 2)
emergency.grid(row = 4, column = 2)
paymentmood.grid(row = 5, column = 2)

nameValue = StringVar
phoneValue = StringVar
genderValue = StringVar
emergencyValue = StringVar
paymentmoodValue = StringVar
checkValue = IntVar

nameentry = Entry(root, textvariable = nameValue)
phoneentry = Entry(root, textvariable = phoneValue)
genderentry = Entry(root, textvariable = genderValue)
emergencyentry = Entry(root, textvariable = emergencyValue)
paymentmoodentry = Entry(root, textvariable = paymentmoodValue)

nameentry.grid(row = 1, column = 3)
phoneentry.grid(row = 2, column = 3)
genderentry.grid(row = 3, column = 3)
emergencyentry.grid(row = 4, column = 3)
paymentmoodentry.grid(row = 5, column = 3)

checkbtn = Checkbutton(text = "remember me ?", variable = checkValue)
checkbtn.grid(row = 6, column = 3)

Button(text = "Submit", command = getvals).grid(row = 7, column = 3)

root.mainloop()