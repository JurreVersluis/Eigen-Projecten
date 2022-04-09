import time
import keyboard
import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os
import win32gui


window = tk.Tk()

window.title('Robs afk fishing paneel.')
window.geometry("400x400")
window.configure(bg='grey')

def disco():
   window.config(bg=random.choice(["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]))
   window.after(1, disco)




button1 = tk.Button(window, text='Disco!', bg='#A9A9A9', command=disco, font='Arial 12 bold')
button1.place(relx=0.5, rely=0.5, anchor='center')

window.mainloop()