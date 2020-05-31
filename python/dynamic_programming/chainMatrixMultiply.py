import sys
arr = [1,2,3,4]
'''
This represents the following:
1x2 array times a 2x3 array times a 3x4 array.
We want the minimum number of multiplications to perform to get the matrix multiplication to complete.
'''

'''
What is the cost of mutliplying matrices you ask? Great question!
(1x2)(2x3)(3x4)

This can be done two ways - (AB)C or A(BC).
We can't do (AC)B since a 1x2 cannot be multiplied by a 3x4 as their inner dimensions do not match.

The cost of (AB)C is as follows:
1x2x3 = 6 and represents the cost of AB
The result of this is a 1x3 matrix
We then multiply that by 3x4 so the cost is 1x3x4 
We add 6 and 12 and get 18.

We then try A(BC)
The cost of BC is 2x3x4 = 24 for a 2x4 matrix to be multiplied by A which is 1x2
Cost is 1x2x4 = 8
Total cost is 32 which is more than 18.

So the minimal cost is 18.

On to the algorithm.
'''

n = len(arr)
m = [[0 for x in range(n)] for x in range(n)]

# m[i,j] = Minimum number of scalar multiplications needed
# to compute the matrix A[i]A[i+1]...A[j] = A[i..j] where
# dimension of A[i] is p[i-1] x p[i]

# cost is zero when multiplying one matrix.
for i in range(1, n):
    m[i][i] = 0

# L is chain length.
for L in range(2, n):
    for i in range(1, n - L + 1):
        j = i + L - 1
        m[i][j] = sys.maxsize
        for k in range(i, j):

            # q = cost/scalar multiplications
            q = m[i][k] + m[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
            if q < m[i][j]:
                m[i][j] = q
print(m[1][n-1])

'''
Full explanation at https://www.youtube.com/watch?v=_WncuhSJZyA.
This is seriously not a straightforward scenario. 
You fill in the diagonals as 0's.
Work your way towards the top-right corner where your answer will be for minimum cost.
Ex)

0   24  28  58
    0   16  36
        0   40
            0

Algorithm:
C[i,j] = min { C[i,k] + c[k+1,j] + d(i-1)*dk*dj
         i<k<j

This code keeps a track of the minimum values in the m matrix.
arr is used as the dimensions of the input matrices.
The min over all k values per cell is done through a for loop.

Runtime is O(N^3).
'''