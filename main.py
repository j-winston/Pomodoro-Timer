from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
MAROON = "#A9294F"
BLUE = "#6F9EAF"
BROWN = "#C7753D"
BEIGE = "#F6D887"

# ----Angela's --------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    REPS = 0
    canvas.itemconfig(timer_display, text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    if REPS % 8 == 0:
        timer_label.config(text="Break", fg=BEIGE)
        countdown(LONG_BREAK_MIN * 60)
    elif REPS % 2 == 0:
        timer_label.config(text="Break", fg=GREEN)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Working", fg=MAROON)
        countdown(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    # -----REFACTOR----- #
    minutes = count // 60
    seconds = count % 60
    # To display :00 correctly
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_display, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Draw our window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BLUE)

# Create tomato background
canvas = Canvas(width=250, height=250, bg=BLUE, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
canvas.grid(row=1, column=1)

# Display countdown timer
timer_display = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# Draw 'Timer' label
timer_label = Label(text="Timer", font=(FONT_NAME, 36))
timer_label.grid(row=0, column=1)

# Change background and font color
timer_label.config(bg=BLUE, fg=BEIGE)

# Draw start and Reset Buttons
start_button = Button(text="Start", borderwidth=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", borderwidth=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Draw checkmarks
check_mark = Label(text="✔", fg=MAROON, bg=BLUE, font=("courier", 33, "bold"))
check_mark.grid(row=3, column=1)

window.mainloop()
