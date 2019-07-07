# napis = input("Podaj napis: ")

napis = "Ala ma kota"
liczniki = {}

# sposób 1
# for l in napis:
#     if l in liczniki:
#         liczniki[l] += 1
#     else:
#         liczniki[l] = 1
#
# # sposób 2
# for l in napis:
#     liczniki[l] = liczniki.get(l, 0) + 1

# sposób 3
# from collections import defaultdict
# liczniki = defaultdict(int)
# for l in napis:
#     liczniki[l] += 1

# sposób 4
for l in napis:
    liczniki[l] = napis.count(l)

dict()

print(liczniki)

