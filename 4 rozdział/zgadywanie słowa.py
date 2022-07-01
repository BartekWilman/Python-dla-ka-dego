import random

#krotka słów do wyboru

GODS =("Khorne", "Slanesh", "Nurgle",
       "Tzeentch", "Malal", "Khaine",
       "Sigmar", "Morr", "Ulryk",
       "Grungi", "Grimir", "Valaya",
       "Rogaty Szczur", "Matka Nocy", "Ursun")

word = random.choice(GODS)
present_letters = ""

#powitanie i wyjaśnienie zasad gry

print("\t\t\t\t\t\t\t\a\a\a\a\azgadywanie słowa".upper())
print("\n\n\n\nprogram zaraz wyświetli Ci ilość znaków znajdujących się w słowie, które wylosowało.")
print("Będziesz miał 5 możliwości zapytania o znak, czy występuje w imieniu wylosowanego boga, zanim będziesz musiał odpowiedzieć")
print("Jako że jestem fanem Warhammera fantasy, kategorią są bogowie z tego uniwersum")



#początek gry
print("\n\n\n\nZgadnij, co to za bóg, którego imię składa się z", len(word), "znaków.")


#pętla pytająca o znaki w wylosowanym słowie
for i in range(5):
    ask = input("Podaj literę o której istnieniu chcesz być pewnym (spacja też się liczy): ")
    if ask in word.lower():
        print("Tak, ten znak tam jest")
        ask += present_letters

    else:
        print("Tego znaku tam nie ma")


#zgadywanie słów
print("Te znaki są częścią imienia tego boga,", present_letters)
guess = input("Teraz podaj jego imię...")
guess.capitalize
if guess == word:
    print("Zgadłeś")

elif guess != word:
    print("Nie zgadłeś, bogowie są wściekli")

#zakończenie
print("Ten bóg to ", word)
input()

        
