x = [[1, 12], [2, 1], [80, 100], [0, 45]]


def second(x):
    return x[1]


def xxx(x, y):
    return x + y


lll = second
print(lll([20, 30]))

xxx = lambda x, y: x + y

print(xxx(10, 24))

print(sorted(x, key=lambda x: x[1]))

przytnij(
    data=[1, 2, 3, 4, 5, 6, 7],
    start=lambda x: x == 3,
    stop=lambda x: x == 6,
)

["a", "b", "c", 2, 4, "dy", "x",  5, 6, "a", "b", "c", "dy", "x"]

przytnij(
    data=["a", "b", "c", "dy", "x"],
    start=lambda x: x == "b",
    stop=lambda x: x.endswith("y"),
)
