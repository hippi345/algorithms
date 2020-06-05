def stairsToHeaven(n):
    ways = [0] * (n + 1)
    ways[0] = 1
    ways[1] = 1

    for x in range(2, n+1):
        ways[x] = ways[x - 1] + ways[x - 2]
    return ways[n]


print(stairsToHeaven(6))
