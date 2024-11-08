import tkinter as tk
from tkinter import messagebox

def encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

def perform_action():
    text = text_entry.get()
    shift_input = shift_entry.get()
    
    try:
        shift = int(shift_input)
        if shift < 1 or shift > 25:
            messagebox.showerror("Input Error", "Shift must be between 1 and 25.")
            return
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer for shift.")
        return
    
    choice = action_var.get()
    if choice == 'E':
        result = encrypt(text, shift)
        result_label.config(text="Encrypted: " + result)
    elif choice == 'D':
        result = decrypt(text, shift)
        result_label.config(text="Decrypted: " + result)

# Initialize the main window
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("400x300")
root.config(bg="#f5f5f5")

# Header Label
header_label = tk.Label(root, text="Caesar Cipher Tool", font=("Arial", 16, "bold"), bg="#f5f5f5")
header_label.pack(pady=10)

# Frame for input fields and options
frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(pady=10)

# Radio buttons for action choice (Encrypt/Decrypt)
action_var = tk.StringVar(value='E')
encrypt_radio = tk.Radiobutton(frame, text="Encrypt", variable=action_var, value='E', bg="#f5f5f5")
decrypt_radio = tk.Radiobutton(frame, text="Decrypt", variable=action_var, value='D', bg="#f5f5f5")
encrypt_radio.grid(row=0, column=0, padx=5)
decrypt_radio.grid(row=0, column=1, padx=5)

# Label and Entry for Text Input
text_label = tk.Label(frame, text="Enter Text:", bg="#f5f5f5")
text_label.grid(row=1, column=0, pady=5, sticky="e")
text_entry = tk.Entry(frame, width=30)
text_entry.grid(row=1, column=1, pady=5, padx=5)

# Label and Entry for Shift Value
shift_label = tk.Label(frame, text="Enter Shift (1-25):", bg="#f5f5f5")
shift_label.grid(row=2, column=0, pady=5, sticky="e")
shift_entry = tk.Entry(frame, width=10)
shift_entry.grid(row=2, column=1, pady=5, padx=5, sticky="w")

# Button to perform encryption/decryption
action_button = tk.Button(root, text="Go", command=perform_action, bg="#4CAF50", fg="white", width=10)
action_button.pack(pady=15)

# Label to show the result
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f5f5f5")
result_label.pack(pady=10)

# Run the main event loop
root.mainloop()
