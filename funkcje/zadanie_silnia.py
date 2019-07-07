def silnia(x):
    if x == 0:
        return 1
    return x * silnia(x-1)
    # 5 * 4 * 3 * 2 * 1 * 1


def test_silnia():
    assert silnia(3) == 6
    assert silnia(0) == 1

