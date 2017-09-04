from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import time
from time import strftime
import math

root = Tk()
root.geometry('320x300')
state = 'on'

def quit():
    state = 'off'


root.option_add('*tearOff', False)
menu = Menu(root)
root.config(menu = menu)
menu.add_command(label = 'Quit', command = quit)

timeDisplay = Text(root)
timeDisplay.grid()
p = strftime('%I:%M:%S')
timeDisplay.insert(INSERT, p)
timeDisplay.config(font = 'Nueva 60', foreground = 'red')



