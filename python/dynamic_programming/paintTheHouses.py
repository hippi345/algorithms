"""
cost[][] =
[[17,2,17],
[16,16,5],
[14,3,9]]

We want to minimize the cost such that no two adjacent homes are painted the same color.
Answer in this case would be to paint Blue-Green-Blue (2,3,2) such that the total cost is 10 and
no two homes adjacent to one another are painted the same color since the two homes painted blue (1,3) are
separated by home 2 which is painted green.
"""

cost = [[17, 2, 17],
        [16, 16, 5],
        [14, 3, 9]]

w = len(cost[0])
h = len(cost)

minCost = [[False for x in range(w)] for y in range(h)]

baseMin = cost[0][0]
minCost[0][0] = True
for x in range(1, w):
    if cost[0][x] < baseMin:
        baseMin = cost[0][x]
        minCost[0][x] = True
        minCost[0][x - 1] = False

baseMin = -1
baseMindex = 0
for y in range(1, h):
    for x in range(0, w):
        if x == 0:
            if not minCost[y - 1][x]:
                baseMin = cost[y][x]
                minCost[y][x] = True
                baseMindex = x
            else:
                continue
        else:
            if cost[y][x] <= baseMin and not minCost[y - 1][x]:
                baseMin = cost[y][x]
                minCost[y][x] = True
                minCost[y][baseMindex] = False
                baseMindex = x
    baseMin = -1
    baseMindex = 0

'''
Computing the total and outputting the elements.
'''
sumCost = 0
for y in range(0, h):
    for x in range(0, w):
        if minCost[y][x]:
            sumCost = sumCost + cost[y][x]
            if x == 0:
                print("House " + str(y) + " painted: Red")
            elif x == 1:
                print("House " + str(y) + " painted: Green")
            elif x == 2:
                print("House " + str(y) + " painted: Blue")
print("Total Cost: " + str(sumCost))

RED = 0
BLUE = 1
GREEN = 2


def min_cost_dp(costs):
    n = len(costs)
    dp = [[0 for _ in range(0, 3)] for _ in range(0, n + 1)]
    for i in range(1, n + 1):
        dp[i][RED] = costs[i - 1][RED] + min(dp[i - 1][BLUE], dp[i - 1][GREEN])
        dp[i][BLUE] = costs[i - 1][BLUE] + min(dp[i - 1][RED], dp[i - 1][GREEN])
        dp[i][GREEN] = costs[i - 1][GREEN] + min(dp[i - 1][RED], dp[i - 1][BLUE])
    return min(dp[n][RED], min(dp[n][BLUE], dp[n][GREEN]))


'''
The above way works a little differently by effectively working in O(N) time but it also assumes a very fixed scope.
In other words, the algorithm knows how many houses there are and that there are 3 colors.
In the case where these values are not fixed, I believe the solution is more complex (above) and also I have
it as O(N^2).
Thanks.
'''

print(min_cost_dp(cost))
