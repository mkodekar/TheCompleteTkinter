"""
@Dev Rehan Kodekar
@Date 2017-04-26
@Version 11
message box
"""


from tkinter import *
from tkinter import messagebox


class Window:

    def __init__(self, master):
        self.answe = ''
        rootFrame = Frame(master)
        master.title('Alert Message example')
        dialogButton = Button(rootFrame, text='Launch a dialogbox', fg='blue', bg='grey', command=self.showMesssage)
        dialogButton.pack(side=LEFT, padx=2, pady=2)
        yesNoDialog = Button(rootFrame, text='ask a question', fg='blue', bg='grey')
        yesNoDialog.pack(side=LEFT, padx=2, pady=2)
        print(self.answe)
        rootFrame.pack()

    def showMesssage(self):
        messagebox.showinfo('An Example', 'This shows and info')

    def askQuestionBox(self):
        asnswer = messagebox.askquestion('Asking a question', 'Is this dialog good ? ')
        return asnswer

root = Tk()
root.geometry("400x300")
mainWindow = Window(root)
root.mainloop()
