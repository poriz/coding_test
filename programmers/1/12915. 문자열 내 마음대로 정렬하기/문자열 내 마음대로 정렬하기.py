def solution(strings, n):
    # 내장 함수를 사용한 풀이
    answer = sorted(strings, key = lambda x:[x[n],x])

    # 버블 정렬 (최초 작성)
    # for j in range(len(strings)):
    #     for i in range(len(strings)-1):
    #         if strings[i][n] > strings[i+1][n]:
    #             strings[i],strings[i+1] = strings[i+1],strings[i]
    #         if strings[i][n] == strings[i+1][n]:
    #             if strings[i] > strings[i+1]:
    #                 strings[i],strings[i+1] = strings[i+1],strings[i]

    # 버블 정렬 (코드 최적화)
    # length = len(strings)
    # for j in range(length):
    #     for i in range(length - 1 - j):
    #         if (strings[i][n], strings[i]) > (strings[i+1][n], strings[i+1]):
    #             strings[i], strings[i+1] = strings[i+1], strings[i]

    
    return answer
