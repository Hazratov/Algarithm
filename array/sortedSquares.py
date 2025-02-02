def generate_sorted(nums):
    n = len(nums)

    for i in range(n):
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]



def sortedSquares(nums: list) -> list:
    for num in range(0, len(nums)):
        nums[num] **= 2
    generate_sorted(nums)
    return nums

print(sortedSquares([-4,-1,0,3,10]))