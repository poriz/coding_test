import sys
from heapq import heappush,heappop
N = int(sys.stdin.readline())
h = []
for i in range(N):
    v = int(sys.stdin.readline())
    heappush(h,v)

for j in range(N):
    print(heappop(h))