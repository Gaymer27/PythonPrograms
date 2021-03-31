from tkinter import *
from tkinter import ttk

import tkinter as tk
import requests
import time
import json

frame_buttons = Tk()
frame_buttons.title("Minecraft Recourse Calculator")
frame_buttons.geometry("390x380")
frame_buttons.configure(background = "#c6c6c6")

frame = Frame(frame_buttons,bg="yellow")

b1 = Button(frame_buttons,text="1")


b1.grid(row = 0,column =0)


frame.grid_columnconfigure(0, weight=1)



frame_buttons.mainloop()
