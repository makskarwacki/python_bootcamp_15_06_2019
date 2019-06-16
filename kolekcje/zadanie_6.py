
lista = [55, 10, 1, 17, 11, 20, 25]

# v_min = min(lista)
# v_max = max(lista)
#
# i_min = lista.index(v_min)
# i_max = lista.index(v_max)
#
# lista[i_min] = v_max
# lista[i_max] = v_min

i_min = 0
i_max = 0

for i in range(len(lista)):
    if lista[i] < lista[i_min]:
        i_min = i
    if lista[i] > lista[i_max]:
        i_max = i

# temp = lista[i_max]
# lista[i_max] = lista[i_min]
# lista[i_min] = temp

lista[i_max], lista[i_min] = lista[i_min], lista[i_max]
assert lista == [1, 10, 55, 17, 11, 20, 25]
