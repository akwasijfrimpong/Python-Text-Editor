import sys
from tkinter import *
def exit():
    root.destroy()

def save():
    filename = title.get('1.0','end')
    filename = filename.strip() + '.txt'
    print(filename)
    output = open(filename +'.txt', 'w')
    text = textbox.get('1.0','end')
    output.write(text)
    output.write("hello world")

    print(text)


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

fileMenu.add_command(label="Save", command=save)
fileMenu.add_command(label="Exit", command=exit)
editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")

#title
frame = Frame(root, width=10, height = 160)
frame.pack()
title = Text(frame, background = 'Yellow', height=1.5)
title.pack(side = TOP)

#text box
textbox = Text(root, yscrollcommand = scrollbar.set, undo=True)
textbox.pack(fill = BOTH, expand = True)


scrollbar.config(command=textbox.yview)

root.mainloop()
