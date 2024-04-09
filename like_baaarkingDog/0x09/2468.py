import sys
from collections import deque

N = int(sys.stdin.readline())

graph = []
for i in range(N):
    row = list(map(int,sys.stdin.readline().split()))
    graph.append(row)

m = max(map(max, graph))

answer_list = []

for t in range(m+1):
    visited = [[0]*N for i in range(N)]
    # print(visited)
    answer = 0
    def bfs(r,c,visited,graph):
        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q= deque()
        q.append([r,c])
        while q:
            row, col = q.popleft()

            for m in move:
                dr = row + m[0]
                dc = col + m[1]

                if 0<=dr<N and 0<=dc<N and visited[dr][dc]==0 and graph[dr][dc]>t:
                    q.append([dr,dc])
                    visited[dr][dc] = 1


    #
    for r in range(N):
        for c in range(N):
            if graph[r][c] >t and visited[r][c] == 0:
                visited[r][c] = 1
                bfs(r,c,visited,graph)
                answer+=1
    answer_list.append(answer)
print(max(answer_list))