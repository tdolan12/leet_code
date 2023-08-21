def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    j = 0
    for i in range(len(nums)):
        try:
            if nums[i] == 0:
                j +=1
        except:
            pass
    if j > 0:
        for k in range(j):
            nums.remove(0)
            nums.append(0)

nums = [0,0,1]
moveZeroes(nums)
print(nums)