"""
When looking at knapsack with reconstruction, the key ideas are the following:
Solve for the optimal value the same way.
Keep track of whether you choose an item or not in each sub-problem.
In the end loop over the the items chosen on the overall problem.
The ones chosen for that final sub-problem will be having values of True for the items.
Key Tip: know the scenario for which you are adding an item vs. taking the previous best.
The condition for making the decision value true is the same as the condition for adding the value
of the current sub-problem item's value to the global solution.
"""


def knapsack_DP_reconstruct(W, weights, values):
    dp = [[0 for i in range(0, len(weights) + 1)] for j in range(0, W + 1)]
    n = len(weights)
    decisions = [[False for i in range(0, len(weights) + 1)] for j in range(0, W + 1)]
    dp[W][0] = 0
    for i in range(1, n + 1):
        for w in range(0, W + 1):
            if weights[i - 1] <= w:
                if dp[w - weights[i - 1]][i - 1] + values[i - 1] > dp[w][i - 1]:
                    # We record the decision here that its beneficial to pick the ith item
                    decisions[w][i] = True
                    dp[w][i] = dp[w - weights[i - 1]][i - 1] + values[i - 1]
                else:
                    dp[w][i] = dp[w][i - 1]
            else:
                dp[w][i] = dp[w][i - 1]

    i = n
    w = W
    while i > 0 and w > 0:
        if decisions[w][i]:
            print("Picked up {} , Weight {} , Value {}".format(i - 1, weights[i - 1], values[i - 1]))
            w -= weights[i - 1]
            i -= 1;
        else:
            i -= 1
    return dp[W][n]


print(knapsack_DP_reconstruct(5, [1, 2, 3, 4], [1, 2, 3, 4]))
