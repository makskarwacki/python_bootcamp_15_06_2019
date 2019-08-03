import math

def oblicz_delte(a, b, c):
    return b*b - 4 * a * c

def miejsca_zerowe(a, b, c):
    delta = oblicz_delte(a, b, c)
    if delta<0:
        return None
    if delta==0:
        wynik = -b/(2*a)
        return wynik, wynik
    wynik1 = (-b - math.sqrt(delta))/(2*a)
    wynik2 = (-b + math.sqrt(delta))/(2*a)
    return wynik1, wynik2
