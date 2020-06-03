arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 5, 6]

'''
Goal is to output true if elements are sequential and false otherwise.
Recurrence Relation: areInSequence(i) = { arr[i] = arr[i-1] + 1 ? true : false }
'''


def areInSequence(arr):
    for i in range(1, len(arr)):
        if (arr[i] != arr[i - 1] + 1):
            return False
    return True

print(areInSequence(arr1))
print(areInSequence(arr2))
print(areInSequence([-1,0,1]))