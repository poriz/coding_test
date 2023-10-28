import sys
N = int(sys.stdin.readline().strip())
dots=[]
for _ in range(N):
    x,y = map(int,sys.stdin.readline().split(" "))
    dots.append((x,y))

dots = sorted(dots,key = lambda x:(x[0],x[1]))

for d in dots:
    print(*d)