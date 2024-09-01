def increasingTriplet(nums):
    for i in range(len(nums)):
        try:
            if nums[i] < nums[i+1] < nums[i+2]:
                return 'true'
        except:
            pass
    return 'false'

print(increasingTriplet(nums = [5,4,3,2,1]))


# sliding window of three where 