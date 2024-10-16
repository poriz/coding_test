def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        # if phone_book[i+1].startswith(phone_book[i]):
        if startswith_method(phone_book[i+1],phone_book[i]):
            return False
    return True

# startswith 구현
def startswith_method(string:str ,prefix:str) -> bool:
    l_string = len(string)
    l_prefix = len(prefix)
    
    if l_string == 0:
        return False
    
    elif l_string < l_prefix:
        return False
    
    elif string[:l_prefix] == prefix:
        return True
    else:
        return False
