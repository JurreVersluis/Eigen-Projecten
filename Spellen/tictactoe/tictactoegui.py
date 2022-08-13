import tkinter as tk
from tkinter import messagebox
from tkinter import *

nummers = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6], [0, 4, 8]]
counter2 = 0
window = tk.Tk()
window.title('Tic-Tac-Toe')
window.configure(bg='#4D5057')
window.resizable(False, False)


def score():
    global counter2, label, scroll_bar, scroll_bar2
    counter2 += 1
    if counter2 % 2 == 1:
        label = Listbox(speelscherm, width=1, height=1, font='Arial 14')
        label.grid(row=0, column=0, ipadx=200, ipady=220, pady=0, columnspan=3, rowspan=3)

        scroll_bar = tk.Scrollbar(label)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_bar.config(command=label.yview)

        scroll_bar2 = tk.Scrollbar(label, orient='horizontal')
        scroll_bar2.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_bar2.config(command=label.xview)
    else:
        label.destroy(), scroll_bar.destroy(), scroll_bar2.destroy()


def eindspel(einden):
    informatie.destroy()
    window.geometry("611x730")
    winnaar = tk.Label(speelscherm, text=einden, font='Arial 25 bold', justify='center', fg='#E1D9D1', bg='#4D5057')
    winnaar.grid(row=3, column=0, columnspan=3, pady=13)
    scorebutton = tk.Button(speelscherm, text="Score", command=score, bg='#ff726f', width=15, height=2, font='Arial 11 bold')
    scorebutton.grid(row=4, column=0, pady=7)
    retrybutton = tk.Button(speelscherm, text="Retry", command=lambda: startgame(True), bg='#F2AF29', width=15, height=2, font='Arial 11 bold')
    retrybutton.grid(row=4, column=1, pady=7)
    homescreenbutton = tk.Button(speelscherm, text="Home screen", command=lambda: homescreen(True), bg='#B4CC00', width=15, height=2, font='Arial 11 bold')
    homescreenbutton.grid(row=4, column=2, pady=7)


def switch():
    global counter1
    counter1 += 1
    if counter1 % 2 == 0:
        namen['naam1'][2].set(namen['naam1'][0]), namen['naam2'][2].set(namen['naam2'][0])
    else:
        namen['naam1'][2].set(namen['naam2'][0]), namen['naam2'][2].set(namen['naam1'][0])


def algewonnen(number1, number2, number3):
    if not Hetbord[number1].get() == '-':
        if Hetbord[number1].get() == Hetbord[number2].get() == Hetbord[number3].get():
            eindspel(' 🏆 | ' + namen[f'naam{(counter % 2) + 1}'][1].get() +'   |   '+namen[f'naam{(counter % 2) + 1}'][0]+ ' ')
    if counter == 10:
        eindspel('gelijkspel')


def select(e, id):
    global counter
    if Hetbord[id - 1].get() == '-':
        counter += 1
        Hetbord[id - 1].set(namen[f'naam{(counter % 2) + 1}'][0])
    for item in nummers:
        algewonnen(item[0], item[1], item[2])


def startgame(secondtime):
    if 3 < len(namen['naam1'][1].get()) < 15:
        global speelscherm, informatie, endgame, Hetbord, counter
        endgame = False
        Hetbord = []
        counter = 1
        beginscherm.destroy()
        if secondtime:
            speelscherm.destroy()
        speelscherm = tk.Frame(window, bg='#4D5057')
        speelscherm.grid(row=0, column=0)
        window.geometry("611x640")
        namen['naam1'][0], namen['naam2'][0] = namen['naam1'][2].get(), namen['naam2'][2].get()
        count = 0
        for x in range(3):
            for y in range(3):
                count += 1
                vakjevar = tk.StringVar(value='-')
                vakje = tk.Label(speelscherm, textvariable=vakjevar, font='Arial 25 bold', borderwidth=1, relief="solid", width=10, height=5, bg='#98B9AB')
                Hetbord.append(vakjevar)
                vakje.grid(row=x, column=y)
                vakje.bind('<1>', lambda e, id=count: select(e, id))
        informatie = tk.Label(speelscherm, text=f"{namen['naam1'][1].get()} :   {namen['naam1'][0]}   | VS |   {namen['naam2'][1].get()} :   {namen['naam2'][0]}", font='Arial 16 bold', justify='center', fg='#E1D9D1', bg='#4D5057')
        informatie.grid(row=3, column=0, columnspan=3, pady=13)
    else:
        messagebox.showinfo('Whoooppssss...', "Youre name's are either too long or too short, change them.")


def homescreen(secondtime):
    global beginscherm, namen, counter1, counter

    namen = {'naam1': ['X'], 'naam2': ['O']}
    counter1, counter = 0, 1
    window.geometry("800x200")

    if secondtime:
        speelscherm.destroy()

    beginscherm = tk.Frame(window, bg='#4D5057')
    beginscherm.grid(row=0, column=0)

    for i in range(2):
        naam = tk.StringVar()
        symbooltje = tk.StringVar(value=namen[f'naam{i + 1}'][0])
        naamtext = tk.Label(beginscherm, text=f'Player {i+1}:  ', font='Arial 25 bold', justify='center', fg='#E1D9D1', bg='#4D5057')
        naamtext.grid(row=i, column=0, padx=20)
        naaminput = tk.Entry(beginscherm, textvariable=naam, font='Arial 25', justify='center', width=20, bg='#98B9AB')
        naaminput.grid(row=i, column=1)
        symbool = tk.Label(beginscherm, textvariable=symbooltje, font='Arial 25 bold', justify='center', fg='#E1D9D1', bg='#4D5057')
        symbool.grid(row=i, column=2, padx=25)
        namen[f'naam{i + 1}'].append(naam), namen[f'naam{i + 1}'].append(symbooltje)

    switchbutton = tk.Button(beginscherm, text ="Switch", command = switch, bg='#F2AF29', width=15, height=2)
    switchbutton.grid(row=0, column=3, padx=15, pady=35)

    startbutton = tk.Button(beginscherm, text ="Start", command = lambda: startgame(False), bg='#B4CC00', width=15, height=2)
    startbutton.grid(row=1, column=3, padx=15)


homescreen(False)
window.mainloop()


