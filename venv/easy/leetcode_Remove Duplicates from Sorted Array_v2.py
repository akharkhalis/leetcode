nums = [1,1,2]
length = 1
in_len = len(nums) - 1
new_nums = []
i = 0
s_i = 0
while i < in_len:
    if nums[i] != nums[i + 1]:
        length += 1
        i += 1
    elif nums[i] == nums[i + 1]:
        i += 1
        s_i += 1
    print(i, '-', nums[i])
print (length)