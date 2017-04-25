"""
@Dev Rehan Kodekar
@Date 2017-04-24
@Version 01
Creating a window 
"""

from tkinter import *

root = Tk()
theLabel = Label(root, text='Gui application')
theLabel.pack()
root.geometry("400x300")

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button = Button(topFrame, text='Hey', bg='black', fg='red')
button2 = Button(topFrame, text='hi', bg='red', fg='blue')
button3 = Button(bottomFrame, text='hello', bg='orange', fg='yellow')
button.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=BOTTOM)
root.mainloop()
