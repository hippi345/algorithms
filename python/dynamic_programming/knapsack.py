values = [1,2,3,4]
weights = [1,2,3,4]
capacity = 5
n = len(values)

# setting all the elements to zero
K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
for i in range(n + 1):
    for j in range(capacity + 1):
        if i == 0 or j == 0:
            K[i][j] = 0
        # compare the weights
        # if less than the capacity then take the max of the previous value + the difference value or the previous value
        elif weights[i - 1] <= j:
            K[i][j] = max(values[i - 1] + K[i - 1][j - weights[i - 1]], K[i - 1][j])
        else:
            K[i][j] = K[i - 1][j]
print(K[n][capacity])

'''
The reflection is that we compare the current subproblem weight and capacity being observed.
If the current weight is less than the current capacity then we can set the value in our DP table to be the max of the previous row value
and the current value plus the value differenced off the current capacity in the row above.
The max of these two values is the current max value achievable.
'''