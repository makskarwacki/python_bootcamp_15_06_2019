"""
Napisz funkcję, która sprawdzi, czy podany napis
jest palindromem

"""
def is_palindrom(tekst: str) -> bool:
    tekst = tekst.lower()
    do_usuniecia = ' .,;?!-'
    for znak in do_usuniecia:
        tekst = tekst.replace(znak, "")
    # return tekst == tekst[::-1] # 1 rozwiązanie

    left = 0
    right = len(tekst) - 1

    while left <= right:
        if not tekst[left] == tekst[right]:
            return False
        left += 1
        right -= 1
    return True


def test_is_palindrom():
    # assert is_palindrom("ala") == True
    # assert is_palindrom("Ala") == True
    # assert is_palindrom("może jeż łysy łże jeżom") == True
    # assert id_palindrom("ala ma kota") == False

    assert is_palindrom("ala")
    assert is_palindrom("Ala")
    assert is_palindrom("możejeżłysyłżejeżom")
    assert is_palindrom("może jeż łysy łże jeżom")
    assert not is_palindrom("ala ma kota")
    assert is_palindrom("O, ty z Katowic, Iwo? Tak, Zyto")
