
liczby_parzyste_0_100 = set(range(0, 100, 2))

liczby = set()
while True:
    komenda = input("Podaj liczbę lub k by zakończyć ")
    if komenda == 'k':
        break
    else:
        liczby.add(int(komenda))

print(f"Liczb parzystych w zakresie od 0 do 100 było: {len(liczby & liczby_parzyste_0_100)}")
