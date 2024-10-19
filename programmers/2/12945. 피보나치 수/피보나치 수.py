# def solution(n):

#     dp=[0,1]
#     n+=1
    
#     while len(dp)<n:
#         dp.append(dp[-2]+dp[-1])
#     return dp[-1]%1234567
def solution(n):
    mem = [0,1]
    i = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    while i<n:
        mem.append(mem[i]+mem[i-1])
        i+=1
    
    return mem[-1]%1234567
