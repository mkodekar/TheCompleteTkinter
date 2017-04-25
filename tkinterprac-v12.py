
"""
@Dev Rehan Kodekar
@Date 2017-04-25
@Version 12
Photo and images
"""


from tkinter import *

root = Tk()
root.title('Image view')
photo = PhotoImage(fil='smileyface.png')
label = Label(root, image=photo)
label.pack()
root.mainloop()
