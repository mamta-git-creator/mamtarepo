
import tkinter as tk
from time import strftime


def update_clock():
    current_time = strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_clock)


root = tk.Tk()
root.title("Experience Clock")
root.geometry("400x220")
root.configure(bg="#111827")

title_label = tk.Label(
    root,
    text="8 Years Experience",
    font=("Arial", 24, "bold"),
    fg="#F9FAFB",
    bg="#111827",
)
title_label.pack(pady=(20, 10))

clock_label = tk.Label(
    root,
    text="",
    font=("Arial", 40, "bold"),
    fg="#34D399",
    bg="#111827",
)
clock_label.pack()

status_label = tk.Label(
    root,
    text="Professional Experience",
    font=("Arial", 16),
    fg="#93C5FD",
    bg="#111827",
)
status_label.pack(pady=(10, 0))

update_clock()
root.mainloop()