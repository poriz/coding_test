# 토마토의 방향은 위,아래,왼쪽,오른쪽,앞,뒤
from collections import deque
import sys

# 가로 M, 세로 N, 상자 수 H
# 한판은 가로 M, 세로 N개가 들어오면 끝남.
M,N,H = map(int,sys.stdin.readline().strip().split())

t_box = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
# 높이 만큼 반복
for h in range(H):
    for n in range(N):
        row=list(map(int, sys.stdin.readline().strip().split()))
        for m in range(M):
            t_box[h][n][m] = row[m]


# check init tomato(1)
# store init_location
ripe_tomatoes = deque()
# 저장 구조: h,n,m,저장 날짜
for h in range(H):
    for n in range(N):
        for m in range(M):
            if t_box[h][n][m] == 1:
                ripe_tomatoes.append((h,n,m,0))
max_days = 0
while ripe_tomatoes:
    h,n,m,day = ripe_tomatoes.popleft()
    # check 6 dir
    dh=[1,-1,0,0,0,0]
    dn=[0,0,1,-1,0,0]
    dm=[0,0,0,0,1,-1]

    for i in range(6):
        rh =h+dh[i]
        rn =n+dn[i]
        rm = m+dm[i]
        try:

            if H>=rh>=0 and N>=rn>=0 and M>=rm>=0 and t_box[rh][rn][rm] == 0:
                t_box[rh][rn][rm] = 1
                ripe_tomatoes.append((rh,rn,rm,day+1))
                max_days = max(max_days, (day+1))
        except:
            pass


# BFS 탐색 후 실행
all_ripe = True  # 모든 토마토가 익었다고 가정
 # 모든 토마토가 익는데 걸린 최대 일수

for h in range(H):
    for n in range(N):
        for m in range(M):
            if t_box[h][n][m] == 0:  # 익지 않은 토마토가 있는 경우
                all_ripe = False
                break  # 더 이상 확인할 필요가 없으므로 반복문 종료
    if not all_ripe:
        break

if not all_ripe:
    print(-1)
else:
    print(max_days)





