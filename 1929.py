import sys
M,N = map(int,sys.stdin.readline().split(" "))
N+=1
nums = [True] * N

for j in range(2,(N//2)+1):
    if nums[j]:
        for k in range(j+j,N,j):

            nums[k] = False
nums[0],nums[1] = False,False

for i in range(M,N):
    if nums[i] == True:
        print(i)


