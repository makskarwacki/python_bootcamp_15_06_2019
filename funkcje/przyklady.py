def nazwa(a: int) -> str:
    """
    Return '-' times a
    example:
    >>> nazwa(10)
    '----------'

    :param a: int
    :return: str
    """

    return "-"*a

a = 5
b = 0

print("Przed")
print('a', a)
print('b', b)


def podkreslenie(a):
    global b
    b += 1
    a = 15
    print("W środku")
    print('a', a)
    print('b', b)


def wieksze_niz_2(a):
    if a > 2:
        return True
    return False

podkreslenie(10)

print("Po")
print('a', a)
print('b', b)
