import tkinter
from tkinter import *
from PIL import Image,ImageTk

mainWindow = Tk()
mainWindow.minsize(300,500)
timerImage = Image.open('img/timer.png')
timerImage = ImageTk.PhotoImage(timerImage)

label_name = tkinter.Label(text='Timer')
label_name.pack()
label_name.config(height=3,width=4,font=("Arial",24))

image_label = tkinter.Label(mainWindow,image=timerImage)
image_label.config(height=220,width=200)
image_label.pack()

timer_label = tkinter.Label(mainWindow,text = "Enter Time")
timer_label.config(height=3,width=7)
timer_label.pack()

input_timer = tkinter.Entry()
input_timer.pack()

button_timer_start = tkinter.Button(text = 'Start')
button_timer_start.config(width=4,height = 2)
button_timer_start.pack(pady=8)

button_timer_stop = tkinter.Button(text = 'Stop')
button_timer_stop.config(width=4,height=2)
button_timer_stop.pack()


mainWindow.mainloop()