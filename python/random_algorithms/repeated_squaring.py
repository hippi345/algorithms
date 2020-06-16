import math
import datetime


def mod_exp(x, y, N):
    if y == 0:
        return 1
    z = mod_exp(x, math.floor(y / 2), N)
    if z % 2 == 0:
        return math.pow(z, 2) % N
    else:
        return x * math.pow(z, 2) % N


start_time1 = datetime.datetime.now()
# 2 ^ 4 = 16. 16mod5 equals 1
print(mod_exp(2, 4, 5))
stop_time1 = datetime.datetime.now()
time_diff1 = stop_time1 - start_time1
print(time_diff1.total_seconds())

start_time2 = datetime.datetime.now()
# this also equals 1 but is much larger
print(mod_exp(13, 27, 4))
stop_time2 = datetime.datetime.now()
time_diff2 = stop_time2 - start_time2
print(time_diff2.total_seconds())

start_time3 = datetime.datetime.now()
print(mod_exp(13, 45, 67))
stop_time3 = datetime.datetime.now()
time_diff3 = stop_time2 - start_time2
print(time_diff3.total_seconds())
