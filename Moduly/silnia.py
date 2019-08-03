
def silnia_v1(n):
    if n==0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def silnia_v2(n):
    if n==0:
        return 1
    return n*silnia_v2(n-1)



