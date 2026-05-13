import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from encrypt import encrypt_file
from decrypt import decrypt_file


# Create main window
window = tk.Tk()

window.title("Advanced Encryption Tool")
window.geometry("500x350")
window.config(bg="white")


# Variable to store selected file
selected_file = ""


# Function to choose file
def choose_file():

    global selected_file

    selected_file = filedialog.askopenfilename()

    file_label.config(text=selected_file)


# Function to encrypt file
def start_encryption():

    if selected_file == "":
        messagebox.showerror(
            "Error",
            "Please select a file first"
        )
        return

    encrypted = encrypt_file(selected_file)

    messagebox.showinfo(
        "Success",
        f"File Encrypted Successfully\n\nSaved As:\n{encrypted}"
    )


# Function to decrypt file
def start_decryption():

    if selected_file == "":
        messagebox.showerror(
            "Error",
            "Please select a file first"
        )
        return

    try:

        decrypted = decrypt_file(selected_file)

        messagebox.showinfo(
            "Success",
            f"File Decrypted Successfully\n\nSaved As:\n{decrypted}"
        )

    except:

        messagebox.showerror(
            "Error",
            "Decryption Failed"
        )


# Heading
heading = tk.Label(
    window,
    text="Advanced Encryption Tool",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="darkblue"
)

heading.pack(pady=20)


# File selection button
choose_btn = tk.Button(
    window,
    text="Choose File",
    command=choose_file,
    bg="orange",
    fg="white",
    width=20,
    height=2,
    font=("Arial", 11)
)

choose_btn.pack(pady=10)


# Label to display selected file
file_label = tk.Label(
    window,
    text="No File Selected",
    bg="white",
    fg="black",
    wraplength=400
)

file_label.pack(pady=10)


# Encrypt button
encrypt_btn = tk.Button(
    window,
    text="Encrypt File",
    command=start_encryption,
    bg="green",
    fg="white",
    width=20,
    height=2,
    font=("Arial", 11)
)

encrypt_btn.pack(pady=10)


# Decrypt button
decrypt_btn = tk.Button(
    window,
    text="Decrypt File",
    command=start_decryption,
    bg="blue",
    fg="white",
    width=20,
    height=2,
    font=("Arial", 11)
)

decrypt_btn.pack(pady=10)


# Run window
window.mainloop()