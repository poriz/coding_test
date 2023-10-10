import sys
answer = []
N = int(sys.stdin.readline())
lines = []
for _ in range(N):
    l = sys.stdin.readline().strip()
    for i in l:
        if i =='(' or i == ')':
            pass
        else:
            l.replace(i,"")
    lines.append(l)

for line in lines:
    stack = []

    for ps in line:
        if stack == []:
            stack.append(ps)
        else:
            if stack[-1] == '(' and ps == ')':
                stack.pop()
            else:
                stack.append(ps)

    if len(stack) !=0:
        answer.append('NO')
    else:
        answer.append('YES')

for b in answer:
    print(b)