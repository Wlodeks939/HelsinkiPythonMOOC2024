
def factorials(n: int):

    d = {}
    d[1] = 1

    for i in range(2,n+1):
        d[i] = d[i-1] * i

    return d    