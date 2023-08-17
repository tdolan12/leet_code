import itertools
def gcdOfStrings(str1, str2):
    str_dict = {}
    str_dict_pop = []
    gcd_candidates = []
    gcd_max = ''
    if len(str1) >= len(str2):
        maxstr = str1
    else:
        maxstr = str2
    for i in maxstr:
        str_dict[i] = str1.count(i)
    for key, value in str_dict.items():
         if value < max(str_dict.values()):
            str_dict_pop.append(key)
    for key in str_dict_pop:
            str_dict.pop(key)
    gcd_candidates = combinations(str_dict.values(), len(str_dict))
    return str_dict

        


    

print(gcdOfStrings("ABABABC", "AB"))