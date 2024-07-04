import sys
w,h = map(int, sys.stdin.readline().split())

people = {}

for _ in range(w):
    p = sys.stdin.readline().strip()
    try:
        people[p]+=1
    except:
        people[p] = 1
        
for _ in range(w):
    p = sys.stdin.readline().strip()
    try:
        people[p]+=1
    except:
        people[p] = 1
        
answer = []
for k,v in people.items():
    if v == 2:
        answer.append(k)
print(len(answer))
answer.sort()
for i in answer:
    print(i)
       