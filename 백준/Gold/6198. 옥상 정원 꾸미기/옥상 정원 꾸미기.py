import sys

N = int(sys.stdin.readline())
stack = []
total = 0

for _ in range(N):
    height = int(sys.stdin.readline())
    
    while stack and stack[-1] <= height:
        stack.pop()
    
    total += len(stack)
    stack.append(height)

print(total)