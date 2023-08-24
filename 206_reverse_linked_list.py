def reverseList(head):
    if len(head) < 1:
        return []
    else:
        ans = head[::-1]
    return ans

head = []
print(reverseList(head))