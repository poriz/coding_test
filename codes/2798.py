import sys
from itertools import combinations
N,M = map(int,sys.stdin.readline().split(" "))
ll = list(map(int, sys.stdin.readline().strip().split(" ")))

c=list(set([sum(i) for i in combinations(ll,3) if sum(i)<=M]))
print(max(c))


