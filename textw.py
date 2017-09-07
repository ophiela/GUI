from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.ttk import *
#from functools import partial

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

def font_ver():
    doc.config(font = 'Verdana')

def font_courier():
    doc.config(font = 'Courier')

def font_times():
    doc.config(font = 'Times')

def font_italic():
    italic = font.Font(slant = 'italic')
    doc.config(font = italic)

def font_roman():
    roman = font.Font(slant = 'roman')
    doc.config(font = roman)

def font_15():
    s15 = font.Font(size = 15)
    doc.config(font = s15)

def font_20():
    s20 = font.Font(size = 20)
    doc.config(font = s20)
#    doc.config()

menu.add_cascade(menu = Font, label = 'Font')
menu.add_cascade(menu = Color, label = 'Color')
menu.add_cascade(menu = Size, label = 'Size')
Size.add_command(label = '15', command = font_15)
Size.add_command(label = '20', command = font_20)
Font.add_command(label = 'Nueva', command = font_nueva)
Font.add_command(label = 'Verdana', command = font_ver)
Font.add_command(label = 'Courier', command = font_courier)
Font.add_command(label = 'Times', command = font_times)
Font.add_command(label = 'Italic', command = font_italic)
Font.add_command(label = 'Roman', command = font_roman)
Color.add_command(label = 'Red', command = color_red)
Color.add_command(label = 'Blue', command = color_blue)
Color.add_command(label = 'Orange', command = color_orange)
Color.add_command(label = 'Black', command = color_black)
