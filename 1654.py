import sys
K,N = map(int,sys.stdin.readline().split(" "))
lines = []
for _ in range(K):
    lines.append(int(sys.stdin.readline()))

l = 1
h = max(lines)
s = set(lines)

tk = False
if len(lines)!=1 and len(s) == 1:
    print(lines[0])
else:
    while True:

        m = ((h-l) // 2) + l
        k =sum(list(map(lambda x: x//m, lines)))

        if k<N:
            h = m
        elif k >= N:
            if h == 1:
                print(h)
                break
            elif h!=(l+1):
                l = m
            else:
                print(l)
                break



