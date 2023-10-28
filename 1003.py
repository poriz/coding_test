# 0번의 등장 횟수의 값은 N+1번 째의 값과 동일하다.
# 1번의 등장 횟수의 값은 보통의 비포나치 수열과 동일하다.
import sys
answer = []
def fib(n):
    list = [0,1]
    while len(list)<n+1:
        list.append(list[-1]+list[-2])
    if n == 0:
        return 0,1
    else:
        return list[-1],list[-2]

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    f1,f0=fib(N)
    answer.append((f0,f1))

for a,b in answer:
    print(a,b)



