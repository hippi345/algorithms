def fib2Recursive(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1 + fib2Recursive(x-1)
    return fib2Recursive(x-2) + fib2Recursive(x-1)

N = 22
DP = [0 for col in range(N)]

DP[0] = 1
DP[1] = 1

for x in range(2, N):
    DP[x] = DP[x-1] + DP[x-2]

print(DP[N-1])

'''
Pretty straightforward but wanted to include.
Key thing is don't forget base cases and this comes up in more difficult problems and 2D scenarios where you have to take
care of the base cases. 
You also have to know what element in your array or matrix is your answer to return.
Lastly, the most important thing is the formula that relates your current subproblem to the previous subproblems.
'''

print(fib2Recursive(22))