# cena samochody
# obliczanie ceny auta funkcjami int

cena_netto = int(input("ile kosztuje ten samochód bez dodatkowych opłat? "))

prowizja_dealera = 300
print ("Koszt prowizji dla dealera", prowizja_dealera)

opłata_za_sprowadzenie = 200
print("Koszt sprowadzenia", opłata_za_sprowadzenie)

ubezpieczenie = cena_netto * 0.3
print("Koszt ubezpieczenia", ubezpieczenie)

podatek_od_spalin = cena_netto * 0.4
print("Koszt podatku od spalin", podatek_od_spalin)


total = cena_netto + prowizja_dealera +opłata_za_sprowadzenie + ubezpieczenie + podatek_od_spalin
print("Ostatecznie, należy zapłacić",total)

input("Enter")
