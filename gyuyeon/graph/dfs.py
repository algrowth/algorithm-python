from sys import stdin

node, edge = map(int, stdin.readline().split())
adj = [[] for _ in range(node)]

for _ in range(edge):
    x, y = map(int, stdin.readline().split())
    adj[x].append(y)
    adj[y].append(x)


visited = set()

def dfs(n):
    visited.add(n)
    print(n, end=' ')
    for i in adj[n]:
        if i not in visited:
            dfs(i)

dfs(2)
