import time
import keyboard
import random
import tkinter as tk


Staff = False
counter = 0
laatstelijn = ""
eenelaatstelijn = ""


BendeVanEllende = ["[Helper]", "[Mod]", "[Owner]", "[Dev]", "[Sr.Mod]", "[CM]"]
Replys = ['Nooo what are you talking about?', 'Loll iam heree?', 'Iam here lmao', 'no worries i am here lol',
          'Lol iam not afk fishing???']


def detector():
    global laatstelijn, eenelaatstelijn, Staff
    logs = open(r"C:\Users\Jurre\AppData\Roaming\.minecraft\logs\latest.log", "r")
    for laatstelijn in logs:
        pass
    logs.close()

    if laatstelijn != eenelaatstelijn:
        for i in range(len(BendeVanEllende)):
            if BendeVanEllende[i] in laatstelijn:
                Staff = True

        if Staff:
            print('Admin detected!')
            keyboard.press('t')
            time.sleep(0.1)
            keyboard.release('t')
            keyboard.write('/r ' + Replys[(random.randrange(-1, 4))])
            time.sleep(1)
            keyboard.press_and_release('enter')
            eenelaatstelijn = laatstelijn
            Staff = False

    window.after(1, detector)



def opslaan():
    global Replys
    print('test')
    antwoorden = Invoer.get("1.0","end-1c")
    Replys.append(antwoorden)
    Invoer.delete("1.0",tk.END)
    print(Replys)




window = tk.Tk()

detector()
Replys = []
window.title('Robs afk fishing paneel.')
window.geometry("700x700")
window.configure(bg='Blue')


Invoer = tk.Text(window, height = 2, width = 40)
Invoer.pack(pady=20)

OpslaanKnop = tk.Button(window, text = "Toevoegen", command=opslaan)

OpslaanKnop.pack(ipady=2,ipadx=15)

allezinnen = tk.Label(window, text="replys")
allezinnen.pack()

alleverbodenwoorden = tk.Label(window, text="verbodenwoorden")
alleverbodenwoorden.pack()




window.mainloop()

