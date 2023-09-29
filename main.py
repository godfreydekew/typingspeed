import random
from tkinter import *
from tkinter import filedialog, messagebox
import time

# Set the initial game duration to 60 seconds
duration = 60

# Define the font name for the game
FONT_NAME = "Courier"

# Show welcome message and instructions in a message box
messagebox.showinfo(
    title="Welcome",
    message="Welcome to Typing Speed Game!\n\nInstructions:\n1. Press 'Start Game' to begin typing.\n2. Type the displayed words as quickly and accurately as possible.\n3. Press 'Quit' button to exit the game.\n4. Your results will be displayed after the game."
)

# Create the main window
window = Tk()
window.title("Typing_speed")
window.geometry("800x800")
window.config(padx=50, pady=50)

# Read the list of strings from a file and choose a random string
with open('my_strings.txt', 'r') as file:
    my_strings_list = file.readlines()
my_strings_list = [string.strip() for string in my_strings_list]
my_string = random.choice(my_strings_list)

# Function to calculate typing speed
def speed():
    score = 0
    words = typing_entry.get()
    words_list = words.split()
    string_list = my_string.split()

    num_comparisons = min(len(words_list), len(string_list))
    for i in range(num_comparisons):
        if words_list[i] == string_list[i]:
            score += 1

    if score > 0:
        cpm = len(words) + 1
    else:
        cpm = 0
    results.itemconfig(results_txt, text=f" WPM : {score}  \n CPM: {cpm} \n Mistakes: \n")

# Function to start the game
def start():
    global duration
    typing_entry.config(state='normal')
    typing_entry.focus()
    if duration > 0:
        canvas.itemconfig(timer_txt, text=f"Time remaining :{duration}")
        duration -= 1
        window.after(1000, start)
    if duration == 0:
        results.pack(pady=20)
        speed()
        messagebox.showinfo(message="Time's up!")
        typing_entry.delete(0, 'end')
        duration = 10
        canvas.itemconfig(timer_txt, text=f"Time remaining : 00")

# Function to exit the game
def exit_the_game():
    x = messagebox.askokcancel(title="Bye!", message="You are about to quit the game")
    if x:
        exit()

# Define the welcome font
welcome_font = ("Helvetica", 30, "italic")

# Create a Canvas for the welcome widget
welcome_canvas = Canvas(window, width=700, height=60, highlightthickness=5)
welcome_text = welcome_canvas.create_text(300, 30, text="Welcome to Typing Speed GAME", fill="grey", font=welcome_font)
welcome_canvas.pack()

# Create a Canvas for the timer
canvas = Canvas(window, width=700, height=60, bg="grey", highlightthickness=5)
timer_txt = canvas.create_text(300, 30, text="Time remaining :60", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.pack()

# Create a Canvas for displaying the text to type
text_canvas = Canvas(window, width=700, height=200, bg="grey", highlightthickness=5)
my_text = text_canvas.create_text(350, 100, text=my_string, fill="white", font=(FONT_NAME, 12, "bold"), width=650,
                                  anchor="center")
text_canvas.pack()

# Create an Entry widget for typing
typing_entry = Entry(window, font=("Helvetica", 15), width=50, state='disabled', justify='center')
typing_entry.pack(pady=(10, 10), padx=10)

# Create a LabelFrame for buttons
border = LabelFrame(window, bd=3, bg="white")
border.pack(pady=5)

# Create a Quit button
speed_btn = Button(border, text="QUIT", command=exit_the_game, width=15,
                   height=2, fg="white", background="red", font=("Times New Roman", 13))
speed_btn.pack(side="left", padx=20)

# Create a Start button
start_btn = Button(border, text="Start game", command=start, height=2, width=15,
                   fg="white", background="green",
                   font=("Times New Roman", 13))
start_btn.pack(side="right", padx=40)

# Create a Canvas for displaying results
results = Canvas(window, width=400, height=300, bg="grey")
results_txt = results.create_text(150, 100, text=" WPM :  \n CPM: \n \n", fill="white",
                                  font=(FONT_NAME, 15, "bold"), width=250
                                  )

window.mainloop()
