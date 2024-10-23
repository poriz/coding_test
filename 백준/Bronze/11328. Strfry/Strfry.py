import sys

# 두 분자열이 재배열해서 동일한 문자로 만들 수 있는지를 확인해야한다.
def strfry(str1:str, str2:str) -> str:
    # 정렬하면 되는거아닐까..
    str1 = sorted(str1)
    str2 = sorted(str2)
    if str1 == str2:
        return 'Possible'
    else:
        return 'Impossible'

answers = []
N = int(input())

for _ in range(N):
    str1,str2 = sys.stdin.readline().strip().split()
    answers.append(strfry(str1,str2))

for answer in answers:
    print(answer)