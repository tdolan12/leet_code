def isSubsequence(s, t):
    s_in_t = str()
    i = 0
    ans = 'false'
    for letter in t:
        if letter in s:
            s_in_t += letter
        i += 1
    if s in s_in_t:
        ans = 'true'
    return ans



s = "aec"
t = "abcde"
print(isSubsequence(s,t))