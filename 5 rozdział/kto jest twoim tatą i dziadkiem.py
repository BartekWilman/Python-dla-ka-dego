import random

print("\t\t\tkto jest twoim tatą".upper())
#Objaśnienie działania programu
print("Program, który po wpisaniu imienia i nazwiska mężczyzny, pokazuje, kto jest jego ojcem")
menu = """Co chcesz zrobić?
          1 - wyświetlić zapisane rody
          2 - dodanie nowego rodu
          3 - usunięcie istniejącego rodu
          4 - zakończenie programu"""

chose = None
name = None
list_of_fam = []
families = {}
trio = None
number = None
index_i = None
index_j = None
index_k = None
POTENTIAL_FATHERS = ("Muhammad Ali", "Bill Gates", "Henry Ford",
                     "Walt Disney", "Elvis Presley", "Michael Jackson",
                     "Frank Sinatra", "Bart Simpson", "Archaon the Everchosen",
                     "Kratos", "Anakin Skywalker", "Zawisza Czarny")
POTETIAL_GRANDPAS = ("Gaius Iulius Caesar", " Vlad Țepeș", "Ezio Auditore da Firenze",
                     "Spartakus", "Leonardo da Vinci", "Malus Darkblade",
                     "Lorgar", "Anubis", "Xardas")

#pętla wyboru działania
while chose != "5":
    print(menu)
    chose = input("\t\tChcę: ")

    #wyświetlenie istniejących par
    if chose == "1":
        print("NAZWA RODU: Założyciel, obecny przywódca, spadkobierca")
        print(families)
        input("Kontynuuj")
            
    #dodanie nowej pary
    elif chose == "2":
        rhodium = input("Podaj nazwę rodu: ")
        if rhodium not in families:
            
            name = input("jak ma na spadkobierca? ")
            father = random.choice(POTENTIAL_FATHERS)
            grandpa = random.choice(POTETIAL_GRANDPAS)
            print("założycielem rodu jest", grandpa, "obecną głową rodu", father, "a spadkobiercą", name)
            trio = [grandpa, father, name]
            families[rhodium] = trio
            print("Nowy ród, który założył", grandpa, "włada nim", father, "a przyszłością jest", name, "został zapisany.")
        else:
            print("Ten ród już istnieje")
            
    #usunięcie pary
    elif chose == "3":
        print("o który ród chodzi?")
        rhodium_delete = input("Mam na myśli ród: ")
        if rhodium_delete in families:
            del families[rhodium_delete]
            print("Usunięto ród")
            input()
        else:
            print("Nie ma takiego rodu.")

    #koniec programu
    elif chose == "4":
        print("Koniec pracy programu \"KTO JESR TWOIM TATĄ... I DZIADKIEM\"")

    #korekta
    else:
        print("Błędny wybór")

print("Dowidzenia\a")
input()
        
                

        
