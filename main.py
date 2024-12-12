from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(8, 10))]

    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]

    password_numbers = [choice(numbers) for number in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) != 0 and len(password) != 0:
        try:
            with open("data.json", "r") as file:
                #reading old data
                data = json.load(file)


        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:

            #updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                #saving updated data
                json.dump(data, file, indent=4)

        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)

    else:
        messagebox.showerror(title="Oops", message="Please don't leave any field empty!")







# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)


# canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# website label
web_label = Label(text="Website:", font=("Ariel", 12))
web_label.grid(row=1, column=0)

# website input
web_input = Entry(width=40)
web_input.grid(row=1, column=1)
web_input.focus()

# email label
email_label = Label(text="Email/ Username:", font=("Ariel", 12))
email_label.grid(row=2, column=0)

# email input
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "rv8961@srmist.edu.in")

# password label
pass_label = Label(text="Password:", font=("Ariel", 12))
pass_label.grid(row=3, column=0)

# password input
pass_input = Entry(width=32)
pass_input.grid(row=3, column=1)

# generate password button
gen_pass_but = Button(text="Generate Password", command=generate_password)
gen_pass_but.grid(row=3, column=2)

def find_pass():
    website = web_input.get()
    with open("data.json", "r") as file:
        data = json.load(file)
        try:
            web_pass = data[f"{website}"]["password"]
        except KeyError:
            messagebox.showinfo(website, f"No Data File Found")
        else:
            messagebox.showinfo(website, f"password: {web_pass}")


# search button
search_but = Button(text="Search", width=10,  command=find_pass)
search_but.grid(row=1, column=2)

# add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)






window.mainloop()
