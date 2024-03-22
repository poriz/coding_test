from collections import deque
M,N = map(int,input().split())

tomatos = []
# (data,length)
for _ in range(N):
    tomatos.append([[i,0] for i in list(map(int,input().split()))])

# BFS > queue
r = [-1,1,0,0]
c = [0,0,-1,1]

tomatos_raw = [smallest[0] for inner_list in tomatos for smallest in inner_list]
#check empty
if 0 not in tomatos_raw:
    print(0)
else:
    q = deque([])
    max= 0
    for row,i in enumerate(tomatos):
        for col,j in enumerate(i):
            if j[0] == 1:
                q.append([row,col])
    while q:
        row_q, col_q = q.popleft()
        for dd in range(4):
            n_row = row_q+r[dd]
            n_col = col_q+c[dd]

# 이부분 문제.
            if (0<=n_row<len(tomatos) and 0<=n_col<len(tomatos[0]))and tomatos[n_row][n_col][0] == 0:
                q.append([n_row,n_col])
                next_day = tomatos[row_q][col_q][1] + 1
                tomatos[n_row][n_col] = [1,next_day]
                if next_day > max:
                    max = next_day


    tomatos_raw = [smallest[0] for inner_list in tomatos for smallest in inner_list]
    if 0 in tomatos_raw:
        print(-1)
    else:
        print(max)
