#Calorie tracker
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import math


root = Tk()
root.option_add('tearOff', False)
root.geometry('130x130')
steps = Entry(root)
goal = Entry(root)
rsteps = Entry(root)
steps.grid(row = 1, column = 0, columnspan = 3)
steps.insert(INSERT, 'Steps Taken')
goal.grid(row = 2, column = 0, columnspan = 3)
goal.insert(INSERT, 'Calorie Goal')
rsteps.grid(row = 3, column = 0, columnspan = 3)
rsteps.insert(INSERT, 'Steps Left')


def get_help():
    messagebox.showinfo('Help', 'Please enter the number of steps walked')

def clear_step(event):
    steps.delete(0, END)

def clear_goal(event):
    goal.delete(0, END)

def reset():
    goal.delete(0, END)
    goal.insert(INSERT, 'Calorie Goal')
    steps.delete(0, END)
    steps.insert(INSERT, 'Steps Taken')
    rsteps.delete(0, END)
    rsteps.insert(INSERT, 'Steps Left')

def step_cal():
    value = steps.get()
    if value != 'Steps Taken':
        steps.delete(0, END)
        calories = int(value) / 20
        steps.insert(INSERT, calories)
        steps.place()
    else:
        steps.insert(INSERT, 'Invalid value')
    userGoal = goal.get()
    if userGoal != 'Calorie Goal':
        goal.delete(0, END)
        remainder = int(userGoal) - calories
        if remainder == 0:
            goal.insert(INSERT, 'You did it!')
            goal.place()
        else:
            remainder = str(remainder)
            goal.insert(INSERT, remainder +' calories left!')
            goal.place()
    rsteps.delete(0, END)
    re = float(remainder)
    moreSteps = (re * 20)
    if moreSteps == 0:
        rsteps.insert(INSERT, 'Take a break!')
    else:
        moreSteps = str(moreSteps)
        rsteps.insert(INSERT, moreSteps +' steps left!')
    
    
    

label_text = Label(root, text = 'Calorie Counter',
                   ).grid(row = 0, column = 1)
cal = ttk.Button(root, text = 'Calculate',
                 command = step_cal).grid(row = 5,
                                          column = 0, columnspan = 3)
steps.bind('<Button-1>', clear_step)
goal.bind('<Button-1>', clear_goal)
root.bind()
menu = Menu(root)
root.config(menu = menu)
menu.add_command(label = 'Quit', command = root.destroy)
menu.add_command(label = 'Help', command = get_help)
menu.add_command(label = 'Reset', command = reset)

mainloop()
