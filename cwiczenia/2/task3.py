questions = []
answers = []

print("Witaj w ankiecie dotyczącej Twoich studiów!")
imie_nazwisko = input("Jak masz na imię i nazwisko? ")

print("Witaj {}! Odpowiedz na poniższe pytania:".format(imie_nazwisko))
kolor_ = "1. Jaki jest twój ulubiony kolor? "
answers += [input(kolor_)]
wolnyCzas = "2. Co robisz w wolnym czasie? "
answers += [input(wolnyCzas)]
jedzenie = "3. Co jest Twoim ulubionym daniem? "
answers += [input(jedzenie)]
questions += [kolor_]
questions += [wolnyCzas]
questions += [jedzenie]

kierunek = "4. Kierunek studiów:"
questions += [kierunek]
print("%s" % kierunek)
print("a) Informatyka")
print("b) Zarządzanie")
print("c) Media art")
kierunek = input("Wybierz literę odpowiadającą Twojemu kierunkowi studiów lub jego nazwe: ")

if kierunek == "a":
    answers += ["Informatyka"]
elif kierunek == "b":
    answers += ["Zarządzanie"]
elif kierunek == "c":
    answers += ["Media art"]
else:
    answers += [f"Inne: {kierunek}"]

stopien = ["5. Stopień studiów:"]
questions += stopien
print(stopien)
print("a) Studia inżynierskie")
print("b) Studia magisterskie")
stopien = input("Wybierz literę odpowiadającą Twojemu stopniowi studiów lub własną nazwe: ")

if stopien == "a":
    answers += ["Studia inżynierskie"]
elif stopien == "b":
    answers += ["Studia magisterskie"]
else:
    answers += [f"Inne: {stopien}"]

finansowanie = "6. Sposób finansowania studiów:"
questions += [finansowanie]
print(finansowanie)
print("a) Studia zaoczne")
print("b) Studia dzienne, płatne")
finansowanie = input("Wybierz literę odpowiadającą sposobowi finansowania Twoich studiów: ")

if finansowanie == "a":
    answers += ["Studia zaoczne"]
elif finansowanie == "b":
    answers += ["Studia dzienne, płatne"]
else:
    answers += [f"Inne: {finansowanie}"]

specjalizacja = "7. Planowana specjalizacja po ukończeniu studiów:"
questions += [specjalizacja]
print(specjalizacja)
print("a) Programowanie aplikacji biznesowych")
print("b) PM lub BA")
print("c) 3D artist")
specjalizacja = input("Wybierz literę odpowiadającą Twojej planowanej specjalizacji po ukończeniu studiów: ")

if specjalizacja == "a":
    answers += ["Programowanie aplikacji biznesowych"]
elif specjalizacja == "b":
    answers += ["PM lub BA"]
elif specjalizacja == "c":
    answers += ["3D artist"]
else:
    answers += [f"Inne: {specjalizacja}"]

print(f"\nPodsumowanie odpowiedzi dla {imie_nazwisko}:")

for x in range(7):
    print("Pytanie: ", questions[x])
    print("Odpowiedz: ", answers[x])
