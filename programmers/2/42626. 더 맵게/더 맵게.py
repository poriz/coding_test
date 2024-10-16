# heapq를 사용하는 버전
from heapq import heapify, heappop, heappush
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while True:
        try:
            f = heappop(scoville)
            if f >=K:
                return answer

            s = heappop(scoville)

            heappush(scoville, f+s*2)

            answer+=1
        except:
            return -1
    

# heap을 만들어 사용하는 버전