def splaszcz(lista):
    rezultat = []
    for el in lista:
        if isinstance(el, list):
            rezultat.extend(splaszcz(el))
        else:
            rezultat.append(el)
    return rezultat


def test_splaszcz():
    assert splaszcz([]) == []
    assert splaszcz([1, 2, 3]) == [1, 2, 3]
    assert splaszcz([1, 2, [3, [4]]]) == [1, 2, 3, 4]
