def DivideAndConquerSingleSellProfit(arr):
    # Base case: If the array has zero or one elements in it, the maximum
    # profit is 0.
    length = len(arr)
    if length <= 1:
        return -1;
    length = len(arr)
    left = arr[0: round(length / 2)]
    right = arr[round(length / 2): len(arr)]

    leftProfit = DivideAndConquerSingleSellProfit(left)
    rightProfit = DivideAndConquerSingleSellProfit(right)

    mixProfit = max(right) - min(left)

    return max(max(leftProfit, rightProfit), mixProfit)


print(DivideAndConquerSingleSellProfit([2, 7, 1, 15, 222]))
