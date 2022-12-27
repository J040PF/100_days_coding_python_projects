from tkinter import *

screen = Tk()
screen.title('conversor')
screen.minsize(width=300, height=100)

label = Label(text='Miles To Km', font=("Arial", 30, "bold"))
label.pack()

text = Entry(width=30)
text.pack()

new_label = Label(text= " ")
new_label.pack()

def converter():
    information = float(text.get())
    miles = information*1.609
    new_label.config(text="{} Km ".format(miles), font=("Arial", 20 , "bold"))


button = Button(text='Converter', command=converter)
button.pack()

screen.mainloop()