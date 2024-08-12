def solution(n):
    jump = [0 for _ in range(n)]
    
    for i in range(n):
        if i == 0:
            jump[i] = 1
        elif i == 1:
            jump[i] = 2
        else:
            jump[i] = jump[i-1]+jump[i-2]
    
    return jump[-1]%1234567