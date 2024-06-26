from collections import deque

# 입력 받기
n, k = map(int, input().split())

# 양방향 연결 리스트(deque) 생성
deq = deque([i for i in range(1, n+1)])

res = []
while len(deq) != 0:
    for _ in range(k-1):
        deq.append(deq.popleft())
    res.append(str(deq.popleft()))

# 결과 출력
print('<'+', '.join(res)+'>')
