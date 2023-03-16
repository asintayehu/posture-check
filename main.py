import tkinter as tk
import time
from playsound import playsound

window = tk.Tk()
window.geometry("907x485")

minutes, hours, seconds, tick_count = 0, 0, 0, 0
tick_total = 0


def update_timer():
    global minutes, hours, seconds, tick_count, tick_total
    seconds += 1
    tick_count += 1
    if tick_count >= 100:
        tick_total += 1
        playsound('Dramatic Vine-Instagram Boom - Sound Effect (HD).mp3')
        tick_count = 0
    if seconds >= 60:
        minutes += 1
        seconds = 0
    if minutes >= 60:
        minutes = 0
        hours += 1

    timer_label.config(text=f'{hours:02d}:{minutes:02d}:{seconds:02d}\n\nTICK COUNT: {tick_total}')
    window.after(1000, update_timer)


timer_label = tk.Label(window, text='00:00:00\n\nTICK COUNT: 0', font='Calibri, 20')
timer_label.pack(pady=20)

window.after(1000, update_timer)

window.mainloop()
