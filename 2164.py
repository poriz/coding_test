from collections import deque
import sys

N = int(sys.stdin.readline())

l = [i for i in range(1,N+1)]
q = deque(l)

while True:
    answer = q.popleft()
    if len(q) == 0:
        print(answer)
        break
    else:
        temp = q.popleft()
        q.append(temp)

