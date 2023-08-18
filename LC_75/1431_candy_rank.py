def kidsWithCandies(candies, extraCandies):
    bool_list = []
    kids_beat = 0
    for kid in candies:
        for i in candies:
            if (kid + extraCandies) >= i:
                kids_beat += 1
        if kids_beat > (len(candies) - 1):
            bool_list.append('true')
        else:
            bool_list.append('false')
        kids_beat = 0
    return bool_list
        



candies = [4,2,1,1,2]
extraCandies = 1
print(kidsWithCandies(candies, extraCandies))