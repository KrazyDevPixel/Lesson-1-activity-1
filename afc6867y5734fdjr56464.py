import tkinter as tk
from tkinter import messagebox
import random
def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    result = ""
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
root.geometry("400x300")
root.resizable(False, False)
heading = tk.Label(root, text="Rock Paper Scissors Game", font=("Helvetica", 16, "bold"))
heading.pack(pady=20)
button_frame = tk.Frame(root)
button_frame.pack(pady=20)
rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)
paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)
scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)
result_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=350)
result_label.pack(pady=20)
exit_button = tk.Button(root, text="Exit", width=10, command=root.destroy)
exit_button.pack(pady=10)
root.mainloop()