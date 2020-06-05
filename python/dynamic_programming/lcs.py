str1 = "abxc"
str2 = "abcd"
n = len(str1)
m = len(str2)
toReturn = 0
DP = [[0 for k in range(n + 1)] for l in range(m + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if str1[i - 1] == str2[j - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1
            toReturn = max(toReturn, DP[i][j])
        else:
            DP[i][j] = 0
print(toReturn)

'''
Reflections on this one include the observation that we are looking for the longest common substring and not just longest common subsequence.
We compare the most current index of each string and if they are the same then we set the current value in the DP table to the diagonal plus one.
We then set the global max to that value if it is greater than the current global max.
We then return the global max.
Improvements would be to remove the need for a 2D array DP table.
'''
