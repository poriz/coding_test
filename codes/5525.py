N = int(input().strip())
M = int(input().strip())
S = input().strip()

answer = 0
i = 0

while i <= M - 2:  # 'OI' 패턴을 확인하기 위한 최소 길이 조건
    if S[i] == 'I':
        o_count = 0
        while i + 2 < M and S[i+1] == 'O' and S[i+2] == 'I':
            o_count += 1
            if o_count >= N:
                answer += 1
            i += 2
        if o_count < N:
            i += 1  # 'OI' 패턴이 N번 미만으로 발견된 경우, 다음 문자로 이동
    else:
        i += 1

print(answer)
