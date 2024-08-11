def solution(n):

    dp=[0,1]
    n+=1
    
    while len(dp)<n:
        dp.append(dp[-2]+dp[-1])
    return dp[-1]%1234567
