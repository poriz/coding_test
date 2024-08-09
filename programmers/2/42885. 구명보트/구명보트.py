from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people)
    
    while q:
        f = q.popleft()
        try:
            b = q.pop()
            answer+=1
            if f+b > limit:
                q.appendleft(f)
        except:
            answer+=1
    
    return answer