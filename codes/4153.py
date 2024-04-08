import sys
answer =[]
while True:
    a, b, c = map(int,sys.stdin.readline().split())
    if a==0 and b==0 and c ==0:
        break
    else:
        l = max(a,b,c)
        if l == a:
            if a**2 == (b**2 + c**2):
                answer.append('right')
            else:
                answer.append('wrong')
        elif l == b:
            if b**2 == (a**2 + c**2):
                answer.append('right')
            else:
                answer.append('wrong')
        elif l == c:
            if c**2 == (b**2 + a**2):
                answer.append('right')
            else:
                answer.append('wrong')

for i in answer:
    print(i)