nums = [12,345,2,6,7896]
def findNumbers(nums):
    even_counter = 0
    for i in nums:
        numLen = len(str(i))
        print (i)
        print (numLen)
        if numLen % 2 == 0:
            even_counter += 1
    return even_counter
    
findNumbers([12,345,2,6,7896])    

