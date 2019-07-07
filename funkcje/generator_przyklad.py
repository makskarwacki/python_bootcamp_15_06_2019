
def kolejne_liczby(n):
    for i in range(n):
        yield i**2


print(list(kolejne_liczby(10)))
for liczba in kolejne_liczby(10):
    print(liczba)

x = kolejne_liczby(10)
print(x.__next__())