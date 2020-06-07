import math

'''
Basic primality testing algorithm. Does not work for large numbers since the math.pow does not support
large numbers but we could use repeated squaring from the other python files to perform this scale of input.
'''


def fermat_witness(r):
    for z in range(1, r - 1):
        zr = math.pow(z, r - 1)
        if zr % r != 1:
            return False
    return True


print(fermat_witness(7))
print(fermat_witness(9))
