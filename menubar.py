from tkinter import *
from __main__ import *

def blank():
   filewin = Toplevel(base)
   button = Button(filewin, text="Do nothing button", command=filewin.destroy)
   button.pack()

menubar = Menu(base)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=blank)
filemenu.add_command(label="Open", command=blank)
filemenu.add_command(label="Save", command=blank)
filemenu.add_command(label="Save as...", command=blank)
filemenu.add_command(label="Close", command=blank)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=base.quit)

menubar.add_cascade(label="File", menu=filemenu)
base.config(menu=menubar)