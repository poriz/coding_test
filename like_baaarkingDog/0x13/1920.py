import sys

N = int(input())
n_list = map(int,sys.stdin.readline().strip().split())
M = int(input())
m_list = map(int,sys.stdin.readline().strip().split())

d1 = {}
for a in n_list:
    d1[a] = 1


for i in m_list:
    try:
        print(d1[i])
    except:
        print(0)