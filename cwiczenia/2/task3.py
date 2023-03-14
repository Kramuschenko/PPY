print("Witaj w ankiecie dotyczącej Twoich studiów!")
imie_nazwisko = input("Jak masz na imię i nazwisko? ")

print("Witaj {}! Odpowiedz na poniższe pytania:".format(imie_nazwisko))
odpowiedz1 = input("1. Jaki jest twój ulubiony kolor? ")
odpowiedz2 = input("2. Co robisz w wolnym czasie? ")
odpowiedz3 = input("4. Co jest Twoim ulubionym daniem? ")

print("\n4. Kierunek studiów:")
print("a) Informatyka")
print("b) Zarządzanie")
print("c) Media art")
kierunek = input("Wybierz literę odpowiadającą Twojemu kierunkowi studiów: ")

print("\n5. Stopień studiów:")
print("a) Studia inżynierskie")
print("b) Studia magisterskie")
stopien = input("Wybierz literę odpowiadającą Twojemu stopniowi studiów: ")

print("\n6. Sposób finansowania studiów:")
print("a) Studia zaoczne")
print("b) Studia dzienne, płatne")
finansowanie = input("Wybierz literę odpowiadającą sposobowi finansowania Twoich studiów: ")

print("\n7. Planowana specjalizacja po ukończeniu studiów:")
print("a) Programowanie aplikacji biznesowych")
print("b) PM lub BA")
print("c) 3D artist")
specjalizacja = input("Wybierz literę odpowiadającą Twojej planowanej specjalizacji po ukończeniu studiów: ")


print("\nPodsumowanie odpowiedzi:")
print("1. Jaki jest twój ulubiony kolor? {}".format(odpowiedz1))
print("2. Co robisz w wolnym czasie? {}".format(odpowiedz2))
print("3. Co jest Twoim ulubionym daniem? {}".format(odpowiedz3))

print("4. Kierunek studiów:", end=" ")
if kierunek == "a":
    print("Informatyka")
elif kierunek == "b":
    print("Zarządzanie")
elif kierunek == "c":
    print("Media art")
else:
    print("Inne: ", kierunek)

print("5. Stopień studiów:", end=" ")
if stopien == "a":
    print("Studia inżynierskie")
elif stopien == "b":
    print("Studia magisterskie")
else:
    print("Niepoprawna odpowiedź")

print("6. Sposób finansowania studiów:", end=" ")
if finansowanie == "a":
    print("Studia zaoczne")
elif finansowanie == "b":
    print("Studia dzienne, płatne")
else:
    print("Inne: ", finansowanie)

print("7. Planowana specjalizacja po ukończeniu studiów:", end=" ")
if specjalizacja == "a":
    print("Programowanie aplikacji biznesowych")
elif specjalizacja == "b":
    print("PM lub BA")
elif specjalizacja == "c":
    print("3D artist")
else:
    print("Inne: ", specjalizacja)