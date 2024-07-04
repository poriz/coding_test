import sys
wds = []
for i in range(3):
    wds.append(int(sys.stdin.readline().strip()))

# case1 
print(wds[0]+wds[1]-wds[2])
# case2
print(int(str(wds[0])+str(wds[1])) - wds[2])