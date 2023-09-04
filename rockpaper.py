import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock' and computer_choice == 'scissors' or \
         user_choice == 'scissors' and computer_choice == 'paper' or \
         user_choice == 'paper' and computer_choice == 'rock':
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    
    user_label.config(text=f"You chose: {user_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)

window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

choices = ['rock', 'paper', 'scissors']

user_choice_var = tk.StringVar()
user_choice_var.set(choices[0])

user_choice_label = tk.Label(window, text="Choose:")
user_choice_label.pack()
user_choice_optionmenu = tk.OptionMenu(window, user_choice_var, *choices)
user_choice_optionmenu.pack()

play_button = tk.Button(window, text="Play", command=play_game)
play_button.pack()


user_label = tk.Label(window, text="")
user_label.pack()
computer_label = tk.Label(window, text="")
computer_label.pack()
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()