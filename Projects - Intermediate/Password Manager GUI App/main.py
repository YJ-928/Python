import pyperclip
from random import randint,choice,shuffle
from tkinter import *
from tkinter import messagebox
import json

# ------------------------------------- CONSTANTS ----------------------------------- #
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 200
BACKGROUND = "Black"
LABELS_COLOR = "Light Green"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    """Generates Random password using letters,numbers and symbols
    and returns it as a string"""
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    Letter_List = [choice(letters) for _ in range(randint(8, 10))]
    Symbol_List = [choice(symbols) for _ in range(randint(2, 4))]
    Number_List = [choice(numbers) for _ in range(randint(2, 4))]

    Password_List = Letter_List + Symbol_List + Number_List
    shuffle(Password_List)

    password = "".join(Password_List)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """Saves the Website,Email and Password to a Data.json file,
    and clears the entries for user"""
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website:{
            "email":email,
            "password":password,
        },
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops",message="Please don't leave any fields empty.")

    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
                data.update(new_data)

        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
            website_entry.delete(0,END)
            password_entry.delete(0, END)
            website_entry.focus()
    

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    """Searches the json file for user given website
    and returns the email and password for it if it exists"""
    website = website_entry.get().title()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
            if website in data.keys():
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(
                    title="Error", message=f"No details for {website} exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")


# ------------------------------- APP EXIT---------------------------------- #
def app_exit():
    """Exit the App or Program with a confirmation message"""
    if_exit = messagebox.askyesno(title="Exit Password Manager",message="Do you really wish to exit?")
    if if_exit == True:
        exit()



# ---------------------------- UI SETUP ------------------------------- #
# Window and Canvas
window = Tk()
window.title("Password Manager By YJ-928")
window.config(padx=50, pady=50, bg=BACKGROUND)
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                bg=BACKGROUND, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(row=0,column=1)

# Labels
website_label = Label(text="Website :",fg=LABELS_COLOR, bg=BACKGROUND)
website_label.grid(row=1, column=0, columnspan=1)
email_label = Label(text="Email/Username :", fg=LABELS_COLOR, bg=BACKGROUND)
email_label.grid(row=2, column=0, columnspan=1)
passowrd_label = Label(text="Password :", fg=LABELS_COLOR, bg=BACKGROUND)
passowrd_label.grid(row=3, column=0, columnspan=1)

# Textbox Entries
# here we use columnspan to stretch 
# the widget over more than 1 column
website_entry = Entry(width=26)
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=1)
email_entry = Entry(width=26)
email_entry.insert(0,"yashjoshi@gmail.com")
email_entry.grid(row=2, column=1, columnspan=1)
password_entry = Entry(width=26)
password_entry.grid(row=3, column=1, columnspan=1)

# Buttons
search_button = Button(text="Search",width=16,fg="Orange",bg=BACKGROUND,command=search_password)
search_button.grid(row=1,column=2,columnspan=1)
generate_password = Button(text="Generate Password", width=16,
                           fg="Orange", bg=BACKGROUND, command=password_generator)
generate_password.grid(row=3, column=2, columnspan=1)
add_password = Button(text="Save Password", width=39,
                      fg="Orange", bg=BACKGROUND,command=save_password)
add_password.grid(row=6, column=1,columnspan=2)
exit_button = Button(text="Exit",fg="White",bg="Red",width=21,command=app_exit)
exit_button.grid(row=8,column=1,columnspan=1)

# blank label to put a space above save button
blank = Label(fg="Black",bg="Black",width=40)
blank.grid(row=5,column=1,columnspan=2)
blank = Label(fg="Black", bg="Black", width=40)
blank.grid(row=7, column=1, columnspan=2)

# to keep window open infinetly
window.mainloop()
