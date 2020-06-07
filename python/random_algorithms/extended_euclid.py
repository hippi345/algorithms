import math


def extended_euclid(x, y):
    if y == 0:
        return x, 1, 0
    else:
        d, a_prime, b_prime = extended_euclid(y, x % y)
    return d, b_prime, a_prime - (math.floor(x / y) * b_prime)


print(extended_euclid(6719, 9))