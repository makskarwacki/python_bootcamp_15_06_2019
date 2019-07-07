"""
Napisz funkcję, która wypisze n pierwszych wierszy trójkąta pascala

[1]
[1, 1]
[1, 2 , 1]


"""


def wypisz_trojkat(wiersze):
    out = ""
    for line in wiersze:
        out += str(line) + "\n"
    print(out)
    return out


def pretty_pascal_print(wiersze):
    max_length = len(" ".join(map(str, wiersze[-1])))
    for w in wiersze:
        print(" ".join(map(str, w)).center(max_length))


def trojkat_pascala(n):
    wiersz = [1]
    wiersze = [wiersz]
    for i in range(n - 1):
        nowywiersz = [1]
        for j in range(len(wiersz) - 1):
            nowywiersz.append(wiersz[j] + wiersz[j + 1])
        nowywiersz.append(1)
        wiersz = nowywiersz
        wiersze.append(wiersz)
    return wiersze


def gen_trojkat_pascala(n, r=[]):
    for x in range(n):
        length = len(r)
        # r = [1 if i==0 or i == length else r[i-1] + r[i] for i in range(length+1)]
        temp = []
        for i in range(length+1):
            if i == 0 or i == length:
                temp.append(1)
            else:
                temp.append(r[i-1] + r[i])
        r = temp
        yield r

# print(list(gen_trojkat_pascala(30)))


t = gen_trojkat_pascala(1)
pretty_pascal_print(list(t))
print("-" * 40)
t = gen_trojkat_pascala(2)
pretty_pascal_print(list(t))
print("-" * 40)
t = gen_trojkat_pascala(30)
pretty_pascal_print(list(t))


def test_trojkat_pascala():
    expected = """[1]
[1, 1]
[1, 2, 1]"""
    assert trojkat_pascala(3) == expected
