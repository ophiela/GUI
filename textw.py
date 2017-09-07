from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

root = Tk()
root.option_add('*tearOff', False)
menu = Menu(root)
root.config(menu = menu)
Quit = menu.add_command(label = 'Quit', command = root.destroy)
Font = Menu(menu)
Color = Menu(menu)
doc = Text(root)
doc.place(anchor = NW)


#Commands
def color_red():
    doc.config(foreground = 'red')

def color_blue():
    doc.config(foreground = 'blue')

def color_orange():
    doc.config(foreground = 'orange')

def color_black():
    doc.config(foreground = 'black')

def font_nueva():
    doc.config(font = 'Nueva')

menu.add_cascade(menu = Font, label = 'Font')
menu.add_cascade(menu = Color, label = 'Color')
Font.add_command(label = 'Nueva', command = font_nueva)
Color.add_command(label = 'Red', command = color_red)
Color.add_command(label = 'Blue', command = color_blue)
Color.add_command(label = 'Orange', command = color_orange)
Color.add_command(label = 'Black', command = color_black)
