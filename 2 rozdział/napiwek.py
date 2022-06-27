# napiwek
# zastosowanie funkcji int

# podanie kwoty należnej do zapłaty

zapłata = int(input("Należna kwota do zapłaty wynosi: "))

# napiwek 15%

mały_napiwek = zapłata * 0.15
print(mały_napiwek)


# napiwek 20%

duży_napiwek = zapłata * 0.2
print(duży_napiwek)


# podsumowanie

print("Miałeś zapłacić ", zapłata, " i zdecydowałeś się dać napiwku: ", mały_napiwek, end="")
print("ale ponieważ kelner był miły dałeś: ", duży_napiwek)


# zakończenie programu

input("Enter")
