nums = [0,0,1,1,1,2,2,3,3,4]
nums_out = []
output = len(nums_out)
i = 0
print ("------ new run --------")
while i < (len(nums)-1):
    j = i + 1
#    print ("candidate - ", nums[i], "i=", i)
#    print ("comparing to ", nums[j], "j =", j)
    if nums[i] != nums[j]:
        nums_out.append(nums[i])
    if j == (len(nums)-1):
        if nums[j] != nums[i]:
            nums_out.append(nums[j])
    i += 1
    print ("output ", nums_out)
print (len(nums_out))





# take number from NUMS
# compare it to previous one
# compare it to next one
# if it's != to pre and next THEN add it to NUMS_OUT
# repete for nex number
# calculate length of NUMS_OUT array