def moveZeroes(nums: list) -> list:
    count = 0
    for i, v in enumerate(nums):
        if v == 0:
            count += 1
            continue
        nums[i], nums[i - count] = nums[i - count], nums[i]
    return nums
