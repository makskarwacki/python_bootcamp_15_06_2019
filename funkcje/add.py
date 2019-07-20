def check_sizes(*args):
    sizes = set()
    for m in args:
        n_row = len(m[0])
        for row in m:
            if len(row) != n_row:
                raise ValueError("Liczba kolumn w wierszach nie jest taka sama")
        sizes.add((len(m), len(m[0])))

    if len(sizes) > 1:
        raise ValueError("Wymiary macierzy nie zgadzają się")

def add(*args):

    check_sizes(*args)

    result = []
    for i in range(len(args[0])):
        row = []
        for j in range(len(args[0][i])):
            x = 0
            for m in args:
                x += m[i][j]
            row.append(x)
        result.append(row)
    return result

print(__name__)

if __name__ == "__main__":
    a = [[10, 20], [30, 40]]
    b = [[11, 22], [33, 44]]

    print(add(a, b))


