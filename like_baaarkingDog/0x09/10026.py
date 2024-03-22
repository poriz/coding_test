from collections import deque
N = int(input())

color_map = []
visited_c =[[0]*N for i in range(N)]
sub_color_map = []
visited_s = [[0]*N for i in range(N)]

for _ in range(N):
    m = input()
    color_map.append([i for i in m])
    sub_color_map.append(['R' if i == 'G' else i for i in m])

q = deque([])
dr = [-1,1,0,0]
dc = [0,0,-1,1]
count_c = 0
count_s = 0

for r in range(N):
    for c in range(N):
        if visited_c[r][c] == 0:
            q.append([r,c])
            visited_c[r][c] = 1

            while q:
                row, col = q.popleft()

                for d in range(4):
                    n_row = row+dr[d]
                    n_col = col+dc[d]

                    if (0<=n_row<N and 0<=n_col<N) and visited_c[n_row][n_col] == 0 and color_map[row][col] == color_map[n_row][n_col]:
                        q.append([n_row,n_col])
                        visited_c[n_row][n_col] = 1
            count_c +=1

for r in range(N):
    for c in range(N):
        if visited_s[r][c] == 0:
            q.append([r,c])
            visited_s[r][c] = 1

            while q:
                row, col = q.popleft()

                for d in range(4):
                    n_row = row+dr[d]
                    n_col = col+dc[d]

                    if (0<=n_row<N and 0<=n_col<N) and visited_s[n_row][n_col] == 0 and sub_color_map[row][col] == sub_color_map[n_row][n_col]:
                        q.append([n_row,n_col])
                        visited_s[n_row][n_col] = 1
            count_s +=1

print(count_c,count_s)


