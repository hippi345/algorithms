arr = [-1, -3, -10, 0, 60]
currMax = arr[0]
currMin = arr[0]
currBest = arr[0]
best = arr[0]

for x in range(1, len(arr)):
    currMax = max(arr[x]*currBest, arr[x]*currMin, arr[x])
    currMin = min(arr[x]*currBest, arr[x]*currMin, arr[x])
    if (currMax > best):
        best = currMax
print(best)

'''
Reflections on this one would be that we maintain a current max and min (to account for negative times negative multiplication).
We take the max or min of either the current value or the current min times the value or the current max times the value.
The current max is compared to the global max and then set to the global max if it is greater.
'''