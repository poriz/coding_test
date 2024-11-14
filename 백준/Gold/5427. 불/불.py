import sys
from collections import deque

def bfs(building, w, h):
    fire = deque()
    person = deque()
    
    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                fire.append((i, j, 0))
            elif building[i][j] == '@':
                person.append((i, j, 0))
                building[i][j] = '.'  # Mark as visited
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while person:
        # Spread fire
        fire_size = len(fire)
        for _ in range(fire_size):
            fx, fy, _ = fire.popleft()
            for i in range(4):
                nfx, nfy = fx + dx[i], fy + dy[i]
                if 0 <= nfx < h and 0 <= nfy < w and building[nfx][nfy] == '.':
                    building[nfx][nfy] = '*'
                    fire.append((nfx, nfy, 0))
        
        # Move person
        person_size = len(person)
        for _ in range(person_size):
            x, y, time = person.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    return time + 1
                if building[nx][ny] == '.':
                    building[nx][ny] = '@'  # Mark as visited
                    person.append((nx, ny, time + 1))
    
    return "IMPOSSIBLE"

n_testcase = int(sys.stdin.readline().strip())

for _ in range(n_testcase):
    w, h = map(int, sys.stdin.readline().split())
    building = [list(sys.stdin.readline().strip()) for _ in range(h)]
    print(bfs(building, w, h))