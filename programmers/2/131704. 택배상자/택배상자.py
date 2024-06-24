# 컨베이너 벨트에 일렬로 놓임. -> 한 방향으로만 진행 가능
# 댁배기사가 알려준 순서에 맞게 택배를 실어야함.
# 벨트앞에 놓인 상자가 현재 트럭에 실어야하는 순서가 아니라면 상자가 실을 순서가 될때까지
# 보조 컨테이너 벨트에 보관함. -> 스택임

# 택배는 1,2,3,4,5 이렇게 오는거임
# order는 넣어야하는 번호를 말하는거임
# 국어를 진짜 좀 배워야할거같은데
# 4번 상자의 위치는 0 이면 4번 상자를 1번쩨로 넣아야함?


from collections import deque

def solution(order):
    answer = 0
    q = deque(order)
    main_belt = deque([i for i in range(1,len(order)+1)])
    truck = []
    sub_belt= []
    
    while main_belt:
        v = main_belt.popleft()
        
        if v == q[0]:
            q.popleft()
            answer+=1
        else:
            sub_belt.append(v)   
        while sub_belt and sub_belt[-1] == q[0]:
            q.popleft()
            answer+=1
            sub_belt.pop()

    return answer