import time
import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *
from PIL import ImageTk, Image

kleuren = ['white', 'black']
ZettenGUI = []

window = tk.Tk()
window.title('Schaakbord')
window.geometry("800x800")
window.configure(bg='grey')
window.resizable(False, False)


schaakbordgui = tk.Frame(window, bg='brown')
schaakbordgui.pack()


schaakstukken = {'B-rook-1': [0, 0], 'B-knight-1': [0, 1], 'B-bishop-1': [0, 2], 'B-queen-1': [0, 3], 'B-king-1': [0, 4], 'B-bishop-2': [0, 5], 'B-knight-2': [0, 6], 'B-rook-2': [0, 7],
                    'B-pawn-1': [1, 0, 2], 'B-pawn-2': [1, 1, 2], 'B-pawn-3': [1, 2, 2], 'B-pawn-4': [1, 3, 2], 'B-pawn-5': [1, 4, 2], 'B-pawn-6': [1, 5, 2], 'B-pawn-7': [1, 6, 2], 'B-pawn-8': [1, 7, 2],
                    'W-rook-1': [7, 0], 'W-knight-1': [7, 1], 'W-bishop-1': [7, 2], 'W-queen-1': [7, 3], 'W-king-1': [7, 4], 'W-bishop-2': [7, 5], 'W-knight-2': [7, 6], 'W-rook-2': [7, 7],
                    'W-pawn-1': [6, 0, 2], 'W-pawn-2': [6, 1, 2], 'W-pawn-3': [6, 2, 2], 'W-pawn-4': [6, 3, 2], 'W-pawn-5': [6, 4, 2], 'W-pawn-6': [6, 5, 2], 'W-pawn-7': [6, 6, 2], 'W-pawn-8': [6, 7, 2]}


def resetpuntjes():
    global ZettenGUI
    for ding in ZettenGUI:
        ding.destroy()
    ZettenGUI = []

    # reset de puntjes^^


def move(e, item, row, column):
    if 'pawn' in item:
        schaakstukken[item][2] = 1
    # zorgt ervoor dat de pion alleen op de eerste zet 2 vakjes kan bewegen^^

    resetpuntjes()
    schaakstukken[item][0], schaakstukken[item][1] = row, column
    for _ in schaakstukken.keys():
        schaakstukken[item][-1].grid(row=schaakstukken[item][0], column=schaakstukken[item][1])

    # beweegt een stuk en reset het bord^^


def select(e, item):
    global ZettenGUI
    resetpuntjes()
    destroy = False
    if 'pawn' in item:
        for b in range(schaakstukken[item][2]):
            dot = tk.Label(schaakbordgui, image=img)
            if item[0:1] == 'B':
                dot.grid(row=(schaakstukken[item][0] + 1 + b), column=schaakstukken[item][1])
            else:
                dot.grid(row=(schaakstukken[item][0] - 1 - b), column=schaakstukken[item][1])
            ZettenGUI.append(dot)
            dot.bind('<1>', lambda e, item=item, row=dot.grid_info()['row'], column=dot.grid_info()['column']: move(e, item, row, column))
            for ding in schaakstukken.values():
                if dot.grid_info()['row'] == ding[0] and dot.grid_info()['column'] == ding[1]:
                    destroy = True
            if destroy:
                ZettenGUI[-1].destroy()

        for ding in schaakstukken.values():
            if item[0:1] == 'B':
                if ding[0] == schaakstukken[item][0] + 1 and ding[1] == schaakstukken[item][1] + 1 or ding[0] == schaakstukken[item][0] + 1 and ding[1] == schaakstukken[item][1] - 1:
                    dot = tk.Label(schaakbordgui, image=img)
                    dot.grid(row=ding[0], column=ding[1])
                    dot.bind('<1>', lambda e, item=item, row=dot.grid_info()['row'], column=dot.grid_info()['column']: move(e, item, row, column))
                    ZettenGUI.append(dot)
            if item[0:1] == 'W':
                if ding[0] == schaakstukken[item][0] - 1 and ding[1] == schaakstukken[item][1] + 1 or ding[0] == schaakstukken[item][0] - 1 and ding[1] == schaakstukken[item][1] - 1:
                    dot = tk.Label(schaakbordgui, image=img)
                    dot.grid(row=ding[0], column=ding[1])
                    dot.bind('<1>', lambda e, item=item, row=dot.grid_info()['row'], column=dot.grid_info()['column']: move(e,item, row,column))
                    ZettenGUI.append(dot)

            # maakt de puntjes aan voor waar een stuk heen kan bewegen^^


for i in range(8):
    for y in range(8):
        schaakvakje = tk.Label(schaakbordgui, bg=kleuren[y % 2])
        schaakvakje.grid(row=y, column=i, ipadx=47, ipady=40)
    kleuren.reverse()

    # maakt de wit en zwart gekleurde vakjes aan^^

for index, item in enumerate(schaakstukken.keys()):
    img = ImageTk.PhotoImage(Image.open(f"{item[:-2]}.png"))
    stuk = tk.Label(schaakbordgui, image=img)
    stuk.grid(row=schaakstukken[item][0], column=schaakstukken[item][1])
    stuk.bind('<1>', lambda e, item=item: select(e, item))
    schaakstukken[item].append(img), schaakstukken[item].append(stuk)

    # maakt alle stukken aan en voegt alles toe aan de DICT^^



img = ImageTk.PhotoImage(Image.open("Dot.png"))
window.mainloop()
