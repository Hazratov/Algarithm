def maxArea(nums: list) -> int:
    left, right = 0, len(nums) - 1
    max_area = 0

    while left < right:
        area = (right-left) * min(nums[left], nums[right])
        max_area = max(max_area, area)

        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1

    return max_area

print(maxArea([1,8,6,2,5,4,8,3,7]))