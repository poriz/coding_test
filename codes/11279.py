import sys
from heapq import heappush,heappop

# input
N = int(sys.stdin.readline().strip())
h = []

# iter
for _ in range(N):
    # max_heap
    x = int(sys.stdin.readline()) * -1
    if x ==0:
        if h == []:
            print(0)
        else:
            print(heappop(h)*(-1))
    else:
        heappush(h,x)





