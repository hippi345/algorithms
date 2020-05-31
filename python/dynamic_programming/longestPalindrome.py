# A Dynamic Programming based Python
# program for LPS problem Returns the length
#  of the longest palindromic subsequence in seq
def lps(str):
    n = len(str)
    L = [[0 for x in range(n)] for x in range(n)]

    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1

    # Build the table. Note that the lower
    # diagonal values of table are
    # useless and not filled in the process.
    # The values are filled in a
    # manner similar to Matrix Chain
    # Multiplication DP solution (See
    # https://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
    # cl is length of substring
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if str[i] == str[j] and cl == 2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1], L[i + 1][j]);
    return L[0][n - 1]


# Driver program to test above functions
seq = "geeks"
n = len(seq)
print("The length of the LPS is " + str(lps(seq)))

# This code is contributed by Bhavya Jain

'''
Reflection:
We start by filling 1's down the diagonal since we know strings of length 1 are a palindrome of length 1
1   x   x
x   1   x
x   x   1

This is much like chain matrix multiplication where the goal is to get to the top right corner.

The way we do that is by comparing the current subproblem characters. 
If they are the same and the length we are observing is strings of length 2 then the answer in that cell is 2.
If they are the same but it is not 2 then the answer is two plus the max of the adjacent cells to the left and below.
If they are different then we don't add anything and just take the max of the adjacent cells.

This is much like chain matrix multiplication.

What we are really doing in the 2D DP table is looking at all possible substrings but in a smart way where we can infer
the previous best palindrome from the smallest substrings up to the bigger substrings.

This is exactly what we do in chain matrix multiplication except with working from the smaller matrix multiplications
to the bigger ones, with regards to computing the cost of multiplication.

In the case of matrix multiplication we are looking at the min cost but here we are looking at the max length so 
we replace the min formula with a max formula.
'''