import time
import keyboard
import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os
import win32gui


window = tk.Tk()

x = 0
y = 400

window.title('Robs afk fishing paneel.')
window.geometry("400x400")
window.configure(bg='grey')

label1 = tk.Label(window, bg='black')
label1.place(x=0, y=400, width=200,height=200)

def w(t=None):
    global y
    global x
    y -= 5
    label1.place(x=x, y=y)

def a(t=None):
    global y
    global x
    x -= 5
    label1.place(x=x, y=y)

def s(t=None):
    global y
    global x
    y += 5
    label1.place(x=x, y=y)


def d(t=None):
    global y
    global x
    x += 5
    label1.place(x=x, y=y)


window.bind('w', w)
window.bind('a', a)
window.bind('s', s)
window.bind('d', d)

window.mainloop()