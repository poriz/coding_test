from collections import Counter
wd1 = Counter([i for i in input()])
wd2 = Counter([i for i in input()])

print(sum((wd1-wd2).values()) + sum((wd2-wd1).values()))

