import sys
N = int(sys.stdin.readline())
user = []

for i in range(N):
    age,name = sys.stdin.readline().strip().split(" ")
    user.append((int(age),name))
s_user=sorted(user, key = lambda x:x[0])
for i in s_user:
    print(i[0],i[1])
