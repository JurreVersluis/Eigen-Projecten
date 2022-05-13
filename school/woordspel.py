import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *

window = tk.Tk()
window.config(bg='grey')
window.geometry('500x300')
window.resizable(False, False)
window.title('Hangman')
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def stelin():
    Doorgaan = True
    if 3 < len(input1.get()) < 8:

        for letter in input1.get():
            if letter == '1' or letter == '2' or letter == '3' or letter == '4' or letter == '5' or letter == '6' or letter == '7' or letter == '8' or letter == '9' or letter == '0':
                tk.messagebox.showinfo(title='Whoopsss..', message='Je kunt geen getallen invoeren.')
                Doorgaan = False
                break

        if Doorgaan:
            frame1.destroy()
            speelscherm()
    else:
        tk.messagebox.showinfo(title='Whoopsss..', message='Je kan alleen een woord van tussen de 4 en 7 letters invoeren.')


def startscherm():
    global input1, frame1
    frame1 = tk.Frame(window, bg='grey')
    frame1.place(relx=0.5, rely=0.5, anchor='center')

    label1 = tk.Label(frame1, text='Kies uw woord 4 - 7 letters: ', font='Arial 16 bold', justify='center', fg='black', bg='grey')
    label1.grid(row=0, column=0, pady=60)

    input1 = tk.StringVar()
    entry1 = ttk.Entry(frame1, textvariable=input1, font='Arial 12 bold', justify='center')
    entry1.grid(row=1, column=0, ipadx=20, ipady=3)

    button1 = tk.Button(frame1, text='Stel woord in', bg='#A9A9A9', command=stelin, font='Arial 12 bold', fg='black')
    button1.grid(row=2, column=0, ipadx=20, ipady=1, pady=50)


def doeeengok():
    global punten
    echtewoord = input1.get().upper()
    geradenwoord = spinbox1var.get() + spinbox2var.get() + spinbox3var.get() + spinbox4var.get() + spinbox5var.get() + spinbox6var.get() + spinbox7var.get()
    counter1 = 0
    goedeletters = 0
    for letter in geradenwoord:
        if letter == echtewoord[counter1:counter1 + 1]:
            goedeletters += 1
        counter1 += 1
    fouteletters = (len(input1.get()) - goedeletters)
    punten -= fouteletters * 2
    if echtewoord == geradenwoord:
        antwoord = tk.messagebox.askyesno(title='Gewonnen!', message=f'Je hebt gewonnen! Het woord was {echtewoord}. Je hebt {punten} punten behaald. Wil je nog een keer spelen?')
        if antwoord:
            frame2.destroy()
            startscherm()
        else:
            exit()
    elif punten < 1:
        antwoord = tk.messagebox.askyesno(title='Gewonnen!', message=f'Je hebt Verloren! Het woord was {echtewoord}. Wil je nog een keer spelen?')
        if antwoord:
            frame2.destroy()
            startscherm()
        else:
            exit()
    else:
        tk.messagebox.showinfo(title='Nog even door raden!', message=f'Je hebt {goedeletters} goede letters en dus {fouteletters} fouten letters. Hierdoor verlies je {fouteletters * 2} punten. Je hebt nog {punten} punten over.')


def speelscherm():
    global spinbox1var, spinbox3var, spinbox2var, spinbox4var, spinbox5var, spinbox6var, spinbox7var, frame2, punten
    lengtewoord = len(input1.get())
    punten = lengtewoord * lengtewoord
    spinbox1var = tk.StringVar()
    spinbox2var = tk.StringVar()
    spinbox3var = tk.StringVar()
    spinbox4var = tk.StringVar()
    spinbox5var = tk.StringVar()
    spinbox6var = tk.StringVar()
    spinbox7var = tk.StringVar()
    draaimolen = [[], [], [], [], [], [], []]

    counter = 0
    for letter in input1.get():
        draaimolen[counter].append(letter.upper())
        counter += 1
    for b in range(lengtewoord):
        for i in range(4):
            randomgetal = random.randrange(0, len(alphabet))
            draaimolen[b].append(alphabet[randomgetal])
        random.shuffle(draaimolen[b])

    frame2 = tk.Frame(window, bg='grey')
    frame2.place(relx=0.5, rely=0.5, anchor='center')

    label2 = tk.Label(frame2, text='Raad het woord ', font='Arial 20 bold', justify='center', fg='black', bg='grey')
    label2.grid(row=0, column=0, columnspan= lengtewoord)

    spinbox1 = tk.Spinbox(frame2, values=draaimolen[0], width=3, font='Arial 12 bold', justify='center', textvariable=spinbox1var)
    spinbox1.grid(row=1, column=0, pady=60, ipady=3)
    spinbox1['state'] = 'readonly'

    spinbox2 = tk.Spinbox(frame2, values=draaimolen[1], width=3, font='Arial 12 bold', justify='center', textvariable=spinbox2var)
    spinbox2.grid(row=1, column=1, pady=60, ipady=3)
    spinbox2['state'] = 'readonly'

    spinbox3 = tk.Spinbox(frame2, values=draaimolen[2], width=3, font='Arial 12 bold', justify='center', textvariable=spinbox3var)
    spinbox3.grid(row=1, column=2, pady=60, ipady=3)
    spinbox3['state'] = 'readonly'

    spinbox4 = tk.Spinbox(frame2,values=draaimolen[3], width=3, font='Arial 12 bold', justify='center', textvariable=spinbox4var)
    spinbox4.grid(row=1, column=3, pady=60, ipady=3)
    spinbox4['state'] = 'readonly'

    if lengtewoord > 4:
        spinbox5 = tk.Spinbox(frame2, values=draaimolen[4], width=3, font='Arial 12 bold', justify='center', textvariable=spinbox5var)
        spinbox5.grid(row=1, column=4, pady=60, ipady=3)
        spinbox5['state'] = 'readonly'
    if lengtewoord > 5:
        spinbox6 = tk.Spinbox(frame2, values=draaimolen[5], width=3, font='Arial 12 bold', justify='center', textvariable=spinbox6var)
        spinbox6.grid(row=1, column=5, pady=60, ipady=3)
        spinbox6['state'] = 'readonly'
    if lengtewoord > 6:
        spinbox7 = tk.Spinbox(frame2, values=draaimolen[6], width=3, font='Arial 12 bold', justify='center', textvariable=spinbox7var)
        spinbox7.grid(row=1, column=6, pady=60, ipady=3)
        spinbox7['state'] = 'readonly'

    button2 = tk.Button(frame2, text='Stel woord in', bg='#A9A9A9', command=doeeengok, font='Arial 12 bold', fg='black')
    button2.grid(row=2, column=0, ipadx=20, ipady=1, columnspan= lengtewoord)


startscherm()
window.mainloop()