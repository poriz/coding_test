t = int(input())
n_list = []
for _ in range(t):
    n_list.append(int(input()))
answer= []

for n in n_list:
    dp = [1,2,4]
    if n == 1:
        answer.append(1)
    elif n == 2:
        answer.append(2)
    elif n == 3:
        answer.append(4)
    else:
        while len(dp)<n:
            dp.append(dp[-1]+dp[-2]+dp[-3])
        answer.append(dp[-1])

for i in answer:
    print(i)
