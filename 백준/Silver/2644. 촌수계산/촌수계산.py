import sys

# 전체 사람 수 N
N = int(sys.stdin.readline())

# 계산하고 싶은 두 사람
a,b = map(int, sys.stdin.readline().strip().split())

# 관계 수 m
M = int(sys.stdin.readline())

# 앞에 나오는 번호는 뒤의 정수의 부모 번호를 나타낸다.
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x,y = map(int, sys.stdin.readline().strip().split())
    graph[x].append(y)
    graph[y].append(x)


from collections import deque

q = deque([])
q.append([a,0])
visited = [0 for _ in range(N+1)]
tk = 0

while q:
    m,count = q.popleft()
    if m == b:
        print(count)
        tk = 1
        break
    else:
        if visited[m] == 0:
            visited[m]=1
            for i in graph[m]:
                q.append([i,count+1])

if tk == 0:
    print(-1)