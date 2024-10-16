from collections import deque
def solution(progresses, speeds):
    answer = []
    speeds = deque(speeds)
    while progresses:
        deploy_count = 0
        progresses = deque([i+p for i,p in zip(progresses,speeds)])
        
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            deploy_count+=1
            
        if deploy_count:
            answer.append(deploy_count)

    return answer