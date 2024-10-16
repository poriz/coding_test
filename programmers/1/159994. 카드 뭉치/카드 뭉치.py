from collections import deque
def solution(cards1, cards2, goal):
    c1 = deque(cards1)
    c2 = deque(cards2)
    goal = deque(goal)
    while goal:
        if c1 and c1[0] == goal[0]:
            c1.popleft()
            goal.popleft()
        elif c2 and c2[0] == goal[0]:
            c2.popleft()
            goal.popleft()
        else:
            return 'No'

    return "Yes"