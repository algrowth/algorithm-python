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
