# 긴 문자열 S, 이 문자열의 접미사도 되고 접두사도 되는
# 문자열들의 길이를 전부 출력
# ex)
# S = ababbaba
# >> 1, 3, 8

S = input()

def getPartialMatch(s):
    strSize = len(s)
    ret = [0] * strSize
    j = 0
    for i in range(1, strSize):
        while j > 0 and s[i] != s[j]:
            j = ret[j-1]
        if s[i] == s[j]:
            j += 1
            ret[i] = j
    return ret
    

def getPrefixSuffix(s):
    ret = []
    pi = getPartialMatch(s)
    k = len(s)
    while k > 0:
        ret.append(k)
        k = pi[k-1]
    return ret
    
print(getPrefixSuffix(S))
