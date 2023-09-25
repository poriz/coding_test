import sys
wd_list = []
while True:
    n = sys.stdin.readline().strip()
    if n == '0':
        break
    else:
        wd_list.append(n)

for w in wd_list:
    if w == w[::-1]:
        print('yes')
    else:
        print("no")
