N, M = map(int,input().split(" "))
g_groups = {}

for i in range(N):
    g_name = input()
    count=int(input())
    group = []
    for j in range(count):
        group.append(input())
    group.sort()
    g_groups[g_name]=group

g_groups_reverse ={}
for key, value in g_groups.items():
    for v in value:
        g_groups_reverse[v]=key

answer = []
for i in range(M):
    p = input()
    type=int(input())

    if type==0:
        for i in g_groups[p]:
            answer.append(i)
    else:
        answer.append(g_groups_reverse[p])

for a in answer:
    print(a)