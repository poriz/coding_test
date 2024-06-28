def solution(board, h, w):
    answer = 0
    
    dr = [0,0,-1,1]
    dc = [1,-1,0,0]

    
    for i in range(4):
        nr = h + dr[i]
        nc = w + dc[i]
        
        if 0<=nr<len(board) and 0<=nc<len(board) and board[nr][nc] == board[h][w]:
            answer+=1

    
    return answer