import os

with open("data.txt", "rb") as f:
    line = f.readline()
    print(line.decode())
    print("Jestem tu: {}".format(f.tell()))

    f.seek(-5, os.SEEK_CUR)
    line = f.readline()
    print(line.decode())
    print("Jestem tu: {}".format(f.tell()))

