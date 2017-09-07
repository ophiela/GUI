from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.ttk import *

root = Tk()
root.option_add('*tearOff', False)
menu = Menu(root)
root.config(menu = menu)
Quit = menu.add_command(label = 'Quit', command = root.destroy)
Font = Menu(menu)
Color = Menu(menu)
Size = Menu(menu)
doc = Text(root)
doc.place(anchor = NW)
default_font = font.Font(family = 'Times', size = 12)
doc.config(font = default_font)

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
    default_font.configure(family = 'Neuva')

def font_ver():
    default_font.configure(family = 'Verdana')

def font_courier():
    default_font.configure(family = 'Courier')

def font_sys():
    default_font.configure(family = 'System')

def font_italic():
    default_font.configure(slant = 'italic')

def font_roman():
    default_font.configure(slant = 'roman')

def font_15():
    default_font.configure(size = 15)


def font_20():
    default_font.configure(size = 20)   


menu.add_cascade(menu = Font, label = 'Font')
menu.add_cascade(menu = Color, label = 'Color')
menu.add_cascade(menu = Size, label = 'Size')
Size.add_command(label = '15', command = font_15)
Size.add_command(label = '20', command = font_20)
Font.add_command(label = 'Nueva', command = font_nueva)
Font.add_command(label = 'Verdana', command = font_ver)
Font.add_command(label = 'Courier', command = font_courier)
Font.add_command(label = 'System', command = font_sys)
Font.add_command(label = 'Italic', command = font_italic)
Font.add_command(label = 'Roman', command = font_roman)
Color.add_command(label = 'Red', command = color_red)
Color.add_command(label = 'Blue', command = color_blue)
Color.add_command(label = 'Orange', command = color_orange)
Color.add_command(label = 'Black', command = color_black)
