# stack = [(,(,(] # 여는 괄호가 세 번
# () # 레이저가 나오면
# 개수 = len(stack)

ir= input()
stack=[]
cnt = 0

for i in range(len(ir)):
    if ir[i] == '(':
        stack.append('(')
    else:
        if ir[i-1] == '(':
            stack.pop()
            cnt+=len(stack)
        else:
            stack.pop()
            cnt+=1
print(cnt)