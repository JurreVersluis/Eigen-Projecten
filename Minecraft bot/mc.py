import time
import keyboard
import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

Staff = False
counter = 0
laatstelijn = ""
eenelaatstelijn = ""
Staffmode = False
Msgmode = False

BendeVanEllende = ["[Helper]", "[Mod]", "[Owner]", "[Dev]", "[Sr.Mod]", "[CM]"]
Replys = ['Nee, ik ben er gewoon.']
Detect = ['Ben jij aan het afk vissen ofzo?']

def checkmessage():
    global Staff
    for a in range(len(Detect)):
        if Detect[a].lower() in laatstelijn.lower():
            Staff = True

def detector():
    global laatstelijn, eenelaatstelijn, Staff
    logs = open(r"C:\Users\Jurre\AppData\Roaming\.minecraft\logs\latest.log", "r")
    for laatstelijn in logs:
        pass
    logs.close()

    if laatstelijn != eenelaatstelijn:
        if Staffmode:
            if Msgmode:
                for i in range(len(BendeVanEllende)):
                    if BendeVanEllende[i] in laatstelijn and '-->' in laatstelijn:
                        checkmessage()
        elif Msgmode:
            if '-->' in laatstelijn:
                checkmessage()
        elif Staffmode:
            for i in range(len(BendeVanEllende)
                           ):
                if BendeVanEllende[i] in laatstelijn:
                        checkmessage()
        else:
            checkmessage()

        if Staff:
            print('Admin detected!')
            for c in range(2):
                keyboard.press('t')
                time.sleep(0.1)
                keyboard.release('t')
                if c == 0:
                    keyboard.write('/r ' + Replys[(random.randrange(-1, len(Replys)))])
                else:
                    keyboard.write('')
                time.sleep(1)
                keyboard.press_and_release('enter')
                laatstelijn = '/r Nee, ik ben er gewoon.'
                eenelaatstelijn = laatstelijn

            Staff = False


    window.after(1, detector)

window = tk.Tk()

detector()

window.title('Robs afk fishing paneel.')
window.geometry("400x825")
window.configure(bg='grey')


def Check():
    global Staffmode
    global Msgmode
    if staffmodeofniet.get() == 1:
        Staffmode = True
    else:
        Staffmode = False

    if msgmodeofniet.get() == 1:
        Msgmode = True
    else:
        Msgmode = False


def toevoegen():
    global Replys, Detect
    if input1.get() == 'Replys':
        Replys.append(input2.get())
    else:
        Detect.append(input2.get())
    check()

def check(event=None):
    if input1.get() == 'Replys':
        huidigelijst.set('  -  '.join(Replys))
    else:
        huidigelijst.set('  -  '.join(Detect))


label1 = tk.Label(window, text='0  1  8  3',font='Arial 40 bold', justify='center', fg='green', bg='gray')
label1.place(relx=0.5,rely=0.1, anchor='center', width=300,height=100)

frame2 = tk.Frame(window, bg='grey')
frame2.place(relx=0.5,rely=0.6, anchor='center')

staffmodeofniet = tk.IntVar()
staffmodeofniet.set(1)
checkbox1 = tk.Checkbutton(frame2, text='Staff-mode', onvalue=1, offvalue=0, variable=staffmodeofniet, command=Check)
checkbox1.deselect()
checkbox1.grid(row=0, column=0, ipadx=5,ipady=4)

msgmodeofniet = tk.IntVar()
msgmodeofniet.set(1)
checkbox2 = tk.Checkbutton(frame2, text='Msg-mode', onvalue=1, offvalue=0, variable=msgmodeofniet, command=Check)
checkbox2.deselect()
checkbox2.grid(row=0, column=1, ipadx=5,ipady=4)


input1 = tk.StringVar()
input1.set('Replys')
combobox1 = ttk.Combobox(frame2, textvariable=input1)
combobox1.grid(row=1, column=0, ipadx=30,ipady=10, pady=35, columnspan=2)
combobox1['state'] = 'readonly'
combobox1['values'] = ["Detect-Message's", 'Replys']
combobox1.bind('<<ComboboxSelected>>', check)

input2 = tk.StringVar()
combobox2 = ttk.Entry(frame2, textvariable=input2)
combobox2.grid(row=2, column=0, ipadx=39,ipady=10, columnspan=2)

button1 = tk.Button(frame2, text='Toevoegen!', bg='#A9A9A9', command=toevoegen)
button1.grid(row=3, column=0, ipadx=39,ipady=10, columnspan=2)


huidigelijst = tk.StringVar()
label2 = tk.Label(frame2, textvariable=huidigelijst, width=1, anchor="nw", wraplengt=265, height=1, font='Arial 12 bold')
label2.grid(row=4, column=0, ipadx=125,ipady=200, pady='20', columnspan=2)


check()
window.mainloop()

