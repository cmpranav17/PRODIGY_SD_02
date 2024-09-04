import tkinter as tk
import random
from PIL import Image, ImageTk

# Function to start a new game
def start_game():
    global random_number, attempts
    random_number = random.randint(1, 100)
    attempts = 0
    result_label.config(text="I'm thinking of a number between 1 and 100.\nCan you guess what it is?")
    entry_guess.delete(0, tk.END)

# Function to check the user's guess
def check_guess():
    global attempts
    try:
        guess = int(entry_guess.get())
        attempts += 1

        if guess < random_number:
            result_label.config(text="Too low! Try again.")
            animate_emoji("☹️", "red")
        elif guess > random_number:
            result_label.config(text="Too high! Try again.")
            animate_emoji("☹️", "red")
        else:
            result_label.config(text=f"Congratulations! You've guessed the number {random_number} correctly in {attempts} attempts!")
            animate_emoji("😊", "green")

    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Function to animate the emoji
def animate_emoji(emoji, color):
    emoji_label = tk.Label(root, text=emoji, font=("Arial", 64), fg=color)
    emoji_label.place(relx=0.5, rely=0.5, anchor="center")
    root.after(1000, lambda: emoji_label.destroy())

# Setting up the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Load the background image
image_path = "guess.jpeg"
bg_image = Image.open(image_path)
bg_image = bg_image.resize((600, 400))
bg_photo = ImageTk.PhotoImage(bg_image)

# Set window size
root.geometry("600x400")

# Create a label to hold the background image
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Set it to fill the window

# Instructions label
instructions_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 16, "bold"), bg="black", fg="cyan")
instructions_label.place(relx=0.5, y=40, anchor="center")

# Entry field for the guess
entry_guess = tk.Entry(root, width=10, font=("Arial", 16), justify="center", highlightthickness=2, highlightcolor="cyan")
entry_guess.place(relx=0.35, rely=0.4, anchor="center")

# Check guess button
check_button = tk.Button(root, text="Check Guess", command=lambda: check_guess(), font=("Arial", 14, "bold"), bg="cyan", fg="black", activebackground="blue", activeforeground="white")
check_button.place(relx=0.65, rely=0.4, anchor="center")

# Label to display result messages
result_label = tk.Label(root, text="", font=("Arial", 14, "italic"), bg="black", fg="cyan", wraplength=500, justify="center")
result_label.place(relx=0.5, rely=0.6, anchor="center")

# Start new game button
new_game_button = tk.Button(root, text="Start New Game", command=start_game, font=("Arial", 14, "bold"), bg="cyan", fg="black", activebackground="blue", activeforeground="white")
new_game_button.place(relx=0.5, rely=0.8, anchor="center")

# Start the game for the first time
start_game()

# Start the main loop
root.mainloop()