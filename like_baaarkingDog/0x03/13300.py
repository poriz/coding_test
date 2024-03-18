# 여: 0, 남:1
# 전체 학생 수: N
# 한 방 최대 인원 수: K
# 입력: 성별, 학년
rooms = {}
answer =0
N,K = map(int,input().split(" "))
for i in range(N):
    s,g = input().split(" ")
    try:
        if rooms[(s,g)]<K:
            rooms[(s,g)]+=1
        else:
            rooms[(s,g)] = 1
            answer+=1
    except:
        rooms[(s,g)] = 1
print(answer+len(rooms))
