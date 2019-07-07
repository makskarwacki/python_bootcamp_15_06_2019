def przytnij(data, start, stop):
    rezultat = []
    czy_dodawac = False

    for element in data:
        if start(element):
            czy_dodawac = True
        if stop(element):
            czy_dodawac = False

        if czy_dodawac:
            rezultat.append(element)
    return rezultat


def test_przytnij():
    actual = przytnij(
        data=[1, 2, 3, 4, 1, 6, 7],
        start=lambda x: x > 3,
        stop=lambda x: x == 6
    )

    assert actual == [4, 1, 7]


def test_przytnij_2():
    actual = przytnij(
        ["a", "b", "c", 2, 4, "dy", "x", 5, 6, "a", "b", "c", "dy", "x"],
        lambda x: isinstance(x, int),
        lambda x: isinstance(x, str),
    )
    assert actual == [2, 4, 5, 6]
