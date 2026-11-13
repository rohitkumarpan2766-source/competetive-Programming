from math import isqrt

def three_divisors(keys, L=10**6):
    is_p = [True] * (L + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, isqrt(L) + 1):
        if is_p[i]:
            for j in range(i * i, L + 1, i):
                is_p[j] = False
                
    res = []
    for x in keys:
        r = isqrt(x)
        res.append(r * r == x and is_p[r])
    return res