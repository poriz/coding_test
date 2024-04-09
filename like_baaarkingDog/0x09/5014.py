import sys
from collections import deque

f,s,g,u,d = map(int,sys.stdin.readline().split())

visited = [0 for _ in range(f+1)]
d = -d
q = deque()
q.append([s,0])
visited[s] = 1
tk = 0
while q:
    s,count = q.popleft()
    if s == g:
        tk = 1
        print(count)
        break
    else:
        for i in (u,d):
            if 0<s+i<f+1 and visited[s+i] == 0:
                q.append([s+i,count+1])
                visited[s+i] = 1
if tk == 0:
    print("use the stairs")