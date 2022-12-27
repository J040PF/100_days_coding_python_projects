from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
# --------------BD manipulation-------------------- #
data = pd.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient='records')
word_learn = {}


# next card ---------------------- #
def next_car():
    global word_learn, flip_timer

    windom.after_cancel(flip_timer)
    word_learn = random.choice(to_learn)
    save(word_learn)
    canva.itemconfig(Idiom_text, fill='black', text='English')
    canva.itemconfig(word_text, fill='black', text=word_learn['English'])

    windom.after(3000, func=flip_card)


# ---------save data --------------#
data_target = []
data_native = []

try:
    words = pd.read_csv('learned_words.csv')
    data_target = list(words['french'])
    data_native = list(words['englis'])

except FileNotFoundError:
    pass


def save(word):
    global data_native, data_target
    target_language = word['French']
    native_language = word['English']
    data_native.append(native_language)
    data_target.append(target_language)

    data = {'englis': data_native,
            'french': data_target}

    new_save = pd.DataFrame(data)
    new_save.to_csv('Learned_words.csv', index=False)


# animation window after 3s ------------- #
def flip_card():
    back_image = PhotoImage(file='images/card_back.png')
    canva.itemconfig(card_background, image=back_image)
    canva.itemconfig(Idiom_text, fill='white', text='French')
    canva.itemconfig(word_text, fill='white', text=word_learn['French'])


# ------------- Screen -------------- #
windom = Tk()
windom.config(padx=5, pady=0, background=BACKGROUND_COLOR)
canva = Canvas(width=800, height=596)

flip_timer = windom.after(3000, func=flip_card)

# front image
img = PhotoImage(file='images/card_front.png')
card_background = canva.create_image(400, 263, image=img)
canva.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canva.grid(column=0, row=0, columnspan=2)

# text image
Idiom_text = canva.create_text(400, 150, text='English', font=('Ariel', 40, 'italic'))
word_text = canva.create_text(400, 263, text="", font=('Ariel', 60, 'bold'))

# Buttons
image_unknown = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=image_unknown, highlightthickness=0, command=next_car)
unknown_button.grid(column=0, row=1)

image_check = PhotoImage(file='images/right.png')
check_button = Button(image=image_check, highlightthickness=0, command=next_car)
check_button.grid(column=1, row=1)

next_car()

windom.mainloop()