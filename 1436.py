import sys
n = int(sys.stdin.readline().strip())

count = 0
num = 665
while count<n:
    num += 1
    if '666' in str(num):
        count+=1
print(num)
