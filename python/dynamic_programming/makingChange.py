coins = [1, 5, 10];
N = 8
ways = [0] * (N)
ways[0] = 1

for i in range(len(coins)):
    for j in range(len(ways)):
        if (coins[i] <= j):
            ways[j] += ways[(j - coins[i])];
print(ways[len(ways) - 1])

'''
Reflections on this one are that we compare the current coin to the subproblem value.
If it is less than or equal then we increment the current index in the ways array since this add a new "way".
What this means is that if we have a coin that is less than or equal to the current subproblem then we can include it in a set of 
solution coins to make change. But we have to add the value from prior in the array by a difference of the value of the coin.
If that value from the difference is zero then that mean we don't have smaller coins to make difference and so we would not have a solution set
even though the coin at the current subsproblem is small enough to be added with even smaller values to get the desired value but those
values have to exist first in order to make change. Observe the below example for where this demonstrates.
'''

coins = [5, 10];
N = 8
ways = [0] * (N)
ways[0] = 1

for i in range(len(coins)):
    for j in range(len(ways)):
        if (coins[i] <= j):
            ways[j] += ways[(j - coins[i])];
print(ways[len(ways) - 1])