N,K = map(int,input().split(" "))
circular = []
answer = []
for i in range(0,N+1):
    if i!=N:
        circular.append([i,i+1])
    else:
        circular.append([i,1])
if K !=1:
    now=1
    check_three = 0
    while len(answer)<N:
        now_value= circular[now]
        next = now_value[1]
        check_three +=1

        if check_three == K-1: #next value 건너뛰기
            next_value = circular[next]
            answer.append(next_value[0])
            circular[now][1] = next_value[1]
            circular[next] = [0, 0]

            check_three = 0

        now = now_value[1]

else:
    answer = [i for i in range(1,N+1)]
formatted_string = f"<{', '.join(map(str,answer))}>"
print(formatted_string)