"""
@Dev Rehan Kodekar
@Date 2017-04-24
@Version 03
Gridlayout
"""

from tkinter import *
root = Tk()
label_1 = Label(root, text='Name : ')
label_2 = Label(root, text='Password : ')
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, stick=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

check_1 = Checkbutton(root, text='Keep me signed in')
check_1.grid(columnspan=2)
root.mainloop()
