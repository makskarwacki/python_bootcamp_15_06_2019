moja_lista = [1, 2, 3, "a", "b", "c"]
moja_lista2 = [11, 12, "xx", "ab", "bv", "cd"]
# print(type(moja_lista))
# print(dir(moja_lista))
#
# moja_lista.append(5)
# print(moja_lista)
#
# moja_lista.append([5, 6, 7])
# print(moja_lista)
#
# print(help(moja_lista.insert))
# moja_lista.insert(1, "d")
# print(moja_lista)
#
# print([1, 2, 3] + [7, 8, 9])
# c = [9, 1, 5, 3, 2]
# print(c.sort(reverse=True))
# print(c.pop())
# print(c)
# d = [1, 2 , 3]
# d[1] = 6
# d.extend([5, 6, 7])
# print(d)

# operuje na elementach
for el in moja_lista:
    # tu jest ciało pętli for
    print(el)
print()

# operuje na inde
for i in range(len(moja_lista)):
    # tu jest ciało pętli for
    print(str(moja_lista[i]) + str(moja_lista2[i]))
