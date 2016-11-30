from tkinter import *
from __main__ import *

def blank():
   filewin = Toplevel(base)
   button = Button(filewin, text="Close", command=filewin.destroy)
   button.pack()

menubar = Menu(base)

firstmenu = Menu(menubar, tearoff=0)
firstmenu.add_command(label="1", command=blank)
firstmenu.add_command(label="2", command=blank)
firstmenu.add_command(label="3", command=blank)
firstmenu.add_command(label="4", command=blank)
firstmenu.add_command(label="5", command=blank)
firstmenu.add_separator()
firstmenu.add_command(label="Exit", command=base.quit)

secondmenu = Menu(menubar, tearoff=0)
secondmenu.add_command(label="1", command=blank)
secondmenu.add_command(label="2", command=blank)
secondmenu.add_command(label="3", command=blank)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Credits", command=blank)
helpmenu.add_command(label="Guide", command=blank)
helpmenu.add_command(label="Report a bug", command=blank)

menubar.add_cascade(label="Fambox", menu=firstmenu)
menubar.add_cascade(label="Test", menu=secondmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

base.config(menu=menubar)
