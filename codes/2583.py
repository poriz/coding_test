from collections import deque
import sys
M,N,K = map(int, sys.stdin.readline().strip().split())
graph = [[0]*N for _ in range(M)]

for _ in range(K):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().strip().split())
    for i in range(x1, x2):
        for j in range(M - y1 - 1, M - y2 - 1, -1):
            graph[j][i] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = []

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            size = 0
            q = deque([])
            q.append((i,j))
            graph[i][j] = 1
            size = 1
            while q:
                x,y = q.popleft()s
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        q.append((nx, ny))
                        size += 1
            count.append(size)

count.sort()
print(len(count))
for i in count:
    print(i, end=' ')