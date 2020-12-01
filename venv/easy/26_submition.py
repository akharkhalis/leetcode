def removeDuplicates(nums):
    nums_out = []
    i = 0
    while i < (len(nums)-1):
        j = i + 1
        print("bfif",i,j)
        print("bfif_val",nums[i], nums[j])
        if nums[i] != nums[j]:
            nums_out.append(nums[i])
            print(i,j)
            print(nums[i], nums[j])
        if j == (len(nums)-1):
            if nums[j] != nums[i]:
                nums_out.append(nums[j])
        i += 1
        print ("---end---")
    return (len(nums_out))

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))