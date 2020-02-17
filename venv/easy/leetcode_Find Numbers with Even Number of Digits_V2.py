def findNumbers(nums):
    return sum(True for n in nums if len(str(n))%2==0)
findNumbers([12, 345, 2, 6, 7896])