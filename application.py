from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import math
import random

#the set up

root = Tk()
root.config(background = 'white')
root.option_add('tearOff', False)
top = Frame(root)
top.grid(sticky = N, column = 2)
style = ttk.Style(root)
style.configure('xpnative')
screen = Canvas(root, height = 100, width = 200)
screen.grid(row = 0,column = 1, sticky = N, columnspan = 3)
screen.config(background = 'white', borderwidth = 30)
number = Entry(root)
numbers = ['0','1', '2', '3', '4','5','6','7','8','9']
value = 'n'
operation = 'n'


#commands

def help_fun():
    messagebox.showinfo('Help', 'Please use Quit to exit. There is no saving.')

def zero():
    global value
    if value == 'n':
        value = numbers[0]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[0]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def one():
    global value
    if value == 'n':
        value = numbers[1]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[1]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def two():
    global value
    if value == 'n':
        value = numbers[2]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[2]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def three():
    global value
    if value == 'n':
        value = numbers[3]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[3]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def four():
    global value
    if value == 'n':
        value = numbers[4]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[4]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def five():
    global value
    if value == 'n':
        value = numbers[5]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[5]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def six():
    global value
    if value == 'n':
        value = numbers[6]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[6]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def seven():
    global value
    if value == 'n':
        value = numbers[7]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[7]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def eight():
    global value
    if value == 'n':
        value = numbers[8]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[8]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def nine():
    global value
    if value == 'n':
        value = numbers[9]
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)
        value = value + numbers[9]
        number.insert(INSERT, value)
        number.place(anchor = NW)

def clear():
    global value
    number.delete(0, END)
    value = 'n'

def square():
    global value
    if value != 'n':
        number.delete(0, END)
        value = int(value) * int(value)
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)

def power ():
    global value
    if value != 'n':
        number.delete(0, END)
        value = value + '^'
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)

def plus ():
    global value
    if value != 'n':
        number.delete(0, END)
        value = value + ' + '
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)

def minus ():
    global value
    if value != 'n':
        number.delete(0, END)
        value = value + ' - '
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)

def multi ():
    global value
    if value != 'n':
        number.delete(0, END)
        value = value + ' x '
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)

def div ():
    global value
    if value != 'n':
        number.delete(0, END)
        value = value + ' / '
        number.insert(INSERT, value)
        number.place(anchor = NW)
    else:
        number.delete(0, END)

def enter():
    global value
    if value != 'n':
        number.delete(0, END)
        if value.find('+') != -1:
            num = value.partition('+')
            result = int(num[0]) + int(num[2])
            number.insert(INSERT, result)
            number.place(anchor = NW)
            value = str(result)
        elif value.find('-') != -1:
            num = value.partition('-')
            result = int(num[0]) - int(num[2])
            number.insert(INSERT, result)
            number.place(anchor = NW)
            value = str(result)
        elif value.find('x') != -1:
            num = value.partition('x')
            result = int(num[0]) * int(num[2])
            number.insert(INSERT, result)
            number.place(anchor = NW)
            value = str(result)
        elif value.find('/') != -1:
            num = value.partition('/')
            result = int(num[0]) / int(num[2])
            number.insert(INSERT, result)
            number.place(anchor = NW)
            value = str(result)
        elif value.find('^') != -1:
            num = value.partition('^')
            result = int(num[0]) ** int(num[2])
            number.insert(INSERT, result)
            number.place(anchor = NW)
            value = str(result)
        else:
            number.delete(0, END)
    else:
        number.delete(0, END)

#Buttons
    
add = ttk.Button(root, text = '+',
                 command = plus).grid(row = 11, column = 3)
minus = ttk.Button(root, text = '-',
                   command = minus).grid(row = 12, column = 3)
multi = ttk.Button(root, text = 'x',
                   command = multi).grid(row = 13, column = 3)
minus = ttk.Button(root, text = '/',
                   command = div).grid(row = 14, column = 3)
clear = ttk.Button(root,
                   text = 'Clear',
                   command = clear).grid(row = 16,column= 2)
one = ttk.Button(root, text = '1',
                 command = one).grid(row = 11, column = 1)
two = ttk.Button(root, text = '2',
                 command = two).grid(row = 11, column = 2)
three = ttk.Button(root, text = '3',
                   command = three).grid(row = 12, column = 1)
four = ttk.Button(root, text = '4',
                  command = four).grid(row = 12, column = 2)
five = ttk.Button(root, text = '5',
                  command = five).grid(row = 13, column = 1)
six = ttk.Button(root, text = '6',
                 command = six).grid(row = 13, column = 2)
seven = ttk.Button(root, text = '7',
                   command = seven).grid(row = 14, column = 1)
eight = ttk.Button(root, text = '8',
                   command = eight).grid(row = 14, column = 2)
nine = ttk.Button(root, text = '9',
                  command = nine).grid(row = 15, column = 1)
zero = ttk.Button(root, text = '0',
                  command = zero).grid(row = 15, column = 2)
square = ttk.Button(root, text = 'Sqr',
                  command = square).grid(row = 15, column = 3)
pwr = ttk.Button(root, text = 'PWR',
                  command = power).grid(row = 16, column = 1)
enter = ttk.Button(root, text = 'Enter',
                  command = enter).grid(row = 16, column = 3)
#style.configure('TButton', foreground = 'red')
menu = Menu(root)
root.config(menu = menu)
menu.add_command(label = 'Quit', command = root.destroy)
menu.add_command(label = 'Help', command = help_fun)



#screen = Entry(top, textvariable= str )
#screen.focus_set()
#screen.grid(row = 0, column = 1)

mainloop()
