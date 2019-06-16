# import random
# random.randint
from random import randint

DEBUG = True

gracz_x = randint(0, 10)
gracz_y = randint(0, 10)

skarb_x, skarb_y = randint(0, 10), randint(0, 10)
odleglosc_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

liczba_ruchow = 0

if DEBUG:
    print(f"Położenie skarbu to: ({skarb_x}, {skarb_y})")
    print(f"Położenie gracza to: ({gracz_x}, {gracz_y})")
    print(f"Odległość po wylosowaniu to: {odleglosc_po_wylosowaniu}")

while True:

    kierunek = input("Podaj kierunek [w-góra, a-lewom, d-prawo, s-dół]: ")
    przed_ruchem = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    if kierunek == "w":
        gracz_y += 1
    elif kierunek == "a":
        gracz_x -= 1
    elif kierunek == "s":
        gracz_y -= 1
    elif kierunek == "d":
        gracz_x += 1

    if gracz_x < 0 or gracz_x > 10 or gracz_y < 0 or gracz_y > 10:
        print("Wypadłeś poza świat. Zginąłeś!!")
        break

    po_ruchu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    liczba_ruchow += 1

    if po_ruchu == 0:
        print("Znalazłeś Skarb! Wygrałeś")
        print(f"Wykonałeś {liczba_ruchow} ruchów")
        break

    if DEBUG:
        print(f"Położenie skarbu to: ({skarb_x}, {skarb_y})")
        print(f"Położenie gracza to: ({gracz_x}, {gracz_y})")

    los = randint(1, 5)
    if DEBUG:
        print("Los: ", los)
    if los != 3:
        if po_ruchu > przed_ruchem:
            print("Zimno")
        else:
            print("Ciepło")
    else:
        print("Jestem złośliwy nie podpowiem ci!")

    if liczba_ruchow > odleglosc_po_wylosowaniu * 2:
        skarb_x, skarb_y = randint(0, 10), randint(0, 10)
        odleglosc_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
        liczba_ruchow = 0
        print("Jesteś gapa. Skarb zmienił położenie.")
        if DEBUG:
            print(f"Położenie skarbu to: ({skarb_x}, {skarb_y})")
            print(f"Położenie gracza to: ({gracz_x}, {gracz_y})")


