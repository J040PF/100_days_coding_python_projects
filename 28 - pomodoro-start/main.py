from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
button_yes = False
n_time = 0

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global button_yes, n_time
    button_yes = False
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer, text="00:00")
    n_time *= 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def starter_timer():
    global WORK_MIN, SHORT_BREAK_MIN, n_time, button_yes
    long_break = 20*60
    short_break = SHORT_BREAK_MIN*60
    WORK_MIN = 1 * 5

    if button_yes is False:
        button_yes = True

        if n_time == 8:
            label.config(text="Long Break")
            time(long_break)
            n_time * 0

        else:

            if n_time % 2 == 0 or n_time == 2:
                n_time += 1
                label.config(text="Work")
                time(WORK_MIN)

            else:
                label.config(text='Break', fg=RED)
                time(short_break)
                n_time += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def time(count):
    global button_yes
    count_min = math.floor(count/60)
    count_sec = count % 60
    if button_yes is True:
        if count_sec == 0 or count_sec < 10:
            count_sec = "0{}".format(count_sec)
        if count_min < 10:
            count_min = "0{}".format(count_min)

        canvas.itemconfig(timer, text="{}:{}".format(count_min, count_sec))

        if count > 0 and button_yes is True:
            window.after(1000, time, count - 1)
        else:
            button_yes = False

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, background=YELLOW)

label = Label(text="Timer", background=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
button_start = Button(text='Start', command=starter_timer)
button_reset = Button(text='Reset', command=reset_timer)

canvas = Canvas(width=200, height=224, bg=YELLOW)
img = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))

canvas.grid(column=1, row=1)
label.grid(column=1, row=0)
button_reset.grid(column=3, row=3)
button_start.grid(column=0, row=3)

window.mainloop()