import tkinter
from tkinter import *
from PIL import Image, ImageTk
import time


def counter(time_left):
        if time_left > 0:
            hours = int(time_left / 3600) % 60
            minutes = int(time_left / 60) % 60
            seconds = time_left % 60
            time_counter_label.config(text=f'{hours:02d}:{minutes:02d}:{seconds:02d}')
            # Schedule the countdown function to be called after 1000ms (1 second)
            mainWindow.after(1000, counter, time_left - 1)
        else:
            print("finish")

def change(hours,minutes,seconds):
    time_counter_label.config(text=f'{hours}:{minutes}:{seconds}')

def timer_function_start():

    count_time = input_timer.get()
    hours_box = int(spin_box_time_hours.get()) * 3600
    minute_box = int(spin_box_time_minuts.get()) * 60
    second_box = int(spin_box_time_second.get())
    timer_sum = hours_box + minute_box + second_box

    counter(timer_sum)



    split_count = count_time.split(':')


    # counter(timer_sum)

    print("finish")


mainWindow = Tk()
mainWindow.minsize(300, 620)
timerImage = Image.open('img/timer.png')
timerImage = ImageTk.PhotoImage(timerImage)

label_name = tkinter.Label(text='Timer')
label_name.pack()
label_name.config(height=3, width=4, font=("Arial", 24))

image_label = tkinter.Label(mainWindow, image=timerImage)
image_label.config(height=220, width=200)
image_label.pack()

button_timer_start = tkinter.Button(text='Start', command=timer_function_start)
button_timer_start.config(width=4, height=2)
button_timer_start.pack(pady=8)

button_timer_stop = tkinter.Button(text='Stop')
button_timer_stop.config(width=4, height=2)
button_timer_stop.pack()

time_counter_label = tkinter.Label(text='00:00:00')
time_counter_label.config(font=('Arial', 22))
time_counter_label.pack(pady=10)

timer_label = tkinter.Label(mainWindow, text="Enter Time")
timer_label.config(height=3, width=7)
timer_label.pack()

input_timer = tkinter.Entry()
input_timer.pack()

list_time_hours = list(map(lambda x: x, range(0, 24 + 1)))
list_time_minit = list(map(lambda x: x, range(0, 60 + 1)))
list_time_second = list(map(lambda x: x, range(0, 60 + 1)))

spin_box_time_hours = tkinter.Spinbox(mainWindow, values=list_time_hours)
spin_box_time_hours.pack(side=tkinter.LEFT, padx=20)
spin_box_time_hours.config(width=3)
spin_box_time_minuts = tkinter.Spinbox(mainWindow, values=list_time_minit)
spin_box_time_minuts.pack(side=tkinter.LEFT, padx=20)
spin_box_time_minuts.config(width=3)
spin_box_time_second = tkinter.Spinbox(mainWindow, values=list_time_second)
spin_box_time_second.pack(side=tkinter.LEFT, padx=20)
spin_box_time_second.config(width=3)

mainWindow.mainloop()
