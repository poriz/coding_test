s = input()
wd = 'abcdefghijklmnopqrstuvwxyz'
wds = {i:0 for i in wd}
for i in s:
    wds[i]+=1
print(*wds.values())
