rule = {0:'D',1:'C',2:'B',3:'A',4:'E'}
answer =[]
for i in range(3):
    l1 = sum(map(int,input().split(" ")))
    answer.append(rule[l1])
for i in answer:
    print(i)