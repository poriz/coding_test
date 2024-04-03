from collections import deque
import sys

N = int(sys.stdin.readline().strip())
test_cases = []

for _ in range(N):
    l = int(sys.stdin.readline())
    now = list(map(int,sys.stdin.readline().strip().split()))
    goal = list(map(int,sys.stdin.readline().strip().split()))

    test_cases.append([l,now,goal])

dr = [2,1,2,1,-2,-1,-2,-1]
dc = [1,2,-1,-2,1,2,-1,-2]
answer = []

for l,now,goal in test_cases:
    board = [[0]*l for _ in range(l)]
    visited = [[0]*l for _ in range(l)]

    board[goal[0]][goal[1]] = 2

    q = deque()

    q.append([now[0],now[1],0])
    visited[now[0]][now[1]] = 1

    while q:
        r,c,v = q.popleft()

        if board[r][c] == 2:
            answer.append(v)


        for i in range(8):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<l and 0<=nc<l and visited[nr][nc] == 0:
                q.append([nr,nc,v+1])
                visited[nr][nc] = 1
for i in answer:
    print(i)

