import sys

N = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().strip().split()))

stack = []
result = [-1] * N


for i in range(N):
    while stack and array[stack[-1]] < array[i]:
        result[stack.pop()] = array[i]
    stack.append(i)

print(*result)