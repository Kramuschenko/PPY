import random

cities = "Warszawa,Kraków,Wrocław,Łódź,Poznań,Gdańsk,Szczecin,Bydgoszcz,Lublin,Białystok"
miasta = cities.split(",")

randCities = []

while len(randCities) < 10:
    miasto = random.choice(miasta)
    if miasto not in randCities:
        randCities.append(miasto)

print("Plan wycieczki:")
for miasto in randCities:
    print(miasto)
