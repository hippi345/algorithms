arr = [10,22,9,33,21,50,41,60]

n = len(arr)
lis = [1]*n

for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            lis[i] = max(lis[i], lis[j]+1)
print(max(lis))

'''
We go over each value in the array and then over each element prior in the array up to the subproblem element we are
observing. We compare them and if the element for our subproblem is greater than the element then we further take the
max of the current max (initialized to one) and the max at the observed prior value + 1. 

This accounts for elements that increasing but not contiguous.

For example when we are observing at element 50:
We compare 50 and 10 and it is greater so we set the count at 50 to 2
We then compare it to 22 and it is greater so we take the count at 22 which is 2 and this increments the count to 3
When we compare it to 9 it is greater but since the count at 9 is 1, then the current value of 3 wins out.

We then compare to 33 and get 4. 21 will give 3 but 4 is greater. 4 wins out. 
We then compare 60 to every prior elemeent at we get that 50 wins out which gives 4 + 1 = 5.

Runtime is O(N^2) worst case.
'''