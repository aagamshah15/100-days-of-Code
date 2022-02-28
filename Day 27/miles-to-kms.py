from tkinter import *
FONT = ("Courier", 16, "normal")


def button_clicked():
    convert_to_kms = float(input_user_miles.get()) * 1.6
    answer["text"]= round(convert_to_kms, 2)


window = Tk()
window.title("Mile to km converter")
# window.minsize(width=400, height=300)
window.config(padx=20, pady=40)

# Lables
miles = Label(text="Miles", font= FONT)
miles.grid(column=2, row=0)

km = Label(text="Km", font=FONT)
km.grid(column=2, row=1)

is_equal_to = Label(text="is equal to", font=(FONT))
is_equal_to.grid(column=0, row=1)

answer = Label(text="", font=FONT)
answer.grid(column=1, row=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

# Entry
input_user_miles = Entry(width=10)
print(input_user_miles.get())
input_user_miles.grid(column=1, row=0)

window.mainloop()