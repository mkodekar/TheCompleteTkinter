"""
@Dev Rehan Kodekar
@Date 2017-04-24
@Version 03
Gui with classes
"""

from tkinter import *


class MyGuiApp:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.printButton = Button(frame, text='Print message', command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text='Quit button', command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print('Print button clicked')


root = Tk()
myGuiApp = MyGuiApp(root)
root.mainloop()
