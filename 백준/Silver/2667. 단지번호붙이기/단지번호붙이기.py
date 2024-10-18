n = int(input())
main_map = []
for i in range(n):
    m = input()
    temp = []
    for j in m:
        temp.append(int(j))
    main_map.append(temp)

m = len(main_map[0])
stack =[]

# 모든 노드 방문이 목적 -> DFS -> 스택&재귀
# visited 대신에 2로 표현해서 사용
def dfs(x,y):
    # 1.범위 체크
    if x<= -1 or x>=n or y<= -1 or y>=m:
        return False
    # 범위가 안쪽이라면 다음 코드 수행
    if main_map[x][y] == 1:
        main_map[x][y] =2 #방문처리를 2로 표현
        stack.append(1)
        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
            dfs(x+dx,y+dy)
    # 1이 아니면 return
    return False

answer = []
for i in range(n):
    for j in range(m):
        if main_map[i][j] == 1:
            dfs(i,j) # dfs로 한번 싹 돌고 count 값을 리턴
        if stack !=[]:
            answer.append(sum(stack))
        stack = []
answer.sort()
print(len(answer))
for i in answer:
    print(i)
