def solution(s):
    answers = []
    for i in range(1,len(s)+1):
        answers.append(cutting(s,i))
    
    return min(answers)

def cutting(s, num):
    num_dict = []
    answer = ''
    s = [s[i:i+num] for i in range(0,len(s),num)]
    
    for i in range(len(s)):
        if i == 0:
            num_dict.append([s[i],1])
        elif s[i] == num_dict[-1][0]:
            num_dict[-1][1] +=1
        else:
            num_dict.append([s[i],1])
            
    for v in num_dict:
        if v[1] != 1:
            answer+= (str(v[1]) + v[0])
        else:
            answer+=v[0]
            
    return len(answer)