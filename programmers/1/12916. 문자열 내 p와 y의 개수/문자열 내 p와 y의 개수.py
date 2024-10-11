def solution(s):
    # 대소문자 구별이 없으니 소문자로 통일
    s = s.lower()
    # p,s 딕셔너리를 만들어서 count를 비교하기.
    my_dict = {'p':0,'y':0}
    
    # 반복문을 돌면서 s,y 찾기
    for word in s:
        if word in my_dict:
            my_dict[word]+=1
            
    # 하나도 없는 경우와 값이 동일한 경우는 True이니까 값이 다른 경우에만 false를 리턴해주면된다.
    if my_dict['p'] != my_dict['y']:
        return False
    else:
        return True