
napis = input("Podaj napis: ")
SAMOGLOSKI = "aeiou"
ile = 0

for litera in napis.lower():
    if litera in SAMOGLOSKI:
        ile += 1

print(f"Znaleziono {ile} samogłosek")

