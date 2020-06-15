"""
Based on example at https://quinston.com/code-snippets/min-max-using-divide-and-conquer-code
"""
import random

globalMin = 99999
globalMax = 0


def getLarger(a, b):
    if b > a:
        return b
    else:
        return a


def getSmaller(a, b):
    if b < a:
        return b
    else:
        return a


def MinMax(minMaxArr, start, end):
    global globalMin
    global globalMax
    # Goal is to get down to elements of 2 recursively
    # We call the method recursively on the two halves of the array
    if end - start > 2:
        MinMax(minMaxArr, start, round((start + end) / 2))
        MinMax(minMaxArr, round((start + end) / 2), end)
    else:
        # Once we have elements of pairs, we can begin this part
        # We recursively get down to 2 then compare them to the global min and max
        # But this is done in two recursive tree paths for O(nlogn)
        minMaxArr = minMaxArr[start:end]
        if end - start == 1:
            minMaxArr.append(minMaxArr[0])
        globalMax = getLarger(globalMax, getLarger(minMaxArr[0], minMaxArr[1]))
        globalMin = getSmaller(globalMin, getSmaller(minMaxArr[0], minMaxArr[1]))


array = list()
length = 100
for x in range(0, length):
    array.append(random.randint(0, length))
print(array)
MinMax(array, 0, length)
print("Max is ", str(globalMax))
print("Min is ", str(globalMin))