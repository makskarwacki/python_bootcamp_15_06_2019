import pickle

x = 42
y = 12.3456
s = "Ala ma kota i jest rudy"
l = [0, 2 , "A", 99.99, True]

print(f"x={x}")
print(f"y={y}")
print(f"s={s}")
print(f"l={l}")

DUMP_FILE = "save.bin"

with open(DUMP_FILE, "wb") as f:
    pickle.dump(x, f, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(y, f)
    pickle.dump(s, f)
    pickle.dump(l, f)

print("===================================")

with open(DUMP_FILE, "rb") as f:
    x1 = pickle.load(f)
    y1 = pickle.load(f)
    s1 = pickle.load(f)
    l1 = pickle.load(f)
    print(f"x={x1}")
    print(f"y={y1}")
    print(f"s={s1}")
    print(f"l={l1}")



