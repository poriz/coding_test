# 백준 1931 회의실 배정
# 링크: https://www.acmicpc.net/problem/1931

import sys
# size 작은 것부터 앞에서 배치
# timeline은 배열로 관리. 번호가 0~임
time_end= 0
answer = 0
# 회의의 수 N
N = int(sys.stdin.readline().strip())

# input을 받아서 길이와 함께 튜플로 저장, 리스트로 튜플 넣어두기
meeting_list = []
for _ in range(N):
    start,end = map(int,sys.stdin.readline().strip().split())
    meeting_list.append((start,end))

# idea: 시작시간이 빠른 순으로 정렬하면서 종료 시간이 빠른 순으로 회의를 진행시킨다.
meeting_list = sorted(meeting_list, key = lambda x:(x[1],x[0]))
for idx,m in enumerate(meeting_list):
    if idx == 0:
        answer+=1
        key = m
        pass
    else:
        if m[0]>=key[1]:
            answer+=1
            key= m
print(answer)





