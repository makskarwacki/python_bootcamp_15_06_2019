import numpy as np

a = np.arange(100).reshape((10, 10)) ** 2

b = np.zeros(shape=(5, 5))
b[1:-1, 1:-1] = 1

c = np.arange(10) * np.arange(10).reshape((10, 1))

print(a)
print(b)
print(c)
