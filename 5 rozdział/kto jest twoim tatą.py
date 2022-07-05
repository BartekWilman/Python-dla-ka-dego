import random

print("\t\t\tkto jest twoim tatą".upper())
#Objaśnienie działania programu
print("Program, który po wpisaniu imienia i nazwiska mężczyzny, pokazuje, kto jest jego ojcem")
menu = """Co chcesz zrobić?
          1 - wyświetlić pary syn ojciec
          2 - dodanie nowej pary syn ojciec
          3 - wymieszanie istniejącej pary syn ojciec
          4 - usunięcie istniejącej pary syn ojciec
          5 - zakończenie programu"""

chose = None
name = None
father = None
pairs = []
duo = None
number = None
index_i = None
index_j = None
index_k = None
POTENTIAL_FATHERS = ("Muhammad Ali", "Bill Gates", "Henry Ford",
                     "Walt Disney", "Elvis Presley", "Michael Jackson",
                     "Frank Sinatra", "Bart Simpson", "Archaon the Everchosen",
                     "Kratos", "Anakin Skywalker", "Zawisza Czarny")

#pętla wyboru działania
while chose != "5":
    print(menu)
    chose = input("\t\tChcę: ")

    #wyświetlenie istniejących par
    if chose == "1":
        for i in range(len(pairs)):
            print(pairs[i][0], "jest ojcem dla", pairs[i][1])
            
    #dodanie nowej pary
    elif chose == "2":
        name = input("jak ma na imię ta osoba? ")
        father = random.choice(POTENTIAL_FATHERS)
        duo = [father, name]
        pairs.append(duo)
        print("Nowa para ojciec", father, "syn", name, "została dodana")

    #wymieszanie pary
    elif chose == "3":
        print("o którą parę chodzi?")
        for j in range(len(pairs)):
            print("ojciec", pairs[j][0], "syn", pairs[j][1])
            number = input("Czy chodziło o tą parę? (T/N): ")
            number.upper()
            if number == "T":
                pairs[j].reverse()
                input("dokonano zamiany")
                break
            else:
                print("Dalej")
                continue
    #usunięcie pary
    elif chose == "4":
        print("o którą parę chodzi?")
        for k in range(len(pairs)):
            print("ojciec", pairs[k][0], "syn", pairs[k][1])
            number = input("Czy chodziło o tą parę? (T/N): ")
            number.upper()
            if number == "T":
                pairs.remove(pairs[k])
                input("dokonano zamiany")
                break
            else:
                print("Dalej")
                continue

    #koniec programu
    elif chose == "5":
        print("Koniec pracy programu \"KTO JESR TWOIM TATĄ\"")

    #korekta
    else:
        print("Błędny wybór")

print("Dowidzenia\a")
input()
        
                

        
