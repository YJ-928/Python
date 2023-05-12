# to import all modules
from tkinter import *

window = Tk()
window.title("GUI with Button")
window.minsize(width=150, height=100)


def change_label():
    """Changes The label display text when button is clicked"""
    newtext = text_box.get()
    label.config(text=newtext)


label = Label(text="Click the Button Below")
label.pack()

button = Button(text="Click Me", command=change_label)
button.pack()

text_box = Entry(width=30)
text_box.pack()

window.mainloop()
