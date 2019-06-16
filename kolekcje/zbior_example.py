A = {1, 2, "a", 0, "cc", 3}
B = {3, 4, 5}

# x = set()
print(type(A))
print(A | B)

print(A & B)

print(A-B)
print(A^B)

A.add(7)
print(A)

for i in A:
    print(i)