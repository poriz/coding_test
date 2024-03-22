from collections import deque
ROW,COL = map(int,input().split())

art_map = []
for _ in range(ROW):
    art_map.append(list(map(int,input().split())))

q = deque([])
dr = [-1,1,0,0]
dc = [0,0,-1,1]

max = 0
art_num =0
for r in range(ROW):
    for c in range(COL):
        count = 0
        if art_map[r][c] == 1:
            q.append([r,c])
            art_map[r][c] = 2
            count+=1
            while q:
                row,col = q.popleft()
                for dd in range(4):
                    n_row = row + dr[dd]
                    n_col = col + dc[dd]

                    if (0<=n_row<ROW and 0<=n_col<COL) and art_map[n_row][n_col] == 1:
                        q.append([n_row,n_col])
                        art_map[n_row][n_col] = 2
                        count+=1
            if count>max:
                max = count
            art_num +=1

print(art_num)
print(max)