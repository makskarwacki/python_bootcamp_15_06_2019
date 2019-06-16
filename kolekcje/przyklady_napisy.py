napis = "Ala ma kota"

print(napis[0])
print(len(napis))
print(napis.index('m'))
print(napis[::-1])

for litera in napis:
    print(litera)
z = "k"
print(z in "aeiou")

print("B" in napis)
for i in napis.lower():
    if i in samogloski:
        licznik += 1