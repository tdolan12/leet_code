def reverseVowels(s):
    vowels_in_s = []
    vowels_in_s_reversed = []
    vowels_in_s_index = []
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    s_as_list = []
    # index for string
    i = 0
    for letter in s:
        if letter in vowels:
            vowels_in_s.append(letter)
            vowels_in_s_index.append(i)
        else:
            s_as_list.append(letter)
        i += 1
    # Reverse vowels
    vowels_in_s_reversed = vowels_in_s[::-1]
    # Replace reversed vowels
    for i in range(len(vowels_in_s_reversed)):
        s_as_list.insert(vowels_in_s_index[i],vowels_in_s_reversed[i])
    #List to string
    ans = "".join(s_as_list)
    return ans
    

s = "leetcode"
reverseVowels(s)
