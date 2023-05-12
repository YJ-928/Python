# importing whole TKinter module 
from tkinter import *

def miles_to_kilometer():
    """Takes Miles as input and converts to KiloMeters
    And creates a Label to display the output"""
    miles = int(mile_input.get())
    Kilometers = round(miles*1.609)
    result_label = Label(
        text=f"{miles} Miles is equal to {Kilometers} Km",font=("Roboto", 10, "bold"), fg="red", bg="Black")
    result_label.grid(row=4, column=1)

# setting initial window
window = Tk()
window.title("Mile To KM")
window.config(padx=20,pady=20)
window.config(background="Black")

# heading label
heading_label = Label(
    text="Miles to KM Convertor by YJ-928",font=("Roboto",11), fg="Orange", bg="Black")
heading_label.grid(row=0,column=1)

# gap label to provide gaps/spaces in GUI
gap_label = Label(fg="Black", bg="Black")
gap_label.grid(row=1,column=1)

# taking input
miles_input_label = Label(text="Enter the number of Miles:", font=(
    "Roboto", 10, "bold"), fg="Yellow", bg="Black")
miles_input_label.grid(row=2,column=1)

# Miles display
mile_input = Entry(width=5)
mile_input.grid(row=2,column=2)

# Two gaps, between whom the result will be printed
gap_label = Label(fg="Black", bg="Black")
gap_label.grid(row=3, column=1)

gap_label = Label(fg="Black", bg="Black")
gap_label.grid(row=5, column=1)

# button to calculate
button_cal = Button(text="Calculate", fg="Yellow",
                    bg="Black", command=miles_to_kilometer)
button_cal.grid(row=6, column=1)

gap_label = Label(fg="Black", bg="Black")
gap_label.grid(row=7, column=1)

# button to exit
button_exit = Button(text="Exit", fg="Red", bg="Black", command=exit)
button_exit.grid(row=8,column=1)

# to keep window open until user presses exit
window.mainloop()