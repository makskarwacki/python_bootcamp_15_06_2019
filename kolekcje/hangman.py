slowo = "python"  # można by losowac słowo.. albo jakas inną metoda je pobierać
wynik = ["_" for x in slowo]
# co jest równoważne temu:
# wynik = []
# for x in slowo:
#     wynik.append('_')
szanse = len(slowo) + 3
while True:
    if szanse == 0:
        print("Przegrałeś")
        break
    znak = input("Wprowadź znak: ")

    if znak not in slowo:
        szanse -= 1
    i = 0  # gdy używam enumerate to znika
    # for i, litera in enumerate(slowo)
    for litera in slowo:
        if znak == litera:
            wynik[i] = znak
        i += 1  # gdy używam enumerate to znika

    if "".join(wynik) == slowo:
        print("Wygrałeś!")
        break
    else:
        print(f"Pozostało szans: {szanse}")
        print("".join(wynik))
