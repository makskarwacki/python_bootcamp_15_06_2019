
print("Liczby podzielne przez 3 lub 5: ")
print()
liczby = []
for i in range(101):
    if i % 3 == 0 or i % 5 == 0:
        liczby.append(i)
        print(i)


print(f"W przedziale 0-100 jest {len(liczby)} liczb podzielnych przez 3 lub 5")