lista = [9,1,6,8,4,3,2,0]

for i in range(len(lista)):
    print(i, lista[i:])
    # znajdz najmniejszy w takim podzbiorze

    min_v = lista[i:][0]
    i_min_v = 0
    for j in lista[i:]:
        if j < min_v:
            min_v = j
            i_min_v = lista[i:].index(j)

    # temp = lista[i]
    # lista[i] = lista[i+i_min_v]
    # lista[i+i_min_v] = temp
    lista[i], lista[i + i_min_v] = lista[i + i_min_v],  lista[i]

    print("Po zmianie: ", lista)
    print("znalezione min to: ", min_v, i_min_v)