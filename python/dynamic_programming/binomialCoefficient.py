def binomial_coefficient_dp(n, k):
    dp = [[0 for i in range(0, k + 1)] for i in range(0, n + 1)]
    for i in range(0, n + 1):
        dp[i][0] = 1
        if i <= k:
            dp[i][i] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            '''
            Recurrence relation for a binomial coefficient.
            nCk = (n-1)C(k-1) + (n-1)Ck where nCn = 1 and nC0 = 1.
            So DP says we fill in the base cases where n = k and k = 0 with ones.
            Then we follow the recurrence relation for solving the rest.
            
            So dp[n][k] = dp[n-1][k-1] + dp[n-1][k]
            And we return dp[n][k] for the result of the binomial coefficient.
            '''
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp[n][k]

N=6
K=4

print(binomial_coefficient_dp(N,K))