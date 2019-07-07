"""
Napisz funkcję, która:

1. dla listy, tupli, zbioru zwróci sumę elementów
2. jeśli argument będzie słownikiem, to zwróci sumę wartości
3. Jeśli wartości są stringami to sumuj te, które da sie zrzutowac na liczby
"""


def to_numeric(value):
    if isinstance(value, str) and value.isnumeric():
        return int(value)
    elif isinstance(value, bool):
        return None
    elif isinstance(value, int):
        return value


def my_sum(numbers):
    if isinstance(numbers, dict):
        numbers = numbers.values()
    data = []
    for n in numbers:
        data.append(to_numeric(n))
    return sum(data)


def test_sum_for_list():
    assert my_sum([1, 2, 3]) == 6
    assert my_sum([1, 2, 3, 'a']) == 6
    assert my_sum(['1', 2, '3', 'a']) == 6
    # assert my_sum(['1', (2, 2, 2), '3', 'a']) == 10


def test_sum_for_set():
    assert my_sum({1, 2, 3, 4}) == 10
    assert my_sum({1, 2, 3, 'a'}) == 6
    assert my_sum({'1', 2, '3', 'a'}) == 6


def test_sum_for_tuple():
    assert my_sum((1, 2, 3, 4, 5)) == 15


def test_my_sum_for_dict():
    assert my_sum({'a': 1, "b": 11, 'c': 'a'}) == 12


def test_to_numeric():
    assert to_numeric(True) == None
    assert to_numeric("") == None