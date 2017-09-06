from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

root = Tk()
root.option_add('*tearOff', False)
menu = Menu(root)
root.config(menu = menu)
Quit = menu.add_command(label = 'Quit', command = root.destroy)
Font = Menu(menu)
doc = Text(root)
doc.place(anchor = NW)

#Commands
def color_change():
    doc.config(foreground = 'red')
    


menu.add_cascade(menu = Font, label = 'Font')
color = menu.add_command(label = 'Color', command = color_change)


