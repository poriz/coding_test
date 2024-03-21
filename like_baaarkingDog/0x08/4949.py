import sys
wds = ""
while True:
    wds = sys.stdin.readline().rstrip()
    stack = []
    if wds == '.':
        break
    tk = 0
    for w in wds:
        if w == '[':
            stack.append(w)
        elif w == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                tk = 1
                break

        elif w == '(':
            stack.append(w)
        elif w == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                tk =1
                break
    if tk ==0:
        if stack:
            print('no')
        else:
            print('yes')


