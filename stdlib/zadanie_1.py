import json

# [{...},{...},{...}]

def dodaj_pracownika(pracownicy):
    """
    Dodaje pracownika do listy
    :param pracownicy: list - Lista pracowników
    :return: list
    """
    imie = input("Imie: ")
    nazwisko = input("Nazwisko: ")
    rok_ur = int(input("Rok urodzenia: "))
    pensja = float(input("Pensa: "))

    pracownik = {
        "imie": imie,
        "nazwisko": nazwisko,
        "rok_ur": rok_ur,
        "pensja": pensja
    }
    pracownicy.append(pracownik)
    return pracownicy

def wypisz_pracownikow(pracownicy):
    for i, pracownik in enumerate(pracownicy, start=1):
        imie = pracownik['imie']
        nazwisko = pracownik['nazwisko']
        rok = pracownik['rok_ur']
        pensja = pracownik['pensja']
        print(f' - [{i}] {imie} {nazwisko} - rok: {rok}, pensja: {pensja} PLN')


def zaladuj_pracownikow():
    with open("pracownicy.json") as f:
        pracownicy = json.load(f)
    return pracownicy

def zapisz_pracownikow(pracownicy):
    with open("pracownicy.json", 'w') as f:
        json.dump(pracownicy, f)

def main():
    try:
        pracownicy = zaladuj_pracownikow()
    except FileNotFoundError:
        pracownicy = []
    wybor = input("Co chcesz zrobić? [d-dodaj, w-wypisz]")
    if wybor == 'd':
        pracownicy = dodaj_pracownika(pracownicy)
        zapisz_pracownikow(pracownicy)
    elif wybor == 'w':
        wypisz_pracownikow(pracownicy)

main()