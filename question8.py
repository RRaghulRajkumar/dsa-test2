def minimumScore(nums, k):
    minimum = min(nums)
    maximum = max(nums)
    
    if maximum - minimum <= 2 * k:
        return 0
    
    min_score1 = maximum - (minimum + k)
    min_score2 = maximum - k - minimum
    
    return min(min_score1, min_score2)
nums = [1]
k = 0
print(minimumScore(nums, k))
