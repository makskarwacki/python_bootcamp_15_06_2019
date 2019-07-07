# list comprehensions
import sys

print([(x, x**2) for x in range(100) if x % 2 == 0 ])
print({x**3 for x in range(100) if x % 2 == 0 })
gen = ((x, x**2) for x in range(1000000) if x % 2 == 0)
as_list = list(gen)

print(sys.getsizeof(gen))
print(sys.getsizeof(as_list))
