def solution(s):
    answer = ''
    for idx,v in enumerate(s):
        if idx ==0:
            answer+= v.upper()
        elif s[idx-1] == ' ':
            answer += v.upper()
        else:
            answer+=v.lower()
                
    return answer