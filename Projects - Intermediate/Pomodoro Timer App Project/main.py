from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
FONT_SIZE = 35
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- GLOBAL VARIBALES ------------------------------- #
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    """Resets the timer back to 00:00 starting value"""
    global timer
    global reps
    canvas.itemconfig(timer_text,text="00:00")
    window.after_cancel(timer)
    title_label.config(text="Timer")
    check_mark_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """Starts the timer calls the count_down mechanism function"""
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # after 8 repitations Long Break
    if reps % 8 == 0:
        title_label.config(text="Break", foreground=RED)
        count_down(long_break_sec)
    # after every work section Short Break
    elif reps % 2 == 0:
        title_label.config(text="Break", foreground=PINK)
        count_down(short_break_sec)
    # work section count_down time
    else:
        title_label.config(text="Work",foreground=GREEN)
        count_down(work_sec)
    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    """Takes in a count value and displays the count every second
    on the canvas until the count reaches zero"""
    global timer
    # to display time in min:seconds format
    count_min = math.floor(count/60)
    count_sec = count % 60
    # to display the starting count as 0.00 instead of 0.0
    if count_sec == 0:
        count_sec = "00"
    # to display num < 10 as 09,08.. instead of 9,8..
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    # to update the canvas text, slightly different steps than tkinter label
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro by YJ-928")
window.config(padx=100,pady=50,background=YELLOW)


title_label = Label(text="Timer",foreground=GREEN,background=YELLOW,font=(FONT_NAME,50,"bold"))
title_label.grid(row=0,column=1)


# creating a canvas using canva class
# to add tomato img as background
canvas = Canvas(width=200,height=224,background=YELLOW,highlightthickness=0)
# importing the image from the path
tomato_img = PhotoImage(file="tomato.png")
# creating canvas with our image as its background
# (100,112)-->(X,Y) coords where the image will be anchored
canvas.create_image(100,112,image=tomato_img)
# to create text over our image
timer_text = canvas.create_text(100,130,text="00:00",fill="White",font=(FONT_NAME,FONT_SIZE,"bold"))
# to display our canvas on window
canvas.grid(row=1,column=1)


start_button = Button(text="Start",command=start_timer)
start_button.grid(row=2, column=0)


reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(row=2, column=2)


check_mark_label = Label(foreground=GREEN,
                         background=YELLOW)
check_mark_label.grid(row=3,column=1)


# to display window
window.mainloop()
