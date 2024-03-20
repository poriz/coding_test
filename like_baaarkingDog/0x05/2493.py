import sys
N = int(sys.stdin.readline())
towers = list(map(int,sys.stdin.readline().strip().split(" ")))
answer= [0 for i in range(N)]
stay =[]

for idx in range(len(towers)-1,-1,-1):
    while stay:
        i = stay.pop()
        if i[0] < towers[idx]:
            answer[i[1]] = (idx+1)
        else:
            stay.append(i)
            break
    stay.append((towers[idx],idx))

print(*answer)
