# 연구소
# 안전 영역크기의 최댓값을 구하기
# 벽은 3개

import sys
import copy
from itertools import combinations
from collections import deque

def init():
    lab = []
    N,M = map(int,sys.stdin.readline().split())
    for _ in range(N):
        lab.append(list(map(int,sys.stdin.readline().split())))
    return lab, N, M

def bfs(new_map, x,y, N, M):
    q = deque([[x,y]])
    nr = [-1,1,0,0]
    nc = [0,0,-1,1]

    while q:
        r,c = q.popleft()
        for i in range(4):
            dr,dc = r+nr[i], c+nc[i]
            if 0<=dr<N and 0<=dc<M and new_map[dr][dc] == 0:
                q.append([dr,dc])
                new_map[dr][dc] = 2
    return new_map
def count_zero(new_map,N,M):
    count = 0
    for i in range(N):
        for j in range(M):
            if new_map[i][j] == 0:
                count+=1
    return count

def main():
    lab_map, N, M= init()
    safe_zone_sizes = []
    empty_list = []
    for i in range(N):
        for j in range(M):
            if lab_map[i][j] == 0:
                empty_list.append((i,j))
    for comb in combinations(empty_list,3):
        new_map = copy.deepcopy(lab_map)
        for r,c in comb:
            new_map[r][c] = 1

        for i in range(N):
            for j in range(M):
                if new_map[i][j] ==2:
                    new_map = bfs(new_map,i,j, N, M)
        safe_zone_sizes.append(count_zero(new_map,N,M))
    print(max(safe_zone_sizes))

if __name__ == '__main__':
    main()
