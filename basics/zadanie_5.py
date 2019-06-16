
miasto_a = input("Miasto A: ")
miasto_b = input("Miasto B: ")

dystans = float(input(f"Dystans {miasto_a}-{miasto_b }: "))
cena = float(input("Cena paliwa: "))
spalanie = float(input("Spalanie na 100 km: "))
print()

koszt = (dystans / 100) * spalanie *  cena
koszt = round(koszt, 0)

print("Koszt przejazdu",miasto_a + "-" + miasto_b , koszt ,"PLN")
print(f"Koszt przejazdu {miasto_a}-{miasto_b} {koszt} PLN")