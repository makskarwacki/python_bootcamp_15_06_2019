# 1. stworz slownik przechowujacy informacje o produktach i ich cenach
# 2. wypisz
# Nasz zieleniak oferuje:
# - pomidory: 2.55 PLN
# - ogorki:   3.55 PLN
# ...
# Co chcesz kupić? ogorki
# Ile chcesz kupić [ogorki]? 2
# Za ogorki placisz: 7.10 PLN

produkty = {
    "pomidory": 3.65,
    "ogorki": 2.95,
    "ziemniaki": 1.99
}
magazyn = {
    "pomidory": 40,
    "ogorki": 40,
    "ziemniaki": 40
}

# deklinacje = {
#     'ogorki': {
#         "mianownik": "ogorki",
#         "dopelniacz": "ogorka",
#         "xxx": "ogórków"
#     }
# }

# interakcja
print("Nasz zieleniak oferuje: ")
for p in produkty:
    print(f" - {p}: {produkty[p]} PLN")

co = input("Co chcesz kupić? ")
ile = float(input(f"Ile chcesz kupić [{co}]? "))
if ile > magazyn[co]:
    print("Nie mam tyle produktu")
else:
    koszt = ile * produkty[co]
    magazyn[co] -= ile
    print(f"Do zapłaty: {koszt:.2f}")

print(f"Magazyn: {magazyn}")
