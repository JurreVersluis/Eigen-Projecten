import time
import keyboard
import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os
from datetime import datetime
from tkinter import *
from tkinter.simpledialog import askstring

logs = open(os.getenv('APPDATA') + r'\.minecraft\logs\latest.log', 'r')
BendeVanEllende = ["[Helper]", "[Mod]", "[Owner]", "[Dev]", "[Sr.Mod]", "[CM], [Admin]"]
Staffmode = False
Msgmode = False
Staff = False
laatstelijn = ""
eenelaatstelijn = ""
Replys = ['Zet hier in ieder geval iets neer om bugs te voorkomen. (clear dit bericht met de clear knop)  X']
Detect = ['Zet hier in ieder geval iets neer om bugs te voorkomen. (clear dit bericht met de clear knop)  X']
gedetect = []
counter = 0
counter2 = 0
username = "O183"

# [00:11:43] [main/INFO]: [CHAT] [FoxGoddess] Tanivi -> (you): hello


def checkmessage():
    global Staff
    for item in Detect:
        if item.lower() in laatstelijn.lower():
            Staff = True


def detector():
    global laatstelijn, eenelaatstelijn, Staff, counter2

    logs.seek(0)
    laatstelijn = (logs.readlines()[-1])

    if '[CHAT]' in laatstelijn:
        laatstelijn = laatstelijn[30:len(laatstelijn)]
        index = 0
        self_send = False

        for letter in laatstelijn:
            index += 1
            if letter == '>':
                # : voor fox, > voor normal
                self_send = True
                break
        if not self_send:
            index = 0

        if username not in laatstelijn[0:index]:
            if Staffmode and Msgmode:
                for Member in BendeVanEllende:
                    if Member in laatstelijn and '-> (you)' in laatstelijn:
                        checkmessage()
            elif Staffmode:
                for Member2 in BendeVanEllende:
                    if Member2 in laatstelijn:
                        checkmessage()
            elif Msgmode:
                if '-> (you)' in laatstelijn:
                    checkmessage()
            else:
                checkmessage()

    if Staff:
        time.sleep(2)
        print('Admin detected!')
        keyboard.press('t')
        time.sleep(0.1)
        keyboard.release('t')
        bericht = Replys[(random.randrange(-1, len(Replys)))]
        keyboard.write(bericht)
        time.sleep(random.randrange(7, 10))
        keyboard.press_and_release('enter')
        counter2 += 1
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        gedetect.append(f'{str(counter2)} ---- {current_time} - {laatstelijn} - Teruggestuurd: {bericht} ---')
        combocheck()
        Staff = False

    window.after(200, detector)


window = tk.Tk()

detector()

window.title('Robs afk fishing paneel.')
window.geometry("400x840")
window.configure(bg='grey')
window.resizable(False, False)


def check():
    global Staffmode
    global Msgmode
    Staffmode = staffmodeofniet.get() == 1
    Msgmode = msgmodeofniet.get() == 1


def toevoegen():
    global Replys, Detect
    if input1.get() == 'Replys':
        Replys.append(input2.get())
    elif input1.get() == 'Gedetecteerd':
        gedetect.append(input2.get())
    else:
        Detect.append(input2.get())

    combocheck()


def clear():
    global Detect, Replys, gedetect
    if input1.get() == 'Replys':
        Replys = []
    elif input1.get() == 'Gedetecteerd':
        gedetect = []
    else:
        Detect = []
    combocheck()


def combocheck(event=None):
    frame2.focus()
    if input1.get() == 'Replys':
        huidigelijst.set('  -  '.join(Replys))
    elif input1.get() == 'Gedetecteerd':
        huidigelijst.set('  -  '.join(gedetect))
    else:
        huidigelijst.set('  -  '.join(Detect))


label1 = tk.Label(window, text='0  1  8  3',font='Arial 40 bold', justify='center', fg='green', bg='grey')
label1.place(relx=0.5,rely=0.1, anchor='center', width=300,height=100)

frame2 = tk.Frame(window, bg='grey')
frame2.place(relx=0.5,rely=0.58, anchor='center')

staffmodeofniet = tk.IntVar()
staffmodeofniet.set(1)
checkbox1 = tk.Checkbutton(frame2, text='Staff-mode', onvalue=1, offvalue=0, variable=staffmodeofniet, command=check)
checkbox1.deselect()
checkbox1.grid(row=0, column=0, ipadx=5,ipady=4)

msgmodeofniet = tk.IntVar()
msgmodeofniet.set(1)
checkbox2 = tk.Checkbutton(frame2, text='Msg-mode', onvalue=1, offvalue=0, variable=msgmodeofniet, command=check)
checkbox2.deselect()
checkbox2.grid(row=0, column=1, ipadx=5, ipady=4)


input1 = tk.StringVar()
input1.set('Replys')
combobox1 = ttk.Combobox(frame2, textvariable=input1)
combobox1.grid(row=1, column=0, ipadx=30, ipady=10, pady=35, columnspan=2)
combobox1['state'] = 'readonly'
combobox1['values'] = ["Detect-Message's", 'Replys', "Gedetecteerd"]
combobox1.bind('<<ComboboxSelected>>', combocheck)


input2 = tk.StringVar()
combobox2 = ttk.Entry(frame2, textvariable=input2)
combobox2.grid(row=2, column=0, ipadx=39, ipady=10, columnspan=2)

button1 = tk.Button(frame2, text='Toevoegen!', bg='#A9A9A9', command=toevoegen, font='Arial 12 bold')
button1.grid(row=3, column=0, ipadx=39, ipady=10, columnspan=2, pady=20)


huidigelijst = tk.StringVar()
label2 = tk.Label(frame2, textvariable=huidigelijst, width=1, anchor="nw", wraplengt=265, height=1, font='Arial 9')
label2.grid(row=4, column=0, ipadx=125, ipady=160, pady=0, columnspan=2)

scroll_bar = tk.Scrollbar(label2)
scroll_bar.pack(side=tk.RIGHT, fill =tk.Y)


button2 = tk.Button(frame2, text='X', bg='#A9A9A9', command=clear, font='Arial 12 bold', fg='red')
button2.grid(row=5, column=0, ipadx=20, ipady=1, columnspan=2)


combocheck()
window.mainloop()

