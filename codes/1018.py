import sys
sys.setrecursionlimit(10**6)

n,m = map(int, sys.stdin.readline().split(" "))
board = [[]for _ in range(n)]
for i in range(n):
    temp = input()
    for j in temp:
        board[i].append(j)

do_w = [[] for _ in range(8)]
do_b = [[] for _ in range(8)]
for i in range(8):
    for j in range(8):
        if i%2 == 0:
            if j%2 ==0:
                do_w[i].append("W")
                do_b[i].append("B")
            else:
                do_b[i].append("W")
                do_w[i].append("B")
        else:
            if j%2 ==0:
                do_b[i].append("W")
                do_w[i].append("B")
            else:
                do_w[i].append("W")
                do_b[i].append("B")

stack = []
def dfs(r,c):
    if m-c<8:
        print(min(stack))
        return min(stack)
    elif n-r<8:
        dfs(0,c+1)
    else:
        count_b = 0
        count_w = 0

        for i in range(8):
            for j in range(8):
                if board[i+r][j+c] != do_b[i][j]:
                    count_b +=1
                if board[i+r][j+c] !=do_w[i][j]:
                    count_w +=1
        stack.append(min(count_w,count_b))
        dfs(r+1,c)

dfs(0,0)