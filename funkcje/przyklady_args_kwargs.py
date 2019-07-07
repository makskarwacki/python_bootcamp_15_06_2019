
slownik = {'a': 1, 'b': 2}
mapowanie = {'a':'c', 'b':'d'}
tekst1 = "aa bb ab"
tekst2 = "cc dd ac"
output = "cc dd cd cc dd cc"

def mapownik(*teksty, **kwargs):
    tekst = " ".join(teksty)

    for znak in kwargs:
        print(f"zamieniam {znak} na {kwargs[znak]}")
        tekst = tekst.replace(znak, kwargs[znak])
    return tekst

assert mapownik(tekst1, tekst2, a='c', b='d') == output

#
#
# def jakas_funkcja(*args, **kwargs):
#     print('args', args)
#     print('kwargs', kwargs)
#
# jakas_funkcja(10, 20, c=10, g=11, **slownik)
# jakas_funkcja(10, 20, c=10, g=11, a=1, b=2)

# def sumator(a, *b, c=10, d=11, **kwargs):
#     print(a, type(a))
#     print(b, type(b))
#     #print(lala)
#     return a+sum(b) + c+d
#
# def test_sumator():
#     # assert sumator() == 0
#     assert sumator(1) == 22
#     assert sumator(1, 1) == 23
#     assert sumator(1, 1, 5, 6, 7) == 41
#     assert sumator(1, 1, 5, 6, 7, 8) == 49
#     assert sumator(1, 1, 5, 6, 7, 8, 10) == 59
#
