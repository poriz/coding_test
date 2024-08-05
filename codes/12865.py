import sys

N, V = map(int,sys.stdin.readline().strip().split())

bag = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(V+1) for _ in range((N+1))]

for i in range(1,N+1):
    for j in range(1,V+1):
        if j>= bag[i-1][0]:
            # 작다면 배낭의 이전 물품의 무게가 버틸수있는 무게보다 작다면 -> 버틸수있다면
            dp[i][j] = max(bag[i - 1][1] + dp[i - 1][j - bag[i - 1][0]], dp[i - 1][j])
        else: # 이미 무게보다 크면 이전의 값을 사용한다.
            dp[i][j] = dp[i-1][j]
print(dp[N][V])
print(bag)





