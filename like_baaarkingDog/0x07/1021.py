from collections import deque
import sys
N,M = map(int,sys.stdin.readline().strip().split())
goal = list(map(int,sys.stdin.readline().strip().split()))

q = deque([i for i in range(1,N+1)])
answer = 0
for i in goal:
    l = len(q)
    if i == q[0]:
        q.popleft()
    else:
        i_index = q.index(i)
        if i_index < l-i_index:
            q.rotate(-i_index)
            q.popleft()
            answer+=i_index
        else:
            q.rotate(l-i_index)
            q.popleft()
            answer+=(l-i_index)
print(answer)