arr = [2,3,5,6]
n = 10

dp = [0 for x in range(n+1)]
dp[0] = 1

for i in range(0, len(arr)):
    for j in range(arr[i], n+1):
        dp[j] += dp[j-arr[i]]
print(dp[n])