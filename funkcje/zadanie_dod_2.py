"""

Napisz funkcję (lub funkcje), które zwrócą maksylną spośród 3 liczb.

W rozwiązaniu skorzystaj tylko z możliwości definiowania funkcji i
używania operatorów porównania.

"""


def max_of_two(x, y):
    if x > y:
        return x
    return y


def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))

def max_of_four(t, x, y, z):
    return max_of_two(t, max_of_two(x, max_of_two(y, z)))

def test_max_of_three():
    assert max_of_three(3, 6, -5) == 6
    assert max_of_three(10, 20, 100) == 100


def test_max_of_four():
    assert max_of_four(3, 6, -5, 2) == 6
    assert max_of_four(10, 20, 100, 50) == 100
