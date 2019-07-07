"""
Napisz funkcję, która sprawdzi, czy zadana liczba jest liczbą doskonałą

6
1 + 2 + 3

6
28
496
8128



"""


def czy_doskonala(x):
    suma = 0
    for i in range(1, x):
        if x % i == 0:
            suma += i
    return x == suma


def test_czy_doskonala():
    assert czy_doskonala(6)
    assert czy_doskonala(28)
    assert czy_doskonala(496)
    assert czy_doskonala(8128)
    assert not czy_doskonala(24)
