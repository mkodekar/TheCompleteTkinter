"""
@Dev Rehan Kodekar
@Date 2017-04-24
@Version 04
binding functions to ui
"""

from tkinter import *


def printname():
    print('Hello my name is {}'.format('Rehan'))


root = Tk()

button = Button(root, text='Click to print your name', bg='red', fg='white', command=printname)
button.pack()
root.mainloop()
