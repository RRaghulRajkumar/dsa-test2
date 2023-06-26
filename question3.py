def findLHS(nums):
    num_counts = {}
    max_length = 0

    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    for num in nums:
        if num + 1 in num_counts:
            length = num_counts[num] + num_counts[num + 1]
            max_length = max(max_length, length)

    return max_length
nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(findLHS(nums))
