"""
Given a string S and a regular expression R, return whether the regular expression matches the string.
"""


def matches_dp(S, R):
    M = len(S)
    N = len(R)
    dp = [[False for _ in range(N + 1)] for _ in range(0, M + 1)]
    dp[0][0] = True
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if S[i - 1] == R[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif R[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            elif R[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    return dp[M][N]


print(matches_dp("ABBA", "A..A"))
