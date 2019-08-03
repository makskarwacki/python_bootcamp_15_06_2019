import sys

fname = sys.argv[1]

with open(fname) as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line}", end="")
