nums1 = [0]
m = 0
nums2 = [1]
n = 1
counter = 1

if m == 0:
    while len(nums2) > 0: 
        nums1.insert(0, nums2.pop(0))
    while len(nums1) > m + n:
     nums1.pop()

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
print(nums1)


    