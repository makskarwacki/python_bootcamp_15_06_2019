class Konwerter:
    def int_to_roman(number):
        if number > 3999:
            raise ValueError('Wartości powyżej 3999 są niedozwolone, podałeś: {}'.format(number))
        print(number)
        if number < 0:
            raise ValueError('Liczba ujemna jest niedozwolona, podałeś: {}'.format(number))
        to_romain_tab = [(3000, "MMM"),
                         (2000, "MM"),
                         (1000, "M"),
                         (900, "CM"),
                         (800, "DCCC"),
                         (700, "DCC"),
                         (600, "DC"),
                         (500, "D"),
                         (400, "CD"),
                         (300, "CCC"),
                         (200, "CC"),
                         (100, "C"),
                         (90, "XC"),
                         (80, "LXXX"),
                         (70, "LXX"),
                         (60, "LX"),
                         (50, "L"),
                         (40, "XL"),
                         (30, "XXX"),
                         (20, "XX"),
                         (10, "X"),
                         (9, "IX"),
                         (8, "VIII"),
                         (7, "VII"),
                         (6, "VI"),
                         (5, "V"),
                         (4, "IV"),
                         (3, "III"),
                         (2, "II"),
                         (1, "I")
                         ]
        roman_numerals = []
        for value, numer in to_romain_tab:
            count = number // value
            number -= count * value
            if count > 0:
                roman_numerals.append(numer)
        return ''.join(roman_numerals)

    def roman_to_int(string):
        romanian_values = {'I': 1,
                           'V': 5,
                           'X': 10,
                           'L': 50,
                           'C': 100,
                           'D': 500,
                           'M': 1000}
        total = 0
        for i in range(len(string)):
            if i > 0 and romanian_values[string[i]] > romanian_values[string[i - 1]]:
                total += romanian_values[string[i]] - 2 * romanian_values[string[i - 1]]
            else:
                total += romanian_values[string[i]]
        return total


# print(Konwerter.int_to_roman(1000))
print(Konwerter.roman_to_int("MMMCMXCIX"))


def test_to_roman():
    assert Konwerter.int_to_roman(1) == "I"
    assert Konwerter.int_to_roman(4) == "IV"
    assert Konwerter.int_to_roman(3999) == "MMMCMXCIX"


def test_roman_to_number():
    assert Konwerter.roman_to_int("MMMCMXCIX") == 3999
    assert Konwerter.roman_to_int("IV") == 4
    assert Konwerter.roman_to_int("II") == 2
