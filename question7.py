def isMonotonic(nums):
    increasing = True
    decreasing = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            increasing = False
        if nums[i] > nums[i - 1]:
            decreasing = False

    return increasing or decreasing
nums = [1, 2, 2, 3]
print(isMonotonic(nums))
