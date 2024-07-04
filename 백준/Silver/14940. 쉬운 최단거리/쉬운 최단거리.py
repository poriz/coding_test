import sys
from collections import deque
n,m = map(int, sys.stdin.readline().strip().split())
graph = []

for i in range(n):
    tmp = list(map(int,sys.stdin.readline().strip().split()))
    if 2 in tmp:
        start_point = [i,tmp.index(2)]
    graph.append(tmp)
visited = [[0 for _ in range(m)] for _ in range(n)]

r,c = start_point
q = deque()
q.append([r,c,0])
graph[r][c] = 0
visited[r][c] = 1

while q:
    r,c,d = q.popleft()

    dr = [0,0,-1,1]
    dc = [-1,1,0,0]

    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]

        if 0<=nr<n and 0<=nc<m and graph[nr][nc] == 1 and visited[nr][nc] == 0:
            q.append([nr,nc,d+1])
            graph[nr][nc] = d+1
            visited[nr][nc] = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            graph[i][j] = -1

for i in range(n):
    print(*graph[i])