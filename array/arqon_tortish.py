def leftRightDifference(nums: list) -> list:
    n = len(nums)
    result = []

    for i in range(n):
        left = sum(nums[:i])
        right = sum(nums[i+1:])

        if left > right:
            result.append(-1)
        elif left < right:
            result.append(1)
        else:
            result.append(0)

    return result




print(leftRightDifference([1, 2, 3, 4]))