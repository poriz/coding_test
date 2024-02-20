import sys
from collections import deque
# N = user_count, M = relation_count
def input_method():
    return map(int,sys.stdin.readline().strip().split())


if __name__=="__main__":
    N,M = input_method()
    user_graph = [[] for _ in range(N+1)]

    # input relations
    for _ in range(M):
        A,B = input_method()
        user_graph[A].append(B)
        user_graph[B].append(A)


    k_num = [0 for _ in range(N+1)]

    # iter user_graph -> init queue
    for idx,user in enumerate(user_graph):
        if user:
            q = deque([(idx,0)])
            visited = {idx}

            while q:
                current,distance = q.popleft()
                for n in user_graph[current]:
                    if n not in visited:
                        visited.add(n)
                        q.append((n,distance+1))
                        k_num[idx]+=distance+1

    answer_idx,min_value = min(enumerate(k_num[1:],1),key=lambda x:(x[1],x[0]))
    print(answer_idx)

