import random

print("Odwrócone jaka to liczba.\n\n\n".upper())
print("pomyśl o jakieś liczbie z przedziału od 1 do 100\n\n")

start = 1
finish = 100

ans = random.randint(1, 10)

print("Sądzę, że ta liczba to:", ans)
solution = ""

while solution !="OK":
    
    solution = input("Czy mam rację, mniej, czy więcej? ")
    
    if solution == "mniej":
        finish = (ans - 1)
        ans = random.randint(start, finish)
        print("Sądzę, że ta liczba to: ", ans)

    elif solution == "więcej":
        start = (ans + 1)
        ans = random.randint(start, finish)
        print("Sądzę, że ta liczba to: ", ans)

    elif solution == "OK":
        print("Brawo ja")

    else:
        print("Możesz napisać \"OK\", \"mniej\", \"więcej\"")
        ans = random.randint(start, finish)
        print("Sądzę, że ta liczba to: ", ans)

    

print("\n\n\n\n\aUdało mi się zgadnąć twoją liczbę, jest to:", ans)
input()


