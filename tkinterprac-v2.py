"""
@Dev Rehan Kodekar
@Date 2017-04-24
@Version 02
Setting up widgets
"""

from tkinter import *

root = Tk()
theLabel = Label(root, text='Gui application 2')
theLabel.pack()
root.geometry("400x300")

button = Label(text='Hey', bg='black', fg='red')
button2 = Label(text='hi', bg='red', fg='blue')
button3 = Label(text='hello', bg='orange', fg='yellow')
button.pack()
button2.pack(fill=X)
button3.pack(side=LEFT, fill=Y)
root.mainloop()
