import sys
from collections import deque

N,M = map(int, sys.stdin.readline().split())
# M개의 줄
# N은 정점의 수
graph = [[] for _ in range(N+1)]
visited = [[] for _ in range(N+1)]

for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    if u not in graph[v]:
        graph[v].append(u)
answer=-1
answer_list =[]
# 연결 요소가 없는경우도 포함
for i in graph:
    if i == []:
        answer+=1

for start in range(1,N+1):
    stack = deque(graph[start])
    if stack !=deque([]):
        answer += 1
        while stack:
            for i in graph[stack[0]]:
                stack.append(i)
            n = stack.popleft()
            graph[n] = []
    else:
        pass

print(answer)



