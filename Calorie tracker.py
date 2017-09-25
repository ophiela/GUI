#Calorie tracker
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import math

root = Tk()
root.option_add('tearOff', False)
root.geometry('90x90')
steps = Entry(root)
goal = Entry(root)
steps.grid(row = 1, column = 0, columnspan = 3)
steps.insert(INSERT, 'Steps Taken')
goal.grid(row = 2, column = 0, columnspan = 3)
goal.insert(INSERT, 'Calorie Goal')


def get_help():
    messagebox.showinfo('Help', 'Please enter the number of steps walked')

def step_cal():
    value = steps.get()
    steps.delete(0, END)
    calories = int(value) / 20
    steps.insert(INSERT, calories)
    steps.place()
    userGoal = goal.get()
    goal.delete(0, END)
    remainder = int(userGoal) - calories
    remainder = str(remainder)
    goal.insert(INSERT, remainder +' calories left!')
    goal.place()
    
    
    

label_text = Label(root, text = 'Calorie Counter',
                   ).grid(row = 0, column = 1)
cal = ttk.Button(root, text = 'Calculate',
                 command = step_cal).grid(row = 4,
                                          column = 0, columnspan = 3)
menu = Menu(root)
root.config(menu = menu)
menu.add_command(label = 'Quit', command = root.destroy)
menu.add_command(label = 'Help', command = get_help)

mainloop()
