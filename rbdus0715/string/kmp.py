# kmp 알고리즘 구현

H = input()
N = input()

def getPartialMatch(pattern):
    patternSize = len(pattern)
    table = [0] * patternSize
    j = 0
    for i in range(1, patternSize):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            table[i] = j + 1
            j += 1
                
    return table
    
    
def kmpSearch(H, N):
    n = len(H); m = len(N)
    ret = []
    pi = getPartialMatch(N)
    
    begin = 0; matched = 0
    while begin + m <= n:
        
        if matched < m and H[begin + matched] == N[matched]:
            matched += 1
            if matched == m: ret.append(begin)
            
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched - 1]
                
    return ret
        
        
print(kmpSearch(H, N))


# parent = input()
# pattern = input()

# def failure(pattern):
#     patternSize = len(pattern)
#     ret = [0] * patternSize
#     j = 0
#     for i in range(1, patternSize):
#         while j > 0 and pattern[i] != pattern[j]:
#             j = ret[j-1]
#         if pattern[i] == pattern[j]: 
#             j += 1
#             ret[i] = j
#     return ret

# def kmp(parent, pattern):
#     pi = failure(pattern)
#     parentSize = len(parent)
#     patternSize = len(pattern)
#     result = []
#     j = 0
#     for i in range(parentSize):
#         while j > 0 and parent[i] != pattern[j]:
#             j = pi[j-1]
#         if parent[i] == pattern[j]:
#             j += 1
#             if j == patternSize:
#                 result.append(j-i+1)
#                 j = pi[j-1]
#     return result
    
# # abababadababacabad
# # ababacaba
# print(kmp(parent, pattern))
