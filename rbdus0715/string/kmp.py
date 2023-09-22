parent = input()
pattern = input()

def failure(pattern):
    patternSize = len(pattern)
    ret = [0] * patternSize
    j = 0
    for i in range(1, patternSize):
        while j > 0 and pattern[i] != pattern[j]:
            j = ret[j-1]
        if pattern[i] == pattern[j]: 
            j += 1
            ret[i] = j
    return ret

def kmp(parent, pattern):
    pi = failure(pattern)
    parentSize = len(parent)
    patternSize = len(pattern)
    result = []
    j = 0
    for i in range(parentSize):
        while j > 0 and parent[i] != pattern[j]:
            j = pi[j-1]
        if parent[i] == pattern[j]:
            j += 1
            if j == patternSize:
                result.append(i-j+1)
                j = pi[j-1]
    return result
    
print(kmp(parent, pattern))

# 예제
# abababadababacabad
# ababacaba
# |8|
