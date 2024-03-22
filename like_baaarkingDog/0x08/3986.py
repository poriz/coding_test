import sys

N = int(sys.stdin.readline())
answer = 0

for _ in range(N):
    word = sys.stdin.readline().strip()
    stack = []

    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if not stack:
        answer += 1

print(answer)