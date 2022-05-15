import time
import keyboard
import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os
from datetime import datetime
from tkinter import *

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
        laatstelijn = laatstelijn[35:len(laatstelijn)]
        index = 0
        self_send = False

        for letter in laatstelijn:
            index += 1
            if letter == ':':
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

window.title('Robs afk fishing paneel.')
window.geometry("200x200")
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


def combocheck(event=None):
    frame2.focus()
    label2.delete(0, END)
    if input1.get() == 'Replys':
        for i in range(len(Replys)):
            label2.insert(i, str(i + 1) + ': ' + Replys[i])
    elif input1.get() == 'Gedetecteerd':
        for i in range(len(gedetect)):
            label2.insert(i, str(i + 1) + ': ' + gedetect[i])
    else:
        for i in range(len(Detect)):
            label2.insert(i, str(i + 1) + ': ' + Detect[i])


def clear():
    global Detect, Replys, gedetect
    if input1.get() == 'Replys':
        Replys = []
    elif input1.get() == 'Gedetecteerd':
        gedetect = []
    else:
        Detect = []
    combocheck()


def submit():
    global frame2, label2, input1, input2, staffmodeofniet, msgmodeofniet, username

    button3.destroy()
    Entry5.destroy()
    label3.destroy()
    username = input5.get()
    window.geometry("400x840")
    detector()
    mooieusername = ''
    for letter in username:
        if len(username) < 5:
            mooieusername += letter + '  '
        else:
            mooieusername = username
    if len(username) < 5:
        mooieusername = mooieusername[0:len(mooieusername) - 2]

    frame2 = tk.Frame(window, bg='grey')
    frame2.place(relx=0.5,rely=0.5, anchor='center')

    label1 = tk.Label(frame2, text=mooieusername, font='Arial 45 bold', justify='center', fg='green', bg='grey')
    label1.grid(row=0, column=0, ipadx=50, columnspan=2, pady=20)

    staffmodeofniet = tk.IntVar()
    staffmodeofniet.set(1)
    checkbox1 = tk.Checkbutton(frame2, text='Staff-mode', onvalue=1, offvalue=0, variable=staffmodeofniet, command=check)
    checkbox1.deselect()
    checkbox1.grid(row=1, column=0, ipadx=5,ipady=4,sticky=tk.E, pady=25, padx=10)

    msgmodeofniet = tk.IntVar()
    msgmodeofniet.set(1)
    checkbox2 = tk.Checkbutton(frame2, text='Msg-mode', onvalue=1, offvalue=0, variable=msgmodeofniet, command=check)
    checkbox2.deselect()
    checkbox2.grid(row=1, column=1, ipadx=5, ipady=4, sticky=tk.W, pady=25, padx=10)

    input1 = tk.StringVar()
    input1.set('Replys')
    combobox1 = ttk.Combobox(frame2, textvariable=input1)
    combobox1.grid(row=2, column=0, ipadx=30, ipady=10, columnspan=2, pady=20)
    combobox1['state'] = 'readonly'
    combobox1['values'] = ["Detect-Message's", 'Replys', "Gedetecteerd"]
    combobox1.bind('<<ComboboxSelected>>', combocheck)

    input2 = tk.StringVar()
    combobox2 = ttk.Entry(frame2, textvariable=input2)
    combobox2.grid(row=3, column=0, ipadx=39, ipady=10, columnspan=2)

    button1 = tk.Button(frame2, text='Toevoegen!', bg='#A9A9A9', command=toevoegen, font='Arial 12 bold')
    button1.grid(row=4, column=0, ipadx=39, ipady=10, columnspan=2, pady=20)

    label2 = Listbox(frame2, width=1, height=1, font='Arial 9')
    label2.grid(row=5, column=0, ipadx=90, ipady=150, pady=0, columnspan=2)

    scroll_bar = tk.Scrollbar(label2)
    scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
    scroll_bar.config(command=label2.yview)

    scroll_bar2 = tk.Scrollbar(label2, orient='horizontal')
    scroll_bar2.pack(side=tk.BOTTOM, fill=tk.X)
    scroll_bar2.config(command=label2.xview)

    label2.config(yscrollcommand=scroll_bar.set, xscrollcommand=scroll_bar2.set)

    button2 = tk.Button(frame2, text='X', bg='#A9A9A9', command=clear, font='Arial 12 bold', fg='red')
    button2.grid(row=6, column=0, ipadx=20, ipady=1, columnspan=2)

    combocheck()


label3 = tk.Label(window, text='Username:', font='Arial 22 bold', justify='center', fg='black', bg='grey')
label3.place(relx=0.5, rely=0.16, anchor=CENTER)

input5 = tk.StringVar()
Entry5 = ttk.Entry(window, textvariable=input5, justify='center', font='Arial 12 bold')
Entry5.place(relx=0.5, rely=0.46, anchor=CENTER, width=130, height=25)

button3 = tk.Button(window, text='Submit', bg='#A9A9A9', command=submit, font='Arial 12 bold', fg='black', justify='center')
button3.place(relx=0.5, rely=0.76, anchor=CENTER)
window.mainloop()

