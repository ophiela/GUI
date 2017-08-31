from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import math
import random

root = Tk()
root.config(background = 'white')
root.option_add('tearOff', False)
top = Frame(root)
top.grid(sticky = N, column = 2)
style = ttk.Style(root)
style.configure('xpnative')



def help_fun():
    messagebox.showinfo('Help', 'Help message')


add = ttk.Button(root, text = '+',
                 command = help_fun).grid(row = 11, column = 3)
minus = ttk.Button(root, text = '-',
                   command = help_fun).grid(row = 12, column = 3)
multi = ttk.Button(root, text = 'x',
                   command = help_fun).grid(row = 13, column = 3)
minus = ttk.Button(root, text = '/',
                   command = help_fun).grid(row = 14, column = 3)
clear = ttk.Button(root,
                   text = 'Clear',
                   command = help_fun).grid(row = 15,column= 2,
                                            columnspan = 2, ipadx = 45)
one = ttk.Button(root, text = '1',
                 command = help_fun).grid(row = 11, column = 1)
two = ttk.Button(root, text = '2',
                 command = help_fun).grid(row = 11, column = 2)
three = ttk.Button(root, text = '3',
                   command = help_fun).grid(row = 12, column = 1)
four = ttk.Button(root, text = '4',
                  command = help_fun).grid(row = 12, column = 2)
five = ttk.Button(root, text = '5',
                  command = help_fun).grid(row = 13, column = 1)
six = ttk.Button(root, text = '6',
                 command = help_fun).grid(row = 13, column = 2)
seven = ttk.Button(root, text = '7',
                   command = help_fun).grid(row = 14, column = 1)
eight = ttk.Button(root, text = '8',
                   command = help_fun).grid(row = 14, column = 2)
nine = ttk.Button(root, text = '9',
                  command = help_fun).grid(row = 15, column = 1)
screen = Canvas(root, height = 100, width = 200)
screen.grid(row = 0,column = 1, sticky = N, columnspan = 3)
screen.config(background = 'white', borderwidth = 30)
#style.configure('TButton', foreground = 'red')
menu = Menu(root)
root.config(menu = menu)
menu.add_command(label = 'Quit', command = root.destroy)
menu.add_command(label = 'Help', command = help_fun)

#screen = Entry(top, textvariable= str )
#screen.focus_set()
#screen.grid(row = 0, column = 1)

mainloop()
