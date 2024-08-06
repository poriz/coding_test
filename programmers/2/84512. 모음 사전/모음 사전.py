def solution(word):
    global answer
    alphabets = ['A','E','I','O','U']
    answer = 0
    
    def dfs(wd):
        global answer
        answer += 1
        if wd == word:
            return True
        
        if len(wd) == 5:
            return False
        
        for a in alphabets:
            if dfs(wd+a) == True:
                return True
    
    for a in alphabets:
        if dfs(a) == True:
            return answer