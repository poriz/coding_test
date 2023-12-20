import sys
from collections import deque

# input num of test_case T
T = int(sys.stdin.readline())
answer_Arr = []
for _ in range(T):
    answer = '['
    token = True
    # input AC function p
    p = sys.stdin.readline().strip()
    p.replace('RR',"")
    # input array length n
    n = int(sys.stdin.readline())
    # input array
    arr = sys.stdin.readline().strip().replace('[',"").replace(']',"")
    if arr == '':
        if 'D' in p:
            answer_Arr.append('error')
        else:
            answer_Arr.append('[]')

    else:
        arr = deque(list(map(int, arr.split(","))))
        r_token = False
        for i in p:
            if i == 'R':
                if r_token == False:
                    r_token = True
                else:
                    r_token = False
            elif i == 'D':
                try:
                    if r_token == False:
                        arr.popleft()
                    else:
                        arr.pop()
                except:
                    answer_Arr.append("error")
                    token = False
                    break

        if token == True:
            if p.count('R') % 2 != 0:
                arr.reverse()

            for i in arr:
                answer = answer+str(i)+','
            if answer == '[':
                answer_Arr.append('[]')
            else:
                answer= answer[:-1]+']'
                answer_Arr.append(answer)
        else:
            pass
for i in answer_Arr:
    print(i)

