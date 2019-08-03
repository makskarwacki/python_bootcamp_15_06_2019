class Konwerter:

    @staticmethod
    def int_to_roman(number):
        number = str(number)
        number = "0" * (4 - len(number)) + number
        result = ""
        for n in number:
            if number.index(n) == 3:
                b = int(n)
                if b == 0:
                    continue
                if 0 < b < 4:
                    result += "I" * b
                if b == 4:
                    result += "IV"
                if b == 5:
                    result += "V"
                if 5 < b < 9:
                    result += "V" + "I" * (b - 5)
                if b == 9:
                    result += "IX"

            elif number.index(n) == 2:
                b = int(n)
                if b == 0:
                    continue
                if 0 < b < 4:
                    result += "X" * b
                if b == 4:
                    result += "XL"
                if b == 5:
                    result += "L"
                if 5 < b < 9:
                    result += "L" + "X" * (b - 5)
                if b == 9:
                    result += "XC"

            elif number.index(n) == 1:
                b = int(n)
                if b == 0:
                    continue
                if 0 < b < 4:
                    result += "C" * b
                if b == 4:
                    result += "CD"
                if b == 5:
                    result += "D"
                if 5 < b < 9:
                    result += "D" + "C" * (b - 5)
                if b == 9:
                    result += "CM"

            elif number.index(n) == 0:
                b = int(n)
                if b == 0:
                    continue
                if 0 < b < 4:
                    result += "M" * b
                if b >= 4:
                    break
            number = number.replace(n, "0", 1)

        return result

    @staticmethod
    def roman_to_int(number):
        result = set()
        number += "000"
        for n in number:
            i = number.find(n)
            if n == "0":
                continue
            elif n == "M":
                if number[i + 2] == "M":
                    result.add(3000)

                elif number[i + 1] == "M":
                    result.add(2000)

                else:
                    result.add(1000)

            elif n == "C":
                if number[i + 2] == "C":
                    result.add(300)

                elif number[i + 1] == "C":
                    result.add(200)

                elif number[i + 1] == "M":
                    result.add(900)

                elif number[i + 1] == "D":
                    result.add(400)

                else:
                    result.add(100)

            elif n == "D":
                if number[i + 3] == "C":
                    result.add(800)

                elif number[i + 2] == "C":
                    result.add(700)

                elif number[i + 1] == "C":
                    result.add(600)

                elif number[i - 1] != "C":
                    result.add(500)

            elif n == "X":
                if number[i + 2] == "X":
                    result.add(30)

                elif number[i + 1] == "X":
                    result.add(20)

                elif number[i + 1] == "C":
                    result.add(90)

                elif number[i + 1] == "L":
                    result.add(40)

                else:
                    result.add(10)

            elif n == "L":
                if number[i + 3] == "X":
                    result.add(80)

                elif number[i + 2] == "X":
                    result.add(70)

                elif number[i + 1] == "X":
                    result.add(60)

                elif number[i - 1] != "X":
                    result.add(50)

            elif n == "I":
                if number[i + 2] == "I":
                    result.add(3)

                elif number[i + 1] == "I":
                    result.add(2)

                elif number[i + 1] == "X":
                    result.add(9)

                elif number[i + 1] == "V":
                    result.add(4)

                else:
                    result.add(1)

            elif n == "V":
                if number[i + 3] == "I":
                    result.add(8)

                elif number[i + 2] == "I":
                    result.add(7)

                elif number[i + 1] == "I":
                    result.add(6)

                elif number[i - 1] != "I":
                    result.add(5)
        return sum(result)

    @staticmethod
    def cel_to_farh(cel):
        if cel == 0:
            result = 32.0

        else:
            result = 32.0 + cel * 1.8

        return result

    @staticmethod
    def farh_to_cel(farh):
        if farh == 32:
            result = 0
        else:
            result = (farh - 32) * 5 / 9

        return result


print(Konwerter().roman_to_int("IV"))


class Test_konwerter:

    def test_konwerter_to_roman_numbers(self):
        assert Konwerter().int_to_roman(1) == "I"
        assert Konwerter().int_to_roman(4) == "IV"
        assert Konwerter().int_to_roman(3999) == "MMMCMXCIX"

    def test_konwerter_from_roman_numbers(self):
        assert Konwerter().roman_to_int("MMMCMXCIX") == 3999
        assert Konwerter().roman_to_int("IV") == 4
        assert Konwerter().roman_to_int("II") == 2

    def test_konwerter_cel_to_farh(self):
        assert Konwerter().cel_to_farh(0) == 32.0
        assert Konwerter().cel_to_farh(-6) == 21.2
        assert Konwerter().cel_to_farh(20) == 68.0

    def test_konwerter_farh_to_cel(self):
        assert Konwerter().farh_to_cel(32.0) == 0
        assert Konwerter().farh_to_cel(21.2) == -6.0
        assert Konwerter().farh_to_cel(68.0) == 20.0


class Osoba:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show(self):
        print(f"{self.name}, email: {self.email}")


class Adres:
    def __init__(self, street, city):
        self.street = street
        self.city = city

    def show(self):
        print(f"adres: {self.street}, {self.city}")


class Kontakt(Osoba, Adres):
    def __init__(self, person, address):
        self.person = person
        self.address = address

    def show(self):
        print(f"""
{Osoba.show(self.person)},
{Adres.show(self.address)}
""")


class Notebook(Kontakt):
    def __init__(self):
        self.storage = []
        self.contact = Kontakt()

    def add(self, name, email, street, city):
        self.person = Osoba(name, email)
        self.address = Adres(street, city)
        self.contact = Kontakt(self.person, self.address)
        self.storage.append(self.contact)

    def show(self, name):
        pass


os = Osoba("Zenek", "cos tam")
# os.show()

ad = Adres("Rynek 7", "Gdańsk")
# ad.show()

contact = Kontakt(os, ad)
contact.show()
