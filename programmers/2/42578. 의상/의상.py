def solution(clothes):
    answer = 1
    
    clothes_dict = {}
    
    # update dict
    # 같은 이름을 갖는 의상이 없으므로 굳이 배열로 저장안해도됨
    for c,v in clothes:
        try:
            clothes_dict[v] += 1
        except:
            clothes_dict[v] = 1
    
    # 1~n 개의 전체 경우의 수
    # (N+1)(M+1) = NM + N + M + 1
    for i in clothes_dict.values():
        answer*= (i+1)
    
    
    return answer-1