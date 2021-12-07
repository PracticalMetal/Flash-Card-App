from tkinter import *
from pandas import *
import random

GREEN = "#9bdeac"
FONT_NAME = "Ariel"
random_word = {}
### ------------------ READING CSV DATA ------------------ ###
try:
    data = read_csv("to_learn.csv")
except:
    data = read_csv("data/french_words.csv")
finally:
    data_list = data.to_dict(orient="records")

### ------------------ COMMANDS ------------------ #


def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(bg, image=card_front)
    random_word = random.choice(data_list)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_word["French"], fill="black")
    flip_timer = window.after(3000, flip_mechanism)


def next_card_correct():
    global random_word, flip_timer, data_list
    window.after_cancel(flip_timer)
    canvas.itemconfig(bg, image=card_front)
    random_word = random.choice(data_list)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_word["French"], fill="black")
    data_list.remove(random_word)
    new_data = DataFrame(data_list)
    new_data.to_csv("to_learn.csv", index=False)
    flip_timer = window.after(3000, flip_mechanism)


def next_card_wrong():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(bg, image=card_front)
    random_word = random.choice(data_list)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_word["French"], fill="black")
    flip_timer = window.after(3000, flip_mechanism)


def flip_mechanism():
    global random_word
    canvas.itemconfig(bg, image=card_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, fill="white", text=random_word["English"])

### ------------------ UI ------------------ ###


window = Tk()
window.config(pady=50, padx=50, bg=GREEN)
window.title("Flash Card Learner")

### ------------------ FLIPPING MECHANISM ------------------ ###
flip_timer = window.after(3000, flip_mechanism)
# window.config(padx=50,pady=50)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas(height=526, width=800, bg=GREEN, highlightthickness=0)
bg = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

# text
title_text = canvas.create_text(400, 150, text="French", fill="black",
                                font=(FONT_NAME, 40, "italic"))


word_text = canvas.create_text(400, 263, text="trouve", fill="black",
                               font=(FONT_NAME, 40, "bold italic"))
next_card()

# buttons
right_button = Button(image=right, highlightthickness=0,
                      borderwidth=0, bd=0, bg=GREEN, command=next_card_correct)
right_button.grid(row=1, column=0)

wrong_button = Button(image=wrong, highlightthickness=0,
                      borderwidth=0, bd=0, bg=GREEN, command=next_card_wrong)
wrong_button.grid(row=1, column=1)


window.mainloop()
