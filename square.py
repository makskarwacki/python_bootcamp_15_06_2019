from math import sqrt


class Square:

    def __init__(self, a):
        self._a = a

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, x):
        if x < 0:
            raise ValueError("Bok nie może być mniejszy niż 0")
        else:
            self._a = x

    @property
    def area(self):
        return self._a ** 2

    @area.setter
    def area(self, x):
        self._a = sqrt(x)


kw = Square(3)
kw.a = 10
print(kw.a)

kw.a = -10