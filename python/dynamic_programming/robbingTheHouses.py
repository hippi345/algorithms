housesVals = [10,20,10,15,10,40]

N = len(housesVals)
dp = [0] * (N + 1)
dp[1] = housesVals[0]

for i in range(2,N+1):
    dp[i] = max(dp[i-2] + housesVals[i-1], dp[i-1])

print(dp[N])

'''
You cannot rob adjacent homes but you want to maximize profit.
'''