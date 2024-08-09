import sys
from collections import deque

N = int(sys.stdin.readline().strip())

graph = []
for _ in range(N):
    graph.append(sys.stdin.readline().strip())
visited = [[0 for _ in range(N)] for _ in range(N)]


def bfs(s_r,s_c):
    q = deque()
    q.append([s_r,s_c])
    visited[s_r][s_c] = 1
    count = 1

    while q:
        r,c = q.popleft()
        dr = [0,0,-1,1]
        dc = [-1,1,0,0]

        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]

            if 0<=nr<N and 0<=nc<N and graph[nr][nc] == '1' and visited[nr][nc] == 0:
                count+=1
                q.append([nr,nc])
                visited[nr][nc] = 1
    return count

answers = []
for row in range(N):
    for j in range(N):
        if graph[row][j] == '1' and visited[row][j]== 0:
            c = bfs(row,j)
            answers.append(c)
# print answer
print(len(answers))
answers.sort()
for a in answers:
    print(a)
