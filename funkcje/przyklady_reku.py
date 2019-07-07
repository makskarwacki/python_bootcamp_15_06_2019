# 6!
# 5!*6
# 1*2*3*4*5*6
#
# 0!->1


def foo(x):
    if x == 100:
        return x
    else:
        print(x)
        foo(x+1)

#foo(1)


def reku_print(x):
    if len(x) == 1:
        print(x[0])
    else:
        print(x[0])
        reku_print(x[1:])

reku_print([1, 2, 3, 'a', 'a']*1000)