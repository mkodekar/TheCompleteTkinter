"""
@Dev Rehan Kodekar
@Date 2017-04-25
@Version 09
Creating a drop down menu
"""

from tkinter import *


class Window:
    def __init__(self, master):
        frame = Frame(master,  width=400, height=300)
        master.title('Python Like menu')
        frame.pack()
        mainMenu = Menu(master)
        master.config(menu=mainMenu)
        fileMenu = Menu(mainMenu)
        mainMenu.add_cascade(label='File', menu=fileMenu)
        fileMenu.add_command(label='New Project...', command=self.doNothing)
        fileMenu.add_command(label='New...', command=self.doNothing)
        fileMenu.add_command(label='New Scratch File', command=self.doNothing)
        fileMenu.add_command(label='Open', command=self.doNothing)
        fileMenu.add_separator()
        editMenu= Menu(fileMenu)
        fileMenu.add_cascade(label='Edit', menu=editMenu)
        editMenu.add_command(label='Choose Project', command=self.doNothing)
        fileMenu.add_command(label='Settings', command=self.doNothing)
        fileMenu.add_command(label='Exit', command=frame.quit)
        self.initToolbar(master)



    def doNothing(self):
        print('Print somethong')

    def initToolbar(self, master):
        toolbar = Frame(master, bg='black')
        insertButton = Button(toolbar, text='Insert a image', command=self.doNothing)
        insertButton.pack(side=LEFT, padx=2, pady=2)
        printButton = Button(toolbar, text='Print', command=self.doNothing)
        printButton.pack(side=LEFT, padx=2, pady=2)
        toolbar.pack(side=TOP, fill=X)

root = Tk()
mainWindow = Window(root)
root.mainloop()
