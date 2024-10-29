import sys
N = int(input())

stack = []
answer = 0
for _ in range(N):
    a = int(sys.stdin.readline())
    while stack and stack[-1][0]< a:
        p = stack.pop()
        answer+= p[1]

    if stack and stack[-1][0] == a:
        answer+= stack[-1][1]
        stack[-1][1] +=1
    else:
        stack.append([a,1])
    if stack and len(stack)>1:
        answer+=1

print(answer)