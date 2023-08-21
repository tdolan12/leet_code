def findMaxAverage(nums, k):
    window = []
    window_max = [nums[0:3]]
    for i in range(len(nums)):
        try:
            window.append(nums[i:i+3])
            if sum(window) >= sum(window_max):
                window_max = window
        except:
            pass
    return int(sum(window_max)) / 4



nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums,k))