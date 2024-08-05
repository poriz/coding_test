import sys

N = int(input())

s_cards = list(map(int,sys.stdin.readline().split(" ")))

M = int(input())

samples = list(map(int,sys.stdin.readline().split(" ")))


s_cards.sort()

# def bin_search(num, cards):
#     m = len(cards)//2
#     if m == 0:
#         return 0

#     elif cards[m] == num:
#         return 1
#     else:
#         if m > num:
#             bin_search(num,cards[:m])
#         else:
#             bin_search(num,cards[num:])
#     return 0


def bin_search(num, cards):
    left, right = 0, len(cards) - 1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == num:
            return 1
        elif cards[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return 0

answer = []

for num in samples:
    s = bin_search(num,s_cards)
    answer.append(s)

print(*answer)


# answer = []
# for s in samples:
#     try:
#         if s_cards[s]:
#             answer.append(1)
#     except:
#         answer.append(0)