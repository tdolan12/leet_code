def merge(nums1, m, nums2, n):
    counter = 1
    for i in range(m):
        try:
            if nums1[i] >= nums2[0]:
                nums1.insert(i + 1, nums2.pop(0))
        except:
            pass 
        counter += 1
    while len(nums2) > 0:
        nums1.insert(counter, nums2.pop(0))
        counter += 1
    while len(nums1) > m + n:
        nums1.pop() 

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1 = nums1, m = m, nums2 = nums2, n = n)
print(nums1)