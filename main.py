from tkinter import filedialog
from tkinter import *
import m_transformations

def open_files():
    filename = filedialog.askopenfilenames(initialdir="/", title="Select file",
                                           filetypes=(("tif files", "*.tif"), ("all files", "*.*")))
    global path
    path = filename


def transform():
    global path
    m_transformations.transform(path)


root = Tk()
frame = Frame(root)
frame.pack()
global path
E1 = Entry(frame, bd=5)
E1.pack(side=LEFT)
B = Button(frame, text="browse", command=open_files)
R = Button(frame, text="run", command=transform)
B.pack()
R.pack()
frame.mainloop()

