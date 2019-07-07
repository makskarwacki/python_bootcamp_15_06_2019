def czy_jest_pierwsza(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def test_czy_jest_pierwsza_dla_l_pierwsze():
    assert czy_jest_pierwsza(2)
    assert czy_jest_pierwsza(3)
    assert czy_jest_pierwsza(11)


def test_czy_jest_pierwsza_dla_l_nie_pierwszej():
    assert czy_jest_pierwsza(4) is False
    assert not czy_jest_pierwsza(12)
    assert czy_jest_pierwsza(21) == False
