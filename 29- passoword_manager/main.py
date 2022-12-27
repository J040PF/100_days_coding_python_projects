import random
from tkinter import *
from tkinter import messagebox
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passwor_random():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = ""
    for x in range(0, 8):
        random_character = random.choice(letters+numbers+symbols)
        password += str(random_character)

    text_senha.delete(0, END)
    text_senha.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    senha = text_senha.get()
    email = text_email.get()
    web = text_web.get()
    new_data = {web:{"email": email,
                     "passoword": senha}
                }

    is_ok = messagebox.askokcancel(title=web, message='Do you want continue???\n{}\n{}'.format(web, email))

    senha = senha.strip()
    email = email.strip()
    web = web.strip()

    if is_ok is True:
        try:
            with open('data.json', "r") as data:
                y_data = json.load(data)

        except FileNotFoundError:
            with open("data.json", "w")as data:
                json.dump(new_data, data, indent=4)

        else:
            y_data.update(new_data)
            with open("data.json", "w") as data:
                json.dump(y_data, data, indent=4)

        finally:
            text_web.delete(0, END)
            text_senha.delete(0, END)


def find_site():

    text = text_web.get()
    try:
        with open("data.json", "r") as data:
            r_data = json.load(data)

        if r_data[text]:
            messagebox.askokcancel(message=r_data[text])
        else:
            messagebox.showerror(message='nothing found')
    except:
        messagebox.showerror(message='nothing found')
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

label_web = Label(text='WebSite')
label_web.grid(column=0, row=1)
text_web = Entry(width=50)
text_web.focus()
text_web.grid(column=1, row=1)

label_email = Label(text='Email')
label_email.grid(column=0, row=2)
text_email = Entry(width=50)
text_email.insert(0, 'enice@gmail.com')
text_email.grid(column=1, row=2)

label_senha = Label(text='PassWord')
label_senha.grid(column=0, row=3)
text_senha = Entry(width=50)
text_senha.grid(column=1, row=3,)
button_generate = Button(text='Generate', command=passwor_random)
button_generate.config(width=10)
button_generate.grid(column=2, row=3, columnspan=2)

button_add = Button(text='Add', command= save)
button_add.config(width=30)
button_add.grid(column=0, row=4, columnspan=4)

button_search = Button(text='Search', command= find_site)
button_search.config(width=10)
button_search.grid(column=3, row=1)

window.mainloop()