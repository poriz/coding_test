import sys
M = int(sys.stdin.readline())
s_card = list(sys.stdin.readline().strip().split())

N = int(sys.stdin.readline())

m_s = sys.stdin.readline().strip().split()
card_deck = {i:0 for i in m_s}

for j in s_card:
    if j in card_deck:
        card_deck[j] += 1

answer = []

for i in m_s:
    answer.append(str(card_deck[i]))

print(' '.join(answer))