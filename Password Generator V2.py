import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password():
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of length 12
    password = ''.join(secrets.choice(characters) for _ in range(12))

    # Display the generated password in a message box
    messagebox.showinfo("Generated Password", f"Your random password is:\n{password}")

# Create the main application window
app = tk.Tk()
app.title("Random Password Generator")

# Create a button to generate a random password
button = tk.Button(app, text="Generate Password", command=generate_password)
button.pack(pady=20)

# Run the application
app.mainloop()
