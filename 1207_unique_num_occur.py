def uniqueOccurrences(arr):
    num_dict = {}
    num_list = []
    for num in arr:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] = num_dict[num] + 1
    for value in num_dict.values():
        num_list.append(value)
    if len(num_list) == len(set(num_list)):
        return 'true'
    else:
        return 'false'

arr = [1,2]
print(uniqueOccurrences(arr))