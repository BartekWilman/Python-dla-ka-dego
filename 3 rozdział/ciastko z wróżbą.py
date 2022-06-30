import random

print("\t\t\t CIASTKO Z WRÓŻBĄ \a")


input("Przeczytaj swoją wróżbę")


print("Twoja wróżba to...")


wrozba = random.randint(1, 5)

if wrozba == 1:
    print("Obserwuj niebo")

elif wrozba == 2:
    print("Nie marnuj jedzenia, a nie zgłodniejesz")

elif wrozba == 3:
    print("Bądź dobry, ale nie przesadnie miły")

elif wrozba == 4:
    print("Doceniaj to co masz")

elif wrozba == 5:
    print("Szanuj rodziców")

input("Ciastko zjedzone, wróżba przeczytana, pora kończyć")
