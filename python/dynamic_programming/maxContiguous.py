arr = [5, 15, -30, 10, -5, 40, 10]
n = len(arr)
sumArr = [0 for x in range(n)]
maxSumLength = [0 for y in range(n)]
globalMaxIndex = 0

# setting up the base case
if (arr[0] < 0):
    sumArr[0] = 0
    maxSumLength[0] = 0
else:
    sumArr[0] = arr[0]
    maxSumLength[0] = arr[0]
    globalMaxIndex = 0

for x in range(1,n):
    # Key algorithm
    sumArr[x] = arr[x] + max(sumArr[x-1], 0)
    if (sumArr[x] >= 0):
        maxSumLength[x] = maxSumLength[x-1] + 1
        if (sumArr[x] > sumArr[globalMaxIndex]):
            globalMaxIndex = x
    else:
        maxSumLength[x] = 0
# globalMaxIndex - maxSumLength[globalMaxIndex] + 1
for x in range(globalMaxIndex - maxSumLength[globalMaxIndex] + 1, globalMaxIndex + 1):
    print(arr[x])