import sys
from collections import deque
N, K = map(int,sys.stdin.readline().split())

q = deque()

q.append((N,0))
M = 10 ** 5
visited = [0]*(M+1)

while q:
    n, t = q.popleft()

    if n != K:
        for i in (n-1,n+1,2*n):
            if 0<=i<=M and visited[i] == 0:
                visited[i] = 1
                q.append([i,t+1])
    else:
        print(t)
        break

