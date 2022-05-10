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
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    canvas.delete(ALL)
    canvas.create_text(103, 130, fill="white", text="25:00", font=(FONT_NAME, 35, "bold"))

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    countdown(25)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(minutes):
    canvas.update()
    canvas.delete(initial_display)
    while minutes > 0:
        seconds = 60
        minutes -= 1
        while seconds > 0:
            time.sleep(1)
            seconds -= 1
            # if less than 10 seconds, display the extra 0 ie; 00:09
            if seconds < 10:
                label = canvas.create_text(103, 130, fill="white", text=f"{minutes}:0{seconds}", font=(FONT_NAME, 35, "bold"))
                window.update()
                canvas.delete(label)
            else:
                label_2 = canvas.create_text(103, 130, fill="white", text=f"{minutes}:{seconds}", font=(FONT_NAME, 35, "bold"))
                window.update()
                canvas.delete(label_2)



# ---------------------------- UI SETUP ------------------------------- #
# Draw our window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BLUE)

# Create tomato background
canvas = Canvas(width=210, height=224, bg=BLUE, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
canvas.grid(row=1, column=1)

# Display countdown timer
initial_display = canvas.create_text(103, 130, text=f"{WORK_MIN}:00", fill="white", font=(FONT_NAME, 35, "bold"))

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