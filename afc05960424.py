import tkinter as tk
import random

def generate_random_number():
    random_number = random.randint(100000, 999999)  # Generates a random 6-digit OTP
    label.config(text=f"Your OTP: {random_number}")

# Create the main window
root = tk.Tk()
root.title("Random Number Generator")
root.geometry("300x150")

# Create a label to display the OTP
label = tk.Label(root, text="Click 'Generate' to get an OTP", font=("Arial", 12))
label.pack(pady=10)

# Create a button to trigger OTP generation
generate_button = tk.Button(root, text="Generate OTP", command=generate_random_number,font=("Arial",12))
generate_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
