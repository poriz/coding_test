import sys

n = int(sys.stdin.readline().strip())
sizes = list(map(int, sys.stdin.readline().strip().split()))
t, p = map(int, sys.stdin.readline().strip().split())
size2 = []
for s in sizes:
    if s % t == 0:
        size2.append(s // t)
    else:
        size2.append(s // t + 1)

print(sum(size2))
print(n // p, n % p)