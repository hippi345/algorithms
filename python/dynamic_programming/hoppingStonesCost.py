import sys

# Max hop distance
X = 3

stonesCost = [0, 20, 30, 40, 25, 15, 20, 28]
totalCost = 0

'''
I want to look at one-ahead, two-ahead, and three-ahead and choose the minimum of these three.
'''
i = 0
currStone = 0
costMin = 9999
costMindex = 0
options = [0] * X
while i < len(stonesCost) - 1:
    if (len(stonesCost) - i) <= X:
        options = [0] * (len(stonesCost) - i - 1)
        valTest = len(stonesCost) - i
        for x in range(0, len(stonesCost) - i - 1):
            options[x] = stonesCost[i + x + 1]
    else:
        for x in range(0, X):
            options[x] = stonesCost[i + x + 1]
    localMax = 9999
    for x in range(0, len(options)):
        if options[x] < localMax:
            localMax = options[x]
            costMindex = i + x + 1
    i = costMindex
    currStone = localMax
    totalCost = totalCost + localMax

print(totalCost)


def min_cost_dp(C, X):
    N = len(C)
    dp = [sys.maxsize for _ in range(0, N)]
    dp[0] = 0
    for k in range(0, N):
        for j in range(1, min(X, k) + 1):
            dp[k] = min(dp[k], dp[k - j] + C[k])
    return dp[N - 1]


print(min_cost_dp(stonesCost, X))
