import math


def mod_exp(x, y, N):
    if y == 0:
        return 1
    z = mod_exp(x, math.floor(y / 2), N)
    if z % 2 == 0:
        return math.pow(z, 2) % N
    else:
        return x * math.pow(z, 2) % N


print(mod_exp(2, 4, 5))
