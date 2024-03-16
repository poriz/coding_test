N = input()
l1 = {str(i):0 for i in range(0,10)}

for i in N:
    if i == '6' or i =='9':
        if l1['6'] <= l1['9']:
            l1['6']+=1
        else:
            l1['9']+=1
    else:
        l1[i]+=1
print(max(l1.values()))