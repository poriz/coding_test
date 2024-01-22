import sys
from heapq import heappush,heappop

# input
N = int(sys.stdin.readline())
h = []

# iter
for _ in range(N):
    # max_heap
    x = int(sys.stdin.readline())
    if x ==0:
        if h == []:
            print(0)
        else:
            print(heappop(h))
    else:
        heappush(h,x)





