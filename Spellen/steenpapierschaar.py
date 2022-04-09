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


Keuzes = ['Steen!', 'Papier', 'Schaar!']
Namen = []


def starten():
    ietsvragen('Typ: 1. (Ik wil met twee echte spelers spelen.), 2. (Ik wil met mezelf en een robot spelen.)', ['1', '2'])
    if antwoord == '1':
        for i in range(2):
            naam = input(f'Typ Speler {i + 1} zijn naam: ')
            Namen.append(naam)
    else:
        naam = input(f'Typ Speler 1 zijn naam: ')
        Namen.append(naam)
        naam = ('Barry')
        print('Speler 2, Barry (bot) is ook toegevoegd!')
        Namen.append(naam)


def beginspel():
    print(f'{Namen[1]} kijkt nu weg van het scherm terwijl {Namen[0]} zijn keuze maakt...')
    time.sleep(1)
    ietsvragen('Typ: 1. (Ik wil met twee echte spelers spelen.), 2. (Ik wil met mezelf en een robot spelen.)', ['1', '2'])

starten()
beginspel()