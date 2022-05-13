import tkinter as tk
import random
from tkinter import messagebox



window = tk.Tk()
window.title('Regristatie Efteling')
window.geometry('500x400')
window.configure(bg='grey')
window.resizable(False, False)


def submit():
    if input1.get() != '' and '@' in input2.get() and int(input3.get()) > 0 and input5.get() != 0:
        frame1.destroy()
        if input4.get() == 1:
            fastpass = 'Ja'
        else:
            fastpass = 'Nee'
        if input5.get() == 1:
            geslacht = 'man'
        else:
            geslacht = 'Vrouw'
        tekst = (f'Naam: {input1.get()} \n E-Mail: {input2.get()} \n Leeftijd: {input3.get()} \n Fastpass: {fastpass} \n Geslacht: {geslacht} \n regestratie code: {random.randrange(10000,100000)}')
        label10 = tk.Label(window, text='Regrestatieformulier Efteling', font='Arial 23 bold', justify='center', fg='black', bg='grey')
        label10.place(relx=0.5, rely=0.15, anchor='center')
        label11 = tk.Label(window, text='-------------------------------------------------------------------------------------', font='Arial 15 bold', justify='center', fg='black', bg='grey')
        label11.place(relx=0.5, rely=0.3, anchor='center')
        label9 = tk.Label(window, text=tekst, font='Arial 15 bold', justify='center', fg='black', bg='grey')
        label9.place(relx=0.5, rely=0.6, anchor='center')

    else:
        tk.messagebox.showinfo(title='Whoopsss..', message='Dit formulier is niet valide!')


frame1 = tk.Frame(window, bg='grey')
frame1.place(relx=0.5, rely=0.5, anchor='center')

label1 = tk.Label(frame1, text='Regrestatieformulier Efteling', font='Arial 23 bold', justify='center', fg='black', bg='grey')
label1.grid(row=0, column=0, columnspan=2, pady=30)

label2 = tk.Label(frame1, text='Naam:', font='Arial 15 bold', justify='center', fg='black', bg='grey')
label2.grid(row=4, column=0, sticky=tk.E, padx=5)

input1 = tk.StringVar()
entry1 = tk.Entry(frame1, textvariable=input1, font='Arial 12 bold', justify='center', width=20)
entry1.grid(row=4, column=1, sticky=tk.W, padx=5)

label3 = tk.Label(frame1, text='E-mail:', font='Arial 15 bold', justify='center', fg='black', bg='grey')
label3.grid(row=5, column=0, sticky=tk.E, padx=5)

input2 = tk.StringVar()
entry2 = tk.Entry(frame1, textvariable=input2, font='Arial 12 bold', justify='center', width=20)
entry2.grid(row=5, column=1, sticky=tk.W, padx=5)


label4 = tk.Label(frame1, text='Leeftijd:', font='Arial 15 bold', justify='center', fg='black', bg='grey')
label4.grid(row=6, column=0, sticky=tk.E, padx=5)

input3 = tk.StringVar()
spinbox1 = tk.Spinbox(frame1, textvariable=input3, from_=0,to=150, font='Arial 12 bold', justify='center', width=5)
spinbox1.grid(row=6, column=1, sticky=tk.W, padx=5)
spinbox1['state'] = 'readonly'

label5 = tk.Label(frame1, text='Fastpass:', font='Arial 15 bold', justify='center', fg='black', bg='grey')
label5.grid(row=7, column=0, sticky=tk.E, padx=5)

input4 = tk.IntVar()
checkbox1 = tk.Checkbutton(frame1, onvalue=1, offvalue=0, variable=input4, font='Arial 12 bold', justify='center', width=3)
checkbox1.grid(row=7, column=1, sticky=tk.W, padx=5)

label6 = tk.Label(frame1, text='Man:', font='Arial 15 bold', justify='center', fg='black', bg='grey')
label6.grid(row=1, column=0, padx=5)

label7 = tk.Label(frame1, text='Vrouw:', font='Arial 15 bold', justify='center', fg='black', bg='grey')
label7.grid(row=1, column=1, padx=5)

input5 = tk.IntVar()
Radiobutton1 = tk.Radiobutton(frame1, variable=input5, value=1)
Radiobutton1.grid(row=2, column=0, padx=5)
Radiobutton2 = tk.Radiobutton(frame1, variable=input5, value=2)
Radiobutton2.grid(row=2, column=1, padx=5)

label8 = tk.Label(frame1, text='', font='Arial 15 bold', justify='center', fg='black', bg='grey')
label8.grid(row=3, columnspan=2, pady=5)

button1 = tk.Button(frame1, text='Submit', bg='#A9A9A9', command=submit, font='Arial 16 bold', fg='black')
button1.grid(row=9, column=0, ipadx=40, ipady=1, columnspan=2, pady=30)

window.mainloop()