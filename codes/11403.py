import sys
from collections import deque
from itertools import combinations
#graph
N = int(sys.stdin.readline().strip())
connect = [[] for _ in range(N)]
graph = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    l = list(map(int, sys.stdin.readline().strip().split()))
    for j,v in enumerate(l):
        if v == 1:
            connect[i].append(j)


# 그래프를 순회하면서 연결 확인하기.
# 연결된 점을 bfs해야함.
q = deque()
for i in range(N):
    # i에서 j로 가는 경로가 있으면 graph[i][j]를 1로 만들기.
    connect_nodes = []
    for v in connect[i]:
        q.append(v)
    while q:
        next = q.popleft()
        if next in connect_nodes:
            pass
        else:
            connect_nodes.append(next)
            for v in connect[next]:
                q.append(v)
    for c in connect_nodes:
        graph[i][c] = 1

for i in graph:
    print(*i)

### GPT 풀이는 아래에
# import sys
# from collections import deque
#
# N = int(sys.stdin.readline().strip())
# connect = [[] for _ in range(N)]
# graph = [[0 for _ in range(N)] for _ in range(N)]
#
# for i in range(N):
#     l = list(map(int, sys.stdin.readline().strip().split()))
#     for j, v in enumerate(l):
#         if v == 1:
#             connect[i].append(j)
#
# def bfs(start):
#     visited = [False] * N
#     q = deque([start])
#     visited[start] = True
#
#     while q:
#         node = q.popleft()
#         for next_node in connect[node]:
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 graph[start][next_node] = 1
#                 q.append(next_node)
#
# for i in range(N):
#     bfs(i)
#
# for row in graph:
#     print(*row)
