import tkinter

# to create a new window, same as screen in turtle
window = tkinter.Tk()
# to give a title to our window and resize
window.title("The First King GUI")
window.minsize(width=500, height=300)  # 500x300 pexels

# to create a label on the window
label = tkinter.Label(text="Created By: YJ-928", font=("Arial", 20, "bold"))
# to display the created label
# to display in extact center we use expand
label.pack(expand=True)


# to keep window open, same as screen.exitonclick()
# keep this line at end of your code
window.mainloop()
