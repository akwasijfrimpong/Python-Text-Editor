import sys
from tkinter import *

root = Tk()
root.geometry("600x800")
root.minsize(height=560)
root.title("Akwasi Text Editor")

#scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill = Y)

#Menu
menubar = Menu(root)
fileMenu = Menu(menubar)
menubar.add_cascade(label="File", menu=fileMenu)

editMenu = Menu(menubar)
menubar.add_cascade(label="Edit", menu=editMenu)
root.config(menu=menubar)

fileMenu.add_command(label="Item")
fileMenu.add_command(label="Exit")
editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")

#title
frame = Frame(root, width=10, height = 160)
frame.pack()
title = Text(frame, background = 'Yellow', height=1.5)
title.insert(INSERT, "Title: ")
title.pack(side = TOP)

#text box
textbox = Text(root, yscrollcommand = scrollbar.set, undo=True)
textbox.pack(fill = BOTH, expand = True)


scrollbar.config(command=textbox.yview)

root.mainloop()