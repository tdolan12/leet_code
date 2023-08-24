def findDifference(nums1, nums2):
    unique_nums1 = []
    unique_nums2 = []
    for number in nums1:
        if number not in nums2:
            unique_nums1.append(number)
    for number in nums2:
        if number not in nums1:
                unique_nums2.append(number)
    nums1 = list(set(unique_nums1))
    nums2 = list(set(unique_nums2))
    return [nums1, nums2]

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(findDifference(nums1, nums2))