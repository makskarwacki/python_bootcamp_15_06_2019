# class Osoba:
#     nazwisko = "Korzeniewski" # atrybut klasowy
#
#     def __init__(self, imie):
#         self.imie = imie  # atrybuty instancji
#         self.wiek = 10
#
#     def __str__(self):
#         return (f"Instancja klasy Osoba: {self.imie}")
#
#     def przedstaw_sie(self):
#         return f"Cześć, jestem {self.imie} {self.nazwisko}"
#
# os1 = Osoba("Rafał")
# os2 = Osoba("Dominka")
# os3 = Osoba("Stanisław")
#
# os1.nazwisko  = "Wyspiański"
# Osoba.nazwisko = "Rej"
#
# print(os1.nazwisko)
# print(os2.nazwisko)
# print(os3.przedstaw_sie())
#
# Osoba.przedstaw_sie(os3)
#
# os1.imie = "Krzys"
# os2.imie = "Ania"
# # os3.imie = "123"
#
# print(os1)
# print(os2)
# print(os3)
#
#
# print(dir(os1))
# x = object()
# print(dir(x))
#
# print(os1 == os2)
# print(isinstance(os1, object))
# print(isinstance("ala", object))
#


class Animal:

    def __init__(self, name):
        self.name = name

    def sound(self):
        x = 1
        print("Unknown")
        return x

class Dog(Animal):

    def __init__(self, name, race):
        super().__init__(name)
        self.race = race

    @property
    def sound(self):
        x = super().sound()
        print("How how")
        print(x)

a = Dog("Rex", "Pudel")
print(dir(a))
a.sound
print(a.name)


class Dlugosc():
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Dlugosc(self.value + other.value)

    def __eq__(self, other):
        return self.value == other.value

d = Dlugosc(10)
print(isinstance(d, Dlugosc))


class Foo:

    def __init__(self):
        self.x = 10

    def bar(self):
        print("Coś tam")

    @classmethod
    def baz(cls):
        print(cls)
        print(cls.x)

    @staticmethod
    def fight(a, b):
        for i in range(10):
            a.get_damage()

f = Foo()
f.baz()
