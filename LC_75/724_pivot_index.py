def pivotIndex(nums):
    l = int()
    r = int()
    ans = -1
    for i in range(len(nums)):
        l = sum(nums[0:i])
        r = sum(nums[i+1::])
        if l == r:
            ans = i
            break
    return ans
nums = [1,7,3,6,5,6]
print(pivotIndex(nums))      
