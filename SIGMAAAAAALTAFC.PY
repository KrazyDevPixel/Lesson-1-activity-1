import tkinter as tk
from tkinter import ttk
import random

def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    if choice == computer_choice:
        result = f"Both chose {choice}. It's a Tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = f"You chose {choice}, Computer chose {computer_choice}. You Win!"
    else:
        result = f"You chose {choice}, Computer chose {computer_choice}. You Lose!"
    result_label.config(text=result)

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("420x360")
root.configure(bg="#eaf4fc")

style = ttk.Style()
style.theme_use("clam")
style.configure("Rounded.TButton",
                font=("Segoe UI", 12, "bold"),
                padding=10,
                borderwidth=0,
                foreground="#ffffff",
                background="#4a90e2",
                relief="flat")
style.map("Rounded.TButton",
          background=[("active", "#357ABD")])

heading = tk.Label(root,
                   text="Rock Paper Scissors",
                   font=("Segoe UI", 20, "bold"),
                   bg="#eaf4fc",
                   fg="#2c3e50")
heading.pack(pady=25)

button_frame = tk.Frame(root, bg="#eaf4fc")
button_frame.pack(pady=10)

for i, option in enumerate(["Rock", "Paper", "Scissors"]):
    ttk.Button(button_frame,
               text=option,
               style="Rounded.TButton",
               command=lambda opt=option: play(opt)).grid(row=0, column=i, padx=10)

result_label = tk.Label(root,
                        text="",
                        font=("Segoe UI", 13),
                        bg="#eaf4fc",
                        fg="#34495e",
                        wraplength=360,
                        justify="center")
result_label.pack(pady=30)

ttk.Button(root,
           text="Exit",
           style="Rounded.TButton",
           command=root.destroy).pack()

root.mainloop()
