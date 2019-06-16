liczby = []

while len(liczby) < 10:
    odp = input("Podaj liczbę lub k by zakończyć: ")
    if odp == "k":
        break
    liczba = int(odp)
    liczby.append(liczba)

if len(liczby) > 0:
    srednia = sum(liczby) / len(liczby)
    print(f"Średnia z {liczby} wynosi {srednia}")
else:
    print("Nie wprowadziłeś liczb")
