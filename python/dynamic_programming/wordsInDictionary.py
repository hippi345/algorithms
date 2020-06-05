S = "pineapplepenapple"
D = ["apple", "pen", "applepen", "pine", "pineapple"]

'''
Goal is to output the number of ways that the string can be broken up into words from the dictionary D.
'''


def count_ways_dp(i, S, D):
    N = len(S)
    dp = [0 for _ in range(0, N + 1)]
    dp[0] = 1
    for i in range(1, N + 1):
        for j in range(i, 0, -1):
            sampleString = S[j - 1:i]
            if S[j-1:i] in D:
                dp[i] += dp[j-1]
    return dp[N]


print(count_ways_dp(len(S), S, D))
