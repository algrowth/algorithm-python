# 그래프

## 그래프 기초
#### (1) 인접 행렬로 입력받기
```python
from sys import stdin

# 노드와 간선의 개수를 입력받아 int형으로 저장
node, edge = map(int, stdin.readline().split())

# 인접 행렬 초기화
adj = [[0 for _ in range(node)] for _ in range(node)]

# 인접 행렬 리스트 입력
for _ in range(edge):
    x, y = map(int, stdin.readline().split())
    adj[x][y] = 1
    adj[y][x] = 1
```

#### (2) 인접 리스트로 입력받기
```python
from sys import stdin

node, edge = map(int, stdin.readline().split())

adj = [[] for _ in range(node)]

for _ in range(edge):
    x, y = map(int, stdin.readline().split())
    adj[x].append(y)
    adj[y].apeend(x)
```
