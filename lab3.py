def findX(x):
    res = []
    k = 0

    while 3**k <= x:
        l = 0
        while 3**k * 5**l <= x:
            m = 0
            while 3**k * 5 ** l * 7 ** m <= x:
                n = 3**k * 5**l * 7 ** m
                res.append(n)
                m += 1
            l += 1
        k += 1

    return set(sorted(res))

x = 9

print(findX(x))

