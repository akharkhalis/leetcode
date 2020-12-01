#nums = [3,2,2,3]
#val = 3
def remE(nums, val):
    i = 0
    while i < len(nums):
        print ("i", i)
        if nums[i] == val:
            nums.pop(i)
            i -= 1
        i +=1
        print (nums)
    print ("---end---")


remE([3,2,2,3,5,7,3],3)
remE([0,1,2,2,3,0,4,2],2)
remE([0,0,0,0,0,0,3],0)