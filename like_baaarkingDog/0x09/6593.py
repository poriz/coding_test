from collections import deque
import sys

def init_map(L,R,C):
    sb_building = []
    start, end = [], []

    for l in range(L):
        floor = []
        for r in range(R+1):
            temp = sys.stdin.readline().strip().split()
            if not temp:
                pass
            else:
                temp = [i for i in temp[0]]
                if 'S' in temp:
                    start = [l,r,temp.index('S')]
                if 'E' in temp:
                    end = [l,r,temp.index('E')]
                floor.append(temp)
        sb_building.append(floor)

    return sb_building, start, end


def bfs(L,R,C,building,start,end):
    q=deque([])
    sl,sr,sc = start
    q.append([sl,sr,sc,0])
    building[sl][sr][sc] = '#'

    nl = [-1,1,0,0,0,0]
    nr = [0,0,-1,1,0,0]
    nc = [0,0,0,0,-1,1]

    while q:
        l,r,c,count = q.popleft()
        if [l,r,c] == end:
            return count
        else:
            for i in range(6):
                dl = l + nl[i]
                dr = r + nr[i]
                dc = c + nc[i]

                if 0<=dl<L and 0<=dr<R and 0<=dc<C and building[dl][dr][dc] != '#':
                    q.append([dl,dr,dc,count+1])
                    building[dl][dr][dc] = '#'
    return -1


if __name__ =="__main__":
    while True:
        L, R, C = map(int, sys.stdin.readline().split())
        if (L,R,C) != (0,0,0):
            sb_building, start, end = init_map(L,R,C)
            s = bfs(L,R,C,sb_building,start,end)
            if s>0:
                print(f'Escaped in {s} minute(s).')
            else:
                print('Trapped!')
        else:
            break


