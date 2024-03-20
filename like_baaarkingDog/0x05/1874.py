N = int(input())
nums = [i for i in range(1, N+1)]
nums.reverse()
answer = []
for _ in range(N):
    answer.append(int(input()))
answer.reverse()
stack = []
result = []
tk = 0
while answer:
    if stack == []:
        stack.append(nums.pop())
        result.append('+')
    elif answer[-1] == stack[-1]:
        result.append('-')
        answer.pop()
        stack.pop()

    elif answer[-1] != stack[-1]:
        try:
            v = nums.pop()
            if stack[-1] <v:
                stack.append(v)
                result.append('+')
            else:
                print('NO')
                tk=1
                break
        except:
            print('NO')
            tk=1
            break

if tk ==0:
    for i in result:
        print(i)