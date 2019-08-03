

with open("data.txt", "rt") as f:
    line = f.read(10)
    print(line)
    print("\nMoja pozycja to {}".format(f.tell()))

    f.seek(3,0)
    line = f.read(10)
    print(line)
    print("\nMoja pozycja to {}".format(f.tell()))
