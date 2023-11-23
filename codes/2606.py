# 연결된 모든 컴퓨터의 수를 해야함 -> 전체 탐색
# DFS 사용 -> queue

import sys
from collections import deque

PC_N = int(sys.stdin.readline())
net_N = int(sys.stdin.readline())
graph = [[] for i in range(PC_N+1)]
visited = [False for i in range(PC_N+1)]

for _ in range(net_N):
    a,b = map(int,sys.stdin.readline().split(" "))
    graph[a].append(b)
    graph[b].append(a)

graph = [list(set(i)) for i in graph]

start = 1
q = deque([start])
visited[start] = True

while q:
    v = q.popleft()
    for i in graph[v]:
        if not visited[i]:
            q.append(i)
            visited[i] = True

print(sum(visited)-1)

# input:
# 9
# 8
# 2 3
# 4 5
# 6 7
# 8 9
# 2 5
# 4 7
# 6 9
# 1 8
# output: 2
# answer: 8