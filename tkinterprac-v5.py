"""
@Dev Rehan Kodekar
@Date 2017-04-24
@Version 05
binding functions to ui part 2
"""

from tkinter import *


def printname(event):
    print('Hello my name is {}'.format('Rehan'))


root = Tk()

button = Button(root, text='Click to print your name', bg='red', fg='white')

#here <Button-1> is the right mouse button
button.bind("<Button-1>", printname)
button.pack()
root.mainloop()
