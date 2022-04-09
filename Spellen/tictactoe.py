import time
import random


def ietsvragen(devraag, antwoorden):
    global antwoord
    vraag = True
    while vraag:
        antwoord = input(devraag + '\n')
        if antwoord in str(antwoorden):
            vraag = False
        else:
            print('Dat is geen geldige invoer.')


Hetbord = [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ']
Namen = []
Rondjeofkruisje = []
Xof0 = []
gewonnen = False

def starten():
    print('Welkom bij rondje kruisje!\n')

    ietsvragen('Typ: 1. (Ik wil met twee echte spelers spelen.), 2. (Ik wil met mezelf en een robot spelen.)', ['1', '2'])

    if antwoord == '1':
        for i in range(2):
            naam = input(f'Typ Speler {i + 1} zijn naam: ')
            Namen.append(naam)
        ietsvragen(f'{Namen[0]} wil jij  1. ( 0 )   of   2. ( X )  zijn?', ['1','2'])
        antwoord1 = antwoord
        ietsvragen(f'{Namen[1]} wil jij  1. ( 0 )   of   2. ( X )  zijn?', ['1', '2'])
        antwoord2 = antwoord
        if antwoord1 == antwoord2:
            print('Omdat jullie allebei dezelfde vorm willen zijn wordt er random een gekozen!\n')
            time.sleep(2)
            print('Tromgeroffel....\n\n\n')
            time.sleep(2)
            antwoord1 = random.randrange(0,2)

        if str(antwoord1) == '1':
            Rondjeofkruisje.append('rondje')
            Rondjeofkruisje.append('kruisje')
            Xof0.append(' 0 ')
            Xof0.append(' X ')
        else:
            Rondjeofkruisje.append('kruisje')
            Rondjeofkruisje.append('rondje')
            Xof0.append(' X ')
            Xof0.append(' 0 ')
        print(f'{Namen[0]} is {Rondjeofkruisje[0]} gemaakt!')
        print(f'{Namen[1]} is {Rondjeofkruisje[1]} gemaakt!\n\n\n')
        time.sleep(3)
        Wieis()
    else:
            print('robot.exe werkt nog niet lol denk je dat ik elon musk ben ofzo dat ik een robot voor rondje kruisje maak pfff')

def Wieis():
    global count
    print('Er wordt nu random iemand gekozen die als eerste mag beginnen...\n')
    count = random.randrange(0,2)
    time.sleep(3)
    print(f'{Namen[count]} is random gekozen om te mogen beginnen, Veel plezierr!')
    time.sleep(3)
    for i in range(10):
        print('')



def spelen():
    bord()
    global count
    Kanjezetten = True
    while Kanjezetten:
        ietsvragen(f'{Namen[count]} / {Rondjeofkruisje[count]}  is aan de beurt, op welke plek wil je een {Rondjeofkruisje[count]} plaatsen?',['1','2','3','4','5','6','7','8','9'])

        if Hetbord[int(antwoord) - 1] == ' - ':
            Hetbord.pop(int(antwoord) - 1)
            Hetbord.insert(int(antwoord) - 1,Xof0[count])
            Kanjezetten = False
        else:
            print('Daar staat al een rondje of kruisje!')
            time.sleep(2)
            bord()

    count += 1
    if count > 1:
        count = 0


def bord():
    for i in range(100):
        print('')
    counter = 0
    for i in range(3):
        for b in range(3):
            print(Hetbord[b + counter],end='')
        print('')
        counter += 3
    for i in range(2):
        print('')



def Algewonnen():
    global gewonnen

    if not Hetbord[0] == ' - ':
        if Hetbord[0] == Hetbord[1] and Hetbord[1] == Hetbord[2]:
            gewonnen = True
    if not Hetbord[3] == ' - ':
        if Hetbord[3] == Hetbord[4] and Hetbord[4] ==  Hetbord[5]:
            gewonnen = True
    if not Hetbord[6] == ' - ':
        if Hetbord[6] == Hetbord[7] and Hetbord[7] == Hetbord[8]:
            gewonnen = True

    # horizontaal gewonnen

        if not Hetbord[0] == ' - ':
            if Hetbord[0] == Hetbord[3] and Hetbord[3] ==  Hetbord[6]:
                gewonnen = True
        if not Hetbord[1] == ' - ':
            if Hetbord[1] == Hetbord[4] and Hetbord[4] ==  Hetbord[7]:
                gewonnen = True
        if not Hetbord[2] == ' - ':
            if Hetbord[2] == Hetbord[5] and Hetbord[5] == Hetbord[8]:
                gewonnen = True

    # verticaal gewonnen

    if not Hetbord[2] == ' - ':
        if Hetbord[2] == Hetbord[4] and Hetbord[4] == Hetbord[6]:
            gewonnen = True
    if not Hetbord[0] == ' - ':
        if Hetbord[0] == Hetbord[4] and Hetbord[4] == Hetbord[8]:
            gewonnen = True

    #diagonaal gewonnen

    if gewonnen:
        bord()
        print('Je hebt gewonnen.')
        Nogeenkeer()
    if not Hetbord.__contains__(' - '):
        bord()
        print('Het is gelijkspel.')
        Nogeenkeer()


def Nogeenkeer():
    global Loop, Hetbord, gewonnen
    ietsvragen('Wil je nog een keer spelen?', ['ja', 'nee'])
    if antwoord == 'ja':
        Hetbord = [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ']
        gewonnen = False
        Wieis()
    else:
            Loop = False
            print('Bedankt voor het spelen!')


starten()
Loop = True
while Loop:
    spelen()
    Algewonnen()
