sfrom tkinter import *
from __main__ import *

def blank():
   filewin = Toplevel(base)
   button = Button(filewin, text="Close", command=filewin.destroy)
   button.pack()

menubar = Menu(base)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="1", command=blank)
filemenu.add_command(label="2", command=blank)
filemenu.add_command(label="3", command=blank)
filemenu.add_command(label="4", command=blank)
filemenu.add_command(label="5", command=blank)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=base.quit)

menubar.add_cascade(label="Fambox", menu=filemenu)
base.config(menu=menubar)
