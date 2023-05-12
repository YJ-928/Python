from tkinter import *

window = Tk()
window.title("GUI By YJ-928")
window.minsize(width=250, height=200)

label = Label(text="The Button Label")
label.grid(row=0, column=0)

button = Button(text="Click Me")
button.grid(row=1, column=1)

window.mainloop()
