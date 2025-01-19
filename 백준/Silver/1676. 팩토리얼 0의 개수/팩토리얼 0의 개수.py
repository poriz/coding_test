def n_fact(n,next,fin):
    if next<=fin:
        return n_fact(n*next,next+1,fin)
    return n

if __name__ == "__main__":
    answer = 0
    N = int(input())
    res=str(n_fact(1,2,N))
    
    for i in res[::-1]:
        if i == '0':
            answer+=1
        else:
            print(answer)
            break