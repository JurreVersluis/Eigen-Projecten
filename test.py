import random
import tkinter as tk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.config(bg='grey')
window.geometry('500x300')
window.resizable(False, False)
window.title('Hangman')
input1 = tk.StringVar()
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def stelin():
    Doorgaan = True
    if 3 < len(input1.get()) < 8:
        for letter in input1.get():
            if letter.isnumeric():
                tk.messagebox.showinfo(title='Whoopsss..', message='Je kunt geen getallen invoeren.')
                Doorgaan = False
                break
        if Doorgaan:
            speelscherm()
    else:
        tk.messagebox.showinfo(title='Whoopsss..', message='Je kan alleen een woord van tussen de 4 en 7 letters invoeren.')


def startscherm():
    global punten, frame, input1, label, button, entry
    frame = tk.Frame(window, bg='grey')
    frame.place(relx=0.5, rely=0.5, anchor='center')

    label = tk.Label(frame, text='Kies uw woord 4 - 7 letters: ', font='Arial 16 bold', justify='center', fg='black', bg='grey')
    label.grid(row=0, column=0, pady=60)

    entry = tk.Entry(frame, textvariable=input1, font='Arial 12 bold', justify='center')
    entry.grid(row=1, column=0, ipadx=20, ipady=3)

    button = tk.Button(frame, text='Stel woord in', bg='#A9A9A9', command=stelin, font='Arial 12 bold', fg='black')
    button.grid(row=2, column=0, ipadx=20, ipady=1, pady=50)


def doeeengok():
    global punten, frame
    goedeletters, antwoord, = 0, None

    for index, letter in enumerate(input1.get().upper()):
        if letter == draaimolen[index].get().upper():
            goedeletters += 1

    punten -= (len(input1.get()) - goedeletters) * 2

    if goedeletters == len(input1.get()):
        antwoord = tk.messagebox.askyesno(title='Gewonnen!', message=f'Je hebt gewonnen! Je hebt {punten} punten behaald. Het woord was {input1.get()}. Wil je nog een keer spelen?')
    elif punten < 1:
        antwoord = tk.messagebox.askyesno(title='Gewonnen!', message=f'Je hebt Verloren!. Het woord was {input1.get()}. Wil je nog een keer spelen?')
    else:
        tk.messagebox.showinfo(title='Nog even door raden!', message=f'Je hebt {goedeletters} goede letters en dus {len(input1.get()) - goedeletters} fouten letters. Hierdoor verlies je {(len(input1.get()) - goedeletters) * 2} punten. Je hebt nog {punten} punten over.')
    if antwoord:
        frame.destroy()
        startscherm()
    elif antwoord == False:
        exit()


def speelscherm():
    global punten, frame, entry, draaimolen
    entry.destroy()

    punten, draaimolen = len(input1.get()) * len(input1.get()), []

    for index, letter in enumerate(input1.get()):
        letters = [letter.upper()]
        for i in range(4):
            letters.append(alphabet[random.randrange(0, len(alphabet))])
        random.shuffle(letters)
        letterVar = tk.StringVar()
        spinbox = tk.Spinbox(frame, values=letters, width=3, font='Arial 12 bold', justify='center', textvariable=letterVar, wrap=True, state='readonly')
        spinbox.grid(row=1, column=index, pady=60, ipady=3)
        draaimolen.append(letterVar)

    label.config(text='Raad het woord', font='Arial 20 bold', justify='center', fg='black', bg='grey')
    label.grid(row=0, column=0, columnspan=len(input1.get()), pady=0)

    button.config(text='Controleer!', bg='#A9A9A9', command=doeeengok, font='Arial 12 bold', fg='black')
    button.grid(pady=0, row=2, column=0, ipadx=20, ipady=1, columnspan=len(input1.get()))


startscherm()
window.mainloop()