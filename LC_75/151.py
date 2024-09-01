def reverseWords(s):
    s_list = s.split()
    ans = ' '.join(s_list[::-1])
    return ans


print(reverseWords(s = 'hello world  one'))