
# Sposob 1
with open("data.txt", "rt") as f:
    while True:
        linia = f.readline()
        print(linia, end='')
        if not linia:
            break

print("\n===========================")

# Sposob 2
with open("data.txt", "rt") as f:
    for linia in f:
        print(linia, end='')

print("\n===========================")

#Sposob 3
lines = []
with open("data.txt", "rt") as f:
    lines = f.readlines()
for line in lines:
    print(line, end='')
