import sys
from collections import deque
N = int(sys.stdin.readline().strip())

a, b = map(int,sys.stdin.readline().strip().split())

m = int(sys.stdin.readline().strip())

graph = []
for _ in range(m):
    tmp =  list(map(int,sys.stdin.readline().strip().split()))
    graph.append(tmp)

q = deque([])
q.append([a,0])
tk = 0
visited = []

while q:
    m,count = q.popleft()
    if m == b:
        print(count)
        tk = 1
        break
    else:
        for s,e in graph:
            if s == m and [s,e] not in visited:
                visited.append([s,e])
                q.append([e,count+1])
            elif e == m and [e,s] not in visited:
                visited.append([e,s])
                q.append([s,count+1])
if tk == 0:
    print(-1)
