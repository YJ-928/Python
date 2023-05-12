import pandas
from tkinter import *
from tkinter import messagebox
from random import choice
# ------------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 526
TITLE_FONT = ("Ariel",40,"italic")
WORD_FONT = ("Ariel",40,"bold")
EXIT_FONT = ("Ariel",18,"bold")
current_card = {}
to_learn = {}

# ------------------- Fetching Data from CSV File ------------------- #
try:
    data = pandas.read_csv(filepath_or_buffer="data/words_to_learn.csv")
except FileNotFoundError:
    orginal_data = pandas.read_csv(filepath_or_buffer="data/french_words.csv")
    to_learn = orginal_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------------------- FLASH CARDS SETUP --------------------- #
def next_card():
    """Generates new Flash Cards using the data from Words_To_Learn.csv"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer = window.after(3000,func=flip_card)


# ------------------- FLASH CARD FLIP ---------------- #
def flip_card():
    """Changes the Flash card to English after delay of 3s"""
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ------------------- FLASH CARD SAVE ---------------- #
def save_card():
    """Saves the Flash Card to seperate csv, when user clicks right_button.
    Then only the words user dosent know will be showed again"""
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()


# -------------==-- THE APP EXIT ------------- #
def app_exit():
    """Exit the App or Program with a confirmation message"""
    if_exit = messagebox.askyesno(
        title="Exit Password Manager", message="Do you really wish to exit?")
    if if_exit == True:
        exit()


# --------------- UI SETUP -------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=CANVAS_WIDTH,height=CANVAS_HEIGHT,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=card_front_img)
card_title = canvas.create_text(400,150,text="",font=TITLE_FONT)
card_word = canvas.create_text(400,263,text="",font=WORD_FONT)
canvas.grid(row=0,column=0,columnspan=2)

# Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,bg=BACKGROUND_COLOR,highlightthickness=0,command=save_card)
right_button.grid(row=1,column=1)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR,
                      highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
exit_button = Button(text="EXIT",font=EXIT_FONT, bg="red", highlightthickness=0,command=app_exit)
exit_button.grid(row=2,column=0,columnspan=2)


# to change to Eng after delay of 3s
flip_timer = window.after(3000, func=flip_card)

# to display French card as we start the app
next_card()

# to run the window continously
window.mainloop()