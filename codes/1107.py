import sys

N = sys.stdin.readline().strip()
M = int(sys.stdin.readline().strip())

broken = list(map(int,sys.stdin.readline().split()))
not_broken = [i for i in range(10) if i not in broken]

now = 100

# 수를 입력해서 최대한 근접한 수를 만들어야함.
# 채널에 접근하는 방법에는 3가지가 존재한다.
# 1. 직접 입력
# 2. 최대한 가까운 수 입력 후 + -
# 3. +,- 만으로 이동하기.

# 버튼을 누르는 횟수를 비교하기위한 배열
clicks = []

# 1. 직접 입력하기
# 1-1. 고장난 번호가 있으면 불가능함
# check number
token = True
for i in N:
    i = int(i)
    if i in broken:
        token = False
        break
if token:
    clicks.append(len(N))

# 2. +,- 만으로 이동하기
clicks.append(abs(int(N)-now))

# 3. 고장난 버튼을 제외하고 가장 가까운 수에 접근하기
# 0을 잘 처리해야함. 문자열접근말고 수의 차이를 이용해서 접근하는것이 편할거같다.
# +나 -를해서 근접한 수를 찾는데 그 범위가 clicks의 최소보다 크면 멈춘다.
limit = min(clicks)

up_count=0
up = int(N)
down_count=0
down = int(N)
# up,down 두 경우 판별해야한다.
while up_count+len(str(up))<limit:
    token = True
    up_count+=1
    up+=1
    for i in str(up):
        if int(i) in broken:
            token = True
            break
        else:
            token = False
    if not token:
        limit = up_count+len(str(up))
        break
while down_count+len(str(down))<limit and down>0:
    token = True
    down_count+=1
    down-=1
    for i in str(down):
        if int(i) in broken:
            token = True
            break
        else:
            token = False
    if token == False:
        limit = down_count + len(str(down))
        break
print(limit)
