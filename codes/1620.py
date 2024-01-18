import sys

N,M = map(int, sys.stdin.readline().split(" "))
# name_input
name_list = {}
number_list ={}
answer = []
for n in range(1,N+1):
    name = sys.stdin.readline().strip()
    name_list[name] = n
    number_list[str(n)] = name

for _ in range(M):
    m = sys.stdin.readline().strip()
    try:
        answer.append(name_list[m])
    except:
        answer.append(number_list[m])

# print answer
for a in answer:
    print(a)

