import random
import getpass

choise = 0
player1 = ''
player2 = ''
iloscRund = int(input('Wprowadz ilosc rund: '))
roundsHist = []

while True:
    str = input('a) chce zagrać z komputerem\nb) chce zagrac z kolegą\n')
    if str == 'a':
        choise = 1
        player1 = input('Podaj pierwszego gracza: ')
        break
    if str == 'b':
        choise = 2
        player1 = input('Podaj pierwszego gracza: ')
        player2 = input('Podaj drugiego gracza: ')
        break
    else:
        print('Niepoprawny wybór')

elements = ['kamien', 'papier', 'nozyce']
playerCount1 = 0
playerCount2 = 0
if choise == 1:
    player2 = 'computer'
    for x in range(iloscRund):

        while True:
            choiseElement = int(input("Wybierz kamień(0), papier(1) lub nożyce(2): "))
            if choiseElement == 1 or choiseElement == 0 or choiseElement == 2:
                break

        computerChoise = random.randrange(3)

        if computerChoise == choiseElement:
            wins = 'remis'
            print(wins)
            roundsHist.append(wins)
        elif (choiseElement == 0 and computerChoise == 2) or (choiseElement == 1 and computerChoise == 0) or (choiseElement == 2 and computerChoise == 1):
            wins = f'{player1} wins round {x}'
            print(wins)
            roundsHist.append(wins)
            playerCount1 += 1
        else:
            wins = f'{player2} wins round {x}'
            print(wins)
            roundsHist.append(wins)
            playerCount2 += 1

        print(elements[choiseElement], ' vs ', elements[computerChoise])

if choise == 2:
    for x in range(iloscRund):
        while True:
            choiseElement1 = getpass.getpass(f"{player1}, Wybierz kamień(0), papier(1) lub nożyce(2): ")
            if choiseElement1 in ('0', '1', '2'):
                choiseElement1 = int(choiseElement1)
                break
        while True:
            choiseElement2 = getpass.getpass(f"{player2}, Wybierz kamień(0), papier(1) lub nożyce(2): ")
            if choiseElement2 in ('0', '1', '2'):
                choiseElement2 = int(choiseElement2)
                break
        if choiseElement1 == choiseElement2:
            wins = 'remis'
            print(wins)
            roundsHist.append(wins)
        elif (choiseElement1 == 0 and choiseElement2 == 2) or (choiseElement1 == 1 and choiseElement2 == 0) or (choiseElement1 == 2 and choiseElement2 == 1):
            wins = f'{player1} wins round {x}'
            print(wins)
            roundsHist.append(wins)
            playerCount1 += 1
        else:
            wins = f'{player2} wins round {x}'
            print(wins)
            roundsHist.append(wins)
            playerCount2 += 1
        print(elements[choiseElement1], ' vs ', elements[choiseElement2])

if playerCount1 > playerCount2:
    print(f"{player1} wins match")
elif playerCount2 > playerCount1:
    print(f"{player2} wins match")
else:
    print("remis")
