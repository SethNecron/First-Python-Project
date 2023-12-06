import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password():
    #Get the desired password length from the user
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")
        return

    #Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    #Generate a random password of the specified length
    password = ''.join(secrets.choice(characters) for _ in range(length))

    #Display the generated password in the entry widget
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    #Get the password from the entry widget
    password = password_entry.get()

    #Copy the password to the clipboard
    app.clipboard_clear()
    app.clipboard_append(password)
    app.update()

    #Notify the user that the password has been copied
    messagebox.showinfo("Copied to Clipboard", "Password copied to clipboard!")

#Create the main application window
app = tk.Tk()
app.title("Random Password Generator")

#Create an entry widget to take the desired password length
length_label = tk.Label(app, text="Password Length:")
length_label.pack(pady=5)
length_entry = tk.Entry(app, width=10, font=("Helvetica", 12))
length_entry.pack(pady=5)

#Create an entry widget to display the generated password
password_entry = tk.Entry(app, width=32, font=("Helvetica", 14))
password_entry.pack(pady=20)

#Create a button to generate a random password
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

#Create a button to copy the password to the clipboard
copy_button = tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

#Run the application
app.mainloop()
