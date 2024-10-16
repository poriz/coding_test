from heapq import heapify, heappush, heappop
def solution(operations):
    answer = []
    q = []
    # operations
    for operation in operations:
        o,v = operation.split()
        v = eval(v)
        if o == 'I':
            heappush(q,[v,v*(-1),v]) # a,b,기본값
        if o == 'D':
            try:
                if v<0:
                    heapify(q)
                    heappop(q)
                else:
                    q = [[i[2]*-1, i[2], i[2]] for i in q]
                    heapify(q)
                    heappop(q)
                    q = [[i[2],i[2]*-1, i[2]] for i in q] 
            except:
                pass
    if q == []:
        return [0,0]
    else:
        for i in q:
            answer.append(i[0])
        return [max(answer),min(answer)]
        