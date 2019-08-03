

f = open("data.txt", "rt")
print("Czy zamknięty = {}".format(f.closed))
f.close()
print("Czy zamknięty = {}".format(f.closed))

print("==========================")

with open("data.txt", "rt") as f:
    print("Czy zamknięty = {}".format(f.closed))
print("Czy zamknięty = {}".format(f.closed))

print("==========================")

f = None
try:
    f = open("data1.txt", "rt")
except IOError as e:
    print(str(e))
finally:
    if f is not None:
        f.close()
