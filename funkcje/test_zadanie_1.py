from zadanie_1 import czy_jest_pierwsza

def test_czy_jest_pierwsza_dla_l_pierwsze():
    assert czy_jest_pierwsza(2)
    assert czy_jest_pierwsza(3)
    assert czy_jest_pierwsza(11)


def test_czy_jest_pierwsza_dla_l_nie_pierwszej():
    assert czy_jest_pierwsza(4) is False
    assert czy_jest_pierwsza(12) is False
    assert czy_jest_pierwsza(21) is False
