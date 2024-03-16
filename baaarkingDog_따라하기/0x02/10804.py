num_list = [i for i in range(1,21)]
for i in range(10):
    a,b = map(int,input().split(" "))
    a -=1
    re = num_list[a:b][::-1]
    num_list[a:b] = re
print(*num_list)