"""
Given a string S, find the number of deletions to make the string a Palindrome.
2D problem because we look at the string from both sides.
Let minDeletion(S,i,j) be the minimum number of deletions to make the substring on S, starting at index i and ending at
index j, a palindrome.
"""

S = "KAZYAK"
N = len(S)
dp = [[0 for i in range(0, N)] for j in range(0, N)]

for l in range(1, N + 1):
    for i in range(0, N - l + 1):
        j = i + l - 1
        if i == j:
            continue
        if S[i] == S[j]:
            dp[i][j] = dp[i + 1][j - 1]
        else:
            dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
print(dp[0][N - 1])
