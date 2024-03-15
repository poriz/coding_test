odds = []
for _ in range(7):
    i = int(input())
    if i%2 !=0:
        odds.append(i)
if odds == []:
    print(-1)
else:
    print(sum(odds))
    print(min(odds))


