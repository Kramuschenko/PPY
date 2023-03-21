import random

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
if choise == 1:
    computerCount = 0
    playerCount = 0
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
            playerCount += 1
        else:
            wins = f'computer wins round {x}'
            print(wins)
            roundsHist.append(wins)
            computerCount += 1
        print(elements[choiseElement], ' vs ', elements[computerChoise])
    if playerCount > computerCount:
        print(f"{player1} wins match")
    elif computerCount > playerCount:
        print(f"computer wins match")
    else:
        print("remis")
if choise == 2:
    for x in range(iloscRund):
