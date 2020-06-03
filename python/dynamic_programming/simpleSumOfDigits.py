def simpleSumOfDigits(x):
    """
    Recurrence relation in words:
    Let T(i) be equal to the sum of digits up to the ith element in a number made of individual single digits
    sum = sum + arr[i]
    """

    sumVal = 0
    strNum = str(x)
    digits = list(strNum)
    for val in digits:
        sumVal = sumVal + int(val)
    return sumVal

def simpleSumOfDigits2(x):
    sumVal = 0
    while x > 9:
        sumVal = sumVal + x % 10
        x = round(x / 10)
    sumVal = sumVal + x
    return sumVal

print(simpleSumOfDigits(1111))
print(simpleSumOfDigits2(1111))

# Runtime is O(N) where N is the number of digits in the number input
