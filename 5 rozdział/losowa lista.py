import random


#lista bogów
gods = ["Khorne", "Slanesh", "Nurgle",
       "Tzeentch", "Malal", "Khaine",
       "Sigmar", "Morr", "Ulryk",
       "Grungi", "Grimir", "Valaya",
       "Rogaty Szczur", "Matka Nocy", "Ursun"]

new_gods = []
#przedstawienie programu

print("\t\t\t\t\t\t\tlosowa lista".upper())
print("\nProgram ten wyświetli listę bogów ze świata warhammera fantasy w losowej kolejności")

#tworzenie nowej listy
while gods:
    god = random.choice(gods)
    new_gods.append(god)
    gods.remove(god)

#wypisanie nowej listy
for i in new_gods:
    print(i, "\n")

print("Nowa list w losowej kolejności")
input()

