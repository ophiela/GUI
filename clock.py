from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
from time import *
import math


state = 'True'
root = Tk()
root.geometry('440x250')
timeDisplay = Text(root)
timeDisplay.grid()

def change_time():
    timeDisplay.delete(1.0,END)
    p = strftime('%I:%M:%S')
    timeDisplay.insert(INSERT, p)
    timeDisplay.config(font = 'Nueva 80', foreground = 'red')
    root.after(100, change_time)

state = 'on'
root.option_add('*tearOff', False)
menu = Menu(root)
root.config(menu = menu)
menu.add_command(label = 'Quit', command = root.destroy)
change_time()



root.mainloop()
