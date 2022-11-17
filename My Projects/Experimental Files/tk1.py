import tkinter
import tkinter as tk
from tkinter.constants import COMMAND
wndw = tkinter.Tk()
wndw.title('Main Window')
btn=tk.Button(wndw,text='Close!',width=40,height=10,command=wndw.destroy)
btn.pack()
# Code to add widgets will go here...
wndw.mainloop()

