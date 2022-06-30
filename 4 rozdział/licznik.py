#powitanie
print("\t\t\t\t\tcudowny licznik".upper())

print("\n\n\n\nTen program umożliwi Ci podanie danych do licznika")


#początek zbioru
print("\n\aNajpierw podaj początek zakresu liczenia")

beginning = int(input("Podaj początkową liczbę: "))


#koniec zbioru
print("\n\aTeraz podaj końcową liczbę zakresu")

end = int(input("Podaj ostatnią liczbę zakresu: "))


#odstępy między liczbami
print("\n\aOstatnią wymaganą daną przez nas jest odstęp między kolejnymi liczbami")

space = int(input("Podaj odstęp między liczbami: "))


#pętla
print("\n\n\nTeraz nastąpi liczenie")

for i in range(beginning, end, space):
    print(i, "\n")

input("Dziękuję, za uwagę")

