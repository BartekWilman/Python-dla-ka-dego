import random

print("\t\t\t\t\t STO RZUTÓW MONETĄ")

orzel = 0
reszka = 0

kolejka = 1

while kolejka < 101:
    rzut = random.randint(1,2)

    if rzut == 1:
        orzel +=1
        kolejka += 1

    elif rzut == 2:
        reszka += 1
        kolejka += 1

print("Po wykonaniu stu rzutów monetą przez program, reszka wypadła",
      reszka, "razy, a orzeł", orzel)
input()
