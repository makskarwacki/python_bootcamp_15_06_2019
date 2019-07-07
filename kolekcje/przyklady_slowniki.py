osoba = {
    "imie": "Rafał",
    "nazwisko": "Korzeniewski",
    "hobby": ["muzyka", "historia", "..."],
    "dzieci": {"corka1":"Gabriela" },
    1: "jeden"
}
dzieci = osoba['dzieci']
dzieci["corka1"] = "Gabi"

osoba["sport"] = ["armwrestling"]
# print(osoba)
#
# print(osoba.get("zona", "brak"))
# print(osoba.get("dlugi", "brak"))
#
#
# print(osoba.keys())
# print(osoba.values())
# print(osoba.items())


# for k in osoba:
#     print(k)
#
# if "zona" in osoba:
#     print(osoba['zona'])
#
#
# print(dir(osoba))

print(osoba.pop('sport'))
print(osoba)

print(osoba.popitem())