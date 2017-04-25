"""
@Dev Rehan Kodekar
@Date 2017-04-24
@Version 05
mouse click events
"""

from tkinter import *

root = Tk()

def leftmouseClick(event):
    print('Left mouse click')

def rightmouseClick(event):
    print('Right mouse click')

def middlemouseClick(event):
    print('middle mouse click')

basicFrame = Frame(root, width=300, height=250)
basicFrame.bind("<Button-1>", leftmouseClick)
basicFrame.bind("<Button-2>", middlemouseClick)
basicFrame.bind("<Button-3>", rightmouseClick)

basicFrame.pack()
root.mainloop()
