"""
You are given a grid where you can move right or down and you want to compute the minimum cost path from top left
to bottom right.

minPath(i,j,G) = minimum cost to reach cell i,j in grid G moving only right or down.
"""
import sys


def min_path_dp(G):
    M = len(G)
    dp = [[0 for _ in range(0, M)] for _ in range(0, M)]
    for i in range(0, M):
        for j in range(0, M):
            if i == 0 and j == 0:
                continue
            dp[i][j] = sys.maxsize
            if i > 0:
                dp[i][j] = dp[i - 1][j] + G[i][j]
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + G[i][j])
    return dp[M - 1][M - 1]


G = [[0, 2, 3],
     [3, 4, 5],
     [5, 6, 7]]

print(min_path_dp(G))