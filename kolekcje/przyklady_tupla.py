zmienna1 = 0
a = 200
my_tuple = (1, 2, 3, 'a', 'b', 'c', 'a', zmienna1, a)
print(type(my_tuple))
print(my_tuple)
print(dir(my_tuple))
print(my_tuple.count(0))
print(my_tuple.index('a'))
print(my_tuple[-1])
print(my_tuple[1:6])
print(my_tuple[1:8:2])
print(my_tuple[::2])
print(my_tuple[::-2])

t1 = (1, 2, 3)
print(id(t1))
t2 = (4, 5, 6)

t1 = t1 + t2
print(id(t1))


# pusta tupla

x = tuple()
print(tuple(range(10)))
#print(t1+ t2)