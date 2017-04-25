from tkinter import *


class Drawings:
    def __init__(self, master):
        frame = Frame(master, width=400, height=300)
        frame.pack()
        can = Canvas(frame, width=200, height=100)
        black_line = can.create_line(0, 0, 200, 50)
        red_line = can.create_line(0, 100, 200, 50, fill='red')
        greenBox = can.create_rectangle(25, 25, 130, 60, fill='green')
        can.delete(red_line)
        can.pack()


root = Tk()
root.title('Shapes and drawings')
drawing = Drawings(root)
root.mainloop()
