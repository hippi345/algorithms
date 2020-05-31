str1 = "sunday"
str2 = "saturday"

m = len(str1)
n = len(str2)

# Create a table to store results of subproblems
dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

# Fill d[][] in bottom up manner
for i in range(m + 1):
    for j in range(n + 1):

        # Base cases
        if i == 0:
            dp[i][j] = j
        elif j == 0:
            dp[i][j] = i

        # If last characters are same, ignore last char
        # and recur for remaining string
        elif str1[i - 1] == str2[j - 1]:
            str1Char = str1[i - 1]
            str2Char = str2[j - 1]
            dp[i][j] = dp[i - 1][j - 1]

        # If last character are different, consider all
        # possibilities and find minimum
        else:
            dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                               dp[i - 1][j],  # Remove
                               dp[i - 1][j - 1])  # Replace
print(dp[m][n])

'''
The reflection on edit distance is that we compare the strings at each subproblem indices pair and if they are the 
same then we just take the diagonal value prior as this value represents the change cost for the prior substrings.
Since the values are the same, we don't need to add anything to this cost.

If they are different then we add one to the min cost between a deletion, insertion, or replacement/update and this
is the cost of the current subproblem.

Fortunately, the costs of those values are the left, top, and diagonal from our current index.
So we just take the min of those values and add one.

The minimum edit distance will be the last element in the 2D DP table.

Runtime is O(nm) where n and m are the lengths of the two strings being compared.
'''