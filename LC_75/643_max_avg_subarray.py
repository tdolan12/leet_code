def findMaxAverage(nums, k):
    window = []
    window_max = nums[0:k]
    for i in range(len(nums) - k + 1):
        window = (nums[i:i+k])
        if sum(window) >= sum(window_max) and window != []:
            window_max = window.copy()
        window.clear()
    return sum(window_max)/k



nums = [7,4,5,8,8,3,9,8,7,6]
k = 7
print(findMaxAverage(nums,k))