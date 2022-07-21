import random

def ask_number(question, low, high, step = 1):
    """Poproś o podanie liczby z odpowiedniego zakresu."""
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response

print("\t\t\t\t\\t\t\a JAKA TO LICZBA")

print("Zaraz wymyślę jedną liczbę z przedziału od 1 do 100, a Ty musisz ją odgadnąć")


liczba = random.randint(1, 100)
odp = ask_number("Ta liczba to: ", 1, 100, 1)
zycia = 3

while odp != liczba and zycia > 1:

    if odp > liczba:
        print("Mniej")
        zycia -= 1

    elif odp < liczba:
        print("więcej")
        zycia -= 1

    elif zycia == 1:
        print("Straciłeś wszystkie szanse")

    odp = int(input("Ta liczba to: "))

if odp == liczba:
    print("Zgadłeś, poprawny wynik to", liczba)

else:
    print("Nie udało Ci się, poprawną odpowiedzią jest", liczba)

input("Koniec gry")
