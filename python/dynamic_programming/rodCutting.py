"""
We are given a rod of length L. We are also given a table of prices for various cut lengths on the rod.
We want to cut the rod such that we maximize the price of the cut pieces.
"""
import sys


def max_profit_dp(L, p):
    dp = [0 for _ in range(0, L + 1)]
    for l in range(1, L + 1):
        dp[l] = -sys.maxsize
        for i in range(0, l):
            dp[l] = max(dp[l], p[i] + dp[l - i - 1])
    return dp[L]


p = [0, 0, 1, 0, 0, 0, 0, 7, 0, 0]
L = 10
print(max_profit_dp(L, p))
