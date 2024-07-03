from collections import deque

def bfs(graph, r, c):
    max_c = len(graph[0])
    max_r = len(graph)
    block_columns = set()
    block_size = 0
    q = deque()
    q.append((r, c))
    graph[r][c] = 2
    
    while q:
        r, c = q.popleft()
        block_columns.add(c)
        block_size += 1
        
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < max_r and 0 <= nc < max_c and graph[nr][nc] == 1:
                graph[nr][nc] = 2
                q.append((nr, nc))
    
    return block_columns, block_size

def solution(land):
    max_c = len(land[0])
    max_r = len(land)
    
    cols = {i: 0 for i in range(max_c)}
    
    for r in range(max_r):
        for c in range(max_c):
            if land[r][c] == 1:
                block_columns, block_size = bfs(land, r, c)
                for col in block_columns:
                    cols[col] += block_size
    
    return max(cols.values())