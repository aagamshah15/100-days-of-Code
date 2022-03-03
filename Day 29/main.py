from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = user_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password):
        messagebox.showinfo(message="Please make sure you haven't left any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f'These are the details you entered: \nEmail: {email} \nPassword: '
                                               f'{password} \nIs this ok to save?')

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

user_entry = Entry(width=52)
user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
user_entry.insert(0, "aagam@gmail.com")

pass_entry = Entry(width=32)
pass_entry.grid(column=1, row=3, sticky="EW")

# Button
gen_pass_button = Button(text="Generate Password", command=pass_gen)
gen_pass_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
