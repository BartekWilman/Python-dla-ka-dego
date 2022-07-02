import random

#krotka słów do wyboru

GODS =("Khorne", "Slanesh", "Nurgle",
       "Tzeentch", "Malal", "Khaine",
       "Sigmar", "Morr", "Ulryk",
       "Grungi", "Grimir", "Valaya",
       "Rogaty Szczur", "Matka Nocy", "Ursun")

word = random.choice(GODS)
correct = word
jumble = ""
score = 0
hint = 0

#pętla mieszająca litery w wylosowanym słowie

while word:
    i = random.randrange(len(word))
    jumble += word[i]
    word = word[:i] + word[(i + 1):]

#powitanie i wyjaśnienie zasad gry

print("\t\t\t\t\t\t\t\a\a\a\a\awymieszane słowa".upper())
print("\n\n\n\nprogram zaraz wyświetli Ci pomieszane litery słowa losowo wybranego.")
print("Jako że jestem fanem Warhammera fantasy, kategorią są bogowie z tego uniwersum")



#początek gry
print("\n\n\n\nZgadnij, co to za bóg:", jumble.upper())

guess = input("Twoja odpowiedź to: ")

if guess == correct:
    score = len(correct) * 100 - (hint * 10)
    print("Zgadza się")
    print("Poprawna odpowiedź to", correct, ", a w trakcie gry uzyskałeś", score, "punktów\a")

elif guess != correct and guess != "":

    while guess != correct and guess != "":

        if guess != correct:

            print("Niestety nie...")

            #pytanie o podpowiedź
            ask = input("Chcesz podpowiedź? (T/N)... ")
            
            if ask == "T":
                print("Imię tego boga zaczyna się na", correct[0], ",a kończy na", correct[-1])
                hint += len(correct) / 3

            elif ask == "N":
                print("Słusznie, szkoda punktów ;)")

            guess = input("Twoja odpowiedź to: ")
            score = len(correct) * 100 - (hint * 10)
            print("Zgadza się")
            print("Poprawna odpowiedź to", correct, ", a w trakcie gry uzyskałeś", score, "punktów\a")

        elif guess == correct:
            score = len(correct) * 100 - (hint * 10)
            print("Zgadza się")
            print("Poprawna odpowiedź to", correct, ", a w trakcie gry uzyskałeś", score, "punktów\a")

print("Dzięki za udział w grze, mam nadzieję, że bawiłeś się tak samo dobrze jak ja pisząc ten program ;)")
input()
        
