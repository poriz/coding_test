# 1. 하나가 남았다면 목적지로 바로 이동시켜야한다.
# 2. n-1개가 이동하는 걸로 한다. -> 이때 목적지가 아니라 중간지로 이동시켜야함
# 3. 맨 아래의 것은 목적지로 이동시킴

def solution(n):
    answer = []
    def move_to(n,start, mid, fin):
    # n==1이면 시작점에서 끝으로 바로 이동
        if n == 1:
            answer.append([start,fin]) 
        else:
            # n-1개를 가운데로 이동시키기
            move_to(n-1,start,fin,mid)
            # 1개 남았을테니까 fin으로 이동시키기
            move_to(1,start,mid,fin)
            # mid에 남은것들을 fin으로 보내는 작업
            move_to(n-1,mid,start,fin)
    move_to(n,1,2,3)
    return answer

    
