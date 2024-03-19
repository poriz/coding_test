import sys
from collections import deque

init_wd= sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
cmds = []
for _ in range(N):
    i = sys.stdin.readline().strip()
    if len(i)==3:
        cmds.append(i[2])
    else:
        cmds.append(i)

left,right = deque([[i,0] for i in init_wd]), deque([])

for i in cmds:
    if i == 'L':
        if left:
            wd = left.pop()
            right.appendleft(wd)
    elif i == 'D':
        if right:
            wd = right.popleft()
            left.append(wd)
    elif i == 'B':
        if left:
            wd = left.pop()
    else:
        left.append([i,0])

first_elements = ''.join([item[0] for item in (left+right) if item[1] != 1])
print(first_elements.strip())