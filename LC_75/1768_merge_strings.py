
def mergeAlternately(word1, word2):
    answer = []
    if len(word1) >= len(word2):
        maxword = word1
    else:
        maxword = word2
    for i in range((len(maxword)*2)):
        try:
            answer.append(word1[i])
        except IndexError:
            pass
        try:
            answer.append(word2[i])
        except IndexError:
            pass
    answer = ''.join(answer)
    return answer

print(mergeAlternately("f","beebaeca"))