
def gcdOfStrings(str1, str2):
    str_dict = {}
    str_dict_pop = []
    gcd_candidates = ''
    gcd_max = ''
    #Find max length
    if len(str1) >= len(str2):
        maxstr = str1
    else:
        maxstr = str2
    #Find max count of characters
    for i in maxstr:
        str_dict[i] = str1.count(i)
    #Remove if not >= max
    for key, value in str_dict.items():
         if value < max(str_dict.values()):
            str_dict_pop.append(key)
    for key in str_dict_pop:
            str_dict.pop(key)
    #Get building combination
    gcd_list = []

    keys = list(str_dict.keys())
    for i in range(len(keys)):
        temp_str = ''
        for j in range(i + 1):
            temp_str += keys[j]
        gcd_list.append(temp_str)
    # Check highest GCD
    gcd_count = 0
    for gcd in gcd_list:
        if str1.count(gcd) >= gcd_count:
            gcd_count = str1.count(gcd)
            gcd_max = gcd
    return gcd_max

print(gcdOfStrings("ABABABC", "AB"))