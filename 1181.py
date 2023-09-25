import sys
N = int(sys.stdin.readline())
wd = {}
for i in range(N):
    w =sys.stdin.readline().strip()
    wd[w] = len(w)

wd = sorted(wd.items(), key= lambda x:(x[1],x[0]))

for k in wd:
    print(k[0])

