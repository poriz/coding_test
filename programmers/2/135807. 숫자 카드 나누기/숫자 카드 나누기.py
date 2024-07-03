# 왼쪽 최대 공약수, 오른쪽 최대공약수 못나누면?
# 조건을 판별해 구할때마다.
# 만약 조건에 걸리면 break
# 몽땅 안걸리면 -> 약수 1나오겠지? -> result = 0
from math import gcd

def gcds(list1):
    if len(list1) == 1:
        return list1[0]
    if len(list1) == 2:
        return gcd(list1[0], list1[1])
    else:
        a = list1[0]
        for i in range(1, len(list1)):
            a = gcd(a, list1[i])
        return a

def cal(arrayA, arrayB):
    a = gcds(arrayA)
    b = gcds(arrayB)
    
    if a > b:
        for i in arrayB:
            if i % a == 0:
                return 0
    else:
        for i in arrayA:
            if i % b == 0:
                return 0
    
    return max(a, b)

def solution(arrayA, arrayB):
    a = cal(arrayA, arrayB)
    b = cal(arrayB, arrayA)
    return max(a, b)
