import sys
N = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
l.sort()
l2 = []
answer = 0
for i in l:
    answer+=i
    l2.append(answer)

print(sum(l2))