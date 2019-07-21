class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.length() < other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return Vector.__mul__(self, other)

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)


def test_vector_add():
    v1 = Vector(1, 2)
    v2 = Vector(2, 3)

    result = v1 + v2
    assert result.x == 3
    assert result.y == 5


def test_vector_sub():
    v1 = Vector(1, 3)
    v2 = Vector(4, 7)

    result = v1 - v2
    assert result.x == -3
    assert result.y == -4


def test_vector_equal():
    v1 = Vector(1, 3)
    v2 = Vector(1, 3)

    assert v1 == v2


def test_vector_lower_than():
    v1 = Vector(4, 4)
    v2 = Vector(1, 1)

    assert v2 < v1
    assert v1 > v2


def test_vector_lte():
    v1 = Vector(4, 4)
    v2 = Vector(1, 1)

    assert v2 <= v1
    assert v1 >= v2

def test_vector_length():
    v = Vector(3, 4)
    assert v.length() == 5


def test_vector_multiplication():
    v1 = Vector(2, 3)
    x = 5
    v2 = Vector(2, 2)

    result = v1 * x
    assert result.x == 10
    assert result.y == 15

    assert v1 * v2 == 10  # iloczyn skalarny

    result2 = x * v1
    assert result2.x == 10
    assert result2.y == 15
