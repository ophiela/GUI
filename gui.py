from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
root = Tk()
root.config(background = 'grey')
style = Style(root)
style.configure('TButton', font='Nueva 14',foreground='maroon', padding=15)
style.configure('.', background = 'white')
#Create Menu
root.option_add('*tearOff', False)
menu = Menu(root)
root.config(menu = menu)
File = Menu(menu)
menu.add_cascade(menu = File, label = 'File')
File.add_command(label = 'New', command = lambda: print('new file'))
File.add_separator()
File.add_command(label = 'Open...', command = lambda: print('Open...'))
File.add_separator()
File.add_command(label = 'Save', command = lambda: print('Saving'))
File.entryconfig('New', accelerator = 'Ctrl + N')
File.entryconfig('Open...', accelerator = 'Ctrl + O')
File.entryconfig('Save', accelerator = 'Ctrl + S')


#create navigate tool menu and canvas
navigate = ttk.Frame(root)
navigate.grid(row = 0, column = 0, sticky = 'nesw')
navigate.config(height = 640, width = 300, relief = GROOVE)
navigate.config(padding = (15, 15))
ttk.Button(navigate, text = 'Clear').grid(padx = 15, pady = 15)
ttk.Button(navigate, text = 'Button').grid(padx = 15, pady = 15)
drawPad = Canvas(root)
drawPad.grid(row = 1, column = 1)
#drawPad.config(expand = YES)
drawPad.config(height = 540, width = 680)
scrollbar = ttk.Scrollbar(root, orient = VERTICAL)
scrollbar.grid( row = 3, column = 1, sticky = 'ns')
drawPad.create_line(160, 280, 450, 560, fill = 'blue')
root.mainloop()
