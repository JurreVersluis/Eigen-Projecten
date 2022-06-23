import time
import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *
from PIL import ImageTk, Image

kleuren = ['white', 'black']

window = tk.Tk()
window.title('Schaakbord')
window.geometry("800x800")
window.configure(bg='grey')
window.resizable(False, False)

schaakbordgui = tk.Frame(window, bg='brown')
schaakbordgui.pack()

spelersbord = tk.Frame(window, bg='blue')
spelersbord.pack()


def rook(event):
    print(item)
    print('test')


def knight(event):
    print('test1')


def bishop(event):
    print('test2')


def king(event, item):
    print('test3')


def queen(event, item):
    print('test4')


def bpawn(event, item):
    print('test5')

def wpawn(event, item):
    print('test6')


schaakstukken = {'B-rook-1': [0, 0, rook], 'B-knight-1': [0, 1, knight], 'B-bishop-1': [0, 2, bishop], 'B-queen-1': [0, 3, queen], 'B-king-1': [0, 4, king], 'B-bishop-2': [0, 5, bishop], 'B-knight-2': [0, 6, knight], 'B-rook-2': [0, 7, rook],
                    'B-pawn-1': [1, 0, bpawn], 'B-pawn-2': [1, 1, bpawn], 'B-pawn-3': [1, 2, bpawn], 'B-pawn-4': [1, 3, bpawn], 'B-pawn-5': [1, 4, bpawn], 'B-pawn-6': [1, 5, bpawn], 'B-pawn-7': [1, 6, bpawn], 'B-pawn-8': [1, 7, bpawn],
                    'W-rook-1': [7, 0, rook], 'W-knight-1': [7, 1, knight], 'W-bishop-1': [7, 2, bishop], 'W-queen-1': [7, 3, queen], 'W-king-1': [7, 4, king], 'W-bishop-2': [7, 5, bishop], 'W-knight-2': [7, 6, knight], 'W-rook-2': [7, 7, rook],
                    'W-pawn-1': [6, 0, wpawn], 'W-pawn-2': [6, 1, wpawn], 'W-pawn-3': [6, 2, wpawn], 'W-pawn-4': [6, 3, wpawn], 'W-pawn-5': [6, 4, wpawn], 'W-pawn-6': [6, 5, wpawn], 'W-pawn-7': [6, 6, wpawn], 'W-pawn-8': [6, 7, wpawn]}

def test(event):
    print(event)




for i in range(8):
    for y in range(8):
        schaakvakje = tk.Label(schaakbordgui, bg=kleuren[y % 2])
        schaakvakje.grid(row=y, column=i, ipadx=47, ipady=40)

    kleuren.reverse()

for index, item in enumerate(schaakstukken.keys()):
    img = ImageTk.PhotoImage(Image.open(f"{item[:-2]}.png"))
    plaatje = tk.Label(schaakbordgui, image=img)
    plaatje.grid(row=schaakstukken[item][0], column=schaakstukken[item][1])
    #plaatje.bind('<1>', schaakstukken[item][2])
    schaakstukken[item].append(img)


label1 = tk.Label(spelersbord, text='Player1:', font='Arial 20', justify='center', fg='white', bg='#58544c')
label1.grid(row=0, column=0)

label2 = tk.Label(spelersbord, text='Player2:', font='Arial 20', justify='center', fg='white', bg='#58544c')
label2.grid(row=0, column=5)




window.mainloop()
