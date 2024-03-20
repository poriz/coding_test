import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    cmd = sys.stdin.readline().strip().split(" ")
    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        try:
            print(stack.pop())
        except:
            print(-1)
    elif cmd[0] == 'empty':
        if stack ==[]:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'size':
        print(len(stack))
    else:
        if stack == []:
            print(-1)
        else:
            print(stack[-1])