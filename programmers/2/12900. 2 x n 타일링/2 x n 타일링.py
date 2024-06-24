def solution(n):
    answer = 0
    dp = [1,2]
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    while len(dp) <n:
        dp.append((dp[-1] + dp[-2]) % 1000000007)
    
    
    return dp[-1]