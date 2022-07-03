"""kreator postaci"""


skills = [["Siła", 0], ["Zdrowie", 0], ["Mądrość", 0], ["Zwinność", 0]]
skill_points = 30

ask_1 = None
ask_2 = None
menu = None
print("\t\t\tKreator postaci")
print("Masz 30 punktów do rozdania między: siłę, zdrowię, mądrość i zwinność")
print("W każdej chwili możesz dodać, zmniejszyć lub po prostu sprawdzić wartość atrybutów")

while menu != "0":
    print("""Wybierz co chcesz zrobić:
             1 - obejrzyj swoje atrybuty
             2 - zwiększ swoje atrybuty
             3 - zmniejsz swoje atrybuty
             0 - zakończ""")
#wybór opcji z menu
    menu = str(input("CHCĘ: "))

#obejrzenie statystyk   
    if menu == "1":
        for skill in range(len(skills)):
            print(skills[skill - 1], "\n")

#dodawanie punktów
    elif menu == "2":
        while ask_1 != "0":
            ask = input("""Który atrybut chcesz zwiększyć?
                    1 - Siła
                    2 - Zdrowie
                    3 - Mądrość
                    4 - Zwinność
                    0 - Wróćmy do menu główneg
                    Wybieram: """)
            
            if ask == "1":
                if skill_points > 0:
                    skills[0][1] += 1
                    skill_points -= 1
                    print("Twoja siła wzrosła o 1")
                    print(skills[0])
                    input("\nKontynuuj\n")
                elif skill_points <= 0:
                    print("Brakuje Ci punktów umiejętności")
                    input()

            elif ask == "2":
                if skill_points > 0:
                    skills[1][1] += 1
                    skill_points -= 1
                    print("Twoje zdrowie wzrosło o 1")
                    print(skills[1])
                    input("\nKontynuuj\n")
                elif skill_points <= 0:
                    print("Brakuje Ci punktów umiejętności")
                    input()

            elif ask == "3":
                if skill_points > 0:
                    skills[2][1] =+ 1
                    skill_points -= 1
                    print("Twoja mądrość wzrosła o 1")
                    print(skills[2])
                    input("\nKontynuuj\n")
                elif skill_points <= 0:
                    print("Brakuje Ci punktów umiejętności")
                    input()

            elif ask == "4":
                if skill_points > 0:
                    skills[3][1] += 1
                    skill_points -= 1
                    print("Twoja zwinność wzrosła o 1")
                    print(skills[3])
                    input("\nKontynuuj\n")
                elif skill_points <= 0:
                    print("Brakuje Ci punktów umiejętności")
                    input()

            elif ask == "0":
                print("Niech tak będzie")
                input("\nKontynuuj\n")
                break

            else:
                print("Niepoprawny wybór\n")

#odejmowanie punktów
    elif menu == "3":
        while ask_2 != "0":
            ask = input("""Który atrybut chcesz zmniejszyć?
                    1 - Siła
                    2 - Zdrowie
                    3 - Mądrość
                    4 - Zwinność
                    0 - Wróćmy do menu główneg
                    Wybieram: """)
            if ask == "1" and skills[0][1] > 0:
                skills[0][1] -= 1
                skill_points += 1
                print("Twoja siła zmalała o 1")
                print(skills[0][1])
                input("\nKontynuuj\n")

            elif ask == "2" and skills[1][1] > 0:
                skills[1][1] -= 1
                skill_points += 1
                print("Twoje zdrowie zmalało o 1")
                print(skills[1][1])
                input("\nKontynuuj\n")

            elif ask == "3" and skills[2][1] > 0:
                skills[2][1] -= 1
                skill_points =+ 1
                print("Twoja mądrość zmalała o 1")
                print(skills[2][1])
                input("\nKontynuuj\n")
    
            elif ask == "4" and skills[3][1] > 0:
                skills[3][1] -= 1
                skill_points =+ 1
                print("Twoja zwinność zmalała o 1")
                print(skills[3][1])
                input("\nKontynuuj\n")

            elif ask == "0":
                print("Niech tak będzie")
                input("\nKontynuuj\n")
                break

            else:
                print("Wybrany atrybut jest za słaby, lub dokonałeś błędnego wyboru\n")
    elif menu == "0":
        print("Kończymy")
        
    else:
        print("Niepoprawny wybór\n")
        
print("Żegnam \a\a\a")
input()
