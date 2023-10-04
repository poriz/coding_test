import sys
from heapq import heapify,heappop,heappush
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split(" ")))
M = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split(" ")))
d1 = {}
for a in A:
    d1[a] = 1


for i in B:
    try:
        print(d1[i])
    except:
        print(0)


