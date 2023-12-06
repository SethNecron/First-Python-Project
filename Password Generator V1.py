import tkinter as tk

def button_click():
    entered_text = entry.get()
    label.config(text=f"You entered: {entered_text}")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create an entry (text box)
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button
button = tk.Button(root, text="Generate Password", command=button_click)
button.pack(pady=10)

# Run the main loop
root.mainloop()
