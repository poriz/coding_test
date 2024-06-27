import sys
a,b = map(int,sys.stdin.readline().split())

cache = [[0 for _ in range(b+1)] for _ in range(a+1)]


# 하나를 뽑는것과 모두를 뽑는 가짓수는 1이다.
for i in range(a+1):
    cache[i][0] = 1

for j in range(b+1):
    cache[j][j] = 1

# nCk = n-1Ck + n-1Ck-1
for i in range(1,a+1):
    for j in range(1,b+1):
        cache[i][j] = cache[i-1][j] + cache[i-1][j-1]
print(cache[a][b])

# 이렇게 푸는 법도 있음.
from math import factorial
print(factorial(a)//(factorial(a-b)*factorial(b)))
