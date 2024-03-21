import sys
from collections import deque

N,L = map(int,sys.stdin.readline().strip().split())
A_list = list(map(int,sys.stdin.readline().strip().split()))
q = deque()
for i in range(N):
    if q and q[0][0] <= i-L:
        q.popleft()
    while q and A_list[i] < q[-1][1]:
        q.pop()
    q.append((i,A_list[i]))
    print(q[0][1], end=" ")
