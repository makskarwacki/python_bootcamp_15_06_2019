# slownik = {}
slownik = dict()

print(slownik, type(slownik))

slownik["a"] = "arbuz"
slownik["b"] = "banan"

print(slownik)

osoba = {
    "imie": "Rafał",
    "nazwisko": "Korzeniewski",
    "zawod": "programista",
    1: "a",
    (1, 2): "lista",
    type: "funkcja"
}

print(osoba)
print(osoba["zawod"])
print(osoba[(1, 2)])

print("imie" in osoba)
print(osoba.items())

osoba["wyksztalcenie"] = "podyplomowe"

print(osoba.get("wzrost", 176))

print(dir(osoba))
print(osoba.pop("wyksztalcenie"))
print(osoba)