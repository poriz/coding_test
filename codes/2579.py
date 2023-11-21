import sys
N = int(sys.stdin.readline())
answer = [0 for _ in range(N+1)]
stairs = [0]
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

for i,v in enumerate(stairs):
    if i==0:
        pass
    elif i == 1:
        answer[i] = v
    elif i == 2:
        answer[i] =  answer[i-1]+v
    elif i == 3:
        answer[i] = max(stairs[1]+v,stairs[2]+v)
    else:
        answer[i] = max(answer[i-3]+stairs[i-1]+v,answer[i-2]+v)

print(answer[N])


