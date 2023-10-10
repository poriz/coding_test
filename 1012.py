import sys
sys.setrecursionlimit(10**7)
N = int(sys.stdin.readline())

maps = []

for _ in range(N):
    col,row,n = map(int,sys.stdin.readline().split(" "))
    m = [[ 0 for _ in range(col)] for _ in range(row)]
    maps.append(m)
    for i in range(n):
        x,y = map(int,sys.stdin.readline().split(" "))
        m[y][x] = 1


for world in maps:
    def dfs(row,col):
        if row<0 or row>=len(world) or col<0 or col>=len(world[0]) or world[row][col]!=1:
            return False
        else:
            world[row][col] = 2
            for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
                dfs(row+dr,col+dc)
    count = 0
    for row in range(len(world)):
        for col in range(len(world[0])):

            if world[row][col] == 0 or world[row][col] == 2:
                pass
            else:
                count += 1
                dfs(row,col)

    print(count)

