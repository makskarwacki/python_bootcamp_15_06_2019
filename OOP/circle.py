from math import pi


class Circle:
    def __init__(self, radius=1):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, x):
        if x < 0:
            raise ValueError("Radius cannot be negative")
        else:
            self._radius = x

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return pi * self.radius ** 2

    def __str__(self):
        return f"Circle({self.radius})"

    def __repr__(self):
        return self.__str__()
