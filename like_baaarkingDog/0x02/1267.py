N = int(input())
times = list(map(int,input().split(" ")))

Y = []
M = []

for i in times:
    yn = 10*(i//30) + 10
    mn = 15*(i//60) + 15

    Y.append(yn)
    M.append(mn)
y_sum = sum(Y)
m_sum = sum(M)

if y_sum < m_sum:
    print(f"Y {y_sum}")
elif y_sum > m_sum:
    print(f"M {m_sum}")
else:
    print(f"Y M {m_sum}")