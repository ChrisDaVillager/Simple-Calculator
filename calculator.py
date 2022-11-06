# imports
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.constants import SUNKEN

root = Tk()

frame = tk.Frame(root, pady=25)
frame.grid()

tk.Label(frame, text='Hello! This will be a calculator').grid(column=0,row=0)
tk.Button(frame, text='Leave', command=root.destroy).grid(column=1,row=0)

root.mainloop()
