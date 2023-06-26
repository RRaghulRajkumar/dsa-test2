def maxCandies(candyType):
    n=len(candyType)
    unique_candies=set()

    for candy in candyType:
        unique_candies.add(candy)
    return min(len(unique_candies),n//2)    

candyType = [1, 1, 2, 2, 3, 3]
print(maxCandies(candyType))

