coin = [2,3,5,6]
n = 10

dp = [0 for x in range(n+1)]
dp[0] = 1

for i in range(0, len(coin)):
    for j in range(coin[i], n+1):
        dp[j] += dp[j-coin[i]]
print(dp[n])

'''
Explanation at https://stackoverflow.com/questions/14992411/understanding-change-making-algorithm
Each subproblem j looks at an interval up to the value n which is our goal.
We cannot make change on values less than the coin we are observing, for that coin, beyond the optimal number of ways
we can make change on the smaller values.
So we are only considering values from the size of the current coin to the target.

Example:
When looking at coin 3, there is no new way for which we can make change on 2 or 1. So we start the loop at 3 which pulls
the one for itself from the base case dp[3-3] = 1.
This is the case for all coins in our set.
Then from there we add the values incrementally.

Let's take a look at the case n=5.
We previously had 0 in this spot when we were just considering coin 2 but when we consider 3, we minus 3 and we get a 1 from 2.
What this means is that if we can make change on 5-3 with the other coins prior then we can make change now (in either the
first or a new way). So then when we get to 8, we will check if can make change on 5 which we can so 8 becomes 2 because it
was already able to be made change with only 2's but now there is a new way with 3 in addition.

Therefore when we get to n=10 we are considering all the possibilties on making change up to the last coin and then
adding that coin in a new way if 10-coin gives us a non-zero value.
That non-zero value might be more than one and this would represent more than one way to make change with the new coin.
'''